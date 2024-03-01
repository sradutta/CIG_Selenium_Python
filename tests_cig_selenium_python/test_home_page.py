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
        about_url = driver.current_url
        assert about_url == "https://www.careersingear.com/about"

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.advertise_on_home_page
    def test_advertise_on_home_page(self,driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click on advertise and assert
        driver.find_element(By.LINK_TEXT, "Advertise").click()
        time.sleep(2)
        advertise_url = driver.current_url
        assert advertise_url == "https://www.careersingear.com/#tab-advertise"
        assert driver.find_element(By.ID, "contact-page").is_displayed()

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.privacy_policy_on_home_page
    def test_privacy_policy_on_home_page(self,driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click and assert Privacy Policy
        driver.find_element(By.LINK_TEXT, "Randall-Reilly Terms of Use and Privacy Policy").click()
        time.sleep(2)
        p = driver.current_window_handle
        chwd = driver.window_handles
        if len(chwd) != 2:
            print("ERROR: Number of tabs opened is more than 2")
            exit()
        if chwd[0] == p:
            driver.switch_to.window(chwd[1])
        time.sleep(2)
        privacy_url = driver.current_url
        assert privacy_url == "https://randallreilly.com/legal/website-terms-and-privacy-policy/"
        driver.close()

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.do_not_sell_on_home_page
    def test_do_not_sell_on_home_page(self,driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click on Do Not Sell
        driver.find_element(By.LINK_TEXT, "Do Not Sell Or Share My Personal Information").click()
        time.sleep(2)
        p = driver.current_window_handle
        chwd = driver.window_handles
        if len(chwd) != 2:
            print("ERROR: Number of tabs opened is more than 2")
            exit()
        if chwd[0] == p:
            driver.switch_to.window(chwd[1])
        time.sleep(3)
        personal_url = driver.current_url
        assert personal_url == "https://privacyportal-cdn.onetrust.com/dsarwebform/49a9a972-547e-4c49-b23c-4cc77554cacb/cddab1bc-7e58-4eca-a20d-be42716734cf.html"
        driver.close()

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.copyright_on_home_page
    def test_copyright_on_home_page(self,driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click on copyright and assert
        driver.find_element(By.LINK_TEXT, "© 2024 Randall-Reilly").click()
        time.sleep(2)
        p = driver.current_window_handle
        chwd = driver.window_handles
        if len(chwd) != 2:
            print("ERROR: Number of tabs opened is more than 2")
            exit()
        if chwd[0] == p:
            driver.switch_to.window(chwd[1])
        time.sleep(3)
        personal_url = driver.current_url
        assert personal_url == "https://randallreilly.com/"
        driver.close()

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.facebook_on_home_page
    def test_facebook_on_home_page(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click on copyright and assert
        driver.find_element(By.LINK_TEXT, "Careers in Gear Facebook Page").click()
        time.sleep(2)
        p = driver.current_window_handle
        chwd = driver.window_handles
        if len(chwd) != 2:
            print("ERROR: Number of tabs opened is more than 2")
            exit()
        if chwd[0] == p:
            driver.switch_to.window(chwd[1])
        time.sleep(3)
        personal_url = driver.current_url
        assert personal_url == "https://www.facebook.com/CareersinGear"
        driver.close()

    @pytest.mark.various_links_on_home_page_test
    @pytest.mark.twitter_on_home_page
    def test_twitter_on_home_page(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(2)
        # Click on accept cookies
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Click on copyright and assert
        driver.find_element(By.LINK_TEXT, "Careers in Gear Twitter Page").click()
        time.sleep(2)
        p = driver.current_window_handle
        chwd = driver.window_handles
        if len(chwd) != 2:
            print("ERROR: Number of tabs opened is more than 2")
            exit()
        if chwd[0] == p:
            driver.switch_to.window(chwd[1])
        time.sleep(3)
        personal_url = driver.current_url
        assert personal_url == "https://twitter.com/CareersInGear"
        driver.close()