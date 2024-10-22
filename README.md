**Sprint 6. Страница заказа самоката. POM**

Этот проект содержит автоматизированные тесты для страницы заказа самоката с использованием Selenium и Allure.

**Структура тестов:**
- **TestOrderPage**: главный класс тестов.
  - **setup_class**: инициализация драйвера Firefox.
  
**Тесты:**
1. **test_order_scooter_and_return_to_the_main_page**:
   - Проверка создания заказа и перехода на главную страницу.
   - Использует данные из `data.py` и локаторы из `order_page_locators.py`.
   - Проверяет корректность перехода по URL главной страницы.

2. **test_order_scooter_and_transition_to_yandex_dzen**:
   - Проверка создания заказа и перехода на Яндекс Дзен.
   - Аналогично первому тесту, с проверкой URL страницы Яндекс Дзен после выполнения.

3. **test_questions_and_answers**
    - Проверка всех вопросов и ответов на них на главной странице


**Страницы:**

***BasePage:***
1. **open_page(self, url):**
   - Открывает страницу по заданному URL.
2. **find_element_with_wait(self, locator):**
   - Находит элемент на странице, ожидая его появления.
3. **click_to_element(self, locator):**
   - Кликает по элементу на странице, ожидая его появления.
4. **add_text_to_element(self, locator, text):**
   - Вводит текст в элемент на странице, ожидая его появления.
5. **get_text_from_element(self, locator):**
   - Извлекает текст из элемента на странице, ожидая его появления.
6. **scroll_to_element(self, locator):**
   - Прокручивает страницу до элемента, ожидая его появления.
7. **accept_cookies(self, locator):**
   - Принимает cookie, ожидая появления соответствующего элемента.

***MainPage:***
1. **get_answer_text**
   - получаем текст ответа под вопросом

***OrderPage:***
1. **navigation_to_order_page**
   - Переходим на основную страницу и принимаем куки
2. **get_locator_by_color**
   - Получения локатора выбора цвета самоката
3. **select_current_day**
   - Получение текущей даты и формирование локатора для того, чтобы прокликать в календаре
4. **set_order**
   - Создание заказа самоката с переданными данными из теста
5. **check_order**
   - Проверка статуса заказа
6. **switch_to_next_tab**
   - Переключаемся на открытую вкладку
7. **check_url**
   - Сравниваем текущий урл и ожидаемый

**Файлы с локаторами**
1. main_page_locators.py
2. order_page_locators.py

**Conftest**
- хранения фикстуры драйвера

**Helper**
- Содержит метод генерации номера телефона для заказа самоката 

**Файл - data**
   - Содержит наборы тестовых данных 

**pytest.ini**
- Содержит настройки для того, чтобы запускались тесты по команде и в логах были ру символы

**Завершение:**
- **teardown_class**: закрытие браузера после выполнения тестов.

**Запуск тестов**:
- Убедитесь, что Chrome или Firefox установлен и доступен в PATH.
- Запустите тесты с помощью pytest.