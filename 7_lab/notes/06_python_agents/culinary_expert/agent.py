import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from google.adk.agents.llm_agent import Agent

def scale_recipe(current_portions: int, target_portions: int, base_amount: float) -> dict:
    """
    Пропорційно змінює кількість інгредієнта для нової кількості порцій (з перевіркою вводу).
    
    Args:
        current_portions: на скільки порцій розрахований оригінальний рецепт
        target_portions: на скільки порцій потрібно перерахувати
        base_amount: оригінальна кількість інгредієнта
    """
    if current_portions <= 0 or target_portions <= 0:
        return {"error": "Кількість порцій має бути більшою за нуль!", "result": None}
    if base_amount <= 0:
        return {"error": "Кількість інгредієнта має бути більшою за нуль!", "result": None}
        
    multiplier = target_portions / current_portions
    return {"error": None, "result": round(base_amount * multiplier, 2)}

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='culinary_expert',
    description="Кулінарний експерт для точного розрахунку пропорцій.",
    instruction="""
    Ти досвідчений шеф-кухар. Твоя спеціалізація — азіатська кухня (локшина вок, ферментація кімчі тощо), але ти чудово знаєшся на всьому.
    Твоє головне завдання: допомагати масштабувати рецепти за допомогою інструменту scale_recipe.
    Завжди перевіряй наявність помилок від інструменту. Відповідай українською мовою та давай короткі поради щодо балансу смаків.
    """,
    tools=[scale_recipe],
)