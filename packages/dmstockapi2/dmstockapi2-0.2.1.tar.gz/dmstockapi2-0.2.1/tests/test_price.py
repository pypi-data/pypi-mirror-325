import pytest
import dmstockapi as dmapi
import os


@pytest.fixture
def client():
    return dmapi.Client(
        api_key=os.getenv("DATA_API_KEY"),
        api_url=os.getenv("DATA_API_URL"),
        keep_alive=True,
    )


@pytest.mark.parametrize("symbol", ["000001.SZ", "600702.SH", "600519.SH"])
def test_stock_profile(client, symbol):
    df = client.stock_profile(symbol=symbol)
    assert df is not None
    assert not df.empty
    assert df["symbol"].values[0] == symbol


@pytest.mark.parametrize("symbol", ["000001.SZ", "600702.SH", "600519.SH"])
def test_stock_candles(client, symbol):
    df = client.stock_candles(
        symbol=symbol,
        interval="D",
        start_date="2024-12-01",
        end_date="2024-12-31",
        adjust="F",
    ).reset_index()
    assert df is not None
    assert not df.empty
    assert df["symbol"].values[0] == symbol
    assert df["close"].values[0] > 0


@pytest.mark.parametrize("symbol", ["DFJ0", "DFM0"])
def test_future_candles(client, symbol):
    df = client.future_candles(
        symbol=symbol,
        interval="D",
        start_date="2024-12-01",
        end_date="2024-12-31",
    ).reset_index()
    assert df is not None
    assert not df.empty
    assert df["symbol"].values[0] == symbol
    assert df["close"].values[0] > 0
