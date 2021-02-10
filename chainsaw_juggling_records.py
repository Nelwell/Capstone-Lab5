from peewee import *

db = SqliteDatabase('chainsaw_juggling_records.sqlite')


class Record_Holders(Model):
    name = CharField()
    country = CharField()
    num_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.num_catches}'


db.connect()
db.create_tables([Record_Holders])

Record_Holders.delete().execute()  # clear the database table
