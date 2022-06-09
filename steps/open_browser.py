class OpenBrowser:
    
    def __init__(self, browser) -> None:
        self.__browser = browser
        
    def open_google(self):
        self.__browser.visit("https://google.com")
        return self.__browser.dom.title