import unittest
from selenium import webdriver
import HtmlTestRunner


class searchTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #create  firefox driver
        cls.driver = webdriver.Firefox(executable_path=r'C:\Users\Deepak\Downloads\geckodriver.exe')


    def test_pageTitle(self):
        #self.searchField = self.driver.find_element_by_id("search_form_input_homepage")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"Test Passed")
        # self.assertEqual("orange",self.driver.title,"test failed")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title,"Title not matching")



        #Enter search keyword :s





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()








if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\Deepak\PycharmProjects\seleniumFramework\Reports'))


