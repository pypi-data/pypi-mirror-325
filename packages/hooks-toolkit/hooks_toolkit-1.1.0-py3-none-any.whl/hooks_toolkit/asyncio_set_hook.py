#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any

from xahau.clients.sync_client import SyncClient
from xahau.wallet import Wallet
from xahau.models.transactions import SetHook
from xahau.models.transactions.set_hook import Hook
from xahau.utils import calculate_hook_on
from xahau.models.transactions import SetHookFlag

from hooks_toolkit.libs.asyncio.xrpl_helpers.transaction import (
    get_transaction_fee,
    app_transaction,
)
from hooks_toolkit.utils import hex_namespace, read_hook_binary_hex_from_ns
from hooks_toolkit.types import SetHookParams


def create_hook_payload(
    params: SetHookParams,
) -> Hook:
    kwargs: Dict[str, Any] = {
        "hook_api_version": params.version,
        "hook_namespace": hex_namespace(params.namespace),
    }

    if params.create_file is not None:
        if params.version == 0:
            kwargs["create_code"] = read_hook_binary_hex_from_ns(
                params.create_file, "wasm"
            )
        elif params.version == 1:
            kwargs["create_code"] = read_hook_binary_hex_from_ns(
                params.create_file, "bc"
            )

    if params.hook_on_array is not None:
        kwargs["hook_on"] = calculate_hook_on(params.hook_on_array)

    if params.hook_hash is not None:
        kwargs["hook_hash"] = params.hook_hash

    if params.flags is not None:
        kwargs["flags"] = params.flags

    if params.hook_parameters is not None:
        kwargs["hook_parameters"] = params.hook_parameters

    if params.hook_grants is not None:
        kwargs["hook_grants"] = params.hook_grants

    return Hook(**kwargs)


async def set_hooks_v3(client: SyncClient, seed: str, hooks: List[Hook]):
    HOOK_ACCOUNT = Wallet.from_seed(seed)
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
        fee=await get_transaction_fee(client, _tx),
    )

    await app_transaction(
        client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000
    )


async def clear_all_hooks_v3(client: SyncClient, seed: str):
    HOOK_ACCOUNT = Wallet.from_seed(seed)
    hook = Hook(
        **{
            "create_code": "",
            "flags": [SetHookFlag.HSF_OVERRIDE, SetHookFlag.HSF_NS_DELETE],
        }
    )
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=[hook, hook, hook, hook, hook, hook, hook, hook, hook, hook],
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=[hook, hook, hook, hook, hook, hook, hook, hook, hook, hook],
        fee=await get_transaction_fee(client, _tx),
    )

    await app_transaction(
        client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000
    )


async def clear_hook_state_v3(client: SyncClient, seed: str, hooks: List[Hook]):
    HOOK_ACCOUNT = Wallet.from_seed(seed)
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
        fee=await get_transaction_fee(client, _tx),
    )
    await app_transaction(
        client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000
    )
