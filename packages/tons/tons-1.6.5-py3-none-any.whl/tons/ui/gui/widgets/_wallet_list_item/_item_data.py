import html
from datetime import datetime
from enum import Enum, auto
from typing import Dict, Optional, Union, Tuple, Sequence

from pydantic import root_validator, validator, Field

from tons.tonclient._client._base import AddressInfoResult
from tons.tonclient.utils import Record, WhitelistContact
from tons.tonsdk.contract.wallet import NetworkGlobalID
from tons.tonsdk.utils import Address
from tons.ui.gui.utils import wallet_state_with_circle, pretty_balance
from .._base import AbstractListItemModel
from ...exceptions import GuiException
from tons.ui.gui.utils import RichString

class WalletListItemKind(Enum):
    record = auto()
    local_contact = auto()
    global_contact = auto()


class WalletListItemData(AbstractListItemModel):
    name: Optional[str]
    # info: Optional[str]
    address: Optional[str]
    comment: Optional[str]
    balance: Optional[str]
    last_activity: Optional[str]
    kind: WalletListItemKind

    address_info: Optional[AddressInfoResult]

    state: Optional[str] = None
    version: Optional[str] = None
    workchain: Optional[str] = None
    network_id: Optional[str] = None

    record: Optional[Record] = None
    contact: Optional[WhitelistContact] = None

    @classmethod
    def vars_with_user_text(cls) -> Sequence[str]:
        """ Variables with user text. Should not contain html tags"""
        return 'name', 'comment'

    def __eq__(self, other: Optional['WalletListItemData']):
        """ Note: this comparison is keystore-agnostic (does not take keystore name into account) """
        if other is None:
            return False
        if self.kind != other.kind:
            return False
        return self.entity == other.entity

    @root_validator(pre=False)
    def _validate_consistency(cls, values):
        try:
            if values['kind'] == WalletListItemKind.record:
                assert isinstance(values['record'], Record)
            elif values['kind'] in [WalletListItemKind.local_contact, WalletListItemKind.global_contact]:
                assert isinstance(values['contact'], WhitelistContact)
            else:
                assert False
        except AssertionError:
            raise ValueError(f'kind/entity type inconsistency: {values["kind"]}')
        return values

    @property
    def info(self) -> str:
        to_join = [self.state, self.version, self.workchain]
        to_join = [x for x in to_join if x]
        return '  '.join(to_join)

    def set_address_info(self, address_info: Optional[AddressInfoResult] = None):
        if isinstance(self.entity, Record):
            if address_info is not None:
                self.balance = pretty_balance(address_info.balance)
                self.last_activity = _pretty_activity(address_info.last_activity_datetime)
                self.state = wallet_state_with_circle(address_info.state, circle_first=False)

            self.version = self.record.version
            self.workchain = f'WC:{self.record.workchain}'

        elif isinstance(self.entity, WhitelistContact):
            if address_info is not None:
                status_with_circle = wallet_state_with_circle(address_info.state, circle_first=False)
                self.state = status_with_circle
                if address_info.version is not None:
                    self.version = f'v{address_info.version}'  # TODO use contract_type?

                self.workchain = f'WC:{Address(self.contact.address).wc}'
                self.balance = pretty_balance(address_info.balance)
                self.last_activity = _pretty_activity(address_info.last_activity_datetime)
        self.address_info = address_info

    @property
    def entity(self) -> Union[Record, WhitelistContact]:
        if self.kind == WalletListItemKind.record:
            assert self.record is not None
            return self.record

        if self.kind in [WalletListItemKind.local_contact, WalletListItemKind.global_contact]:
            assert self.contact is not None
            return self.contact

        assert False

    @classmethod
    def from_record(cls, record: Record, address_info: Optional[AddressInfoResult] = None) -> 'WalletListItemData':
        obj = WalletListItemData(
            name=record.name,
            address=record.tep_standard_user_address,
            comment=record.comment,
            kind=WalletListItemKind.record,
            record=record,
            network_id=cls._pretty_network_id(record.network_global_id)
        )
        obj.set_address_info(address_info)
        return obj
    
    @classmethod
    def _pretty_network_id(cls, network_id: Optional[int]) -> str:
        if network_id == NetworkGlobalID.main_net:
            return 'Mainnet'
        if network_id == NetworkGlobalID.test_net:
            return 'Testnet'
        return ''

    @classmethod
    def from_whitelist_contact(cls, contact: WhitelistContact, kind: WalletListItemKind,
                               address_info: Optional[AddressInfoResult] = None) -> 'WalletListItemData':

        obj = WalletListItemData(
            name=contact.name,
            address=contact.address_to_show,
            comment=contact.default_message,
            kind=kind,
            contact=contact
        )
        obj.set_address_info(address_info)
        return obj

    def find(self, prompt: str) -> Dict[str, int]:
        search_result = dict()
        for var in vars(self):
            val = getattr(self, var)
            if not isinstance(val, str):
                continue

            case_sensitive = var == 'address'

            # TODO make balance search ignore whitespace between every three digits

            # user should not be able to add html tags, so process their string as a plain string
            if var not in self.vars_with_user_text():
                val = RichString(val).clean_string

            if case_sensitive:
                res = val.find(prompt)
            else:
                res = val.lower().find(prompt.lower())

            if res > -1:
                search_result[var] = res

        return search_result


def _pretty_activity(activity: Optional[datetime]) -> str:
    if activity is None:
        return '(n/a)'
    now = datetime.now()

    if activity.day == now.day:
        result = activity.strftime("%H:%M:%S")
    else:
        result = activity.strftime("%d %b %Y")

    return result


class UnexpectedModelKind(GuiException):
    def __init__(self, kind: WalletListItemKind, expected_kind: WalletListItemKind):
        super().__init__(f"Unexpected model kind: {kind.name}. Expected: {expected_kind.name}")


class UnsupportedWalletKind(GuiException):
    def __init__(self, kind: WalletListItemKind):
        super().__init__(f"Unsupported kind: {kind}")


def _validate_kind(model: WalletListItemData, expected_kind: WalletListItemKind):
    if model.kind != expected_kind:
        raise UnexpectedModelKind(model.kind, expected_kind)


__all__ = ['WalletListItemData',
           'WalletListItemKind']
