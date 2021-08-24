# GSOM JupyterHub
Manual and Demo Jupyter Notebooks for GSOM Students

## Инструкция по входу в JupyterHub
## JupyterHub Log In Manual  


ВАЖНО: вход на платформу осуществляется через авторизацию в домене GSOM поэтому для входа вам необходимо иметь учетную запись в этом домене (например, someone@gsom.spbu.ru). 
NOTE: you should have an account at GSOM and email address (e.g. someone@gsom.spbu.ru) to log in to Jupyter.

Как войти на платформу и начать работать
How to enter Jupyter and start working

Шаг 1. Вход на платформу осуществляется по адресу https://jhas01.gsom.spbu.ru 
Step 1. Enter url https://jhas01.gsom.spbu.ru 



Шаг 2. После нажатия на кнопку [Sign in with Azure AD] вы попадете на страницу авторизации 
Step 2. When you press [Sign in with Azure AD] you will be directed to authorization page





В форме авторизации необходимо указать свои логин (адрес эл.почты) и нажать кнопку [Далее], после чего ввести пароль от этой учетной записи и нажать [Войти]. 
You should enter your login (same as email address) and press [Далее], then enter your password in the password form and press [Войти].



Система может запросить вас остаться авторизованными и не выходить из учетной записи, для минимизации авторизационных запросов нажмите кнопку [Да].
Authorization application may ask you to stay authorized, just press [Да] button.

Шаг 3. После авторизации вы попадете на страницу, на которой вам будет предложено запустить сервер для начала работы. Необходимо выбрать одну из предлагаемых конфигураций для создания окружения (environment):
DataScience environment (рекомендуемое для большинства задач по анализу данных и ML алгоритмов)
Spark environment (для обработки больших массивов данных Spark-ом и чтения данных из S3 бакетов)
R environment (для проектов на языке R)
Minimal Python environment (минимальный Python без большинства библиотек для анализа данных)
и нажать кнопку [Start].
Step 3. Next page will offer you to select one of the possible environments:
DataScience environment (recommended for data analysis and ML tasks)
Spark environment (to use Spark and read from S3)
R environment (R programming language)
Minimal Python environment (pure Python with no data analysis libraries)




Вы увидите окно со статусом запуска сервера, нужно будет дождаться завершения запуска:
You will see progress bar that indicates status of your server launch:



ВНИМАНИЕ: Возможен вариант, когда сервер не запустится с первого раза, тогда вам нужно будет перейти в раздел “Home”, который расположен в левом верхнем углу страницы JupyterHub…
NOTE: It is possible that your server will not start, so you should enter the “Home” page...



....и повторно запустить сервер через нажатие кнопки [Start My Server], как указано на картинке внизу, или через нажатие кнопки [Launch Server], после чего вам может быть опять предложено выбрать выбрать конфигурацию:
...and start your server one more time manually by pressing [Start My Server] button:



Шаг 4. Вы попадете на стартовую страницу JupyterHub, которая будет выглядеть следующим образом:
Step 4. Start page of the JupyterHub looks like this:



Можно начинать работать, на стартовой панели есть кнопки для создания ноутбуков, открытия терминала, загрузки (upload) и пр.
You may start working, create notebooks, open terminals, upload files, etc.



Подробнее о работе в среде Jupyter (JupyterHub) можно прочитать тут: 
User manual for JupyterHub is here:
https://jupyter-notebook.readthedocs.io/en/stable/ 






