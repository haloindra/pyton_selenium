import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(10)
        browser.find_element(By.NAME,"username").send_keys("wakwaayy") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("wakwaayy@yopmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("tester123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Daftar sekarang')]").click() # klik tombol Daftar Sekarang
        time.sleep(10)

        # validasi
        response_message_berhasil_register = browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]").text

        self.assertEqual(response_message_berhasil_register, 'Selamat! Akun anda berhasil dibuat')

    def test_b_failed_register_with_all_field_empty(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Daftar sekarang')]").click() # klik tombol Daftar Sekarang
        time.sleep(10)

        # validasi
        response_message_username = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[2]/div[1]").text
        response_message_email = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[3]/div[1]").text
        response_message_password = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]").text

        self.assertEqual(response_message_username, 'diperlukan username')
        self.assertEqual(response_message_email, 'diperlukan email')
        self.assertEqual(response_message_password, 'diperlukan kata sandi')
    
    def test_c_failed_register_with_empty_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("uhuhuq1a@yopmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("tester123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Daftar sekarang')]").click() # klik tombol Daftar Sekarang
        time.sleep(10)

        # validasi
        response_message_username = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[2]/div[1]").text

        self.assertEqual(response_message_username, 'diperlukan username')

    def test_d_failed_register_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("asdfas") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("123123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Daftar sekarang')]").click() # klik tombol Daftar Sekarang
        time.sleep(10)

        # validasi
        response_message_email = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[3]/div[1]").text

        self.assertEqual(response_message_email, 'diperlukan email')

    def test_e_failed_register_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("uhuhuq1a") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("indraa@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[contains(text(),'Daftar sekarang')]").click() # klik tombol Daftar Sekarang
        time.sleep(10)

        # validasi
        response_message_password = browser.find_element(By.XPATH,"//body/div[@id='__next']/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]").text

        self.assertEqual(response_message_password, 'diperlukan kata sandi')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()


