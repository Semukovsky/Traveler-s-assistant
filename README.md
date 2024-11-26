
# Travellers Assistant

**Travellers Assistant** — это приложение, созданное для помощи путешественникам. Оно включает в себя переводчик, разговорник, конвертер валют и другую полезную информацию, необходимую во время путешествий.

---

## 📋 Основные функции
- **Переводчик и разговорник**: перевод текста между различными языками.
- **Популярные места**: информация о туристических достопримечательностях.
- **Конвертер валют**: быстрый пересчет валют для удобства в поездках.
- **Местное время**: отображение времени в выбранной стране.
- **Частые вопросы**: справка с популярными запросами путешественников.

---

## 🔧 Установка и запуск


### 1. Создайте виртуальное окружение и Склонируйте репозиторий
```bash
git clone (https://github.com/Semukovsky/Traveler-s-assistant.git)

Для управления зависимостями проекта создайте виртуальное окружение:
python -m venv venv
```

### 2. Активируйте виртуальное окружение
- Для Windows:
  ```bash
  venv\Scripts\activate
  ```
- Для macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Установите зависимости
Файл `requirements.txt` содержит все необходимые библиотеки:
```bash
pip install -r requirements.txt
```

---

## 🚀 Запуск приложения
После установки всех зависимостей запустите приложение:
```bash
python main.py
```

---

## 🖼️ Интерфейс
Интерфейс приложения включает в себя удобное меню, в котором можно выбрать необходимые функции, такие как перевод текста, информация о местах или конвертация валют. Пример интерфейса:

![Интерфейс Travellers Assistant](./assets/interface_example.png) <!-- Укажите реальный путь, если изображение находится в проекте -->

---

## Технологии

В проекте используются следующие технологии и библиотеки:

- **SQLite** — легковесная реляционная база данных.
- **Peewee 3.17.7** — легковесный ORM для работы с базами данных.
- **PyQt6 6.7.1 / PyQt6-Qt6 6.7.3 / PyQt6-sip 13.8.0** — библиотека для создания графического интерфейса пользователя (GUI).
- **CurrencyConverter 0.17.34** — библиотека для работы с конвертацией валют.
- **Pathlib** — стандартная библиотека Python для работы с путями файловой системы.
- **OS и SYS** — стандартные модули Python для работы с системными функциями.

Проект написан на Python и использует модульное разделение, включая такие компоненты, как:
- **Qt GUI** (для интерфейса пользователя),
- модуль для создания таблиц базы данных,
- утилита для конвертации данных.
---

## 📂 Структура проекта
```
travellers-assistant/
├── main.py # Главный файл для запуска приложения
├── .venv/ # Виртуальное окружение
├── project/ # Основная папка проекта
│ ├── data/ # Данные проекта
│ │ ├── funcs.py # Функции для работы с данными
│ │ ├── load_db.py # Логика загрузки данных в базу
│ │ └── models.py # Модели данных
│ ├── design/ # Дизайн и интерфейс (UI)
│ │ ├── file.py # Логика работы с интерфейсом
│ │ └── file.ui # Файл интерфейса
│ ├── static/ # Статические ресурсы
│ │ ├── countries/ # Файлы, связанные со странами
│ │ └── images/ # Изображения проекта
│ ├── utils/ # Утилиты проекта
│ │ ├── converter.py #
│ │ └── tranlater.py # Модуль перевода текста
└── README.md # Документация проекта
└── requirements.txt # Зависимости Python
