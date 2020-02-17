class pageObject():
    txtUsername = "txtUsername"
    txtPassword = "txtPassword"
    btnLogin = "Submit"
    logout = "Logout"
    admin = "welcome"

    def __init__(self, driver):
        self.driver = driver

    def Username(self,username):
        self.driver.find_element_by_name(self.txtUsername).send_keys(username)

    def Password(self,password):
        self.driver.find_element_by_name(self.txtPassword).send_keys(password)

    def resultButton(self):
        self.driver.find_element_by_name(self.btnLogin).click()

    def logoutButton(self):
        self.driver.find_element_by_id(self.admin).click()
        self.driver.find_element_by_css_selector("#welcome-menu > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
