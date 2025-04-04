# web_browser.py
from typing import Dict, Any, List, Optional, Callable
from pydantic import Field, BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
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
        "Highly advanced universal web automation tool with advanced element identification, AJAX waiting, modal dismissal, multi-tab and dropdown support, UI labeling (with element number mapping), and custom JS injection.",
        description="Tool description"
    )
    
    default_timeout: int = 15  # Default wait timeout in seconds
    max_retries: int = 3       # Maximum retries for any individual task
    max_overall_attempts: int = 3  # Maximum overall attempts to complete the plan

    # Cache for synonyms to avoid repeated LLM calls.
    synonyms_cache: Dict[str, List[str]] = {}

    # Storage for the UI mapping returned by label_ui.
    ui_mapping: List[Dict[str, Any]] = []

    def execute(self, input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an advanced dynamic web automation workflow.
        
        The process is as follows:
         - Generate an execution plan via the LLM.
         - Automatically insert a UI-labeling task immediately after the first navigation task.
         - Process each task sequentially. If a task fails, retry that task (up to an overall maximum).
         - When using advanced fallback to find an element, the tool uses the UI mapping (the numbers shown over the UI)
           to log which element is being interacted with.
        """
        driver = None
        overall_start = time.time()
        try:
            headless = input.get("headless", False)
            self.default_timeout = int(input.get("timeout", self.default_timeout))
            self.max_retries = int(input.get("max_retries", self.max_retries))
            driver = self._init_browser(headless)
            results = []
            current_url = ""

            plan = self._generate_plan(input.get('query', ''), current_url)
            # Automatically insert a UI-labeling task immediately after the first navigation task.
            nav_index = None
            for i, task in enumerate(plan.tasks):
                if task.get("action", "").lower() == "navigate":
                    nav_index = i
                    break
            if nav_index is not None:
                if not any(task.get("action", "").lower() == "label_ui" for task in plan.tasks[nav_index+1:]):
                    plan.tasks.insert(nav_index+1, {
                        "action": "label_ui",
                        "selector": "",
                        "value": "",
                        "description": "Automatically label UI elements after navigation for improved accuracy."
                    })

            if not plan.tasks:
                raise ValueError("No valid tasks in the generated plan.")

            # Map action names to their corresponding handler functions.
            action_map: Dict[str, Callable[[webdriver.Chrome, Dict[str, Any]], Dict[str, Any]]] = {
                "navigate": lambda d, task: self._handle_navigation(d, task.get("value", "")),
                "click": lambda d, task: self._handle_click(d, task.get("selector", "")),
                "type": lambda d, task: self._handle_typing(d, task.get("selector", ""), task.get("value", ""), task),
                "wait": lambda d, task: self._handle_wait(task.get("value", "")),
                "wait_for_ajax": lambda d, task: self._handle_wait_for_ajax(d, task.get("value", "30")),
                "scroll": lambda d, task: self._handle_scroll(d, task.get("selector", "")),
                "hover": lambda d, task: self._handle_hover(d, task.get("selector", "")),
                "screenshot": lambda d, task: self._handle_screenshot(d, task.get("value", "screenshot.png")),
                "switch_tab": lambda d, task: self._handle_switch_tab(d, task.get("value", "0")),
                "execute_script": lambda d, task: self._handle_execute_script(d, task.get("value", "")),
                "drag_and_drop": lambda d, task: self._handle_drag_and_drop(d, task.get("selector", ""), task.get("value", "")),
                "select": lambda d, task: self._handle_select_dropdown(d, task.get("selector", ""), task.get("value", "")),
                "label_ui": lambda d, task: self._handle_label_ui(d, task)
            }
            
            # Process tasks sequentially; if a task fails, retry that task overall (up to max_overall_attempts).
            task_index = 0
            overall_attempts = 0
            while task_index < len(plan.tasks) and overall_attempts < self.max_overall_attempts:
                task = plan.tasks[task_index]
                action = task.get("action", "").lower()
                handler = action_map.get(action)
                if not handler:
                    logger.warning(f"Unsupported action '{action}' encountered. Skipping this task.")
                    results.append({
                        "action": action,
                        "success": False,
                        "message": f"Unsupported action: {action}"
                    })
                    task_index += 1
                    continue

                logger.info(f"Executing task: {task.get('description', action)}")
                start_time = time.time()
                result = self._execute_with_retries(driver, task, handler)
                elapsed = time.time() - start_time
                result["elapsed"] = elapsed
                logger.info(f"Action '{action}' completed in {elapsed:.2f} seconds.")

                results.append(result)
                if not result.get('success', False):
                    logger.error(f"Task '{action}' failed: {result.get('message')}. Retrying this task (overall attempt {overall_attempts+1}/{self.max_overall_attempts}).")
                    overall_attempts += 1
                    # Do not increment task_index; retry the same task.
                else:
                    task_index += 1  # Proceed to next task

            if task_index == len(plan.tasks):
                logger.info("All tasks completed successfully.")
            else:
                logger.error("Not all tasks could be completed after overall retries.")

            overall_elapsed = time.time() - overall_start
            logger.info(f"Total execution time: {overall_elapsed:.2f} seconds.")
            return {"status": "success", "results": results, "total_time": overall_elapsed}
            
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
            "action": "navigate|click|type|wait|wait_for_ajax|scroll|hover|screenshot|switch_tab|execute_script|drag_and_drop|select|label_ui",
            "selector": "CSS selector (optional)",
            "value": "input text/URL/seconds/filename/target-selector or option visible text",
            "description": "action purpose"
        }}
    ]
}}

Guidelines:
1. Prefer IDs in selectors (#element-id) and semantic attributes.
2. Include wait steps after navigation and wait for AJAX where applicable.
3. Dismiss any modals/pop-ups that are not part of the task.
4. For drag_and_drop, use source selector in 'selector' and target selector in 'value'.
5. For execute_script, 'value' should contain valid JavaScript.
6. For switch_tab, 'value' should be an index or the keyword 'new'.
7. For select, 'value' should be the visible text of the option to select.
8. For label_ui, no selector or value is needed—the tool should label the UI.
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
        """Execute a task with retry logic and exponential backoff (individual task level)."""
        attempts = 0
        result = {}
        while attempts < self.max_retries:
            result = self._execute_safe_task(driver, task, handler)
            if result.get("success", False):
                return result
            attempts += 1
            logger.info(f"Retrying task '{task.get('action')}' (attempt {attempts + 1}/{self.max_retries})")
            time.sleep(1 * attempts)
        return result

    def _execute_safe_task(self, driver: webdriver.Chrome, task: Dict[str, Any],
                             handler: Callable[[webdriver.Chrome, Dict[str, Any]], Dict[str, Any]]) -> Dict[str, Any]:
        """Execute a task with comprehensive error handling."""
        try:
            return handler(driver, task)
        except Exception as e:
            action = task.get("action", "unknown")
            logger.exception(f"Error executing task '{action}':")
            return {"action": action, "success": False, "message": f"Critical error: {str(e)}"}

    def _dismiss_unwanted_modals(self, driver: webdriver.Chrome):
        """
        Dismiss or remove unwanted modals, overlays, or pop-ups.
        Attempts to click on close buttons; if none are found, removes the element via JS.
        """
        try:
            modal_selectors = [".modal", ".popup", '[role="dialog"]', ".overlay", ".lightbox"]
            for selector in modal_selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for modal in elements:
                    if modal.is_displayed():
                        close_selectors = [".close", ".btn-close", "[aria-label='Close']", "[data-dismiss='modal']"]
                        dismissed = False
                        for close_sel in close_selectors:
                            try:
                                close_button = modal.find_element(By.CSS_SELECTOR, close_sel)
                                if close_button.is_displayed():
                                    close_button.click()
                                    dismissed = True
                                    logger.info(f"Dismissed modal using selector {close_sel}")
                                    time.sleep(1)
                                    break
                            except Exception:
                                continue
                        if not dismissed:
                            driver.execute_script("arguments[0].remove();", modal)
                            logger.info(f"Removed overlay/modal with selector {selector}")
        except Exception as e:
            logger.debug(f"Modal dismissal error: {e}")

    def _get_synonyms(self, keyword: str) -> List[str]:
        """
        Dynamically fetch synonyms for the given keyword using the LLM.
        Sends a prompt asking for a comma-separated list of synonyms and caches the results.
        """
        key = keyword.lower()
        if key in self.synonyms_cache:
            return self.synonyms_cache[key]
        prompt = f"Provide a comma-separated list of synonyms for the word '{key}'."
        response = self.llm.generate(prompt=prompt)
        synonyms = [word.strip().lower() for word in response.split(",") if word.strip()]
        self.synonyms_cache[key] = synonyms
        return synonyms

    def _advanced_find_element(self, driver: webdriver.Chrome, keyword: str) -> Optional[webdriver.remote.webelement.WebElement]:
        """
        Advanced fallback for finding an element.
        Searches across multiple attributes and inner text using fuzzy matching.
        Also considers dynamic synonyms from the LLM.
        If a UI mapping exists from a previous label_ui call, attempts to match the element and logs the UI label number.
        """
        candidates = driver.find_elements(By.CSS_SELECTOR, "input, textarea, button, a, div, span")
        best_match = None
        best_ratio = 0.0
        keyword_lower = keyword.lower()
        synonyms = self._get_synonyms(keyword_lower)
        keywords_to_match = set([keyword_lower] + synonyms)

        for candidate in candidates:
            combined_text = " ".join([
                candidate.get_attribute("id") or "",
                candidate.get_attribute("name") or "",
                candidate.get_attribute("placeholder") or "",
                candidate.get_attribute("aria-label") or "",
                candidate.text or ""
            ]).strip().lower()
            current_ratio = 0.0
            for kw in keywords_to_match:
                ratio = difflib.SequenceMatcher(None, combined_text, kw).ratio()
                current_ratio = max(current_ratio, ratio)
            if current_ratio > best_ratio:
                best_ratio = current_ratio
                best_match = candidate

        if best_match and best_ratio > 0.5:
            # If UI mapping is available, try to match and return the UI label number.
            if self.ui_mapping:
                for item in self.ui_mapping:
                    try:
                        candidate_tag = best_match.tag_name.upper()
                        candidate_text = best_match.text.strip()
                        if candidate_tag == item.get("tag", "").upper() and candidate_text == item.get("text", "").strip():
                            logger.info(f"Interacting with UI element labeled as {item.get('index')}.")
                            break
                    except Exception:
                        continue
            logger.info(f"Advanced fallback detected element with similarity {best_ratio:.2f} for keyword '{keyword}'.")
            return best_match
        return None

    def _handle_navigation(self, driver: webdriver.Chrome, url: str) -> Dict[str, Any]:
        """Handle navigation with URL correction."""
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
        """Handle click actions with fallback using JS if needed."""
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            try:
                element.click()
            except Exception:
                driver.execute_script("arguments[0].click();", element)
            return {"action": "click", "success": True, "message": f"Clicked element: {selector}"}
        except Exception as e:
            logger.error(f"Click action failed on selector {selector}: {e}")
            return {"action": "click", "success": False, "message": f"Click failed: {str(e)}"}

    def _handle_typing(self, driver: webdriver.Chrome, selector: str, text: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle typing into an element.
        If the primary selector fails, attempt advanced fallback detection based on inner text and dynamic synonyms.
        If send_keys fails due to an invalid element state, try to remove the readonly attribute or set the value via JavaScript.
        """
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        except Exception as e:
            if "search" in task.get("description", "").lower() or "search" in selector.lower():
                logger.info("Primary selector failed; using advanced fallback for element detection based on inner text and synonyms.")
                element = self._advanced_find_element(driver, "search")
                if not element:
                    return {"action": "type", "success": False,
                            "message": f"Typing failed: No search-like element found; original error: {str(e)}"}
            else:
                fallback_keyword = task.get("description", "")
                element = self._advanced_find_element(driver, fallback_keyword)
                if not element:
                    return {"action": "type", "success": False, "message": f"Typing failed: {str(e)}"}
        try:
            element.clear()
            element.send_keys(text)
            return {"action": "type", "success": True, "message": f"Typed '{text}' into element."}
        except Exception as e:
            error_message = str(e)
            if "invalid element state" in error_message.lower():
                logger.warning("Invalid element state detected. Attempting to remove 'readonly' attribute and set value via JS.")
                try:
                    driver.execute_script("arguments[0].removeAttribute('readonly');", element)
                    element.clear()
                    element.send_keys(text)
                    return {"action": "type", "success": True, "message": f"Typed '{text}' after removing readonly."}
                except Exception as e2:
                    logger.warning(f"Removing readonly attribute failed: {e2}")
                    try:
                        driver.execute_script("arguments[0].value = arguments[1];", element, text)
                        return {"action": "type", "success": True, "message": f"Set value via JS: '{text}'."}
                    except Exception as e3:
                        logger.error(f"JS value injection failed: {e3}")
                        return {"action": "type", "success": False, "message": f"Typing failed after JS injection: {str(e3)}"}
            else:
                logger.error(f"Typing action failed: {e}")
                return {"action": "type", "success": False, "message": f"Typing failed: {error_message}"}

    def _handle_wait(self, seconds: str) -> Dict[str, Any]:
        """Handle a simple wait."""
        try:
            wait_time = float(seconds)
            logger.info(f"Waiting for {wait_time} seconds")
            time.sleep(wait_time)
            return {"action": "wait", "success": True, "message": f"Waited {wait_time} seconds"}
        except ValueError as e:
            logger.error(f"Invalid wait time provided: {seconds}")
            return {"action": "wait", "success": False, "message": "Invalid wait time"}

    def _handle_wait_for_ajax(self, driver: webdriver.Chrome, seconds: str) -> Dict[str, Any]:
        """
        Wait until AJAX/network activity has subsided.
        Checks for jQuery activity and then falls back to a generic wait.
        """
        try:
            timeout = int(seconds)
            logger.info(f"Waiting for AJAX/network activity for up to {timeout} seconds.")
            end_time = time.time() + timeout
            while time.time() < end_time:
                ajax_complete = driver.execute_script("""
                    return (window.jQuery ? jQuery.active === 0 : true) &&
                           (typeof window.fetch === 'function' ? true : true);
                """)
                if ajax_complete:
                    break
                time.sleep(0.5)
            return {"action": "wait_for_ajax", "success": True, "message": "AJAX/network activity subsided."}
        except Exception as e:
            logger.error(f"Wait for AJAX failed: {e}")
            return {"action": "wait_for_ajax", "success": False, "message": f"Wait for AJAX failed: {str(e)}"}

    def _handle_scroll(self, driver: webdriver.Chrome, selector: str) -> Dict[str, Any]:
        """Handle scrolling to a specific element or page bottom."""
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

    def _handle_switch_tab(self, driver: webdriver.Chrome, value: str) -> Dict[str, Any]:
        """
        Switch between tabs. 'value' can be an index or the keyword 'new'.
        """
        try:
            handles = driver.window_handles
            if value.lower() == "new":
                target_handle = handles[-1]
            else:
                idx = int(value)
                if idx < len(handles):
                    target_handle = handles[idx]
                else:
                    return {"action": "switch_tab", "success": False, "message": f"Tab index {value} out of range"}
            driver.switch_to.window(target_handle)
            return {"action": "switch_tab", "success": True, "message": f"Switched to tab {value}"}
        except Exception as e:
            logger.error(f"Switch tab failed: {e}")
            return {"action": "switch_tab", "success": False, "message": f"Switch tab failed: {str(e)}"}

    def _handle_execute_script(self, driver: webdriver.Chrome, script: str) -> Dict[str, Any]:
        """
        Execute arbitrary JavaScript code.
        """
        try:
            result = driver.execute_script(script)
            return {"action": "execute_script", "success": True, "message": "Script executed successfully", "result": result}
        except Exception as e:
            logger.error(f"Execute script failed: {e}")
            return {"action": "execute_script", "success": False, "message": f"Script execution failed: {str(e)}"}

    def _handle_drag_and_drop(self, driver: webdriver.Chrome, source_selector: str, target_selector: str) -> Dict[str, Any]:
        """
        Simulate a drag-and-drop operation.
        """
        try:
            source = WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, source_selector))
            )
            target = WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, target_selector))
            )
            ActionChains(driver).drag_and_drop(source, target).perform()
            return {"action": "drag_and_drop", "success": True, "message": f"Dragged element from {source_selector} to {target_selector}"}
        except Exception as e:
            logger.error(f"Drag and drop failed from {source_selector} to {target_selector}: {e}")
            return {"action": "drag_and_drop", "success": False, "message": f"Drag and drop failed: {str(e)}"}

    def _handle_select_dropdown(self, driver: webdriver.Chrome, selector: str, option_text: str) -> Dict[str, Any]:
        """
        Select an option from a dropdown (HTML <select>) by visible text.
        """
        try:
            element = WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            select_element = Select(element)
            select_element.select_by_visible_text(option_text)
            return {"action": "select", "success": True, "message": f"Selected '{option_text}' from dropdown {selector}"}
        except Exception as e:
            logger.error(f"Dropdown selection failed on selector {selector} with option '{option_text}': {e}")
            return {"action": "select", "success": False, "message": f"Dropdown selection failed: {str(e)}"}

    def _handle_label_ui(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Label UI elements by injecting JavaScript that overlays colored boxes and numbered labels
        on interactive elements. Different tags use different colors. Returns a JSON mapping
        of the labeled elements (with each element's number) so that you can debug better.
        """
        try:
            script = """
            (function() {
                var colorMapping = {
                    "INPUT": "green",
                    "BUTTON": "blue",
                    "A": "orange",
                    "SELECT": "purple",
                    "TEXTAREA": "teal"
                };
                var defaultColor = "red";
                var elements = document.querySelectorAll("input, button, a, select, textarea, div, span");
                var mapping = [];
                for (var i = 0; i < elements.length; i++) {
                    var rect = elements[i].getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) continue;
                    var tag = elements[i].tagName.toUpperCase();
                    var color = colorMapping[tag] || defaultColor;
                    var overlay = document.createElement("div");
                    overlay.style.position = "absolute";
                    overlay.style.left = (rect.left + window.scrollX) + "px";
                    overlay.style.top = (rect.top + window.scrollY) + "px";
                    overlay.style.width = rect.width + "px";
                    overlay.style.height = rect.height + "px";
                    overlay.style.border = "2px solid " + color;
                    overlay.style.zIndex = "9999";
                    overlay.style.pointerEvents = "none";
                    
                    var label = document.createElement("div");
                    label.innerText = (i+1).toString();
                    label.style.position = "absolute";
                    label.style.top = "0px";
                    label.style.left = "0px";
                    label.style.backgroundColor = "yellow";
                    label.style.color = "black";
                    label.style.fontSize = "12px";
                    label.style.fontWeight = "bold";
                    label.style.padding = "2px";
                    overlay.appendChild(label);
                    
                    document.body.appendChild(overlay);
                    
                    mapping.push({
                        index: i+1,
                        tag: tag,
                        text: elements[i].innerText.trim(),
                        class: elements[i].getAttribute("class"),
                        borderColor: color
                    });
                }
                return JSON.stringify(mapping);
            })();
            """
            result = driver.execute_script(script)
            if result is None:
                self.ui_mapping = []
                return {"action": "label_ui", "success": True, "message": "UI elements labeled but no mapping returned.", "mapping": []}
            mapping = json.loads(result)
            self.ui_mapping = mapping
            return {"action": "label_ui", "success": True, "message": "UI elements labeled.", "mapping": mapping}
        except Exception as e:
            logger.error(f"Label UI action failed: {e}")
            return {"action": "label_ui", "success": False, "message": f"Label UI failed: {str(e)}"}

    def _capture_failure_screenshot(self, driver: webdriver.Chrome, action: str):
        """Capture a screenshot for debugging when an error occurs."""
        filename = f"failure_{action}_{int(time.time())}.png"
        try:
            driver.save_screenshot(filename)
            logger.info(f"Failure screenshot captured: {filename}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
