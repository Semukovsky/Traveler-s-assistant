import sys
import os
import pathlib
from datetime import datetime
import pytz

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget

from project.design.file import Ui_MainWindow
from project.data.models import create_tables, database
from project.utils.converter import convert
from project.utils.tranlater import translate

BASE_DIR = pathlib.Path(__file__).parent.absolute()


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        create_tables()

        buttons = {
            "main": self.f_to_page_m,
            "popular": self.f_to_page_p,
            "razgovornik": self.f_to_page_r,
            "converter": self.f_to_page_c,
            "faq": self.f_to_page_f,
            "time": self.f_to_page_t,
        }

        prefixes = ["m", "p", "r", "c", "f", "t"]
        for prefix in prefixes:
            for btn_name, func in buttons.items():
                getattr(self, f"B_{prefix}_{btn_name}").clicked.connect(func)

        self.B_c_run.clicked.connect(self.f_convert_currency)
        self.B_r_translate.clicked.connect(self.f_translate)
        self.B_r_run.clicked.connect(self.f_change_language)
        self.CB_p_country.currentTextChanged.connect(self.f_change_country_popular)

        self.f_style_main()

    def f_fill_questions(self):
        questions_and_answers = [
            (
                "Какие документы нужны для поездки за границу?",
                "Заграничный паспорт, виза (если требуется), медицинская страховка и билет."
            ),
            (
                "Как найти недорогие авиабилеты?",
                "Используйте агрегаторы, такие как Skyscanner или Aviasales, и бронируйте заранее."
            ),
            (
                "Нужно ли получать визу для посещения [страна]?",
                "Зависит от гражданства вашей страны и визовой политики страны назначения."
            ),
            (
                "Что делать, если потерял паспорт за границей?",
                "Обратитесь в консульство вашей страны, предоставив копии документов или фото паспорта."
            ),
            (
                "Какой лучший способ обменять валюту?",
                "Обменяйте деньги в банках или официальных обменных пунктах, избегая обмена в аэропортах."  # max
            ),
            (
                "Нужна ли страховка для путешествия?",
                "Рекомендуется для безопасности."
            ),
            (
                "Как избежать туристических мошенников?",
                "Не показывайте ценные вещи и избегайте подозрительных предложений."
            ),
            (
                "Как выбрать безопасный район для проживания?",
                "Читайте отзывы на Booking или Airbnb и исследуйте карту района."
            ),
            (
                "Как заработать на путешествие мечты?",
                "Hamster combat"
            ),
            (
                "Где узнать о местных обычаях?",
                "В путеводителях или онлайн."
            ),
            (
             "Как найти общественный транспорт?",
             "Спросите у местных или используйте Google Maps."
            ),
            (
                "Какие приложения помогут в путешествиях?",
                "Google Maps, Uber, Booking, Duolingo, переводчики и офлайн-карты, такие как Maps.me."
            ),
        ]
        num_rows = len(questions_and_answers)
        self.TB_f_questions.setRowCount(num_rows)
        for i, (question, answer) in enumerate(questions_and_answers):
            self.TB_f_questions.setItem(i, 0, QTableWidgetItem(question))
            self.TB_f_questions.setItem(i, 1, QTableWidgetItem(answer))
        for row in range(num_rows):
            if row % 2 == 0:
                row_color = QColor("#5e705c")
            else:
                row_color = QColor("#3b4739")
            for col in range(2):
                item = self.TB_f_questions.item(row, col)
                item.setBackground(row_color)

    def f_style_main(self):
        path_to_logo = BASE_DIR / "static" / "images" / "yandex_logo.png"
        pixmap = QPixmap(str(path_to_logo))
        label = self.L_m_yandex_logo
        scaled_pixmap = pixmap.scaled(
            label.width(),
            label.height(),
        )
        label.setPixmap(scaled_pixmap)

    def f_change_country(self):
        try:
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)
        except Exception as e:
            print(f"Ошибка: {e}")

    def update_time(self):
        try:
            timezones = {
                "Англия": "Europe/London",
                "Германия": "Europe/Berlin",
                "Франция": "Europe/Paris",
                "Индия": "Asia/Kolkata",
                "Португалия": "Europe/Lisbon",
                "Китай": "Asia/Shanghai",
                "Россия": "Europe/Moscow"
            }
            country = self.CB_t_country.currentText()
            moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
            tz = timezones[country]
            local_time = moscow_time.astimezone(pytz.timezone(tz))
            self.L_t_result.setText(local_time.strftime("%H:%M:%S"))
        except Exception as e:
            print(f"Ошибка: {e}")

    def f_change_language(self):
        try:
            dct = {
                "Английский": "english_english",
                "Немецкий": "germany_english",
                "Французский": "french_english",
                "Русский": "russian_english",
                "Китайский": "china_english",
                "Хинди": "hindi_english",
                "Португальский": "portugal_english",
            }
            from_language = self.CB_r_from_language.currentText()
            to_language = self.CB_r_to_language.currentText()

            from_language_obj = dct[from_language]
            to_language_obj = dct[to_language]

            if from_language != to_language:
                sql = """
                SELECT DISTINCT {from_language}.phrase, {to_language}.phrase
                FROM {from_language}
                FULL JOIN {to_language}
                ON {from_language}.translate = {to_language}.translate;
                """.format(from_language=from_language_obj, to_language=to_language_obj)
            else:
                sql = """
                SELECT DISTINCT {language}.phrase, {language}.phrase
                FROM {language}
                """.format(language=from_language_obj)
            results = database.execute_sql(sql)
            num_rows = 15
            self.TB_r_languages.setRowCount(num_rows)
            for i, (from_, to_) in enumerate(results):
                self.TB_r_languages.setItem(i, 0, QTableWidgetItem(from_))
                self.TB_r_languages.setItem(i, 1, QTableWidgetItem(to_))
            for row in range(num_rows):
                if row % 2 == 0:
                    row_color = QColor("#5e705c")
                else:
                    row_color = QColor("#3b4739")
                for col in range(2):
                    item = self.TB_r_languages.item(row, col)
                    item.setBackground(row_color)
        except Exception as e:
            print(f"Ошибка: {e}")

    def f_translate(self):
        try:
            dct = {
                "Английский": "en",
                "Немецкий": "de",
                "Французский": "fr",
                "Русский": "ru",
                "Китайский": "zh",
                "Хинди": "hi",
                "Португальский": "pt"
            }
            from_language = self.CB_r_from_language_t.currentText()
            to_language = self.CB_r_to_language_t.currentText()
            abr_from_language = dct[from_language]
            abr_to_language = dct[to_language]
            text = self.LE_r_text.text()
            result = translate(from_language=abr_from_language, to_language=abr_to_language, text=text)
            self.L_r_result.setText(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def f_change_country_popular(self):
        try:
            counties = {
                "Россия": "russia",
                "Дагестан": "dagestan",
                "Турция": "turkey",
                "Америка": "amerika",
                "Франция": "france",
            }
            country = self.CB_p_country.currentText()
            path_to_country = BASE_DIR / "static" / "countries" / counties[country]
            if not path_to_country.exists() or not path_to_country.is_dir():
                print(f"Директория {path_to_country} не найдена")
                return
            for index, image in enumerate(os.listdir(path_to_country), 1):
                image_path = path_to_country / image
                pixmap = QPixmap(str(image_path))
                label = getattr(self, f"L_p_{index}", None)
                scaled_pixmap = pixmap.scaled(
                    label.width(),
                    label.height(),
                )
                label.setPixmap(scaled_pixmap)

        except KeyError:
            print(f"Страна {country} не найдена в словаре counties.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def f_convert_currency(self):
        currency_map = {
            "Доллары США": "USD",
            "Евро": "EUR",
            "Рубли": "RUB",
            "Фунты стерлингов": "GBP",
        }
        try:
            amount = float(self.LE_c_amount_input.text())
            from_currency = currency_map[self.CB_c_from_currency.currentText()]
            to_currency = currency_map[self.CB_c_to_currency.currentText()]
            res = str(round(convert(amount, from_currency, to_currency), 2))
            if len(res) > 15:
                self.LCD_c_result.display("Error")
            else:
                self.L_c_error.setText("")
                self.LCD_c_result.display(res)
        except ValueError:
            self.LCD_c_result.display("Error")
            self.L_c_error.setText("Введите корректное значение")
        except Exception as e:
            self.LCD_c_result.display("Error")
            self.L_c_error.setText("Произошла ошибка")

    def f_to_page_m(self):
        self.stackedWidget.setCurrentWidget(self.page_m)
        self.f_style_main()

    def f_to_page_p(self):
        self.stackedWidget.setCurrentWidget(self.page_p)
        self.f_change_country_popular()

    def f_to_page_r(self):
        self.stackedWidget.setCurrentWidget(self.page_r)

    def f_to_page_c(self):
        self.stackedWidget.setCurrentWidget(self.page_c)

    def f_to_page_f(self):
        self.stackedWidget.setCurrentWidget(self.page_f)
        self.f_fill_questions()

    def f_to_page_t(self):
        self.stackedWidget.setCurrentWidget(self.page_t)
        self.f_change_country()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec())
