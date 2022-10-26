# GSOM JupyterHub
Manual and Demo Jupyter Notebooks for [GSOM](https://gsom.spbu.ru/) Students

## Инструкция по входу в JupyterHub | JupyterHub Log In Manual  


:boom:__ВАЖНО:__ вход на платформу осуществляется через авторизацию в домене GSOM поэтому для входа вам необходимо иметь учетную запись в этом домене (например, someone@gsom.spbu.ru). 

:boom:__NOTE:__ you should have an account at GSOM and email address (e.g. someone@gsom.spbu.ru) to log in to Jupyter.


Как войти на платформу и начать работать

How to enter Jupyter and start working

____
__Шаг 1.__ Вход на платформу осуществляется по адресу https://jhas01.gsom.spbu.ru 

__Step 1.__ Enter url https://jhas01.gsom.spbu.ru 

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_0.png?raw=true "Enter the JupyterHub")

____
__Шаг 2.__ После нажатия на кнопку `Sign in with Azure AD` вы попадете на страницу авторизации 

__Step 2.__ When you press `Sign in with Azure AD` you will be directed to authorization page

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_1.png?raw=true "Login")

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_2.png?raw=true "Password")

В форме авторизации необходимо указать свои логин (адрес эл.почты) и нажать кнопку `Далее`, после чего ввести пароль от этой учетной записи и нажать `Войти`. 

You should enter your login (same as email address) and press `Далее`, then enter your password in the password form and press `Войти`.

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_3.png?raw=true "Leave me authorized")

Система может запросить вас остаться авторизованными и не выходить из учетной записи, для минимизации авторизационных запросов нажмите кнопку `Да`.

Authorization application may ask you to stay authorized, just press `Да` button.

____
__Шаг 3.__ После авторизации вы попадете на страницу, на которой вам будет предложено запустить сервер для начала работы. Необходимо выбрать одну из предлагаемых конфигураций для создания окружения (environment):
- __DataScience environment__ (рекомендуемое для большинства задач по анализу данных и ML алгоритмов)
- __Spark environment__ (для обработки больших массивов данных Spark-ом и чтения данных из S3 бакетов)
- __R environment__ (для проектов на языке R)
- __PostgreSQL environment__ (демонстрационная инсталляция базы данных PostgreSQL)
- __MongoDB environment__ (демонстрационная инсталляция базы данных MongoDB)
- __Airflow environment__ (демонстрационная инсталляция Airflow для локальных экспериментов)
- __Hadoop (with YARN) and Spark environment__ (демонстрационная инсталляция Hadoop кластера с Map-Reduce и Spark)
- __Minimal Python environment__ (минимальный Python без большинства библиотек для анализа данных)

...и нажать кнопку `Start`.

__Step 3.__ Next page will offer you to select one of the possible environments:
- __DataScience environment__ (recommended for data analysis and ML tasks)
- __Spark environment__ (to use Spark and read from S3)
- __R environment__ (R programming language)
- __PostgreSQL environment__ (Demo PostgreSQL database for the local experiments)
- __MongoDB environment__ (Demo MongoDB database for the local experiments)
- __Airflow environment__ (Airflow platform for the local experiments)
- __Hadoop (with YARN) and Spark environment__ (Hadoop mini-cluster with Map-Reduce operations and standalone Spark)
- __Minimal Python environment__ (pure Python with no data analysis libraries)

...and press `Start` button.

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_4.png?raw=true "Select environment")

Вы увидите окно со статусом запуска сервера, нужно будет дождаться завершения запуска:

You will see progress bar that indicates status of your server launch:

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_5.png?raw=true "Launch progress")

:boom:__ВНИМАНИЕ:__ Возможен вариант, когда сервер не запустится с первого раза, тогда вам нужно будет перейти в раздел `Home`, который расположен в левом верхнем углу страницы JupyterHub…

:boom:__NOTE:__ It is possible that your server will not start, so you should enter the `Home` page...

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_6.png?raw=true "Get Home")

....и повторно запустить сервер через нажатие кнопки `Start My Server`, как указано на картинке внизу, или через нажатие кнопки `Launch Server`, после чего вам может быть опять предложено выбрать выбрать конфигурацию:

...and start your server one more time manually by pressing `Start My Server` button:

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_7.png?raw=true "Start server")

____
__Шаг 4.__ Вы попадете на стартовую страницу JupyterHub, которая будет выглядеть следующим образом:

__Step 4.__ Start page of the JupyterHub looks like this:

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_8.png?raw=true "Start page")

Можно начинать работать, на стартовой панели есть кнопки для создания ноутбуков, открытия терминала, загрузки (upload) и пр.

You may start working, create notebooks, open terminals, upload files, etc.

____
__ПЕРЕД НАЧАЛОМ РАБОТЫ.__ Домашняя директория содержит следующие папки по умолчанию:

__BEFORE YOU START.__ Your Home directory contains two defaulf folders:

![Alt text](https://github.com/vgarshin/gsom_jhub_manual/blob/master/images/manual_11.png?raw=true "Default folders")

Краткое описание директорий приведено в следующей таблице:

Brief description of the default folders is in the table below:

| ИМЯ ДИРЕКТОРИИ / FOLDER NAME | СОДЕРЖАНИЕ | CONTENT | ВАЖНО ЗНАТЬ | KEY FACTS |
|:---:|:---|:---|:---|:---|
| :file_folder:MANUAL | Настоящий мануал и демо ноутбуки с примерами кода | This manual and basic code snippets | Мануал и демо ноутбуки обновляются и загружаются в папку MANUAL каждый раз, когда запускается Jupyter, поэтому __:x:изменения в папке MANUAL сохраняться не будут__ | Manual and demo notebooks are loaded to MANUAL folder each time your server started, so __:x:your changes in MANUAL folder will not be saved__ |
| :file_folder:SHARED | Предназначена для открытого обмена файлами между всеми пользователями JupyterHub | For sharing files and documents across all users of the JupyterHub | Доступ на чтение, запись и удаление к папке SHARED разрешен всем пользователям, поэтому __:point_up:будьте внимательны при выкладывании в папку SHARED своих материалов__ | All files in SHARED folder are available for read, write of delete for every user, so __:point_up:be careful while sharing files via SHARED folder__ |
| :file_folder:DATA | Предназначена для хранениия учебных материалов и доступна пользователям JupyterHub только на чтение | This is a read-only folder for the teaching materials | Запись в папку доступна только для преподавателей и администраторов | Only teachers and admins can write to this folder |

____
Подробнее о работе в среде Jupyter (JupyterHub) можно прочитать тут: 

User manual for JupyterHub is here:

https://jupyter-notebook.readthedocs.io/en/stable/ 

