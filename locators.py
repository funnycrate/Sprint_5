from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # кнопка "Личный Кабинет"
    ACC_BTN = (By.LINK_TEXT, "Личный Кабинет")
    
    # кнопка "Зарегистрироваться" в окне входа
    REG_LNK = (By.LINK_TEXT, "Зарегистрироваться")

    # Поле ввода имени в окне регистрации
    REG_NAME_FLD = (By.XPATH, ".//label[contains(text(),'Имя')]/parent::div/input")

    # Поле ввода электронной почты в окне регистрации
    REG_EMAIL_FLD = (By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input")

    # Поле ввода пароля в окне регистрации
    REG_PASS_FLD = (By.XPATH, ".//input[@type = 'password']")

    # Кнопка "Зарегистрироваться" в окне регистрации
    REG_BTN = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")

    # Сообщение об ошибке при вводе невалидного пароля при регистрации
    PASS_ERR_MSG = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")

    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BTN_MAIN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")

    # Поле ввода электронной почты в окне входа
    LOGIN_EMAIL_FLD = (By.XPATH, ".//input[@name = 'name']")

    # Поле ввода пароля в окне входа
    LOGIN_PASS_FLD = (By.XPATH, ".//input[@name = 'Пароль']")

    # Кнопка "Войти" в окне входа
    LOGIN_SUBMIT_BTN = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    # Кнопка "Оформить заказ" в личном кабинете
    PLACE_ORDER_BTN = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")

    # Кнопка "Войти" в окне регистрации
    LOGIN_LNK_REG = (By.LINK_TEXT, "Войти")

    # Кнопка "Восстановить пароль" в окне входа
    FORGOT_PASS_LNK = (By.LINK_TEXT, "Восстановить пароль")

    # Кнопка "Войти" в окне восстановления пароля
    LOGIN_LNK_FORGOT = (By.LINK_TEXT, "Войти")

    # Кнопка выхода из личного кабинета
    LOGOUT_BTN = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    # Раздел "Соусы" в конструкторе бургеров
    SAUCES_LIST = (By.XPATH, ".//h2[contains(text(), 'Соусы')]")

    # Иконка галактического соуса
    GALACTIC_SAUCE_ICON = (By.XPATH, ".//img[@alt = 'Соус традиционный галактический']")

    # Раздел "Начинки" в конструкторе бургеров
    TOPPINGS_LIST = (By.XPATH, ".//h2[contains(text(), 'Начинки')]")

    # Иконка выбора говяжьего метеорита
    BEAF_METEOR_ICON = (By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")

    # Раздел "Булки" в конструкторе бургеров
    BREAD_LIST = (By.XPATH, ".//h2[contains(text(), 'Булки')]")

    # Иконка выбора краторной булки
    CRATER_BREAD_ICON = (By.XPATH, ".//img[@alt = 'Краторная булка N-200i']")

    # Калории в окне галактического соуса
    GALACTIC_SAUCE_CAL = (By.XPATH, ".//p[contains(text(), '99')]")

    # Калории в окне говяжьего метеорита
    BEAF_METEOR_CAL = (By.XPATH, ".//p[contains(text(), '2674')]")

    # Калории в окне краторной булки
    CRATER_BREAD_CAL = (By.XPATH, ".//p[contains(text(), '420')]")

    # Кнопка "Конструктор в личном кабинете
    CONSTR_BTN = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX']")

    # Лого "СтелларБургерс"
    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")