from peewee import Model, SqliteDatabase, CharField, AutoField
from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()

DATABASE = BASE_DIR / "database.db"
database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = database


class GermanyEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "germany_english"

    def __str__(self):
        return f"Немецкий: {self.phrase} - {self.translate}"


class FrenchEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "french_english"

    def __str__(self):
        return f"Французский: {self.phrase} - {self.translate}"


class HindiEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "hindi_english"

    def __str__(self):
        return f"Хинди: {self.phrase} - {self.translate}"


class PortugalEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "portugal_english"

    def __str__(self):
        return f"Португальский: {self.phrase} - {self.translate}"


class ChinaEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "china_english"

    def __str__(self):
        return f"Китайский: {self.phrase} - {self.translate}"


class RussianEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "russian_english"

    def __str__(self):
        return f"Русский: {self.phrase} - {self.translate}"

class EnglishEnglish(BaseModel):
    id = AutoField()
    phrase = CharField(max_length=128, null=False)
    translate = CharField(max_length=128, null=False)

    class Meta:
        db_table = "english_english"

    def __str__(self):
        return f"Английский: {self.phrase} - {self.translate}"


def create_tables():
    with database:
        database.create_tables([
            GermanyEnglish,
            FrenchEnglish,
            HindiEnglish,
            PortugalEnglish,
            ChinaEnglish,
            RussianEnglish,
            EnglishEnglish,
        ])
