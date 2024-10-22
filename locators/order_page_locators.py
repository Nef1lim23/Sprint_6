from selenium.webdriver.common.by import By


class OrderPageLocators:
    #Первая страница оформления заказа
    NAME_INPUT_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_INPUT_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_STATION_LIST = By.XPATH, "//li[{}]" # Станция
    TELEPHONE_INPUT_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    SCOOTER_LOGO_LINK = By.XPATH, "//a[starts-with(@class, 'Header_LogoScooter')]" # Переход на основную страницу с самокатами
    YANDEX_DZEN_LOGO_LINK = By.XPATH, "//a[starts-with(@class, 'Header_LogoYandex')]" # Переход на страницу яндекс дзен
    BUTTON_NEXT = By.XPATH, "//button[contains(text(),'Далее')]"

    #вторая страница оформления заказа
    DATE_WHEN_TO_BRING_SCOOTER = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR_FIELD = By.XPATH, "//div[contains(@class, 'react-datepicker__month-container')]"
    CALENDAR_CLICK_ON_DATA = By.XPATH, "//div[contains(@class, 'react-datepicker__month-container')]//div[text()='{}']"
    TIME_RENTAL_SCOOTER = By.CSS_SELECTOR, "div[class='Dropdown-menu'] div:nth-child({})"
    RENTAL_PERIOD_FIELD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    COLOR_SCOOTER_BLACK = By.XPATH, "//input[@id='black']"
    COLOR_SCOOTER_GREY = By.XPATH, "//input[@id='grey']"
    COMMENT_FOR_COURIER = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BUTTON_CHECK_STATUS = By.XPATH, "//button[contains(text(),'Посмотреть статус')]"
    CALENDAR_BUTTON_NEXT = By.XPATH, "//button[normalize-space()='Next Month']"

    BUTTON_CLOSE_ORDER = By.XPATH, "//button[contains(text(),'Отменить заказ')]"
    BUTTON_LOGO_SCOOTER = By.XPATH, "//img[@alt='Scooter']"

    BUTTON_FOR_TRANSITION_YA_DZEN = By.XPATH, "//img[@alt='Yandex']"
    LOGO_YA_DZEN = By.XPATH, "//a[contains(text(),'Скачайте приложение Дзена')]"

    BUTTON_YES = By.XPATH, "//button[contains(text(),'Да')]"
    BUTTON_NO = By.XPATH, "//button[contains(text(),'Нет')]"
    FORM_ACCEPTED_ORDER = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"

    #Кнопки перехода на форму заказа самоката
    BUTTON_ORDER_UP = By.XPATH, "(//button[@class='Button_Button__ra12g'])[1]"
    BUTTON_ORDER_FROM_FORM_ORDER = By.XPATH,  "(//button[@class='Button_Button__ra12g Button_Middle__1CSJM'])[1]"
    BUTTON_ORDER_LOW = By.XPATH, "(//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp'])[1]"

    FOR_DEBAG = By.XPATH, "//img[@alt='Sppooter']"