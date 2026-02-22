---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 42
style: |
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  .grid-item {
    border: 1px solid #eee;
    padding: 15px;
    border-radius: 5px;
    background-color: #fafafa;
  }
  .text-left {
    text-align: left;
    padding: 5px;
  }
  .image-center {
    max-width: 100%;
    height: auto;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text-large {
    font-size: 40px;
  }
  .text-medium {
    font-size: 30px;
  }
  .text-medium-small {
    font-size: 25px;
  }
  .text-small {
    font-size: 18px;
  }
  .text-tiny {
    font-size: 14px;
  }
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    background-color: #f9f9f9;
  }
  .important-to-remember {
    background-color: #fff3cd;
    border-left: 6px solid #ffecb5;
    padding: 15px;
    margin: 15px 0;
  }
  .borderless {
    border: 0px;
  }
  .task {
    background-color: #e3f2fd;
    border-left: 5px solid #2196f3;
    padding: 15px;
    border-radius: 8px;
  }
  .emoji-large {
    font-size: 3em;
    text-align: center;
    display: block;
  }

---

# Проєкт "Впорядкування даних"

## 🏫 Урок **42**

---

## 🎯 Мета сьогоднішнього уроку

<div class="important-to-remember text-medium">

- 🧠 **Закріпити** навички роботи зі списками в Python.
- 🛠️ **Застосувати** методи сортування `sort()` та функцію `sorted()` на практиці.
- 🚀 **Створити** власні програми для аналізу та обробки даних у межах проєкту.

</div>

---

## ⚡ Бліц-опитування

Пригадаємо вивчене!

<div class="card text-medium-small">

1. Чим відрізняється метод `.sort()` від функції `sorted()`?
2. Як відсортувати список у зворотному порядку (від більшого до меншого)?
3. Які функції допомагають знайти найбільше та найменше значення в списку?

</div>

---

## 🏢 Проєкт "Аналітичний центр"

<div class="text-medium-small">

Уявіть, що ви — розробники програмного забезпечення для збору та аналізу даних.

Ваше завдання на сьогодні: **обробити різні показники** (ціни, температури або бали) та **вивести їх у зручному для користувача вигляді**, використовуючи сортування.

</div>

<div class="text-medium">

- Оберіть рівень, та напишіть програму, щоб виконати завдання.
- Покажіть програму **написану в зошиті** або **знімок екрану з кодом і результатами виконання**.
- Будьте готові пояснити програму, що ви написали.

</div>

<span class="emoji-large">📊 💻 📉</span>

---

## 💻 Практика: Достатній рівень ⭐️ (до 6 балів)

Завдання "Склад магазину"

<div class="task text-small">

1. Скопіюйте код, поданий нижче, в редактор Thonny чи [Python-Online](https://www.onlineide.pro/playground/python).
2. Замініть всі місця в коді, позначені `<_________>`, на відповідні функції чи методи (`sorted()` або `sort()`).

```python
# Початковий список цін на ґаджети в грн.
prices = [12500, 8900, 45000, 15600, 21000]

# 1. Створіть новий список 'sorted_prices', використавши функцію sorted()
sorted_prices = <________>(prices)
print("Оригінальні ціни:", prices)
print("Ціни від найдешевшої до найдорожчої:", sorted_prices)

# 2. Відсортуйте оригінальний список 'prices' за спаданням, не створюючи його копії.
prices.<______>(<__________>)
print("Ціни від найдорожчої до найдешевшої:", prices)
```

---

## 💻 Практика: Середній рівень ⭐️⭐️ (до 9 балів)

<div class="text-medium-small">

Завдання "Метеостанція"

</div>

<div class="task text-medium-small">

В редакторі Thonny чи [Python-Online](https://www.onlineide.pro/playground/python) напишіть програму:

1. Створіть порожній список `weather_data`.
2. За допомогою циклу `for` попросіть користувача ввести температуру повітря за останні 5 днів. (Використайте цикл `for` у поєднанні з функцією `range()`.)
3. Виведіть на екран:
   - Список введених температур (`weather_data`).
   - Температури, відсортовані від найтеплішої до найхолоднішої (використайте параметр `reverse=True`).
   - Середню температуру за період (сума / кількість).

</div>

---

## 💻 Практика: Високий рівень ⭐️⭐️⭐️ (до 12 балів)

Завдання "Турнірна таблиця"

<div class="task text-small">

В редакторі Thonny чи [Python-Online](https://www.onlineide.pro/playground/python) напишіть програму:

1. Запитайте у користувача кількість учасників.
2. Для кожного учасника запитайте кількість набраних балів та додайте їх до списку.
3. Програма повинна:
   - Відсортувати бали від найбільшого до найменшого.
   - Визначити та надрукувати "Топ-3" результати (використовуйте зрізи `[:3]` або `[0:3]`).
   - Вивести повідомлення: "Переможець набрав: {максимальний бал}" (замініть `{максимальний бал}` на найбільший бал у списку).
   - Вивести повідомлення: "Другому місцю не вистачило: {різниця}" (замініть `{різниця}` на різницю між першим і другим елементом відсортованого списку).

</div>
