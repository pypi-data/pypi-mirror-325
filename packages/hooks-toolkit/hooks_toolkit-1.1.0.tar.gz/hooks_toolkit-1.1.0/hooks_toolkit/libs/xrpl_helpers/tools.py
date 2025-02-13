#!/usr/bin/env python
# coding: utf-8

from typing import Union, Dict, Any

from xahau.clients import Client
from xahau.wallet import Wallet
from xahau.models.amounts import IssuedCurrencyAmount
from xahau.models.requests import AccountInfo, LedgerEntry
from xahau.models.transactions import Payment, TrustSet, AccountSet, AccountSetAsfFlag
from xahau.utils import str_to_hex, xah_to_drops
from hooks_toolkit.libs.xrpl_helpers.transaction import app_transaction

from hooks_toolkit.libs.xrpl_helpers.constants import (
    NOT_ACTIVE_WALLET,
    GW_ACCOUNT_WALLET,
    ALICE_ACCOUNT_WALLET,
    BOB_ACCOUNT_WALLET,
    CAROL_ACCOUNT_WALLET,
    DAVE_ACCOUNT_WALLET,
    ELSA_ACCOUNT_WALLET,
    FRANK_ACCOUNT_WALLET,
    GRACE_ACCOUNT_WALLET,
    HEIDI_ACCOUNT_WALLET,
    IVAN_ACCOUNT_WALLET,
    JUDY_ACCOUNT_WALLET,
    HOOK1_ACCOUNT_WALLET,
    HOOK2_ACCOUNT_WALLET,
    HOOK3_ACCOUNT_WALLET,
    HOOK4_ACCOUNT_WALLET,
    HOOK5_ACCOUNT_WALLET,
)

LEDGER_ACCEPT_REQUEST = {"command": "ledger_accept"}


class Account:
    def __init__(self, name: str = None, seed: str = None):
        self.name = name
        if name == "gw":
            self.wallet = GW_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "notactivated":
            self.wallet = NOT_ACTIVE_WALLET
            self.account = self.wallet.classic_address
        if name == "alice":
            self.wallet = ALICE_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "bob":
            self.wallet = BOB_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "carol":
            self.wallet = CAROL_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "dave":
            self.wallet = DAVE_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "elsa":
            self.wallet = ELSA_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "frank":
            self.wallet = FRANK_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "grace":
            self.wallet = GRACE_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "heidi":
            self.wallet = HEIDI_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "ivan":
            self.wallet = IVAN_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "judy":
            self.wallet = JUDY_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "hook1":
            self.wallet = HOOK1_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "hook2":
            self.wallet = HOOK2_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "hook3":
            self.wallet = HOOK3_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "hook4":
            self.wallet = HOOK4_ACCOUNT_WALLET
            self.account = self.wallet.classic_address
        if name == "hook5":
            self.wallet = HOOK5_ACCOUNT_WALLET
            self.account = self.wallet.classic_address


class ICXRP:
    def __init__(self, value: int):
        self.issuer = None
        self.currency = "XRP"
        self.value = value
        self.amount = xah_to_drops(self.value)


class IC:
    def __init__(self, issuer: str, currency: str, value: int):
        self.issuer = issuer
        self.currency = currency
        self.value = value
        self.amount = IssuedCurrencyAmount(
            currency=self.currency, value=str(self.value), issuer=self.issuer
        )

    @staticmethod
    def gw(name: str, gw: str) -> "IC":
        return IC(gw, name, 0)

    def set(self, value: int):
        self.value = value
        self.amount = IssuedCurrencyAmount(
            currency=self.currency, value=str(self.value), issuer=self.issuer
        )
        return self


async def account_seq(ctx: Client, account: str) -> int:
    request = AccountInfo(account=account)
    try:
        response = await ctx.request(request)
        return response.result["account_data"]["Sequence"]
    except Exception as error:
        print(error)
        return 0


def xrp_balance(ctx: Client, account: str) -> float:
    request = AccountInfo(account=account)
    response = ctx.request(request)
    if "error" in response.result and response.result["error"] == "actNotFound":
        return 0
    return float(response.result["account_data"]["Balance"])


def ic_balance(ctx: Client, account: str, ic: IC) -> float:
    request = LedgerEntry(
        ripple_state={
            "currency": ic.currency,
            "accounts": [account, ic.issuer],
        }
    )
    response = ctx.request(request)
    if "error" in response.result:
        return 0
    node = response.result["node"]
    return abs(float(node["Balance"]["value"]))


def balance(ctx: Client, account: str, ic: Union[IC, None] = None) -> float:
    try:
        if not ic:
            return xrp_balance(ctx, account)
        return ic_balance(ctx, account, ic)
    except Exception as error:
        print(error)
        return 0


def limit(ctx: Client, account: str, ic: IC) -> float:
    try:
        request = LedgerEntry(
            ripple_state={
                "currency": ic.currency,
                "accounts": [account, ic.issuer],
            }
        )
        response = ctx.request(request)
        if "error" in response.result:
            return 0
        node = response.result["node"]
        if node["HighLimit"]["issuer"] == ic.issuer:
            return float(node["LowLimit"]["value"])
        else:
            return float(node["HighLimit"]["value"])
    except Exception as error:
        print(error)
        return 0


def fund(ctx: Client, wallet: Wallet, uicx: Union[IC, ICXRP], *accts: str) -> None:
    for acct in accts:
        try:
            built_tx = Payment(
                account=wallet.classic_address,
                destination=acct,
                amount=uicx.amount,
            )
            app_transaction(
                ctx,
                built_tx,
                wallet,
            )
        except Exception as error:
            print(error)
            # print(error.data.decoded)
            # print(error.data.tx)


def pay(ctx: Client, uicx: Union[IC, ICXRP], signer: Wallet, *accts: str) -> None:
    for acct in accts:
        try:
            built_tx = Payment(
                account=signer.classic_address,
                destination=acct,
                amount=uicx.amount,
            )
            app_transaction(
                ctx,
                built_tx,
                signer,
            )
        except Exception as error:
            print(error)


def trust(ctx: Client, uicx: Union[IC, ICXRP], *accts: Wallet) -> None:
    for acct in accts:
        try:
            built_tx = TrustSet(
                account=acct.classic_address,
                limit_amount=uicx.amount,
            )
            app_transaction(
                ctx,
                built_tx,
                acct,
            )
        except Exception as error:
            print(error)


def account_set(ctx: Client, account: Wallet) -> None:
    built_tx = AccountSet(
        account=account.classic_address,
        transfer_rate=0,
        domain=str_to_hex("https://usd.transia.io"),
        set_flag=AccountSetAsfFlag.ASF_DEFAULT_RIPPLE,
    )
    app_transaction(
        ctx,
        built_tx,
        account,
    )


def rpc_tx(ctx: Client, account: Wallet, json: Dict[str, Any]) -> None:
    app_transaction(
        ctx,
        json,
        account,
    )


def rpc(ctx: Client, json: Dict[str, Any]) -> None:
    ctx.request(json)


def close(ctx: Client) -> None:
    ctx.request(LEDGER_ACCEPT_REQUEST)
