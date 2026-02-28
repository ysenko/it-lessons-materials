---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 44
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
  pre {
    background-color: #f6f8fa;
    color: #1f2328;
    border: 1px solid #d0d7de;
    padding: 10px;
    border-radius: 6px;
    font-size: 16px;
    line-height: 1.2;
    overflow-x: auto;
  }
  pre code {
    color: #1f2328;
  }

---

# Створення онлайн-документів

## 🏫 Урок **44**: Wiki та Markdown

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке Wiki та хто її створив
- 🛡️ Як Wiki захищається від вандалізму
- ✏️ Що таке Markdown і як ним користуватись
- 🚀 Як опублікувати статтю онлайн

---

## 🌐 Що таке Wiki?

<div class="important-to-remember">

**Вікі (англ. wiki)** — це технологія для створення сайтів, які можна спільно редагувати. Вікі дозволяє багатьом людям разом писати, зберігати та змінювати текст, гіпертекст, файли та зображення.

</div>

- **Назва:** від гавайського "wiki-wiki" — *швидко*
- **Принцип:** кожен може редагувати вміст

---

## 📜 Історія Wiki

<div class="grid-container">
  <div class="grid-item">
    <div class="emoji-large">👤</div>

**Вард Каннінгем**

Автор Wiki

  </div>
  <div class="grid-item">
    <div class="emoji-large">📅</div>

**1995 рік**

Запуск WikiWikiWeb

  </div>
  <div class="grid-item">
    <div class="emoji-large">💡</div>

**Мета**

Швидка спільна документація

  </div>
</div>

---

## 🛡️ Безпека у Wiki

Оскільки редагувати може будь-хто, існує ризик **вандалізму** (шкідливих змін).

- **Історія версій:** можна швидко повернути попередній стан сторінки
- **Патрулювання:** волонтери перевіряють нові правки
- **Внутрішні посилання:** `[[назва сторінки]]` — швидко створює посилання

---

## 📝 Що таке Markdown?

<div class="important-to-remember">

**Markdown** — це проста мова розмітки для створення структурованих документів за допомогою звичайного тексту.

</div>

- **Винахідники:** Джон Грубер, Аарон Шварц
- **Рік:** 2004
- **Перевага:** текст легко читати навіть без перетворення в HTML

---

## 🛠️ Синтаксис Markdown

| Елемент         | Код                   |
| :-------------- | :-------------------- |
| Заголовок       | `# Заголовок`         |
| Підзаголовок    | `## Підзаголовок`     |
| Жирний текст    | `**текст**`           |
| Курсив          | `*текст*`             |
| Список          | `- елемент`           |
| Зображення      | `![опис](посилання)`  |
| Посилання       | `[назва](посилання)`  |

---

## 💻 Практична робота

<div class="task">

1. Перейдіть на сайт [publishmarkdown.com](https://publishmarkdown.com/)
2. Скопіюйте текст з наступного слайда, використовуючи Markdown
3. Додайте заголовок, підзаголовок, список, посилання, цитату та зображення
4. Опублікуйте документ

</div>

---

## 📄 Зразок Markdown-коду

```markdown
# Історія створення Wiki та Markdown
Технологію **Wiki** винайшов програміст Вард Каннінгем у 1995 році. Це дозволило людям швидко створювати спільні вебсторінки.

## Що таке Markdown?
У 2004 році Джон Грубер створив мову розмітки Markdown. Її переваги:
- Легко читати
- Просто писати
- Швидко вчити
Більше інформації є у [Вікіпедії](https://uk.wikipedia.org/wiki/Markdown).

## Цікавий факт
> Слово "wiki" походить з гавайської мови і означає "швидко".

![Логотип Markdown](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```
