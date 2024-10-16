from graphql_client.client import Client
from graphql_client.find_financial_account import (
    FindFinancialAccountNodeFinancialAccountFinancialAccountActivitiesEdgesNodeSourceDebitTransaction
)
from graphql_client.input_types import (
    CreateUSPersonAccountHolderInput,
    USPersonAccountHolderInput,
    PersonAccountHolderNameInput,
    AddressInput,
    USIdentificationDocumentInput,
    TaxIdentificationDocumentInput,
    CreateAccountHolderCardProductApplicationInput,
    ConsentInput,
    PhoneInput,
    PhoneLabel,
    PersonCreditRiskAttributesInput,
    AmountInput,
    EmploymentStatus,
    IssueFinancialAccountForApplicationInput,
    IssuePaymentCardForFinancialAccountInput,
    IssuePaymentCardOptionsInput,
    AccountHolderApplicationStatusCode,
    MerchantDetailsInput,
    SimulateSingleStepAuthAndClearInput,
    MerchantDetailsInput,
    MerchantDetailsAddressInput
)
import datetime
from time import sleep


def test_client():
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    r5 = client.find_financial_account(
        'ac_c022ac4b949504bd4d4db2f7ddb4ddba5896'
    )
    for transaction in r5.node.financial_account_activities.edges:
        if isinstance(
            transaction.node.source,
            FindFinancialAccountNodeFinancialAccountFinancialAccountActivitiesEdgesNodeSourceDebitTransaction,
        ):
            print(transaction.node)
            print(
                transaction.node.source.transaction_events[0].merchant_details.name
            )
            print(transaction.node.posted_amount)
            transaction_event = transaction.node.source.transaction_events[0]
            print(transaction_event.merchant_details.name)
            print(transaction_event.merchant_details.city)
            print(transaction_event.merchant_details.state)
            print(transaction_event.merchant_details.country_code_alpha_3)


def test_create_account(name='', email=''):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    print('Creating Person')
    person_income = AmountInput(value='10000000', currencyCode='USD')
    person_debt = AmountInput(value='500', currencyCode='USD')
    person_credit_risk = PersonCreditRiskAttributesInput(
        totalAnnualIncome=[person_income],
        currentDebtObligations=[person_debt],
        employmentStatus=EmploymentStatus.EMPLOYED,
    )
    person_identification = TaxIdentificationDocumentInput(
        number='022641111', countryCodeAlpha3='USA'
    )
    id_document = USIdentificationDocumentInput(
        socialSecurityNumber=person_identification
    )
    person_address = AddressInput(
        streetAddress='123 Main St',
        city='San Francisco',
        state='CA',
        postalCode='94103',
        locality='US',
        countryCodeAlpha3='USA',
        region='CA',
    )
    person_phone = PhoneInput(
        number='4155552671', countryCode='1', label=PhoneLabel.MOBILE
    )
    person_holder_name = PersonAccountHolderNameInput(
        givenName='API', familyName='Testing'
    )
    person_account_holder = USPersonAccountHolderInput(
        name=person_holder_name,
        email='api@sibbleconsulting.com',
        billingAddress=person_address,
        dateOfBirth='1981-05-01',
        identificationDocument=id_document,
        phoneNumber=person_phone,
        personCreditRiskAttributes=person_credit_risk,
    )
    person_input = CreateUSPersonAccountHolderInput(
        person_account_holder=person_account_holder
    )
    person = client.create_us_person_account_holder(person_input)
    person_id = person.create_us_person_account_holder.id
    print(
        f'Created Person {person_holder_name.given_name} {person_holder_name.family_name}'
    )
    print(f'Person Created ID: {person_id}')
    print('Submitting Application')
    application_consent = ConsentInput(
        primaryAuthorizedPersonId=person_id,
        consentTimestamp='2023-12-22T17:10:55.662Z',
    )
    application_input = CreateAccountHolderCardProductApplicationInput(
        cardProductId='pd_6e66486e16a145f2a8f121b554f73e20',
        accountHolderId=person_id,
        cardHolderAgreementConsent=application_consent,
    )
    application = client.create_account_holder_card_product_application(
        application_input
    )
    application_id = (
        application.create_account_holder_card_product_application.id
    )
    print(f'Application Submitted - ID: {application_id}')
    print(
        f'Application Status: {application.create_account_holder_card_product_application.application_state.status}'
    )
    application_approved = False
    while not application_approved:
        sleep(5)
        print('Checking Application Status')
        status = check_application(application_id)
        if status == AccountHolderApplicationStatusCode.APPROVED:
            application_approved = True
    print('Issuing Financial Account')
    account_id = create_financial_accounts(application_id, person_id)
    print(f'Financial Account Issued - ID: {account_id}')
    print('Issuing Virtual Card')
    virtual_card = issue_virtual_card(account_id)
    print(f'Virtual Card Issued - ID: {virtual_card.id}')
    print(f'Virtual Card Last 4: {virtual_card.last_4}')
    print('Person created with issued card')
    print('Simulating a transaction')
    sleep(10)
    transaction_amount = 50.00  # Example amount in dollars
    transaction_name = "Test Purchase"
    simulate_input = SimulateSingleStepAuthAndClearInput(
        cardId=virtual_card.id,
        amount=AmountInput(value=int(transaction_amount * 100), currencyCode="USD"),
        merchantDetails=MerchantDetailsInput(
            name=transaction_name,
            category="VETERINARY_SERVICES",
            address=MerchantDetailsAddressInput(
                streetAddress="123 Main St",
                postalCode="94105",
                region="CA",
                locality="San Francisco",
                countryCodeAlpha3="USA",
                
            )
        )
    )
    transaction_result = client.simulate_single_step_auth_and_clear(simulate_input)
    print(transaction_result)
    sleep(60)
    transactions = get_debit_transactions(account_id)
    print(transactions)


def create_financial_accounts(
    application_id='ap_22pcgm305acd9cf1594cafa39abac98e5a69b3',
    person_id='ps_ah01250641adf0d3456a9613749ead9505b8',
):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    account_input = IssueFinancialAccountForApplicationInput(
        applicationId=application_id, name='Test Account'
    )
    account = client.issue_financial_account_for_application(account_input)
    account_id = account.issue_financial_account_for_application.id
    return account_id


def issue_virtual_card(
    account_id='ac_c02281ee2e25793a4f56bab010d76e4cb4a7',
):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    payment_card_options = IssuePaymentCardOptionsInput(
        expirationDate='2026-01-01T23:59:59Z', activateOnCreate=True
    )
    issue_input = IssuePaymentCardForFinancialAccountInput(
        financialAccountId=account_id, options=payment_card_options
    )
    card = client.issue_payment_card_for_financial_account(issue_input)
    return card.issue_payment_card_for_financial_account


def test_transaction(name, amount):
    pass


def check_application(
    application_id='ap_22pcgm305acd9cf1594cafa39abac98e5a69b3',
):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    print('Checking Application ID: ' + application_id)
    application_check = client.lookup_application(application_id)
    print(
        'Current Application Status: '
        + str(application_check.node.application_state.status)
    )
    return application_check.node.application_state.status

def simulate_transaction(card_id, amount, merchant_name="Test Merchant"):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    
    transaction_input = SimulateSingleStepAuthAndClearInput(
        paymentCardId=card_id,
        amount=AmountInput(value=str(amount), currencyCode="USD"),
        merchantDetails=MerchantDetailsInput(name=merchant_name)
    )
    
    try:
        transaction = client.simulate_single_step_auth_and_clear(transaction_input)
        print(f"Transaction simulated successfully for card {card_id}")
        print(f"Amount: ${amount/100:.2f}")
        print(f"Merchant: {merchant_name}")
        print(f"Transaction ID: {transaction.simulate_single_step_auth_and_clear.id}")
        return transaction.simulate_single_step_auth_and_clear
    except Exception as e:
        print(f"Error simulating transaction: {str(e)}")
        return None

def get_debit_transactions(financial_account_id):
    client = Client(
        'https://api.us.test.highnote.com/graphql',
        {
            'Authorization': 'Basic '
            + 'c2tfdGVzdF9MWk00YmFKdEI5NHhiZUxzZ25MZXBvNG9YS3FZQkJwOEQyWVpLZENSbmdidEJGb25hNTFXNUhLNXVYMUt0UkMxU1RTUTU5SHgzVlBTZUxjMXpVU2FRY01jSFE='
        },
    )
    
    account_data = client.find_financial_account(financial_account_id)
    debit_transactions = []
    print(account_data.node.financial_account_activities.edges)
    for transaction in account_data.node.financial_account_activities.edges:
        if isinstance(
            transaction.node.source,
            FindFinancialAccountNodeFinancialAccountFinancialAccountActivitiesEdgesNodeSourceDebitTransaction,
        ):
            transaction_event = transaction.node.source.transaction_events[0]
            print(transaction_event)
            debit_transactions.append({
                'merchant_name': transaction_event.merchant_details.name,
                # 'merchant_city': transaction_event.merchant_details.region,
                # 'merchant_state': transaction_event.merchant_details.locality,
                # 'merchant_country': transaction_event.merchant_details.country_code_alpha_3,
                'date': transaction.node.created_at,
                'transaction_event_id': transaction_event.id,
                'response_code': transaction_event.response_code,
                'transaction_processing_type': transaction_event.transaction_processing_type,
                'approved_amount': transaction_event.approved_amount.value if transaction_event.approved_amount else None,
                'approved_currency': transaction_event.approved_amount.currency_code if transaction_event.approved_amount else None,
            })

    return debit_transactions
