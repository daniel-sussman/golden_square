from datetime import datetime

class Record:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.card_sent_years = []

    def update_name(self, name):
        self.name = name
    
    def update_birthdate(self, birthdate):
        self.birthdate = birthdate

    def mark_done(self):
        if self.card_sent():
            raise Exception("You've already marked this year's card as sent!")
        
        this_year = datetime.now().year
        self.card_sent_years.append(this_year)
    
    def card_sent(self):
        this_year = datetime.now().year
        return this_year in self.card_sent_years