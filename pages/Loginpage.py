class LoginPage:
    def __init__(self, page ):
        self.page = page
        self.username = "//*[@id='username']"
        self.password = "//*[@id='password']"
        self.loginbutton = "//*[@class='fa fa-2x fa-sign-in']"
        self.postlogin_header = "//*[@id='flash']"

    def logindetails(self, url, user, pwd):
        self.page.goto(url)
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.loginbutton)
        print(self.page.inner_text(self.postlogin_header))
        if "secure" in self.page.inner_text(self.postlogin_header).lower():
            print("title has matched")
        else:
            print("title has mismatched")

