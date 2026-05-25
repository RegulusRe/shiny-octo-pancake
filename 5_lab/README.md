# Звіт до роботи
## Тема: Основні парадигми ООП
### Мета роботи: Ознайомитись з ключовими поняттями об’єктно-орієнтованого програмування (ООП) у Python та навчитися реалізовувати їх у власних класах на прикладі ігрової симуляції.

---
### Виконання роботи
* Результати виконання завдання №1;
    1. Добавив

    ```for _ in range(5):
    deposit_amount = random.randint(50, 200)
    withdraw_amount = random.randint(20, 100)
    
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)

    print(f"Кінцевий баланс: {account.get_balance()}")
    ```
    1. Програма вивела значення ...

    ```Кінцевий баланс: 1396```
* Результати виконання завдання №2;
    1. Добавив

    ``` 
        def start_engine(self):
        return "Двигун запущено! Врум-врум!"

        print(car.start_engine())
    ```
    1. Програма вивела значення ...

    ```
    Toyota Camry, Seats: 5
    Двигун запущено! Врум-врум!
    ```
* Результати виконання завдання №3;
    1. Добавив

    ```
    class Fish(Animal):
    pass

    animals = [Dog(), Cat(), Fish()]
    ```
    1. Програма вивела значення ...

    ```
    Dog каже: Woof!
    Cat каже: Meow!
    Fish каже: None
    ```
* Результати виконання завдання №4;
    1. Добавив

    ```
    class Bow(Item):
    def __init__(self, name, attack_power:int, range_power:int = 0):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power
        
    def attack(self, another_item:Item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"Стріляємо з лука {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"
        
    def reload(self):
        self.range_power += 5
        return f"Лук натягнуто сильніше! Додаткова дальність/шкода: {self.range_power}"


        def get_random_weapon():
    weapons = [Sword("Ескалібур", 50), Axe("Кратос", 45), Bow("Леголас", 40)]
    return random.choice(weapons)

    player = get_random_weapon()
    enemy = get_random_weapon()


    while player.health > 0 and enemy.health > 0:
    choice = input("Ваш вибір (1 - Атака, 2 - Підсилення): ")
    
    if choice == '1':
        print(player.attack(enemy))
    elif choice == '2':
        if isinstance(player, Sword):
            print(player.sharpening())
        elif isinstance(player, Bow):
            print(player.reload())
        else:
            print("Сокира не має підсилення, ви пропускаєте хід!")
    ```
    1. Програма вивела значення ...

    ```
     === ПОЧАТОК ГРИ ===
    Ваша зброя: Sword 'Ескалібур' (HP: 500)
     ворога: Sword 'Ескалібур' (HP: 500)
    -------------------

    --- Раунд 1 ---
    Ваш хід! Оберіть дію:
    1 - Атакувати
    2 - Заточити меч (+ до шкоди)
    Завдаємо удару мечем Ескалібур та наносимо 53 шкоди. У Ескалібур залишалось здоровя: 447

    Хід ворога...
    Завдаємо удару мечем Ескалібур та наносимо 60 шкоди. У Ескалібур залишалось здоровя: 440

    --- Раунд 2 ---
    Ваш хід! Оберіть дію:
    1 - Атакувати
    2 - Заточити меч (+ до шкоди)
    Меч заточено! Додаткова шкода: 5

    Хід ворога...
    Завдаємо удару мечем Ескалібур та наносимо 56 шкоди. У Ескалібур залишалось здоровя: 384

    --- Раунд 3 ---
    Ваш хід! Оберіть дію:
    ...
    Хід ворога...
    Завдаємо удару мечем Ескалібур та наносимо 57 шкоди. У Ескалібур залишалось здоровя: -4

    💀 Ви програли! Зброя Ескалібур знищила Ескалібур.
    ```