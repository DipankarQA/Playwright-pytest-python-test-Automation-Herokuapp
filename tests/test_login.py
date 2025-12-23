

from pages.Loginpage import LoginPage

def test_login(page):
    """
    page.goto(url="https://the-internet.herokuapp.com/")
    print( page.title())
    if "The Internet" in page.title():
        print("title has matched")
    else:
        print("title has mismatched")

    """

    l = LoginPage(page)
    l.logindetails("https://the-internet.herokuapp.com/login","tomsmith", "SuperSecretPassword!")






    