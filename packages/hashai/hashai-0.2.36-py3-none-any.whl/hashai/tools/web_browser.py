# web_browser.py
from typing import Dict, Any, List, Callable, Optional
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
        "Advanced autonomous web automation tool with enhanced AI planning and element detection",
        description="Tool description"
    )
    
    default_timeout: int = 15
    max_retries: int = 3
    max_overall_attempts: int = 3
    synonyms_cache: Dict[str, List[str]] = {}
    ui_mapping: List[Dict[str, Any]] = []

    def execute(self, input: Dict[str, Any]) -> Dict[str, Any]:
        driver = None
        try:
            driver = self._init_browser(input.get("headless", False))
            plan = self._generate_plan(input.get("query", ""), driver.current_url if driver else "")
            
            if not plan.tasks:
                raise ValueError("No valid tasks in generated plan")

            action_map = {
                "navigate": self._handle_navigation,
                "click": self._handle_click,
                "type": self._handle_typing,
                "wait": self._handle_wait,
                "label_ui": self._handle_label_ui,
                "scroll": self._handle_scroll,
                "enter": self._handle_enter_key,
                "screenshot": self._handle_screenshot,
            }

            results = []
            task_index = 0
            last_success_index = -1

            while task_index < len(plan.tasks):
                task = plan.tasks[task_index]
                action = task.get("action", "").lower()
                handler = action_map.get(action)

                if not handler:
                    logger.warning(f"Skipping unsupported action: {action}")
                    task_index += 1
                    continue

                result = self._execute_task_with_recovery(driver, task, handler)
                results.append(result)

                if result["success"]:
                    last_success_index = task_index
                    task_index += 1
                else:
                    if task_index == last_success_index + 1:
                        logger.info("Re-labeling UI after consecutive failure")
                        self._insert_label_ui_task(plan, task_index)
                        task_index += 1

            return {"status": "success", "results": results}
        except Exception as e:
            logger.error(f"Execution failed: {str(e)}")
            return {"status": "error", "message": str(e)}
        finally:
            if driver:
                driver.quit()

    def _init_browser(self, headless: bool) -> webdriver.Chrome:
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
        example_plan = {
            "tasks": [
                {
                    "action": "navigate",
                    "value": "https://www.google.com",
                    "description": "Open Google homepage"
                },
                {
                    "action": "label_ui",
                    "description": "Identify interactive elements"
                },
                {
                    "action": "type",
                    "selector": "textarea[name='q']",
                    "value": "{query}",
                    "ui_index": 1,
                    "description": "Enter search query"
                },
                {
                    "action": "click",
                    "selector": "input[value='Google Search']",
                    "ui_index": 2,
                    "description": "Submit search"
                }
            ]
        }

        prompt = f"""Generate browser automation plan for: {query}
Current URL: {current_url or 'None'}

Follow these steps:
1. Start with navigation to target URL
2. Perform UI labeling after page load
3. Use both CSS selectors and UI indices from labeling
4. Include necessary waits between actions

Example for "search YouTube on Google":
{json.dumps(example_plan, indent=2)}

Respond ONLY with valid JSON:"""
        
        response = self.llm.generate(prompt=prompt)
        return self._parse_plan(response)

    def _execute_task_with_recovery(self, driver, task, handler):
        for attempt in range(self.max_retries + 1):
            try:
                result = handler(driver, task)
                if result["success"]:
                    return result
                
                if attempt < self.max_retries:
                    self._refresh_ui_mapping(driver)
                    logger.info(f"Retrying {task['action']} (attempt {attempt+1})")
            except Exception as e:
                logger.error(f"Attempt {attempt+1} failed: {str(e)}")
        
        return {
            "action": task["action"],
            "success": False,
            "message": f"Failed after {self.max_retries} attempts"
        }

    def _handle_label_ui(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        script = """
        function labelUI() {
            const tags = ['INPUT', 'BUTTON', 'A', 'SELECT', 'TEXTAREA'];
            const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD'];
            const elements = [];
            
            document.querySelectorAll('*').forEach((el, index) => {
                if (tags.includes(el.tagName) && el.getBoundingClientRect().width > 0) {
                    const rect = el.getBoundingClientRect();
                    const label = document.createElement('div');
                    
                    label.style = `
                        position: absolute;
                        left: ${rect.left + window.scrollX}px;
                        top: ${rect.top + window.scrollY}px;
                        border: 2px solid ${colors[tags.indexOf(el.tagName)]};
                        z-index: 9999;
                        pointer-events: none;
                        background: rgba(255,255,255,0.9);
                        padding: 2px;
                        font-size: 12px;
                        color: #333;
                    `;
                    label.textContent = `${index+1}: ${el.tagName} ${el.name || el.id || el.className || ''}`;
                    
                    document.body.appendChild(label);
                    elements.push({
                        index: index+1,
                        tag: el.tagName,
                        id: el.id,
                        name: el.name,
                        class: el.className,
                        text: el.innerText,
                        rect: {x: rect.x, y: rect.y}
                    });
                }
            });
            return JSON.stringify(elements);
        }
        return labelUI();
        """
        
        try:
            result = driver.execute_script(script)
            self.ui_mapping = json.loads(result)
            time.sleep(0.5)  # Allow labels to render
            return {"action": "label_ui", "success": True, "mapping": self.ui_mapping}
        except Exception as e:
            logger.error(f"UI labeling failed: {str(e)}")
            return {"action": "label_ui", "success": False}

    def _handle_click(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        element = None
        try:
            if task.get("ui_index"):
                element = self._find_element_by_ui_index(driver, task["ui_index"])
            else:
                element = WebDriverWait(driver, self.default_timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, task["selector"]))
                )
            
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            element.click()
            return {"action": "click", "success": True}
        except Exception as e:
            logger.error(f"Click failed: {str(e)}")
            return {"action": "click", "success": False}

    def _handle_typing(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        try:
            element = None
            if task.get("ui_index"):
                element = self._find_element_by_ui_index(driver, task["ui_index"])
            else:
                element = WebDriverWait(driver, self.default_timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, task["selector"]))
                )
            
            element.clear()
            element.send_keys(task["value"])
            return {"action": "type", "success": True}
        except Exception as e:
            logger.error(f"Typing failed: {str(e)}")
            return {"action": "type", "success": False}

    def _find_element_by_ui_index(self, driver, index: int):
        for item in self.ui_mapping:
            if item["index"] == index:
                return driver.execute_script(f"""
                    return document.elementFromPoint(
                        {item['rect']['x'] + 10}, 
                        {item['rect']['y'] + 10}
                    )
                """)
        raise Exception(f"Element with UI index {index} not found")

    def _insert_label_ui_task(self, plan, index: int):
        plan.tasks.insert(index, {
            "action": "label_ui",
            "description": "Refresh UI element mapping"
        })

    def _refresh_ui_mapping(self, driver):
        self._handle_label_ui(driver, {})
        logger.info("Refreshed UI element mapping")

    def _handle_navigation(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        try:
            driver.get(task["value"])
            WebDriverWait(driver, self.default_timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return {"action": "navigate", "success": True}
        except Exception as e:
            logger.error(f"Navigation failed: {str(e)}")
            return {"action": "navigate", "success": False}

    def _handle_wait(self, task: Dict[str, Any]) -> Dict[str, Any]:
        time.sleep(float(task.get("value", 2)))
        return {"action": "wait", "success": True}

    def _handle_scroll(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        driver.execute_script("window.scrollBy(0, window.innerHeight/2)")
        return {"action": "scroll", "success": True}

    def _handle_enter_key(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        element = self._find_element_by_ui_index(driver, task["ui_index"])
        element.send_keys(webdriver.Keys.RETURN)
        return {"action": "enter", "success": True}

    def _handle_screenshot(self, driver: webdriver.Chrome, task: Dict[str, Any]) -> Dict[str, Any]:
        driver.save_screenshot(task.get("value", "screenshot.png"))
        return {"action": "screenshot", "success": True}