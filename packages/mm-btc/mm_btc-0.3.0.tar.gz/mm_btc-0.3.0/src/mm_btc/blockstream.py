from collections.abc import Sequence

from mm_std import Err, HResponse, Ok, Result, hr
from mm_std.random_ import random_str_choice
from pydantic import BaseModel

MAINNET_BASE_URL = "https://blockstream.info/api"
TESTNET_BASE_URL = "https://blockstream.info/testnet/api"

# ERROR_INVALID_ADDRESS = "INVALID_ADDRESS"
# ERROR_INVALID_NETWORK = "INVALID_NETWORK"

ERROR_400_BAD_REQUEST = "400 Bad Request"

type Proxy = str | Sequence[str] | None


class Mempool(BaseModel):
    count: int
    vsize: int
    total_fee: int
    fee_histogram: list[tuple[float, int]]


class Address(BaseModel):
    class ChainStats(BaseModel):
        funded_txo_count: int
        funded_txo_sum: int
        spent_txo_count: int
        spent_txo_sum: int
        tx_count: int

    class MempoolStats(BaseModel):
        funded_txo_count: int
        funded_txo_sum: int
        spent_txo_count: int
        spent_txo_sum: int
        tx_count: int

    chain_stats: ChainStats
    mempool_stats: MempoolStats


class Utxo(BaseModel):
    class Status(BaseModel):
        confirmed: bool
        block_height: int
        block_hash: str
        block_time: int

    txid: str
    vout: int
    status: Status
    value: int


class BlockstreamClient:
    def __init__(self, testnet: bool = False, timeout: int = 10, proxies: Proxy = None, attempts: int = 1) -> None:
        self.testnet = testnet
        self.timeout = timeout
        self.proxies = proxies
        self.attempts = attempts
        self.base_url = TESTNET_BASE_URL if testnet else MAINNET_BASE_URL

    def get_address(self, address: str) -> Result[Address]:
        result: Result[Address] = Err("not started yet")
        data = None
        for _ in range(self.attempts):
            try:
                res = self._request(f"/address/{address}")
                data = res.to_dict()
                if res.code == 400:
                    return Err("400 Bad Request", data=data)
                return Ok(Address(**res.json), data=data)
            except Exception as err:
                result = Err(err, data=data)
        return result

    def get_confirmed_balance(self, address: str) -> Result[int]:
        return self.get_address(address).and_then(lambda a: Ok(a.chain_stats.funded_txo_sum - a.chain_stats.spent_txo_sum))

    def get_utxo(self, address: str) -> Result[list[Utxo]]:
        result: Result[list[Utxo]] = Err("not started yet")
        data = None
        for _ in range(self.attempts):
            try:
                res = self._request(f"/address/{address}/utxo")
                data = res.to_dict()
                return Ok([Utxo(**out) for out in res.json], data=data)
            except Exception as err:
                result = Err(err, data=data)
        return result

    def get_mempool(self) -> Result[Mempool]:
        result: Result[Mempool] = Err("not started yet")
        data = None
        for _ in range(self.attempts):
            try:
                res = self._request("/mempool")
                data = res.to_dict()
                return Ok(Mempool(**res.json), data=data)
            except Exception as err:
                result = Err(err, data=data)
        return result

    def _request(self, url: str) -> HResponse:
        return hr(f"{self.base_url}{url}", timeout=self.timeout, proxy=random_str_choice(self.proxies))
