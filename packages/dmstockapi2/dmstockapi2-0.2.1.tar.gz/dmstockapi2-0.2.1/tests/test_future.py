import pytest
import os
from dmstockapi.future_client import FutureClient


@pytest.fixture
def client():
    return FutureClient(
        api_key=os.getenv("WEBTRADE_API_KEY"),
        api_url=os.getenv("WEBTRADE_API_URL"),
        keep_alive=True,
    )


@pytest.mark.parametrize(
    "account_id, portfolio_id",
    [
        ("900006", "37a7d824-a2d0-4332-a4b2-15d9318e2635"),
    ],
)
def test_future_trade_planning(client, account_id, portfolio_id):
    df = client.future_trade_planning(account_id=account_id, portfolio_id=portfolio_id)
    assert not df.empty
    assert df.iloc[0]["account"] == account_id
    assert df.iloc[0]["portfolioid"] == portfolio_id
