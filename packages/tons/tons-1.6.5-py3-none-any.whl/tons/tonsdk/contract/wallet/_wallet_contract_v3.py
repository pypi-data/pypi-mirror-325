import typing as t
from ._wallet_contract import WalletContract
from ...boc import Cell


class WalletV3ContractBase(WalletContract):
    def create_data_cell(self):
        cell = Cell()
        cell.bits.write_uint(0, 32)
        cell.bits.write_uint(self.options["subwallet_id"], 32)
        cell.bits.write_bytes(self.options["public_key"])
        return cell

    def create_signing_message(self, seqno=None, valid_until: t.Optional[int] = None):
        seqno = seqno or 0
        message = Cell()
        message.bits.write_uint(self.options["subwallet_id"], 32)
        if seqno == 0:
            for _ in range(32):
                message.bits.write_bit(1)
        else:
            if valid_until is None:
                raise ValueError('Valid until must be specified if seqno is specified')
            message.bits.write_uint(valid_until, 32)

        message.bits.write_uint(seqno, 32)
        return message

    @classmethod
    def max_internal_messages(cls) -> int:
        return 4


class WalletV3ContractR1(WalletV3ContractBase):
    def __init__(self, **kwargs) -> None:
        self.code = "B5EE9C724101010100620000C0FF0020DD2082014C97BA9730ED44D0D70B1FE0A4F2608308D71820D31FD31FD31FF82313BBF263ED44D0D31FD31FD3FFD15132BAF2A15144BAF2A204F901541055F910F2A3F8009320D74A96D307D402FB00E8D101A4C8CB1FCB1FCBFFC9ED543FBE6EE0"  # noqa: E501
        kwargs["code"] = Cell.one_from_boc(self.code)
        super().__init__(**kwargs)
        if "subwallet_id" not in self.options or self.options["subwallet_id"] is None:
            self.options["subwallet_id"] = self.default_subwallet_id(self.options["wc"])


class WalletV3ContractR2(WalletV3ContractBase):
    def __init__(self, **kwargs) -> None:
        self.code = "B5EE9C724101010100710000DEFF0020DD2082014C97BA218201339CBAB19F71B0ED44D0D31FD31F31D70BFFE304E0A4F2608308D71820D31FD31FD31FF82313BBF263ED44D0D31FD31FD3FFD15132BAF2A15144BAF2A204F901541055F910F2A3F8009320D74A96D307D402FB00E8D101A4C8CB1FCB1FCBFFC9ED5410BD6DAD"  # noqa: E501
        kwargs["code"] = Cell.one_from_boc(self.code)
        super().__init__(**kwargs)
        if "subwallet_id" not in self.options or self.options["subwallet_id"] is None:
            self.options["subwallet_id"] = self.default_subwallet_id(self.options["wc"])
