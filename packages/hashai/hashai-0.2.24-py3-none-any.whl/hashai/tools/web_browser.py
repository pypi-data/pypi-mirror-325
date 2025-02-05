# web_browser.py
from typing import Dict, Any, List, Optional, Callable
from pydantic import Field, BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time
import re
import logging
import os
import difflib
from .base_tool import BaseTool

logger = logging.getLogger(__name__)

class BrowserPlan(BaseModel):
    tasks: List[Dict[str, Any]] = Field(
        ...,
        description="List of automation tasks to execute"
    )

class WebBrowserTool(BaseTool):
    name: str = Field("WebBrowser", description="Name of the tool")
    description: str = Field(
        "Universal web automation tool for dynamic website interactions with modal dismissal and flexible field detection",
        description="Tool description"
    )
    
    default_timeout: int = 5  # Default wait timeout in seconds
    max_retries: int = 3       # Maximum retries for any task

    def execute(self, input: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a dynamic web automation workflow with modal dismissal and flexible field matching."""
        driver = None
        try:
            headless = input.get("headless", False)
            self.default_timeout = int(input.get("timeout", self.default_timeout))
            self.max_retries = int(input.get("max_retries", self.max_retries))
            driver = self._init_browser(headless)
            results = []
            current_url = ""

            plan = self._generate_plan(input.get('query', ''), current_url)
            if not plan.tasks:
                raise ValueError("No valid tasks in the generated plan.")

            # Mapping action names to handler functions dynamically.
            action_map: Dict[str, Callable[[webdriver.Chrome, Dict[str, Any]], Dict[str, Any]]] = {
                "navigate": lambda d, task: self._handle_navigation(d, task.get("value", "")),
                "click": lambda d, task: self._handle_click(d, task.get("selector", "")),
                "type": lambda d, task: self._handle_typing(d, task.get("selector", ""), task.get("value", ""), task),
                "wait": lambda d, task: self._handle_wait(task.get("value", "")),
                "scroll": lambda d, task: self._handle_scroll(d, task.get("selector", "")),
                "hover": lambda d, task: self._handle_hover(d, task.get("selector", "")),
                "screenshot": lambda d, task: self._handle_screenshot(d, task.get("value", "screenshot.png"))
            }
            
            for task in plan.tasks:
                # First, attempt to dismiss any unwanted modal/pop-up.
                self._dismiss_unwanted_modals(driver)

                action = task.get("action", "").lower()
                logger.info(f"Executing task: {task.get('description', action)}")
                handler = action_map.get(action)
                if not handler:
                    results.append({
                        "action": action,
                        "success": False,
                        "message": f"Unsupported action: {action}"
                    })
                    continue

                result = self._execute_with_retries(driver, task, handler)
                results.append(result)

                if not result.get('success', False):
                    logger.error(f"Task failed: {result.get('message')}")
                    self._capture_failure_screenshot(driver, action)
                    break

                current_url = driver.current_url

            return {"status": "success", "results": results}
            
        except Exception as e:
            logger.exception("Execution error:")
            return {"status": "error", "message": str(e)}
        finally:
            if driver:
                driver.quit()

    def _init_browser(self, headless: bool) -> webdriver.Chrome:
        """Initialize browser with advanced options."""
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def _generate_plan(self, query: str, current_url: str) -> BrowserPlan:
        """Generate an adaptive execution plan using an LLM or other dynamic planner."""
        prompt = f"""Generate browser automation plan for: {query}

Current URL: {current_url or 'No page loaded yet'}

Required JSON format:
{{
    "tasks": [
        {{
            "action": "navigate|click|type|wait|scroll|hover|screenshot",
            "selector": "CSS selector (optional)",
            "value": "input text/URL/seconds/filename",
            "description": "action purpose"
        }}
    ]
}}

Guidelines:
1. Prefer IDs in selectors (#element-id)
2. Use semantic attributes (aria-label, name)
3. Include wait steps after navigation
4. Prioritize visible elements
5. Add scroll steps for hidden elements
6. Avoid modals/pop-ups that are not part of the task
7. When filling search boxes or similar inputs, choose the element with the closest matching attribute if an exact match is not found.
"""
        response = self.llm.generate(prompt=prompt)
        return self._parse_plan(response)

    def _parse_plan(self, response: str) -> BrowserPlan:
        """Robust JSON parsing with multiple fallback strategies."""
        try:
            json_match = re.search(r'```json\n?(.+?)\n?```', response, re.DOTALL)
            if json_match:
                plan_data = json.loads(json_match.group(1).strip())
            else:
                json_str_match = re.search(r'\{.*\}', response, re.DOTALL)
                if not json_str_match:
                    raise ValueError("No JSON object found in the response.")
                plan_data = json.loads(json_str_match.group())
            validated_tasks = []
            for task in plan_data.get("tasks", []):
                if not all(key in task for key in ["action", "description"]):
                    logger.warning(f"Skipping task due to missing keys: {task}")
                    continue
                validated_tasks.append({
                    "action": task["action"],
                    "selector": task.get("selector", ""),
                    "value": task.get("value", ""),
                    "description": task["description"]
                })
            return BrowserPlan(tasks=validated_tasks)
        except (json.JSONDecodeError, AttributeError, ValueError) as e:
            logger.error(f"Plan parsing failed: {e}")
            return BrowserPlan(tasks=[])

    def _execute_with_retries(self, driver: webdriver.Chrome, task: Dict[str, Any],
                                handler: Callable[[webdriver.Chrome, Dict[str, Any]], Dict[str, Any]]) -> Dict[str, Any]:
        """Execute a task with retry logic."""
        attempts = 0
        result = {}
        while attempts < self.max_retries:
            result = self._execute_safe_task(driver, task, handler)
            if result.get("success", False):
                return result
            attempts += 1
            logger.info(f"Retrying task {task.get('action')} (attempt {attempts + 1}/{self.max_retries})")
            time.sleep(1 * attempts)  # Exponential backoff
        return result

    def _execute_safe_task(self, driver: webdriver.Chrome, task: Dict[str, Any],
                             handler: Callable[[webdriver.Chrome, Dict[str, Any]], Dict[str, Any]]) -> Dict[str, Any]:
        """Execute task with comprehensive error handling."""
        try:
            return handler(driver, task)
        except Exception as e:
            action = task.get("action", "unknown")
            logger.exception(f"Error executing task '{action}':")
            return {
                "action": action,
                "success": False,
                "message": f"Critical error: {str(e)}"
            }

    def _dismiss_unwanted_modals(self, driver: webdriver.Chrome):
        """
        Check for common modal/pop-up selectors and dismiss them.
        This function searches for elements that likely represent unwanted modals and attempts to click their close/dismiss buttons.
        """
        try:
            # List of common modal selectors. You can extend this list as needed.
            modal_selectors = [".modal", ".popup", '[role="dialog"]']
            for selector in modal_selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for modal in elements:
                    if modal.is_displayed():
                        # Look for a close button inside the modal
                        close_selectors = [".close", ".btn-close", "[aria-label='Close']", "[data-dismiss='modal']"]
                        for close_sel in close_selectors:
                            try:
                                close_button = modal.find_element(By.CSS_SELECTOR, close_sel)
                                if close_button.is_displayed():
                                    close_button.click()
                                    logger.info(f"Dismissed modal using selector {close_sel}")
                                    time.sleep(1)  # Give time for modal to disappear
                                    break
                            except Exception:
                                continue
        except Exception as e:
            logger.debug(f"Modal dismissal encountered an error: {e}")

    def _fallback_find_search_input(self, driver: webdriver.Chrome) -> Optional[WebElement]:
        """
        Fallback to detect a search-like input element.
        It scans available input/textarea elements and uses fuzzy matching against the keyword "search".
        """
        candidates = driver.find_elements(By.CSS_SELECTOR, "input, textarea")
        for candidate in candidates:
            for attr in ["id", "name", "placeholder"]:
                try:
                    attr_val = candidate.get_attribute(attr)
                    if attr_val:
                        # Using difflib to compare similarity to "search"
                        if difflib.SequenceMatcher(None, attr_val.lower(), "search").ratio() > 0.5:
                            logger.info(f"Fallback detected search input via attribute {attr}: {attr_val}")
                            return candidate
                except Exception:
                    continue
        return None

    def _handle_navigation(self, driver: webdriver.Chrome, url: str) -> Dict[str, Any]:
        """Handle navigation, including URL correction."""
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"
        try:
            driver.get(url)
            WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return {"action": "navigate", "success": True, "message": f"Navigated to {url}"}
        except Exception as e:
            logger.error(f"Navigation to {url} failed: {e}")
            return {"action": "navigate", "success": False, "message": f"Navigation failed: {str(e)}"}

    def _handle_click(self, driver: webdriver.Chrome, selector: str) -> Dict[str, Any]:
        """Handle dynamic clicking with fallback using BeautifulSoup if needed."""
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            element.click()
            return {"action": "click", "success": True, "message": f"Clicked element: {selector}"}
        except Exception as e:
            logger.error(f"Click action failed on selector {selector}: {e}")
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            if soup.select(selector):
                logger.info(f"Element found via BeautifulSoup, but click still failed: {selector}")
            return {"action": "click", "success": False, "message": f"Click failed: {str(e)}"}

    def _handle_typing(self, driver: webdriver.Chrome, selector: str, text: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle typing by ensuring the element is present.
        If the intended element is not found (especially for search-like inputs), attempt a fallback search.
        """
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        except Exception as e:
            # If the task description suggests a search input or similar and the selector did not yield an element, try fallback.
            if "search" in task.get("description", "").lower() or "search" in selector.lower():
                logger.info("Primary selector failed. Attempting fallback search input detection.")
                element = self._fallback_find_search_input(driver)
                if not element:
                    return {"action": "type", "success": False, "message": f"Typing failed: No search-like input found; original error: {str(e)}"}
            else:
                return {"action": "type", "success": False, "message": f"Typing failed: {str(e)}"}
        try:
            element.clear()
            element.send_keys(text)
            return {"action": "type", "success": True, "message": f"Typed '{text}' into {selector}"}
        except Exception as e:
            logger.error(f"Typing action failed on selector {selector}: {e}")
            return {"action": "type", "success": False, "message": f"Typing failed: {str(e)}"}

    def _handle_wait(self, seconds: str) -> Dict[str, Any]:
        """Handle waiting with configurable time intervals."""
        try:
            wait_time = float(seconds)
            logger.info(f"Waiting for {wait_time} seconds")
            time.sleep(wait_time)
            return {"action": "wait", "success": True, "message": f"Waited {wait_time} seconds"}
        except ValueError as e:
            logger.error(f"Invalid wait time provided: {seconds}")
            return {"action": "wait", "success": False, "message": "Invalid wait time"}

    def _handle_scroll(self, driver: webdriver.Chrome, selector: str) -> Dict[str, Any]:
        """Handle scrolling to an element or page bottom."""
        try:
            if selector:
                element = WebDriverWait(driver, self.default_timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                scroll_target = selector
            else:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                scroll_target = "page bottom"
            return {"action": "scroll", "success": True, "message": f"Scrolled to {scroll_target}"}
        except Exception as e:
            logger.error(f"Scroll action failed on selector {selector}: {e}")
            return {"action": "scroll", "success": False, "message": f"Scroll failed: {str(e)}"}

    def _handle_hover(self, driver: webdriver.Chrome, selector: str) -> Dict[str, Any]:
        """Handle mouse hover action."""
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
            ActionChains(driver).move_to_element(element).perform()
            return {"action": "hover", "success": True, "message": f"Hovered over {selector}"}
        except Exception as e:
            logger.error(f"Hover action failed on selector {selector}: {e}")
            return {"action": "hover", "success": False, "message": f"Hover failed: {str(e)}"}

    def _handle_screenshot(self, driver: webdriver.Chrome, filename: str) -> Dict[str, Any]:
        """Capture a screenshot of the current browser state."""
        try:
            driver.save_screenshot(filename)
            return {"action": "screenshot", "success": True, "message": f"Screenshot saved as {filename}"}
        except Exception as e:
            logger.error(f"Screenshot capture failed: {e}")
            return {"action": "screenshot", "success": False, "message": f"Screenshot failed: {str(e)}"}

    def _capture_failure_screenshot(self, driver: webdriver.Chrome, action: str):
        """Capture a screenshot when an error occurs for debugging purposes."""
        filename = f"failure_{action}_{int(time.time())}.png"
        try:
            driver.save_screenshot(filename)
            logger.info(f"Failure screenshot captured: {filename}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
