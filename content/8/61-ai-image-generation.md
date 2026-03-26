---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 61
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

# Штучний інтелект та зображення

## Етичні норми використання згенерованих зображень

## 🏫 Урок **61**

---

## 🎯 Сьогодні ми дізнаємося

- 🤖 Як ШІ створює зображення з "хаосу".
- 📝 Як правильно писати запити (промпти).
- ⚖️ Яких етичних правил слід дотримуватися.
- 🎨 Створимо власну ілюстрацію до книги чи фільму.

---

## 🧐 Актуалізація: ШІ чи Реальність?

<div class="grid-container">
  <div class="grid-item">

**Завдання:** Відскануйте QR-код та пройдіть вікторину.

Спробуйте вгадати: де справжнє фото, а де робота нейромережі?

  </div>
  <div class="grid-item image-center">

![h:300px](./assets/61/qr-code-for-test.png)

  </div>

</div>



---

## ⚙️ Як працює генеративний ШІ?

Сучасні ШІ (DALL-E, Midjourney) використовують **дифузійні моделі**.

1. **Шум:** ШІ починає з абсолютно випадкового набору кольорових крапок.
2. **Очищення:** Крок за кроком він прибирає "шум", шукаючи в ньому форми, які ви описали словами.
3. **Результат:** З хаосу постає чітка картинка.

---

## 📝 Занотуйте в зошит: Конструктор промпту

Щоб ШІ вас зрозумів, запит (промпт) має бути структурованим:

<div class="important-to-remember">

1. **Об’єкт** (Хто? Що?) — головний герой.
2. **Дія** (Що робить?) — поза або сюжет.
3. **Стиль** (Як виглядає?) — художня техніка.
4. **Деталі** (Оточення) — фон, світло, кольори.

</div>

---

## 🎨 Обираємо стиль (Приклади)

Використовуйте ці назви у своїх запитах:

<div class="grid-container">
  <div class="grid-item">

**Cyberpunk**

Майбутнє, неонові вогні

  </div>
  <div class="grid-item">

**Pixar style**

3D мультфільм

  </div>
  <div class="grid-item">

**Watercolor**

Ніжна акварель

  </div>
  <div class="grid-item">

**Sketch**

Начерк олівцем

  </div>
</div>

---

## 💡 Світло та Деталі

Додайте атмосфери вашій роботі:

<div class="grid-container">
  <div class="grid-item">

**Golden hour**

Тепле світло заходу сонця.

  </div>
  <div class="grid-item">

**Neon glow**

Яскраве нічне сяйво.

  </div>
  <div class="grid-item">

**Cinematic**

Вигляд як у професійному кіно.

  </div>
  <div class="grid-item">

**High detail**

Дуже багато дрібних елементів.

  </div>
</div>

---

## ✍️ Приклад промпту: «Володар Перснів»

<div class="text-small">

Застосуємо конструктор до реальної книги:

| Частина | Приклад |
|---|---|
| **Об'єкт** | Фродо Торбин, молодий гобіт |
| **Дія** | стоїть на краю скелі та тримає Перстень |
| **Стиль** | олійний живопис, у стилі Джона Хоу |
| **Деталі** | похмуре небо, відблиски вогню, епічне кінематографічне освітлення |

</div>

> **Готовий промпт:** *Фродо, молодий гобіт, стоїть на краю скелі та тримає Перстень Всевладдя, олійний живопис у стилі Джона Хоу, похмуре штормове небо, відблиски вогню, епічне кінематографічне освітлення, висока деталізація*

---

## Зображення створене на основі промпту

<div class="image-center">

![h:450px](./assets/61/frodo.jpg)

</div>

---

## ⚖️ Етика та правила

<div class="important-to-remember">

- **Маркування:** Етично додавати примітку "Згенеровано ШІ".
- **Ні фейкам:** Заборонено створювати зображення для обману людей (діпфейки).
- **Повага до авторів:** Не видавайте роботу ШІ за свій особистий малюнок від руки.

</div>

---

## 🚀 Практична робота

<div class="task">

**Завдання:** Створити ілюстрацію до улюбленої книги або фільму.

1. Оберіть сцену або персонажа.
2. Складіть промпт: **Об'єкт + Дія + Стиль + Деталі**.
3. Відкрийте **Microsoft Designer** або **Bing Image Creator**.
4. Згенеруйте результат та продемонструйте вчителю.

</div>

---

## 💬 Рефлексія

- Чи легко було підібрати слова, щоб ШІ вас зрозумів?
- Чи відрізняється результат від того, що ви малювали в уяві?
- Чи вважаєте ви себе "автором" цього зображення?

---

## 🏠 Домашнє завдання

1. **Роздуми:** Напишіть 2-3 речення на тему: *"Чому важливо позначати зображення від ШІ у стрічці новин?"*
2. **Опрацювати** конспект уроку.
