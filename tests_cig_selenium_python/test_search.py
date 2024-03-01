import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestSearch:

    @pytest.mark.advance_search_test
    def test_advance_search(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(10)

        # Click on accept cookies
        cookie_locator = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_locator.click()

        # Click on Advanced Filters Link
        advance_filter_link_locator = driver.find_element(By.LINK_TEXT, "Advanced Filters")
        advance_filter_link_locator.click()
        time.sleep(10)

        # Verify that you have navigated to the advanced search page
        actual_url = driver.current_url
        assert actual_url == "https://www.careersingear.com/search"
        time.sleep(10)

        # Enter the location as 30301 in the location field
        location_field_locator = driver.find_element(By.XPATH, "//form[@id='search-filter']//input[@id='location']")
        location_field_locator.send_keys("30301")
        time.sleep(10)

        # Select the company checkbox as tribe transportation
        company_checkbox_locator = driver.find_element(By.XPATH,
                                                       "//form[@id='search-filter']//label[.='Tribe Transportation']")
        company_checkbox_locator.click()

        # Select the haul type checkbox as hazmat
        haul_type_locator = driver.find_element(By.XPATH, "//form[@id='search-filter']//label[.='Hazmat']")
        haul_type_locator.click()

        # Click on the filter result button
        filter_search_button_locator = driver.find_element(By.XPATH,
                                                           "//form[@id='search-filter']//button[@name='action']")
        time.sleep(10)
        filter_search_button_locator.click()

        # TODO -- Assertion

    @pytest.mark.company_page_search_test
    def test_company_page_search(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(10)

        # Click on accept cookies
        cookie_locator = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_locator.click()

        # Click on company from top-right corner
        company_icon_locator = driver.find_element(By.LINK_TEXT, "Company")
        company_icon_locator.click()
        time.sleep(5)

        company_page_url = driver.current_url
        assert company_page_url == "https://www.careersingear.com/featured-trucking-companies"

        # Click on US Xpress
        usxpress_locator = driver.find_element(By.LINK_TEXT, "US Xpress")
        usxpress_locator.click()
        time.sleep(10)

        # Click on any job
        job_locator = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(1) > .main-link")
        job_locator.click()

        # Confirm we are on a job page
        company_logo_locator = driver.find_element(By.CLASS_NAME, "company-name")
        assert company_logo_locator.text == "US Xpress"
        job_header_locator = driver.find_element(By.ID, "applicationHeader")
        assert job_header_locator.text == "Pre-qualify for this Job"

    @pytest.mark.magnifying_glass_test
    def test_magnifying_glass_top_navigation_search(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(10)

        # Click on accept cookies
        cookie_locator = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_locator.click()

        # Click on company from top-right corner
        company_icon_locator = driver.find_element(By.LINK_TEXT, "Company")
        company_icon_locator.click()
        company_page_url = driver.current_url
        assert company_page_url == "https://www.careersingear.com/featured-trucking-companies"
        time.sleep(5)

        # Click on the magnifying glass on top-right corner
        magnifying_glass_locator = driver.find_element(By.XPATH, "//a[@id = 'mdi-magnify']")
        magnifying_glass_locator.click()

        # Enter value in a field
        location_locator = driver.find_element(By.XPATH, "//form[@id='navigation-search']//input[@name='location']")
        location_locator.send_keys("37501")

        # Select radius
        drop_down_select = Select(
            driver.find_element(By.XPATH, "//form[@id='navigation-search']//select[@name='radius']"))
        drop_down_select.select_by_value("35")

        # Click on Search
        search_button_locator = driver.find_element(By.XPATH, "//form[@id='navigation-search']//span[.='Search']")
        search_button_locator.click()
        time.sleep(10)

        # Confirm there are jobs
        job_listings = driver.find_elements(By.TAG_NAME, 'a')
        assert len(job_listings) > 0, "The element does not exist"

    @pytest.mark.search_test
    def test_search(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(5)

        # Click on accept cookies
        cookie_locator = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_locator.click()

        # Fill in Keywords or Company
        keyword_locator = driver.find_element(By.XPATH, "//input[@id='keywords']")
        keyword_locator.send_keys("US Xpress")
        time.sleep(2)

        # Fill in Zip
        zip_locator = driver.find_element(By.XPATH, "//main[@id='maincontent']/div[@class='home row']//form[@id='navigation-search']//input[@name='location']")
        zip_locator.send_keys("40001")

        # Click on search
        search_locator = driver.find_element(By.XPATH, "//main[@id='maincontent']//form[@id='navigation-search']/button[@name='action']")
        search_locator.click()

        # Confirm there are jobs
        job_listings = driver.find_elements(By.TAG_NAME, 'a')
        assert len(job_listings) > 0, "The element does not exist"



    @pytest.mark.state_page_search_test
    def test_state_page_search(self, driver):
        # Navigate to CIG Website
        driver.get("https://www.careersingear.com/")
        time.sleep(5)

        # Click on accept cookies
        cookie_locator = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_locator.click()

        # Click on State
        state_icon_locoator = driver.find_element(By.LINK_TEXT, "State")
        state_icon_locoator.click()

        # Click on a state
        particular_state_locator = driver.find_element(By.XPATH, "//main[@id='maincontent']//a[@href='https://www.careersingear.com/trucking-jobs/nj']/span[.='New Jersey']")
        particular_state_locator.click()

        # Confirm there are jobs
        job_listings = driver.find_elements(By.TAG_NAME, 'a')
        assert len(job_listings) > 0, "The element does not exist"





