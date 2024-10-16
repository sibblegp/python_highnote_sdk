from highnote import Highnote

from graphql_client.create_us_person_account_holder import CreateUSPersonAccountHolder

class Person():
  
  def __init__(self, person: CreateUSPersonAccountHolder, highnote: Highnote):
    self.highnote: Highnote = highnote
    self.person: CreateUSPersonAccountHolder = person
    self.id = person.create_us_person_account_holder.id

  def get_person(self):
    person = self.highnote.client.get_us_person_account_holder(self.id)
    return person

