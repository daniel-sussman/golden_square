from lib.record_book import RecordBook
from lib.record import Record
from datetime import datetime, timedelta

def test_stores_some_records():
    record_book = RecordBook()
    record_book.create_record('Charlie', '2001/3/4')
    record_book.create_record('Angela', '1979/10/4')
    charlie = record_book.find('Charlie')
    angela = record_book.find('Angela')
    assert charlie.name == 'Charlie'
    assert charlie.birthdate == datetime(2001, 3, 4)

def test_update_name():
    record_book = RecordBook()
    record_book.create_record('Charlie', '2001/3/4')
    charlie = record_book.find('Charlie')
    record_book.update_name('Charlie', 'Charles')
    assert charlie.name == 'Charles'
    assert charlie.birthdate == datetime(2001, 3, 4)

def test_update_birthdate():
    record_book = RecordBook()
    record_book.create_record('Charlie', '2001/3/4')
    charlie = record_book.find('Charlie')
    record_book.update_birthdate('Charlie', '2002/3/4')
    assert charlie.birthdate == datetime(2002, 3, 4)

def test_list_upcoming_birthdays():
    record_book = RecordBook()
    today = datetime.now()
    one_day = today + timedelta(days=1)
    five_days = today + timedelta(days=5)
    seven_days = today + timedelta(days=7)
    eight_days = today + timedelta(days=8)
    record_book.create_record('Charlie', f'2001/{today.month}/{today.day}')
    record_book.create_record('Angela', f'1979/{one_day.month}/{one_day.day}')
    record_book.create_record('Peter', f'1998/{five_days.month}/{five_days.day}')
    record_book.create_record('Taha', f'2006/{seven_days.month}/{seven_days.day}')
    record_book.create_record('Daniel', f'1985/{eight_days.month}/{eight_days.day}')
    charlie = record_book.find('Charlie')
    angela = record_book.find('Angela')
    peter = record_book.find('Peter')
    taha = record_book.find('Taha')
    _ = record_book.find('Daniel')
    assert record_book.list_upcoming_birthdays() == [charlie, angela, peter, taha]

def test_list_upcoming_birthdays_by_age():
    record_book = RecordBook()
    today = datetime.now()
    one_day = today + timedelta(days=1)
    five_days = today + timedelta(days=5)
    seven_days = today + timedelta(days=7)
    eight_days = today + timedelta(days=8)
    charlie_birthdate = f'2001/{today.month}/{today.day}'
    angela_birthdate = f'1979/{one_day.month}/{one_day.day}'
    peter_birthdate = f'1998/{five_days.month}/{five_days.day}'
    taha_birthdate = f'2006/{seven_days.month}/{seven_days.day}'
    daniel_birthdate = f'1985/{eight_days.month}/{eight_days.day}'
    charlie = record_book.create_record('Charlie', charlie_birthdate)
    angela = record_book.create_record('Angela', angela_birthdate)
    peter = record_book.create_record('Peter', peter_birthdate)
    taha = record_book.create_record('Taha', taha_birthdate)
    _ = record_book.create_record('Daniel', daniel_birthdate)
    charlie_age = today.year - charlie.birthdate.year if datetime(today.year, charlie.birthdate.month, charlie.birthdate.day) < today else today.year - charlie.birthdate.year - 1
    angela_age = today.year - angela.birthdate.year if datetime(today.year, angela.birthdate.month, angela.birthdate.day) < today else today.year - angela.birthdate.year - 1
    peter_age = today.year - peter.birthdate.year if datetime(today.year, peter.birthdate.month, peter.birthdate.day) < today else today.year - peter.birthdate.year - 1
    taha_age = today.year - taha.birthdate.year if datetime(today.year, taha.birthdate.month, taha.birthdate.day) < today else today.year - taha.birthdate.year - 1
    assert record_book.list_upcoming_birthdays_by_age() == [('Charlie', charlie_age), ('Angela', angela_age), ('Peter', peter_age), ('Taha', taha_age)]

# As a user
# So I can keep track of cards sent and to be sent
# I want to be able to mark a birthday card for a year as "done"
def test_mark_card_done():
    record_book = RecordBook()
    record_book.create_record('Charlie', '2001/3/4')
    record_book.create_record('Angela', '1979/10/4')
    charlie = record_book.find('Charlie')
    angela = record_book.find('Angela')
    charlie.mark_done()
    assert record_book.unsent_cards() == [angela]