from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, "accordion__heading-{}" #Начало с 16
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}" #начало с 16, конец 23
    QUESTION_LOCATOR_8 = By.ID, "accordion__heading-7" #Это конец вопросов, номер 23
    ACCEPT_COOKIE_BUTTON = By.XPATH, "//button[@id='rcc-confirm-button']"

    BUTTON_ORDER_UP = By.XPATH, "(//button[@class='Button_Button__ra12g'])[1]"
    BUTTON_ORDER_LOW = By.XPATH, "//div[contains(@class, 'Home_FinishButton__')]//button"

    BUTTON_LOGO_SCOOTER = By.XPATH, "//img[@alt='Scooter']"