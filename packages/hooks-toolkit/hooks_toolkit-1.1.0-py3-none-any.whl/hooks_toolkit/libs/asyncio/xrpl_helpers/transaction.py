#!/usr/bin/env python
# coding: utf-8

import json
import os
from typing import Union, List

from xahau.asyncio.transaction import (
    sign_and_submit,
    autofill,
    autofill_and_sign,
    submit_and_wait,
)
from xahau.asyncio.clients import AsyncWebsocketClient
from xahau.models import GenericRequest, Response, Transaction
from xahau.wallet import Wallet
from xahau.core.binarycodec import encode
from xahau.asyncio.ledger import get_fee_estimate
from xahau.models.requests import Tx

LEDGER_ACCEPT_REQUEST = GenericRequest(method="ledger_accept")


async def verify_submitted_transaction(
    client: AsyncWebsocketClient, tx: Union[Transaction, str]
) -> Response:
    # hash = hash_tx if tx else hash_signed_tx(tx)
    hash = tx
    data = await client.request(Tx(transaction=hash))

    # assert data.result
    # assert data.result == (decode(tx) if isinstance(tx, str) else tx)
    # if isinstance(data.result.meta, dict):
    #     assert data.result.meta["TransactionResult"] == "tesSUCCESS"
    # else:
    #     assert data.result.meta == "tesSUCCESS"
    return data


async def get_transaction_fee(client: AsyncWebsocketClient, transaction: Transaction):
    # copy_tx = transaction.to_xrpl()
    # copy_tx["Fee"] = "0"
    # copy_tx["SigningPubKey"] = ""
    prepared_tx = await autofill(transaction, client)

    tx_blob = encode(prepared_tx.to_xrpl())

    result = await get_fee_estimate(client, tx_blob)

    return result


envs: List[str] = ["production", "testnet", "mainnet"]


async def app_transaction(
    client: AsyncWebsocketClient,
    transaction: Transaction,
    wallet: Wallet,
    hard_fail: bool = True,
    count: int = 0,
    delay_ms: int = 0,
) -> Response:
    if os.environ.get("XAHAUD_ENV") == "standalone":
        return await test_transaction(
            client, transaction, wallet, hard_fail, count, delay_ms
        )

    if os.environ.get("XAHAUD_ENV") in envs:
        tx: Transaction = autofill_and_sign(transaction, client, wallet, check_fee=True)
        return await submit_and_wait(tx, client)

    raise ValueError("unimplemented")


async def test_transaction(
    client: AsyncWebsocketClient,
    transaction: Transaction,
    wallet: Wallet,
    hard_fail: bool,
    count: int,
    delay_ms: int,
) -> Response:
    await client.request(LEDGER_ACCEPT_REQUEST)

    response = await sign_and_submit(transaction, client, wallet, True, False)

    assert response.type == "response"

    if response.result["engine_result"] != "tesSUCCESS":
        print(
            (
                f"Transaction was not successful. "
                f"Expected response.result.engine_result to be tesSUCCESS "
                f"but got {response.result['engine_result']}"
            )
        )
        print("The transaction was: ", transaction)
        print("The response was: ", json.dumps(response.result))

    if hard_fail:
        assert response.result["engine_result"] == "tesSUCCESS", response.result[
            "engine_result_message"
        ]

    await client.request(LEDGER_ACCEPT_REQUEST)
    return await verify_submitted_transaction(
        client, response.result["tx_json"]["hash"]
    )
