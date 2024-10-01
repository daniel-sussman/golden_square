# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

    <!-- As a user
    So I don't forget the details
    I want to keep a record of friends' names and birthdates -->

    <!-- As a user
    So I can make edits when I've got dates wrong
    I want to be able to update a record by passing in a name and new date -->

    <!-- As a user
    So I can make edits when people change their name
    I want to be able to update a record by passing in an old and a new name -->

    As a user
    So I can remember to send birthday cards at the right time
    I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

    As a user
    So I can buy age-appropriate birthday cards
    I want to calculate the upcoming ages for friends with birthdays

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

import date_time

class RecordBook:
    def __init__(self):
        self.records = []

    def find_by_name(self, name):
        pass

    def update_name(self, old_name, new_name):
        record = self.find_by_name(old_name)
        record.name = new_name

    def update_birthdate(self, name, new_birthdate):
        record = self.find_by_name(old_name)
        record.birthdate = new_birthdate

    def list_upcoming_birthdays(self):
        # get date now
        # array
        pass

    def list_upcoming_birthdays_by_age(self):
        pass

class Record:
    # User-facing properties:
    #   name: string

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def update(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
