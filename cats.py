from peewee import *

db = SqliteDatabase('cats.sqlite')  # can use any extension you want, .sqlite is common


class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}'


db.connect()
db.create_tables([Cat])

Cat.delete().execute()  # clear the database table

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save()  # make sure to save!

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save()

# query object
cats = Cat.select()
for cat in cats:
    print(cat)

list_of_cats = list(cats)   # regular Python list

""" CRUD operations
Create = insert
Read = select
Update
Delete
"""

fluffy.age = 2
fluffy.save()

print('After Fluffy age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

# can update many rows if needed
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Holly age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

print(rows_modified)

buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three')


cat_with_l_in_name = Cat.select().where(Cat.name % '*l*')  # case-sensitive
for cat in cat_with_l_in_name:
    print(cat, 'has l in name')

cat_with_b_in_name = Cat.select().where(Cat.name.contains('b'))  # case-insensitive
for cat in cat_with_b_in_name:
    print(cat, 'has b in name')


zoe_from_db = Cat.get_or_none(name='Zoe')  # if doesn't exists, returns None
print(zoe_from_db)

# if know the id exists
cat_1 = Cat.get_by_id(1)
print(cat_1)

# if not sure if id exists
cat_1 = Cat.get_or_none(1)
print(cat_1)

# id doesn't exist
cat_100 = Cat.get_or_none(Cat.id == 100)
print(cat_100)
