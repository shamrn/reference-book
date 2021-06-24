<h2>1 - Запуск локальной версии проекта</h2>
<p>1.1 - git clone</p>
<p>1.2 - pip install -r requirements.txt</p>
<p>1.3 - python manage.py migrate</p>
<p>1.4 - python manage.py runserver<p>
  <hr>
<h2>2 - GUI - стандартная Django админ панель, расположена по адресу http://127.0.0.1:8000/admin/h2>
  <hr>
<h2>3 - Работа с api</h2>
<h4>3.1 - Получение списка справочников:</h4>
<p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/book-list/</p>
 <p>Ответ:</p>
  <p>"count" - Кол-во справочников</p>
  <p "next" - Следующая страница списка справочников, ответ приходит по 10 элементов</p>
  <p "previous" - Предыдущая страница списка справочников, ответ приходит по 10 элементов</p>
  <p "results" - Результат запроса, включает в себя:</p>
  <p> "id" - Уникальный идентификатор справочника</p>
  <p> "version" - Версии справочника, включают в себя активные версии справочника, включает в себя:</p>
  <p>"id" - Уникальный идентификатор версии</p>
  <p>"name" - Название справочника текущей версии</p>
  <p>"short_name" - Краткое название справочника</p>
  <p>"desc" - Описание справочника</p>
  <p>"version" - Версия справочника</p>
  <p> "date" - Дата начала справочника</p>
  <p> "count_item" - Кол-во элементов справочника</p>
  <p> "is_active" - Активна или нет версия справочника, один справочник может иметь несколько активных версий</p>
  <p>Возможна передача параметров:</p>
  <p>"is_active" - По умолчанию True, ответ приходит только с активными версиями справочника, если передать False - ответ придет с активными и неактивными версиями справочника, тип boolean</p>
<br>
  <h4>Получение списка справочников, актуальных на указанную дату</h4>
  <p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/book-list/</p>
  <P>К запросу передается параметр "date" - указывается на какую дату нужно получить актуальные версии справочников,значение передается в формате Y-m-d</p>
<br>
  <h4>Получение элементов заданного справочника текущей версии</h4>
  <p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/item/</p>
  <p>К запросу передается параметр "id_book"  - уникальный идентификатор справочника, тиn int</p> 
  <p>Ответ - элементы данного справочника, активных версий, с полями:</p>
  <p> "id" - Уникальный идентификатор элемента</p>
  <p> "reference_book" - Включает в себя "id" - уникальный идентификатор справочника , "short_name" - краткое название справочника</p>
  <p>"code" - Уникальный код элемента</p>
  <p> "value" - Значение элемента</p>
<br>
  <h4>Валидация элементов заданного справочника текущей версии</h4>
  <p>При передаче неверных get-параметров, пример:</p>
  <p>Отправляем запрос http://127.0.0.1:8000/api/v1/item/</p>
  <p>Get-параметр - id_book=23423</p>
  <p>Получаем ответ с 400 ошибкой и телом "Значение '234234' недопустимо,в базе присутствуют справочники с идентификаторами: [1]"</p>
<br>
  <h4>Получение элементов заданного справочника указанной версии</h4>
  <p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/item/</p>
  <p>К запросу передаются параметры:
    <p>"id_book" - уникальный идентификатор справочника, тиn int</p>
  <p>"version" - название версии, тип str</p>
  <p>Ответ - элементы данного справочника указанной версии</h4>
 <p>Также к вышеперечисленным методам, возможна передача параметра:</p>
 <p>"version_actual" - по умолчанию, ответ элементов только активных версий, при передаче "False", ответ придет с элементами активных и неактивных версий справочников, тип boolean</p>
 <br>
 <h4>Валидация элемента заданного справочника по указанной версии</h4>
  <p>При передаче неверных get-параметров, пример:</p>
  <p>Отправляем запрос http://127.0.0.1:8000/api/v1/item/</p>
  <p>Get-параметр - version='Версия 5'</p>
  <p>Получаем ответ с 400 ошибкой и телом "Значение 'Версия 5' недопустимо,в базе присутствуют версии: ['Версия 1', 'Версия 2']"</p>
