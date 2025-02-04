# Binance

- [Binance](#binance)
- [Installation](#installation)
- [Usage](#usage)
  - [Public APIs](#public-apis)
  - [Private API](#private-api)
  - [Context Manager](#context-manager)
- [Supported APIs](#supported-apis)
  - [Spot](#spot)
    - [General](#general)
    - [Market Data](#market-data)
    - [Trading](#trading)
    - [Account](#account)
  - [Margin](#margin)
  - [Simple Earn](#simple-earn)
    - [Account](#account-1)
    - [Earn](#earn)
    - [~~History~~ support unplanned](#history-support-unplanned)
  - [Wallet](#wallet)
    - [Capital](#capital)
    - [~~Asset~~ support unplanned](#asset-support-unplanned)
    - [~~Account~~ support unplanned](#account-support-unplanned)
    - [~~Travel Rule~~ support unplanned](#travel-rule-support-unplanned)


# Installation

```bash
pip install binance-python
```

# Usage

## Public APIs

You can use specific API clients without authentication. E.g:

```python
from binance.spot import MarketData

client = MarketData()
await client.candles('BTCUSDT', interval='1m', limit=4)
# [Candle(open_time=datetime(...), close_time=datetime(...), open=Decimal('93970.04000000'), ...), ...]
```

## Private API

Easiest is to just use the general client:

```python
from binance import Binance

client = Binance(API_KEY, API_SECRET)
# or client = Binance.env() to load `API_KEY` and `API_SECRET` from environment variables or a .env file

await client.spot.new_order('BTCUSDT', {
  'price', 10000, ... # let the type hints guide you
})
```

## Context Manager

To run multiple requests concurrently, I'd recommend using the client as a context manager:

```python
from binance import Binance

client = Binance(API_KEY, API_SECRET)

async with client:
  await client.spot.new_order('BTCUSDT', {
    'price', 10000, ...
  })
  await client.spot.new_order('ETHUSDT', {
    'price', 2000, ...
  })
```


# Supported APIs

## Spot

### General
- [x] [Ping](binance/src/binance/spot/general/_ping.py)
- [x] [Time](binance/src/binance/spot/general/_time.py)
- [x] [Exchange Information](binance/src/binance/spot/general/_info.py)

### Market Data
- [x] [Order Book](binance/src/binance/spot/data/_order_book.py)
- [x] [Recent Trades](binance/src/binance/spot/data/_trades_recent.py)
- [x] [Old Trades](binance/src/binance/spot/data/_trades_old.py)
- [x] [Aggregated Trades](binance/src/binance/spot/data/_trades_agg.py)
- [x] [Candles](binance/src/binance/spot/data/_candles.py)
- [x] [UI Candles](binance/src/binance/spot/data/_candles_ui.py)
- [x] [Average Price](binance/src/binance/spot/data/_avg_price.py)
- [x] [Last 24h Price Change Statistics](binance/src/binance/spot/data/_stats_24h.py)
- [x] [Last Day Price Change Statistics](binance/src/binance/spot/data/_stats_day.py)
- [x] [Current Price](binance/src/binance/spot/data/_price.py)
- [ ] ~~Symbol Order Book Ticker~~ unnecessary, use Order Book instead
- [x] [Window Price Change Statistics](binance/src/binance/spot/data/_stats.py)

### Trading
- [x] [New Order](binance/src/binance/spot/trading/_new_order.py)
- [x] [Test New Order](binance/src/binance/spot/trading/_test_order.py)
- [x] [Query Order](binance/src/binance/spot/trading/_query_order.py)
- [x] [Cancel Order](binance/src/binance/spot/trading/_cancel_order.py)
- [x] [Cancel Open Orders](binance/src/binance/spot/trading/_cancel_open_orders.py)
- [x] [Replace Order](binance/src/binance/spot/trading/_replace_order.py)
- [x] [Query Open Orders](binance/src/binance/spot/trading/_query_open_orders.py)
- [x] [Query All Orders](binance/src/binance/spot/trading/_query_all_orders.py.py)
- [x] [New OCO Order](binance/src/binance/spot/trading/_oco_order.py)
- [x] [New OTO Order](binance/src/binance/spot/trading/_oto_order.py)
- [x] [New OTOCO Order](binance/src/binance/spot/trading/_otoco_order.py)
- [x] [Cancel Order List](binance/src/binance/spot/trading/_cancel_order_list.py)
- [ ] ~~Query Order List~~ support unplanned
- [ ] Query ~~All Order Lists~~ support unplanned
- [ ] Query ~~Open Order Lists~~ support unplanned
- [ ] ~~New SOR Order~~ support unplanned
- [ ] ~~Test SOR Order~~ support unplanned

### Account
- [x] [Information](binance/src/binance/spot/account/_info.py)
- [x] [List Trades](binance/src/binance/spot/account/_trades.py)
- [ ] ~~Query Unfilled Order Count~~ support unplanned
- [ ] ~~Query Prevented Matches~~ support unplanned
- [ ] ~~Query Allocations~~ support unplanned
- [ ] ~~Query Commission Rates~~ support unplanned

## Margin
- [ ] Market Data
- [ ] Trading
- [ ] Borrow and Repay
- [ ] Account
- [ ] Transfer

## Simple Earn

### Account
- [x] [Account Summary](binance/src/binance/simple_earn/account/_account.py)
- [x] [List Flexible Products](binance/src/binance/simple_earn/account/_flexible_products.py)
- [x] [List Locked Products](binance/src/binance/simple_earn/account/_locked_products.py)
- [x] [Flexible Product Position](binance/src/binance/simple_earn/account/_flexible_position.py)
- [x] [Locked Product Position](binance/src/binance/simple_earn/account/_locked_position.py)
- [x] [Flexible Product Left Quota](binance/src/binance/simple_earn/account/_flexible_quota.py)
- [x] [Locked Product Left Quota](binance/src/binance/simple_earn/account/_locked_quota.py)

### Earn
- [x] [Subscribe Flexible Product](binance/src/binance/simple_earn/earn/_flexible_subscribe.py)
- [ ] ~~Subscribe Locked Product~~ support unplanned
- [x] [Redeem Flexible Product](binance/src/binance/simple_earn/earn/_flexible_redeem.py)
- [x] ~~Redeem Locked Product~~ support unplanned
- [ ] ~~Set Flexible Auto-Subscribe~~ support unplanned
- [ ] ~~Set Locked Auto-Subscribe~~ support unplanned
- [x] [Flexible Subscription Preview](binance/src/binance/simple_earn/earn/_flexible_preview.py)
- [ ] ~~Locked Subscription Preview~~ support unplanned
- [ ] ~~Set Locked Redeem Option~~ support unplanned

### ~~History~~ support unplanned

## Wallet

### Capital
- [ ] All Coins Info
- [ ] Withdraw
- [ ] Withdraw History
- [ ] Withdraw Address List
- [ ] Deposit History
- [ ] Deposit Address
- [ ] Deposit Address List
- [ ] ~~One-Click Deposit~~ support unplanned

### ~~Asset~~ support unplanned
### ~~Account~~ support unplanned
### ~~Travel Rule~~ support unplanned