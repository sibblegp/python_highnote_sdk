from highnote import Highnote
from graphql_client.input_types import (
  AddressInput,
  PhoneInput,
  PhoneLabel,
  USIdentificationDocumentInput,
  TaxIdentificationDocumentInput,
  PersonCreditRiskAttributesInput,
  AmountInput,
  EmploymentStatus,
  PersonAccountHolderNameInput,
  USPersonAccountHolderInput,
  CreateUSPersonAccountHolderInput
)

from person import Person

class People():
  
  def __init__(self, highnote: Highnote):
    self.highnote: Highnote = highnote
  
  def create_person(
      self,
      first_name,
      last_name,
      email,
      phone_number,
      address_line_1,
      address_line_2,
      city,
      state,
      postal_code,
      country_code_alpha_3,
      ssn,
      income,
      debt,
      employment_status: EmploymentStatus,
      external_id: str = None
  ):
    person_address = AddressInput(
        streetAddress=address_line_1,
        extendedAddress=address_line_2,
        city=city,
        state=state,
        postalCode=postal_code,
        locality='US',
        countryCodeAlpha3=country_code_alpha_3,
        region=state,
    )
    person_phone = PhoneInput(
        number=phone_number,
        countryCode='1',
        label=PhoneLabel.MOBILE,
    )
    person_identification = TaxIdentificationDocumentInput(
        number=ssn,
        countryCodeAlpha3='USA'
    )
    id_document = USIdentificationDocumentInput(
        socialSecurityNumber=person_identification
    )
    person_credit_risk = PersonCreditRiskAttributesInput(
        totalAnnualIncome=[income],
        currentDebtObligations=[debt],
        employmentStatus=employment_status,
    )
    person_holder_name = PersonAccountHolderNameInput(
        givenName=first_name,
        familyName=last_name
    )
    person_account_holder = USPersonAccountHolderInput(
        name=person_holder_name,
        email=email,
        billingAddress=person_address,
        dateOfBirth='1981-05-01',
        identificationDocument=id_document,
        phoneNumber=person_phone,
        personCreditRiskAttributes=person_credit_risk,
        external_id=external_id
    )
    person_input = CreateUSPersonAccountHolderInput(
        person_account_holder=person_account_holder,
       
    )
    person_response = self.highnote.client.create_us_person_account_holder(person_input)
    person = Person(person_response, self.highnote)
    return person
