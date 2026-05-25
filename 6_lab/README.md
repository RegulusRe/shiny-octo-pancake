# Віртуальні середовища
## Тема: Основні парадигми ООП
### Мета роботи: ...

---
### Виконання роботи
* Результати виконання завдання №1;
    1. Ввів

    ```python 
        pip list
    ```
    1. Програма вивела значення ...

    ```python 
    Package                 Version
    ----------------------- -----------
    aiohappyeyeballs        2.6.1
    aiohttp                 3.11.16
    aiohttp-retry           2.9.1
    aiosignal               1.3.2
    annotated-doc           0.0.3
    annotated-types         0.7.0
    anyio                   4.11.0
    asttokens               3.0.0
    attrs                   25.3.0
    babel                   2.17.0
    bcrypt                  5.0.0
    blinker                 1.9.0
    certifi                 2025.1.31
    cffi                    1.17.1
    charset-normalizer      3.4.1
    click                   8.1.8
    colorama                0.4.6
    comm                    0.2.3
    coverage                7.12.0
    cryptography            44.0.2
    debugpy                 1.8.17
    decorator               5.2.1
    dnspython               2.8.0
    ecdsa                   0.19.1
    email-validator         2.3.0
    executing               2.2.1
    fastapi                 0.120.0
    Flask                   2.3.2
    flask-babel             4.0.0
    Flask-Login             0.6.3
    Flask-SQLAlchemy        3.0.3
    frozenlist              1.5.0
    greenlet                3.1.1
    h11                     0.16.0
    httpcore                1.0.9
    httpx                   0.28.1
    idna                    3.10
    iniconfig               2.3.0
    ipykernel               6.30.1
    ipython                 9.5.0
    ipython_pygments_lexers 1.1.1
    itsdangerous            2.2.0
    jedi                    0.19.2
    Jinja2                  3.1.6
    jupyter_client          8.6.3
    jupyter_core            5.8.1
    MarkupSafe              3.0.2
    matplotlib-inline       0.1.7
    multidict               6.3.2
    mysql-connector-python  8.0.33
    nest-asyncio            1.6.0
    packaging               25.0
    parso                   0.8.5
    passlib                 1.7.4
    pip                     25.2
    platformdirs            4.4.0
    pluggy                  1.6.0
    prompt_toolkit          3.0.52
    propcache               0.3.1
    protobuf                3.20.3
    psutil                  7.1.0
    pure_eval               0.2.3
    pyasn1                  0.6.1
    pycparser               2.22
    pydantic                2.12.3
    pydantic_core           2.41.4
    Pygments                2.19.2
    PyJWT                   2.10.1
    PyMySQL                 1.1.1
    pyTelegramBotAPI        4.26.0
    pytest                  8.4.2
    pytest-asyncio          1.3.0
    pytest-cov              7.0.0
    python-dateutil         2.9.0.post0
    python-dotenv           1.1.1
    python-jose             3.5.0
    python-multipart        0.0.20
    pytz                    2025.2
    pywin32                 311
    pyzmq                   27.1.0
    requests                2.32.3
    rsa                     4.9.1
    six                     1.17.0
    sniffio                 1.3.1
    SQLAlchemy              2.0.40
    stack-data              0.6.3
    starlette               0.48.0
    tornado                 6.5.2
    traitlets               5.14.3
    twilio                  9.5.1
    typing_extensions       4.15.0
    typing-inspection       0.4.2
    urllib3                 2.3.0
    uvicorn                 0.38.0
    wcwidth                 0.2.13
    Werkzeug                3.1.3
    yarl                    1.18.3
    ```
* Результати виконання завдання №2;
    1. Ввів

    ``` 
     pip install requests
    ```
    1. Програма вивела значення ...

    ```python
    Requirement already satisfied: requests in c:\users\master\appdata\local\programs\python\python313\lib\site-packages (2.32.3)
    Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\master\appdata\local\programs\python\python313\lib\site-packages (from requests) (3.4.1)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\master\appdata\local\programs\python\python313\lib\site-packages (from requests) (3.10)
    Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\master\appdata\local\programs\python\python313\lib\site-packages (from requests) (2.3.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\master\appdata\local\programs\python\python313\lib\site-packages (from requests) (2025.1.31)

    [notice] A new release of pip is available: 25.2 -> 26.1.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    ```
* Результати виконання завдання №3;
    1. Добавив

    ```python
    import requests
    requests.__version__
    r = requests.get('https://google.com')
    r.status_code
    ```
    1. Програма вивела значення ...

    ```python
    200
    ```
* Результати виконання завдання №4;
    1. Добавив

    ```python
    from flask import Flask, render_template
    from jikanpy import Jikan

    jikan = Jikan()
    app = Flask(__name__)

    ANIME_ID = 61316

    anime_info = jikan.anime(ANIME_ID)
    anime_title = anime_info["data"]["title"]

    episodes_info = jikan.anime(ANIME_ID, extension='episodes')

    @app.route('/')
    def home():
        html_content = f"<h1>Список епізодів для аніме: {anime_title}</h1>\n"
        
        for episode in episodes_info["data"]: 
            html_content += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}</p>\n"
            
        return html_content

    @app.route('/about')
    def about():
        return render_template('about.html')

    if __name__ == '__main__':
    app.run(debug=True)
    ```
    1. Програма вивела значення ...

    ```
    Список епізодів для аніме: Re:Zero kara Hajimeru Isekai Seikatsu 4th Season
    Епізод 1 з назвою: The Reason I'm Taking You With Me / Gorgeous Tiger Reloaded має оцінку 4.41

    Епізод 2 з назвою: Overcome Sand Time має оцінку 4.74

    Епізод 3 з назвою: The Keeper of the Watchtower має оцінку 4.76

    Епізод 4 з назвою: A White Sky Asterism має оцінку 4.55

    Епізод 5 з назвою: Stick Swinger має оцінку 4.5

    Епізод 6 з назвою: Julius Juukulius має оцінку 4.65

    Епізод 7 з назвою: Walking Out of the Convenience Store and Into a Wondrous World має оцінку 4.54
    ```
    * Результати виконання завдання №5;
    1. Ввів

    ``` 
    pip show requests
    ```
    1. Програма вивела значення ...

    ```python
    Name: requests
    Version: 2.32.3
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache-2.0
    Location: C:\Users\Master\AppData\Local\Programs\Python\Python313\Lib\site-packages
    Requires: certifi, charset-normalizer, idna, urllib3
    Required-by: jikanpy-v4, pyTelegramBotAPI, twilio
    ```
    * Результати виконання завдання №6;
    1. Ввів

    ``` 
    pipenv run python test_api.py
    ```
    1. Програма вивела значення ...

    ```python
        PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab> pipenv run python test_api.py
    b'<!DOCTYPE html>'
    b'<html lang="en">'
    b''
    b'<head>'
    b'    <meta charset="UTF-8">'
    b'    <title>httpbin.org</title>'
    b'    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"'
    b'        rel="stylesheet">'
    b'    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">'
    b'    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />'
    b'    <style>'
    b'        html {'
    b'            box-sizing: border-box;'
    b'            overflow: -moz-scrollbars-vertical;'
    b'            overflow-y: scroll;'
    b'        }'
    b''
    ```


    * Результати виконання завдання №7;
    1. Вибрав бібліотеку art, ввів

    ``` python
    from art import tprint
    tprint("PIPENV")
    ```
    1. Програма вивела значення ...

    ```python
     ____   ___  ____   _____  _   _ __     __
    |  _ \ |_ _||  _ \ | ____|| \ | |\ \   / /
    | |_) | | | | |_) ||  _|  |  \| | \ \ / / 
    |  __/  | | |  __/ | |___ | |\  |  \ V /  
    |_|    |___||_|    |_____||_| \_|   \_/   
                                          
    ```


    * Результати виконання завдання №8;
    1. Ввів

    ``` 
    pipenv install --dev flake8
    ```
    1. Програма вивела значення ...

    ```python
    [dev-packages]
    flake8 = "*"
    ```


    * Результати виконання завдання №9;
    1. Ввів

    ``` 
    pipenv check --scan та pipenv audit
    ```
    1. Програма вивела значення ...

    ```python
    026-05-25 21:51:11 UTC

    Account: API key used
    Git branch: main
    Environment: cicd
    Scan policy: None, using Safety CLI default policies

    C:\Users\Master\.virtualenvs\6_lab-GRk1oT79\Lib\site-packages\safety\auth\main.py:6: AuthlibDeprecationWarning: authlib.jose module is deprecated, please use joserfc instead.
    It will be compatible before version 2.0.0.
    from authlib.jose import jwt
    Your authentication credential 'dummy-key' is invalid. See https://docs.safetycli.com/safety-docs/support/invalid-api-key-error.


    Auditing packages for vulnerabilities...
    pip-audit is required for vulnerability scanning but not installed.
    Would you like to install pip-audit? This will not modify your Pipfile/lockfile. [y/n] (y): y
    Installing pip-audit...
    pip-audit installed successfully!
    No known vulnerabilities found
    ```


    * Результати виконання завдання №10;
    1. Ввів

    ``` python
    import os
    print(f"Значення змінної IT_TEST = {os.environ['IT_TEST']}")
    ```
    1. Програма вивела значення ...

    ```python
    KeyError: 'IT_TEST'
    ```


    * Результати виконання завдання №11;
    1. Ввів

    ``` python
    poetry new myproject
    cd myproject
    poetry add requests
    poetry show --tree
    ```
    1. Програма вивела значення ...

    ```python
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab> poetry new myproject
    Created package myproject in myproject
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab> poetry add requests

    Poetry could not find a pyproject.toml file in C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab or its parents
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab> cd myproject
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab\myproject> poetry add requests
    Creating virtualenv myproject-cnb2gEBy-py3.13 in C:\Users\Master\AppData\Local\pypoetry\Cache\virtualenvs

    Updating dependencies
    Resolving dependencies... (0.8s)

    Package operations: 5 installs, 0 updates, 0 removals
    - Installing certifi (2026.5.20)
    - Installing charset-normalizer (3.4.7)
    - Installing idna (3.16)
    - Installing urllib3 (2.7.0)
    - Installing requests (2.34.2)
    Writing lock file
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab\myproject> poetry show
    certifi            2026.5.20 Python package for providing Mozilla's CA Bundle.
    charset-normalizer 3.4.7     The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
    idna               3.16      Internationalized Domain Names in Applications (IDNA)
    requests           2.34.2    Python HTTP for Humans.
    urllib3            2.7.0     HTTP library with thread-safe connection pooling, file post, and more.
    PS C:\Users\Master\Desktop\Папка\Нова папка (2)\shiny-octo-pancake\6_lab\myproject> poetry show --tree
    requests 2.34.2 Python HTTP for Humans.
    ├── certifi >=2023.5.7
    ├── charset-normalizer >=2,<4
    ├── idna >=2.5,<4
    └── urllib3 >=1.26,<3
    ```


    * Результати виконання завдання №12;
    1. Ввів

    ``` python
    from flask import Flask
    from jikanpy import Jikan

    app = Flask(__name__)
    jikan = Jikan()

    @app.route('/')
    def home():
        return """
        <h1>Вітаємо на нашому сайті!</h1>
        <p>Це програма, створена за допомогою ШІ та запущена через Poetry.</p>
        <p><a href='/anime'>Натисніть тут, щоб переглянути список епізодів аніме</a></p>
        """

    @app.route('/anime')
    def anime_info():
        ANIME_ID = 61316 # ID для Re:Zero
        
        # Отримуємо назву аніме
        anime_data = jikan.anime(ANIME_ID)
        anime_title = anime_data["data"]["title"]
        
        # Отримуємо епізоди
        episodes_info = jikan.anime(ANIME_ID, extension='episodes')
        
        html = f"<h1>Список епізодів для аніме: {anime_title}</h1>\n"
        for episode in episodes_info["data"]: 
            html += f"<p>Епізод {episode['mal_id']}: {episode['title']} — Оцінка: {episode['score']}</p>\n"
            
        return html

    if __name__ == '__main__':
        # Запускаємо сервер
        app.run(debug=True)
    ```
    1. Програма вивела значення ...

    ```python
    Вітаємо на нашому сайті!
    Це програма, створена за допомогою ШІ та запущена через Poetry.

    Натисніть тут, щоб переглянути список епізодів аніме
    ```
