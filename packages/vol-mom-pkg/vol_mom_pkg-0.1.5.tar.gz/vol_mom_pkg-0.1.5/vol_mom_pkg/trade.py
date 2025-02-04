from alpaca_trade_api.rest import REST, TimeFrame
from vol_mom_pkg.signals import calculate_portfolios

ALPACA_API_KEY = "PK5GQYQ3U0O0757WU7UL"
ALPACA_API_SECRET = "BXkteDM64HnCfKcbzyg5k3APgKEDdBtxgfKB6VOM"
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

# Initialize Alpaca API client
api = REST(ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL)

def get_account_info():
    account = api.get_account()
    return float(account.equity)  # Equivalent to Net Liquidation

def place_orders(df, trade_direction):
    def place_market_order(symbol, allocation, direction):
        # Fetch the previous close price using get_bars
        bars = api.get_bars(symbol, TimeFrame.Day, limit=5).df
        
        if bars.empty:
            print(f"Unable to fetch historical data for {symbol}. Skipping...")
            return

        previous_close = bars.iloc[-1].close

        # Calculate the number of shares to trade
        quantity = int(allocation // previous_close)
        if quantity <= 0:
            print(f"Allocation too small for {symbol} at price {previous_close}. Skipping...")
            return

        side = "buy" if direction == "long" else "sell"

        # Submit the order
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side=side,
            type="market",
            time_in_force="gtc"
        )
        print(f"Placed {side.upper()} order for {quantity} shares of {symbol}.")

    for _, row in df.iterrows():
        try:
            place_market_order(row["Symbol"], row["Dollar Allocation"], trade_direction)
        except Exception as e:
            print(f"Error placing order for {row['Symbol']}: {e}")

def close_all_positions():
    try:
        positions = api.list_positions()
        if not positions:
            print("No open positions to close.")
            return
        
        for position in positions:
            symbol = position.symbol
            qty = abs(int(float(position.qty)))  # Ensure quantity is positive
            side = "sell" if position.side == "long" else "buy"
            api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type="market",
                time_in_force="gtc"
            )
            print(f"Closing {side.upper()} order for {qty} shares of {symbol}.")
        
        print("All positions have been closed.")
    except Exception as e:
        print(f"Error closing positions: {e}")


def send_weekly_basket():
    close_all_positions()
    pf = get_account_info()
    lookback = 22
    winners_from_low_vol, losers_from_high_vol, low_vol_from_winners, high_vol_from_losers = calculate_portfolios(lookback, pf)
    place_orders(losers_from_high_vol, 'long')

