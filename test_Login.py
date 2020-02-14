import unittest
from selenium import webdriver


class searchTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #create  firefox driver
        cls.driver = webdriver.Firefox(executable_path=r'C:\Users\Deepak\Downloads\geckodriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://www.google.com/")
        cls.driver.refresh()



    def test_searchByText(self):
        #self.searchField = self.driver.find_element_by_id("search_form_input_homepage")
        self.searchField =self.driver.find_element_by_name("q")


        #Enter search keyword :
        self.searchField.send_keys("Facebook")
        self.searchField.submit()
        print("Test 1")



    def test_searchByText2(self):
        # self.searchField = self.driver.find_element_by_id("search_form_input_homepage")
        self.searchField = self.driver.find_element_by_name("q")

        # Enter search keyword :
        self.searchField.send_keys("facebook")
        self.searchField.submit()
        print("Test 2")

        currentURL = self.driver.current_url

        self.assertNotEqual("http://www.google.com/",currentURL,msg="Test Passed")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()








if __name__ == '__main__':
    unittest.main()


