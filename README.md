<h2>1 - Запуск локальной версии проекта</h2>
<p>1.1 - git clone</p>
<p>1.2 - pip install -r requirements.txt<p/>
<p>1.3 - python manage.py runserver<p>
  <hr>
<h2>2 - Работа с интерфейсом пользователя</h2>
<p>2.1 - http://127.0.0.1:8000, интерфейс интуитивно понятный</p>
  <hr>
<h2>3 - Работа с api</h2>
<p>3.1 - url = 'http://127.0.0.1:8000/api/v1/'</p>
<p>requests.get(url) # Получить все справочники, и версии</p>
<p>requests.get(url,params={'version__date':'15.06.2021'}) # Получить справочники, и версии, на конкретную дату</p>

<p>3.2 - url2 = 'http://127.0.0.1:8000/api/v1/item/'</p>
<p>requests.get(url2)  # Получить все элементы, всех активных справочников</p>
<p>requests.get(url2,params={'version_actual':False}) # Получить все элементы справочника, неактивных справочников в том числе</p>
<p>requests.get(url2,params={'version':'Версия 2'}) # Получить все элементы, заданной версии, активных версий</p>
<p>requests.get(url2,params={'id_book':8})# Получить все элементы справочника, на вход ожидается id справочника
<p>requests.get(url2,</p>
                      <p> params={</p>
                         <p>  'version_actual':False,</p>
                        <p>   'version':'Версия 1',</p>   
                        <p>   'id_book':8,</p>
                    <p>   })</p># передать несколько параметров
