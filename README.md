# Diplom_3
<h3>Автотесты, реализованные для сервиса Stellar Burgers</h3>

<h4>test_personal_account_page.py - тесты для проверки Личного кабинета</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_to_personal_account_from_main_page</td>
      <td>Проверка перехода по клику на «Личный кабинет» с главной страницы</td>
    </tr>
    <tr>
      <td>test_go_to_personal_account_story_order</td>
      <td>Проверка перехода в «Личном кабинете» в раздел «История заказов»</td>
    </tr>
    <tr>
      <td>test_exit_from_account</td>
      <td>Проверка выхода из аккаунта в «Личном кабинете»</td>
    </tr>
  </tbody>
</table>

<h4>test_recover_password_page.py - тесты для проверки страницы восстановления пароля</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_to_recover_password_page</td>
      <td>Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль» на странице авторизации</td>
    </tr>
    <tr>
      <td>test_send_email_to_email_field_on_recover_page</td>
      <td>Проверка ввода почты и клика по кнопке "Восстановить" на странице восстановления пароля</td>
    </tr>
    <tr>
      <td>test_check_visibly_password_on_recover_password_page</td>
      <td>Проверка клика по кнопке показать/скрыть пароль на странице восстановления пароля</td>
    </tr>
  </tbody>
</table>

<h4>test_site_main_page.py - тесты для проверки раздела Конструктор на главной странице</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_to_tape_order_page_from_main_page</td>
      <td>Проверка перехода по клику на «Конструктор» в шапке страницы</td>
    </tr>
    <tr>
      <td>test_click_on_ingredient_name_open_detail_window</td>
      <td>Проверка всплывающего окна с деталями ингредиента по клику на ингредиент в Конструкторе</td>
    </tr>
    <tr>
      <td>test_close_detail_window</td>
      <td>Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик</td>
    </tr>
    <tr>
      <td>test_add_ingredient_in_basket_check_count</td>
      <td>Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ</td>
    </tr>
    <tr>
      <td>test_create_order</td>
      <td>Проверка создания заказа</td>
    </tr>
  </tbody>
</table>

<h4>test_tape_order_page.py - тесты для проверки раздела Лента заказов</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_go_to_tape_order_page_from_main_page</td>
      <td>Проверка перехода по клику на «Лента заказов» в шапке страницы</td>
    </tr>
    <tr>
      <td>test_open_window_with_order_details</td>
      <td>Проверка открытия всплывающего окна с деталями заказа по клику на заказ в ленте</td>
    </tr>
    <tr>
      <td>test_check_user_orders_from_personal_account_in_order_tape</td>
      <td>Проверка наличия заказов пользователя из раздела «История заказов» на странице «Лента заказов»</td>
    </tr>
    <tr>
      <td>test_create_order_change_count_in_all_orders</td>
      <td>Проверка увеличения счетчика "Выполнено за всё время" в ленте заказов при создании нового заказа</td>
    </tr>
    <tr>
      <td>test_create_order_change_count_in_today_orders</td>
      <td>Проверка увеличения счетчика "Выполнено за сегодня" в ленте заказов при создании нового заказа</td>
    </tr>
    <tr>
      <td>test_check_new_order_in_block_in_work</td>
      <td>Проверка наличия номера заказа в разделе "В работе" после создания заказа</td>
    </tr>
  </tbody>
</table>

Для работы необходимы библиотеки: </br>
<li>pytest</li>
<li>selenium</li>
<li>requests</li>
<li>random</li>
<li>allure</li>

Запуск тестов:  <b>pytest -v</b> </br>
Построение отчета о тестировании: <b>allure serve allure_results</b> 