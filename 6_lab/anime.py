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