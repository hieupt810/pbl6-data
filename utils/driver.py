"""Driver class for interacting with a web browser using Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import MAX_LENGTH


class Driver:
    """Driver class for interacting with a web browser using Selenium."""

    def __init__(self) -> None:
        self.__driver = webdriver.Chrome()

    def open_new_tab(self, url: str):
        """
        Opens a new tab in the web browser and navigates to the specified URL.

        Args:
            url (str): The URL to navigate to in the new tab.
        """

        self.__driver.execute_script(f"window.open('{url}', '_blank');")
        self.__driver.switch_to.window(self.__driver.window_handles[-1])

    def close_current_tab(self):
        """
        Closes the current tab in the web browser.

        This method closes the current tab in the web browser and switches to the previous tab.
        """

        self.__driver.close()
        self.__driver.switch_to.window(self.__driver.window_handles[-1])

    def scroll_to_bottom(self):
        """
        Scrolls the web page to the bottom.

        This method uses JavaScript to scroll the web page to the bottom by setting the window's scroll position to the height of the document's body. It then waits for 2 seconds to allow any dynamic content to load.
        """

        self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.__driver.implicitly_wait(2)

    def get(self, url: str):
        """
        Navigate to the specified URL and wait for the page to load.

        Args:
            url (str): The URL to navigate to.
        """

        self.__driver.get(url)
        self.__driver.implicitly_wait(2)

    def find_elements_by_css_selector(
        self, selector: str, max_length: int = MAX_LENGTH
    ):
        """
        Find elements on the page using the given CSS selector.

        Args:
            selector (str): The CSS selector to use for finding elements.
            max_length (int): The maximum number of elements to return. Defaults to 100.

        Returns:
            list: A list of WebElement objects that match the given CSS selector.
        """
        while True:
            list_elements = self.__driver.find_elements(By.CSS_SELECTOR, selector)
            if len(list_elements) >= max_length:
                break

            self.scroll_to_bottom()

        return self.__driver.find_elements(By.CSS_SELECTOR, selector)[:max_length]

    def find_element_by_css_selector(self, selector: str):
        """
        Find an element by its CSS selector.

        Args:
            selector (str): The CSS selector of the element to be found.

        Returns:
            WebElement: The web element found by the CSS selector.
        """

        return self.__driver.find_element(By.CSS_SELECTOR, selector)

    def close(self):
        """
        Closes the current browser window.

        This method will close the browser window associated with the driver instance.
        """

        self.__driver.close()
