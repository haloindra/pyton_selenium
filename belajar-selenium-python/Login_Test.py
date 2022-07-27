import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_wrong_username_wrong_password(self):
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("asdads@yopmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("test123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Masuk')]").click() # klik tombol Masuk
        time.sleep(10)

        # validasi
        response_message_login = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[2]/p[1]").text

        self.assertEqual(response_message_login, 'Alamat email atau kata sandi yang\nanda masukan tidak valid')

    def test_b_no_input_username_password(self):
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Masuk')]").click() # klik tombol Masuk
        time.sleep(10)

        # validasi
        response_message_email = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[2]/div[1]").text
        response_message_password = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[3]/div[1]").text


        self.assertEqual(response_message_email, 'diperlukan email')
        self.assertEqual(response_message_password, 'diperlukan kata sandi')

    def test_c_login_berhasil(self):
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("hepufab@mailinator.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("Pa$$w0rd!") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Masuk')]").click() # klik tombol Masuk
        time.sleep(10)

        # validasi
        expected_current_url = "https://myappventure.herokuapp.com/home"
        self.assertEqual(expected_current_url, browser.current_url)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()