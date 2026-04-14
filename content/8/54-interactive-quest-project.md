---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 54
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
    max-width: 100%; /* Ensures the image scales within its space */
    height: auto;
    text-align: center;
    display: flex;
    flex-direction: column;
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

# ♻️ Створення інтерактивного квесту

## 🏫 Урок **54**

---

## 🎯 План заняття

1.  🔄 **Повторення:** посилання на матеріали [уроків 51, 52 та 53](#3).
2.  🧩 **Логіка:** як побудувати дерево рішень у документі.
3.  💻 **Практика:** проект «Поради для тих, хто хоче врятувати світ».
4.  🎮 **Тест-драйв:** проходимо квести один одного.

---

## 📚 Що нам знадобиться?

Згадайте інструменти, які ми вивчали раніше:

<div class="grid-container">
  <div class="grid-item">
    <a href="https://ysenko.github.io/it-lessons-materials/8/51-ai-image-generation.html" target="_blank" rel="noopener noreferrer">🖼️ Урок 51: Штучний інтелект та зображення</a>
  </div>
  <div class="grid-item">
    <a href="https://ysenko.github.io/it-lessons-materials/8/52-text-docs-automation.html" target="_blank" rel="noopener noreferrer">🤖 Урок 52: Автоматизовані засоби опрацювання текстових документів</a>
  </div>
  <div class="grid-item">
    <a href="https://ysenko.github.io/it-lessons-materials/8/53-document-structure-links-toc.html" target="_blank" rel="noopener noreferrer">📑 Урок 53: Структура документа. Гіперпосилання в текстових документах. Автоматизоване створення змісту документа</a>
  </div>
</div>

---

## 🌍 Проєкт: «Рятуємо планету!»

Ваше завдання — створити в **Google Документах** гру, де читач приймає рішення.

<div class="card text-medium">

**Алгоритм роботи:**

  1. Кожна сцена — на окремій сторінці (**Вставити → Розрив сторінки**).
  2. Варіанти дій — це гіперпосилання, що ведуть на Закладки.

</div>

**[Приклад виконаного квесту (Рівень 2)](https://docs.google.com/document/d/1Y2iH7UK__8LNSz4613TaYnysCRAbYY6KqmxPLRcrbEY/edit?usp=sharing)**

---

## � Порада: Як зробити кнопку (посилання)?

1. Напишіть текст (наприклад, "ВИМКНУТИ СВІТЛО").
2. Виділіть його.
3. Перейдіть в меню **Вставити → Посилання**  (або натисніть `Ctrl + K`).
4. Оберіть **Заголовки, закладки і вкладки** та оберіть потрібний заголовок.

---

## �🟢 Рівень 1: «Еко-активіст» (максимум 9 балів)

<div class="task">

- Титульна сторінка з назвою квесту та автором
- Мінімум **2 вибори** (запитання або ситуації), кожен на окремій сторінці. Кожен вибір має **2 розгалуження** — один вибір екологічний/позитивний, інший — шкідливий/негативний.
- Автоматичний зміст на початку.
- Використання стилів Заголовок 1, 2.

</div>

---

## 🚀 Рівень 2: «Еко-герой» (максимум 12 балів)

<div class="task">

- Мінімум **4 вибори** (запитання або ситуації) з **2 розгалуженнями** кожен.
- **ШІ-ілюстрації:** унікальна картинка для кожної сторінки (мінімум 2 ілюстрації).
- **Навігація:** кнопка «На старт» на кожній сторінці.
- **Оформлення:** колонтитули з назвою квесту та нумерацією сторінок.

</div>

---

## 🏠 Домашнє завдання

1.  Завершити квест та відкрити доступ за посиланням.
2.  Поділитися документом з вчителем yuriy.senko.o@gmail.com
