import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from google.adk.agents.llm_agent import Agent

from tools.common_tools import format_text, count_words

def explain_concept(concept: str, level: str = "beginner") -> dict:
    """Пояснює концепцію програмування."""
    explanations = {
        "beginner": f"Базове пояснення концепції {concept}",
        "intermediate": f"Поглиблене пояснення концепції {concept}",
        "advanced": f"Експертне пояснення концепції {concept}"
    }
    return {
        "status": "success",
        "concept": concept,
        "level": level,
        "explanation": explanations.get(level, "Невідомий рівень")
    }

def check_syntax(code: str, language: str = "python") -> dict:
    """Перевіряє синтаксис коду (базова перевірка)."""
    if not code.strip():
        return {"status": "error", "message": "Код порожній"}
    return {"status": "success", "message": "Синтаксис виглядає коректно", "language": language}

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='student_helper',
    description="Помічник для студентів які вивчають програмування.",
    instruction="""
    Ти досвідчений викладач з ООП програмування який допомагає студентам.
    Окрім перевірки синтаксису, ти можеш використовувати спільні інструменти format_text та count_words для форматування коду або аналізу довжини відповідей.
    Завжди відповідай українською мовою.
    """,
    tools=[explain_concept, check_syntax, format_text, count_words],
)