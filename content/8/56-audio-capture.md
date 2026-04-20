---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 56
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

# Захоплення аудіо. Перетворення аудіо форматів

## 🏫 Урок **56**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке захоплення аудіо та які програми для цього існують
- 🔧 Як записати голос та накласти фонову музику в Audacity
- ✏️ Як експортувати у FLAC та конвертувати файл в MP3 онлайн

---

## ❓ Пригадаємо

- Яка різниця між **MP3** та **FLAC**?
- Що таке стиснення **без втрат**?
- Яку частоту дискретизації вважають стандартом?
- Які програми для роботи з аудіо ви знаєте?

---

## 🎤 Що таке захоплення аудіо?

<div class="card">

**Захоплення аудіо** — перетворення аналогового звуку (голос, інструменти, середовище) на цифровий сигнал за допомогою **АЦП** (аналогово-цифрового перетворювача) та запис у файл.

</div>

<div class="text-medium">

**Ключові параметри запису:**

| Параметр | Стандарт | Відео/Студія |
|----------|----------|--------|
| Частота дискретизації | 44 100 Гц | 48 000 Гц |
| Розрядність | 16 біт | 24 біт |
| Канали | Стерео (2) | Стерео / Моно |

</div>

---

## 🛠️ Програми для захоплення аудіо

<section class="grid-container">
<div class="text-left text-medium-small">

🪟 **Диктофон Windows**
Вбудований, безкоштовний
Простий запис → M4A

🎚️ **Audacity**
Безкоштовний, потужний
Запис + редагування + мультитрек

</div>
<div class="text-left text-medium-small">

🎛️ **Adobe Audition**
Комерційний, студійний
Шумозниження, мастеринг

🌐 **Vocaroo.com**
Онлайн, без реєстрації
Швидкий запис прямо в браузері

</div>
</section>

---

## 🎚️ Інтерфейс Audacity

<section class="card">

- 🎵 **Треки** — горизонтальні смуги з аудіохвилями
- ⏱️ **Часова шкала** — орієнтація у часі
- 🔊 **Gain** — повзунок гучності кожного треку
- ✂️ **Інструменти:** виділення, переміщення, масштаб

</section>

<section class="important-to-remember">

💡 Audacity підтримує роботу з кількома треками одночасно — це називається **мультитрековий запис**.

</section>

---

<!-- _class: lead -->

## 🎬 Відеоінструкція

**Дивіться покрокову відеоінструкцію до практичної роботи:**

<!-- ▼▼▼ ВСТАВТЕ ПОСИЛАННЯ НА YOUTUBE НИЖЧЕ ▼▼▼ -->
### 👉 <a href="https://www.youtube.com/watch?v=hHqQ2Q31jiA" target="_blank">Посилання на відео</a>

![QR-код для переходу до покрокової відеоінструкції на YouTube w:200px](./assets/qr-video-56.png)

---

## 🎵 Фонова музика для завдання

**Завантажте файл фонової музики:**

### 👉 <a href="https://drive.google.com/file/d/1s5NhK0By-XqalGc6jQ2hKqeSkVs4a_bh/view?usp=sharing" target="_blank">Завантажити музику</a>

> Файл надано вчителем. Музика використовується лише в навчальних цілях.

---

<section class="task">

## ⌨️ Практична робота — Кроки 1 та 2

<div class="text-medium">

**Крок 1 — Запис голосу:**
1. Відкрити **Audacity**
2. Перевірити мікрофон у панелі пристроїв
3. Натиснути ⏺️ **Запис** → прочитати 3–5 речень
4. Натиснути ⏹️ **Стоп**

**Крок 2 — Імпорт музики:**
5. Файл → Імпорт → Звукові дані...
6. Відкрити файл музики (посилання на попередньому слайді)

</div>
</section>

---

<section class="task">

## ⌨️ Практична робота — Кроки 3 та 4

<div class="text-medium">

**Крок 3 — Зменшення гучності музики:**
1. На панелі музичного треку знайти повзунок **Gain**
2. Зменшити до **−10 dB**
3. ▶️ Відтворити — перевірити баланс голосу і музики

**Крок 4 — Обрізання зайвої музики:**
4. Виділити частину музичного треку після закінчення голосу
5. Натиснути **Delete**
6. ▶️ Відтворити для перевірки

</div>
</section>

---

<section class="task">

## ⌨️ Практична робота — Кроки 5 та 6

**Крок 5 — Експорт у FLAC:**
1. Файл → Експортувати → **Експортувати як FLAC**
2. Зберегти як `audio_56_прізвище.flac`

**Крок 6 — Конвертація FLAC → MP3:**
3. Відкрити **<a href="https://online-audio-converter.com" target="_blank">online-audio-converter.com</a>**
4. Вибрати: FLAC → MP3
5. Завантажити файл → конвертувати → скачати 🎉

</section>

---

## 🔄 Чому FLAC → MP3, а не одразу MP3?

<section class="grid-container">
<div class="card text-left text-medium-small">

**FLAC** — архів без втрат
✅ Зберігає 100% якості
✅ Ідеально для редагування
❌ Великий розмір файлу

</div>
<div class="card text-left text-medium-small">

**MP3** — стиснення з втратами
✅ Малий розмір (~10× менше)
✅ Сумісний з усіма пристроями
❌ Якість не повернути назад

</div>
</section>

<section class="important-to-remember">

💡 Правило: **редагуй у FLAC → ділись у MP3**. Конвертація — завжди в кінці роботи.

</section>

---

## 🤔 Рефлексія

- Навіщо спочатку зберігати у **FLAC**, а потім конвертувати в **MP3**?
- Чим відрізняється Audacity від стандартного **Диктофону Windows**?
- Де у житті може знадобитись запис та обробка аудіо?

---

## 🏠 Домашнє завдання

1. 📖 Опрацювати матеріал підручника **с. 207–211**
