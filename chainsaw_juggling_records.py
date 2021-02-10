from peewee import *

db = SqliteDatabase('chainsaw_juggling_records.sqlite')


class Record_Holder(Model):
    name = CharField()
    country = CharField()
    num_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.num_catches}'


db.connect()
db.create_tables([Record_Holder])

# Record_Holder.delete().execute()  # clear the database table


def main():
    print('1. ADD new record')
    print('2. DELETE record')
    print('3. SEARCH for record')
    print('4. UPDATE record')
    print('5. QUIT program')
    while True:
        action = int(input('What would you like to do? '))
        if action == 1:
            add_record_holder()
        elif action == 2:
            delete_record()
        elif action == 3:
            search_record_by_name()
        elif action == 4:
            update_catches()
        elif action == 5:
            exit()
        else:
            print('Enter a number for one of the options above.')


def add_record_holder():
    name = input('Who is the new record holder? ').title()
    country = input(f'What country is {name} from? ').title()
    catches = int(input(f'How many catches did {name} manage? '))
    new_record_holder = Record_Holder(name=name, country=country, num_catches=catches)
    new_record_holder.save()


def delete_record():
    record_to_delete = input('Who\'s record do you want to delete? ')
    Record_Holder.delete().where(Record_Holder.name == record_to_delete).execute()
    print('Record deleted for', record_to_delete)


def search_record_by_name():
    find_name = input('Who do you want to find? ').title()
    match_name = Record_Holder.get_or_none(Record_Holder.name == find_name)
    print(f'\nRecord for {find_name}:', match_name)


def update_catches():
    name = input('Who has a new personal best? ').title()
    new_pb = int(input('How many catches have they now achieved? '))
    Record_Holder.update(num_catches=new_pb).where(Record_Holder.name == name).execute()
    print(f'\nChanged {name}\'s catch record to {new_pb}.')


if __name__ == '__main__':
    main()
