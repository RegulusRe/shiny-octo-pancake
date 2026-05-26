import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig

from tools.common_tools import format_text, count_words

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи цікаву історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='creative_writer',
    description="Креативний письменник історій.",
    instruction="""
    Ти талановитий письменник який створює захоплюючі історії українською мовою.
    У тебе також є спільні інструменти:
    - format_text (для зміни регістру тексту)
    - count_words (для підрахунку кількості та унікальності слів в історіях)
    Використовуй їх, коли користувач просить проаналізувати текст або змінити його вигляд.
    """,
    tools=[generate_story_prompt, format_text, count_words],
    generate_content_config=GenerateContentConfig(
        temperature=1.3,
        top_k=40,
        top_p=0.95,
    )
)