---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 57
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

# 🎥 Захоплення відео. Засоби перетворення відеоформатів

## 🏫 Урок **57**

---

## 🎯 Сьогодні ми дізнаємося

- 📹 Які способи захоплення відеозмісту існують
- 🎬 Як записувати одночасно екран та своє зображення
- 📊 Які видеоформати існують і де вони застосовуються
- 🔧 Як працює Google Vids для створення презентацій

---

## 🔄 Актуалізація попередніх знань

Опитування про аудіо:

1. Що таке аудіозапис?
2. Назвіть способи захоплення аудіо
3. Які аудіоформати ви знаєте?
4. Для чого потрібна обробка аудіофайлів?
5. Що таке кодек?

---

## 🎬 Способи захоплення відео

<section class="grid-container">

<div class="grid-item">

### 📹 Камера
Запис через вебкамеру, мобільний телефон

</div>

<div class="grid-item">

### 🖥️ Екран монітора
Screen recording — запис того, що виділяється на екрані

</div>

<div class="grid-item">

### 🎥 Комбінований запис
Одночасний запис екрану та вашого зображення у камері

</div>

</section>

---

## 🎯 Комбінований запис у Google Vids

<section class="card text-medium-small">

Це найпотужніший спосіб для пояснювальних відео!

**Що видно на екрані**:

- Ваше обличчя у куті екрану
- Екран комп'ютера в основній частині
- Все це синхронізовано в одному файлі

**Коли це використовується**:

- Онлайн-уроки (з додатковим вибором OBS Studio у разі недоступності Google Vids)
- Презентації з вашою участю
- Пояснення алгоритмів та процесів

</section>

---

## 📊 Відеоформати

<div class="grid-container text-medium">

<div class="grid-item">

**MP4** (.mp4)

- 📱 YouTube, мобільні пристрої
- ✅ Універсальний

</div>

<div class="grid-item">

**WebM** (.webm)

- 🌐 Веб-трансляції
- 📊 Оптимізований для Інтернету

</div>

<div class="grid-item">

**AVI** (.avi)

- 💾 Архівне зберігання
- 🎞️ Редагування

</div>

</div>

---

## 🔑 Ключові поняття

<section class="card">

**Розширення файлу** або контейнер (.mp4, .webm, .avi)
Визначає формат та як його відтворювати

</section>

<section class="card">

**Кодек**
Алгоритм компресії даних, що впливає на якість та розмір файлу

</section>

<section class="card">

**Розрішення**
Розмір зображення в пікселах (1920×1080, 1280×720)

</section>

<section class="card">

**Частота кадрів (FPS)**
Кількість кадрів на секунду (24, 30, 60 FPS)

</section>

---

## ⚠️ Важливо запам'ятати

<section class="important-to-remember">

Різні пристрої та платформи підтримують різні формати!

Наприклад:

- YouTube краще працює з MP4 ✅
- Старіші мобільні телефони можуть не підтримувати новіші кодеки ❌

</section>

---

## 🎬 Цікавий факт

На YouTube **кожну хвилину** завантажується більше як **500 годин** відеоматеріалу! 🚀

Кожен з цих файлів оптимізується та обробляється для різних пристроїв та інтернет-швидкостей.

---

## ⌨️ Практичне завдання

<section class="task text-medium">

### Запис презентації з вашим участю у Google Vids

**Що вам потрібно зробити**:

1. Відкрити Google Vids (<a href=https://vids.google.com target="_blank">https://vids.google.com</a>) або OBS Studio (завантажити за <a href=https://obsproject.com target="_blank">посиланням</a>).
2. Створити новий проект
3. **Записати коротке відео (30-60 секунд)** з одночасним показом:
   - Вашого зображення в камері
   - Екрану комп'ютера

</section>

---

## 🎯 Теми для запису — виберіть одну

1. 💭 Поясніть як працює **Інтернет**
2. 💻 Розповідайте як розв'язати просту **задачу з програмування**
3. 🔍 Продемонструйте **цікавий факт про комп'ютери**
4. 📖 Пояснення як використовувати **будь-яку програму** на комп'ютері

---

## ✨ Опціонально додайте

- 🎵 Музичний фон (Google Vids пропонує безкоштовну музику)
- 📝 Титри та текст на екран
- 🎨 Фільтри або ефекти

---

## ✅ Критерії оцінювання

<section class="card">

✓ Відео записано з одночасним показом **екрану та вашого зображення**

✓ Тривалість **30-60 секунд**

✓ **Змістовне пояснення** на одну з запропонованих тем

✓ Файл успішно **експортований у форматі MP4**

✓ Файл має **описову назву**

</section>

---

## 🤔 Рефлексія

Обговоримо ваші враження:

1. Що було найцікавішим при роботі з Google Vids?
2. Якими розширеннями файлів ви користуєтеся найчастіше вдома?
3. Чому важливо одночасно записувати екран та себе під час створення пояснювальних відео?
4. Які проблеми ви зустріли? Як їх вирішити?

---

## 🏠 Домашнє завдання

<div class="text-medium">

### Основне (обов'язкове)

<div class="task">

Опрацюйте матеріал з підручника с. 211-216

</div>

### 🔗 Корисні посилання

- 🎬 **Google Vids**: https://vids.google.com
- 📚 **Довідка про відеоформати**: https://developer.mozilla.org/en-US/docs/Web/Media/Formats
- 🎥 **OBS Studio** (захоплення екрану): https://obsproject.com

</div>
