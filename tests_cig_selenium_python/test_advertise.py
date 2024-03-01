import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestHomePage:

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.about_cig_on_home_page
    def test_about_cig_on_home_page(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)

        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click and assert About CIG
        driver.find_element(By.LINK_TEXT, "About CIG").click()
        # Click on advertise and assert
        driver.find_element(By.LINK_TEXT, "Advertise").click()
        time.sleep(2)
        advertise_url = driver.current_url
        assert advertise_url == "https://www.careersingear.com/#tab-advertise"
        assert driver.find_element(By.ID, "contact-page").is_displayed()