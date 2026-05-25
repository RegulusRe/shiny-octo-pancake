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