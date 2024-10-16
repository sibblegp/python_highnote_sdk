# Generated by ariadne-codegen
# Source: queries.gql

from typing import Annotated, Any, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CardTransactionProcessingType,
    ISO3166Alpha3Country,
    MerchantCategory,
    PanEntryMode,
    PaymentCardStatus,
    PinEntryMode,
    PointOfServiceCategory,
    TerminalAttendance,
    TransactionEventResponseCode,
)


class SimulateSingleStepAuthAndClear(BaseModel):
    simulate_single_step_auth_and_clear: Optional[
        Annotated[
            Union[
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEvent",
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearUserError",
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAccessDeniedError",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="simulateSingleStepAuthAndClear")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEvent(
    BaseModel
):
    typename__: Literal["AuthorizationAndClearEvent"] = Field(alias="__typename")
    id: str
    transaction: Optional[
        Annotated[
            Union[
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventTransactionCreditTransaction",
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventTransactionDebitTransaction",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    original_amount: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventOriginalAmount"
    ] = Field(alias="originalAmount")
    requested_amount: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventRequestedAmount"
    ] = Field(alias="requestedAmount")
    approved_amount: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventApprovedAmount"
    ] = Field(alias="approvedAmount")
    response_code: Optional[TransactionEventResponseCode] = Field(alias="responseCode")
    partial: Optional[bool]
    merchant_details: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventMerchantDetails"
    ] = Field(alias="merchantDetails")
    current_financial_account_maximum_balance_amount: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventCurrentFinancialAccountMaximumBalanceAmount"
    ] = Field(alias="currentFinancialAccountMaximumBalanceAmount")
    current_financial_account_available_to_spend_amount: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventCurrentFinancialAccountAvailableToSpendAmount"
    ] = Field(alias="currentFinancialAccountAvailableToSpendAmount")
    transaction_processing_type: Optional[CardTransactionProcessingType] = Field(
        alias="transactionProcessingType"
    )
    point_of_service_details: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPointOfServiceDetails"
    ] = Field(alias="pointOfServiceDetails")
    additional_network_data: Optional[
        Annotated[
            Union[
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventAdditionalNetworkDataVisaData",
                "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventAdditionalNetworkDataMastercardData",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="additionalNetworkData")
    payment_card_snapshot: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPaymentCardSnapshot"
    ] = Field(alias="paymentCardSnapshot")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventTransactionCreditTransaction(
    BaseModel
):
    typename__: Literal["CreditTransaction"] = Field(alias="__typename")
    id: str


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventTransactionDebitTransaction(
    BaseModel
):
    typename__: Literal["DebitTransaction"] = Field(alias="__typename")
    id: str


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventOriginalAmount(
    BaseModel
):
    value: Optional[Any]
    currency_code: Optional[str] = Field(alias="currencyCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventRequestedAmount(
    BaseModel
):
    value: Optional[Any]
    currency_code: Optional[str] = Field(alias="currencyCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventApprovedAmount(
    BaseModel
):
    value: Optional[Any]
    currency_code: Optional[str] = Field(alias="currencyCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventMerchantDetails(
    BaseModel
):
    address: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventMerchantDetailsAddress"
    ]
    country_code_alpha_3: Optional[ISO3166Alpha3Country] = Field(
        alias="countryCodeAlpha3"
    )
    category: Optional[MerchantCategory]
    category_code: Optional[str] = Field(alias="categoryCode")
    name: Optional[str]
    merchant_id: Optional[str] = Field(alias="merchantId")
    description: Optional[str]


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventMerchantDetailsAddress(
    BaseModel
):
    locality: Optional[str]
    region: Optional[str]
    country_code_alpha_3: Optional[str] = Field(alias="countryCodeAlpha3")
    postal_code: Optional[str] = Field(alias="postalCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventCurrentFinancialAccountMaximumBalanceAmount(
    BaseModel
):
    value: Optional[Any]
    currency_code: Optional[str] = Field(alias="currencyCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventCurrentFinancialAccountAvailableToSpendAmount(
    BaseModel
):
    value: Optional[Any]
    currency_code: Optional[str] = Field(alias="currencyCode")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPointOfServiceDetails(
    BaseModel
):
    category: Optional[PointOfServiceCategory]
    pan_entry_mode: Optional[PanEntryMode] = Field(alias="panEntryMode")
    pin_entry_mode: Optional[PinEntryMode] = Field(alias="pinEntryMode")
    terminal_attendance: Optional[TerminalAttendance] = Field(
        alias="terminalAttendance"
    )
    is_card_holder_present: Optional[bool] = Field(alias="isCardHolderPresent")
    is_card_present: Optional[bool] = Field(alias="isCardPresent")
    is_recurring: Optional[bool] = Field(alias="isRecurring")
    terminal_supports_partial_approval: Optional[bool] = Field(
        alias="terminalSupportsPartialApproval"
    )


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventAdditionalNetworkDataVisaData(
    BaseModel
):
    typename__: Literal["VisaData"] = Field(alias="__typename")
    transaction_identifier: Optional[str] = Field(alias="transactionIdentifier")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventAdditionalNetworkDataMastercardData(
    BaseModel
):
    typename__: Literal["MastercardData"] = Field(alias="__typename")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPaymentCardSnapshot(
    BaseModel
):
    created_at: Optional[str] = Field(alias="createdAt")
    status: Optional[PaymentCardStatus]
    payment_card_current: Optional[
        "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPaymentCardSnapshotPaymentCardCurrent"
    ] = Field(alias="paymentCardCurrent")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPaymentCardSnapshotPaymentCardCurrent(
    BaseModel
):
    id: str
    expiration_date: Optional[str] = Field(alias="expirationDate")
    last_4: Optional[str] = Field(alias="last4")


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearUserError(BaseModel):
    typename__: Literal["UserError"] = Field(alias="__typename")
    errors: Optional[
        List[
            "SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearUserErrorErrors"
        ]
    ]


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearUserErrorErrors(
    BaseModel
):
    path: Optional[List[str]]
    code: Optional[str]
    description: Optional[str]


class SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAccessDeniedError(
    BaseModel
):
    typename__: Literal["AccessDeniedError"] = Field(alias="__typename")


SimulateSingleStepAuthAndClear.model_rebuild()
SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEvent.model_rebuild()
SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventMerchantDetails.model_rebuild()
SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearAuthorizationAndClearEventPaymentCardSnapshot.model_rebuild()
SimulateSingleStepAuthAndClearSimulateSingleStepAuthAndClearUserError.model_rebuild()
