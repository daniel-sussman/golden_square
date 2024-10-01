from datetime import datetime, date, timedelta
from lib.record import Record

class RecordBook:
    def __init__(self):
        self.records = []

    def create_record(self, name, birthdate):
        formatted_date = self._format(birthdate)
        new_record = Record(name, formatted_date)
        self.records.append(new_record)
        return new_record

    def find(self, name):
        return next(r for r in self.records if r.name == name)

    def update_name(self, old_name, new_name):
        record = self.find(old_name)
        record.update_name(new_name)

    def update_birthdate(self, name, new_birthdate):
        record = self.find(name)
        record.update_birthdate(self._format(new_birthdate))

    def list_upcoming_birthdays(self):
        today = datetime.now()
        seven_days_from_now = today + timedelta(days=7)
        def this_year_birthday(friend):
            return datetime(today.year, friend.birthdate.month, friend.birthdate.day)
        return [friend for friend in self.records if this_year_birthday(friend) <= seven_days_from_now]

    def list_upcoming_birthdays_by_age(self):
        # As a user
        # So I can buy age-appropriate birthday cards
        # I want to calculate the upcoming ages for friends with birthdays
        today = datetime.now()
        return [(friend.name, today.year - friend.birthdate.year if datetime(today.year, friend.birthdate.month, friend.birthdate.day) < today else today.year - friend.birthdate.year - 1) for friend in self.list_upcoming_birthdays()]
    
    def unsent_cards(self):
        return [friend for friend in self.records if not friend.card_sent()]

    def _format(self, date):
        return datetime(*map(int, date.split('/')))