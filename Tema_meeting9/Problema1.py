import unittest
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestLoginWithCredentials(unittest.TestCase):
    chrome = None

    # executing before each test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/login')
        self.chrome.implicitly_wait(2)

    # executing after every test
    def tearDown(self):
        self.chrome.quit()

    def test_elements(self):
        # Test #1: check and see if the entered URL is the correct one
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected_url, actual_url, 'The URL is incorrect')

        # Test #2: Verify if browser title bar is the correct one
        browser_title = self.chrome.title
        expected_browser_title = 'The Internet'
        self.assertEqual(browser_title, expected_browser_title, 'The page title is not the correct one!')

        # Test #3: Verify if the page title is the correct one
        page_title = self.chrome.find_element(By.XPATH, '//h2[text()="Login Page"]').text
        expected_page_title = "Login Page"
        self.assertEqual(page_title, expected_page_title, 'The Page Title is incorrect!')
        print(page_title)

        # Test #4: Verify if the login button text is being displayed correctly

        login_btn_text = self.chrome.find_element(By.XPATH,
                                                  '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]').text
        expected_login_btn_text = "Login"
        self.assertEqual(login_btn_text, expected_login_btn_text, "Submit button text is incorrect")
        print(expected_login_btn_text)

        # Test #4.1: Verify if the login button is being displayed correctly
        login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        self.assertTrue(login_btn.is_displayed(), "Login button is NOT visible!")

        # Test 5: check if "Elemental Selenium" has the correct atribute
        link_attribute = self.chrome.find_element(By.XPATH, '//*[contains(text(), "Elemental")]').get_attribute('href')
        expected_link_attribute = "http://elementalselenium.com/"
        self.assertEqual(link_attribute, expected_link_attribute, 'Login btn href attribute is incorrect')

    # Test #7: check if error message is correct during login
    def test_login_error_msg(self):
        username = self.chrome.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('FakeUsername')
        password = self.chrome.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('FakePassword')
        login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        sleep(5)
        error_msg = self.chrome.find_element(By.XPATH, '//*[@class="flash error"]').text
        print(error_msg)
        expected_error_msg = "Your username is invalid!"
        self.assertTrue(expected_error_msg in error_msg, 'Error message is not the expected one!')

    # Test #8: check to see if the login error message still shows up after you close it
    def test_login_error_msg2(self):
        username = self.chrome.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('')
        password = self.chrome.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('')
        login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        close_error_msg = self.chrome.find_element(By.XPATH, '//a[@class="close"]')
        close_error_msg.click()
        sleep(5)
        show_error_message = self.chrome.find_elements(By.XPATH, '//*[@class="flash error"]')
        self.assertEqual(len(show_error_message), 0, 'Flash error is not being displayed anymore')
        print(len(show_error_message))

    # Test #9: check to see if the labels are being displayed correctly for the existing inputs
    def test_labels_inputs(self):
        label_elements = self.chrome.find_elements(By.XPATH, '//label')
        expected_label1 = "Username"
        expected_label2 = "Password"
        self.assertEqual(label_elements[0].text, expected_label1, "The 'Username' Label/text is NOT the correct one")
        self.assertEqual(label_elements[1].text, expected_label2, "The 'Password' Label/text is NOT the correct one")

    # Test #10: Login with the correct credentials and check that URL contains /secure

    def test_login_with_credentials(self):
        username = self.chrome.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('tomsmith')
        password = self.chrome.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('SuperSecretPassword!')
        login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        sleep(5)

        current_URL = self.chrome.current_url
        expected_URL = "https://the-internet.herokuapp.com/secure"
        self.assertEqual(current_URL, expected_URL, 'The URL does NOT contain /secure')
        expected_URL2 = "/secure"
        self.assertTrue(expected_URL2 in current_URL, 'The URL does NOT contain /secure')

        # check that element having class="flash success" is being displayed correctly:
        success_msg = self.chrome.find_element(By.XPATH, '//*[@class="flash success"]')
        self.assertTrue(success_msg.is_displayed(), 'The confirmation message is NOT being displayed correctly')


        #check that the text on the element having class="flash success" contains 'secure area!' text
        success_msg_text = self.chrome.find_element(By.XPATH, '//*[@class="flash success"]').text
        print(success_msg_text)
        expected_text = "secure area2!"
        self.assertTrue(expected_text in success_msg_text, 'The text : secure area! is NOT being displayed!')

    # Test #11: Login with credentials, then logout, then check existing URL
    def test_logout_url(self):
        username = self.chrome.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys('tomsmith')
        password = self.chrome.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('SuperSecretPassword!')
        login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
        login_btn.click()
        logout_btn = self.chrome.find_element(By.XPATH, '//*[@class="icon-2x icon-signout"]')
        logout_btn.click()

        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login2"
        self.assertEqual(actual_url, expected_url, "The URL is incorrect!")

    # Test #12: brute force password hacking
    def test_brute_force(self):
        pswd_text = self.chrome.find_element(By. XPATH, '//h4[@class="subheader"]').text
        print(pswd_text)
        print(type(pswd_text))
        pswd_list = pswd_text.split() # divide string into substrings based on "space"
        print(pswd_list)

        for i in range(len(pswd_list)):
            username = self.chrome.find_element(By.XPATH, '//*[@id="username"]')
            username.send_keys('tomsmith')
            password = self.chrome.find_element(By.XPATH, '//*[@id="password"]')
            password.send_keys(pswd_list[i])
            login_btn = self.chrome.find_element(By.XPATH,
                                             '//*[contains(text(), "Login") and @class="fa fa-2x fa-sign-in"]')
            login_btn.click()
            sleep(2)

            flash_class = self.chrome.find_element(By.XPATH, '//*[@id="flash"]').get_attribute('class')
            expected_flash_attribute = "flash success"

            if flash_class != expected_flash_attribute:
                print('the password has not been find yet!')
            else:
                print('The password is: ', pswd_list[i])
                break




