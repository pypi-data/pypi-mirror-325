import datetime as dt
import yfinance as yf

class fetch_option_data:
    """
    A helper class to fetch option chain data from yfinance
    and retrieve specific option parameters (spot, implied vol, etc.)
    for a given ticker and expiration date.
    """

    def __init__(self, ticker, expiry_date_str):
        """
        Initialize with a specific ticker (e.g. 'SPY')
        and an expiration date string in 'YYYY-MM-DD' format
        (e.g. '2025-02-12').
        """
        self.ticker = ticker
        self.expiry_date_str = expiry_date_str
        # yfinance Ticker object
        self.underlying = yf.Ticker(self.ticker)
        # We'll fetch & store the list of available expirations for debugging
        self.available_dates = self.underlying.options

    def get_option_chain(self):
        """
        Retrieves option chain DataFrames for the specified
        ticker & expiration date.
        
        Returns a namedtuple-like object with:
            .calls  -> DataFrame of call options
            .puts   -> DataFrame of put options
        or None if the expiration isn't valid.
        """
        if self.expiry_date_str not in self.available_dates:
            print(f"Requested expiration {self.expiry_date_str} not in "
                  f"available dates: {self.available_dates}")
            return None
        
        # Return the option chain object (calls/puts)
        return self.underlying.option_chain(self.expiry_date_str)

    def fetch_option_data(self, strike, option_type='put'):
        """
        Grabs the latest market data (spot, option chain) for the
        specified strike and option type, then returns a dictionary
        with:
            {
              'spot': <latest underlying price>,
              'strike': <option strike>,
              'expiration': <datetime object>,
              'implied_volatility': <IV in percent>,
              'last_price': <option last trade price>,
              'bid': <option bid>,
              'ask': <option ask>,
            }
        or None if data cannot be found.
        
        Parameters
        ----------
        strike : float
            The desired option strike price.
        option_type : str
            "put" or "call". Defaults to "put".
        """
        # 1. Download minimal price data for the underlying
        data = yf.download(self.ticker, period="1d", interval="1m")
        if data.empty:
            print("No intraday data returned by yfinance.")
            return None
        
        current_spot = data['Close'][-1]

        # 2. Get the option chain
        chain = self.get_option_chain()
        if chain is None:
            return None

        # 3. Select puts or calls
        if option_type.lower() == 'put':
            df = chain.puts
        else:
            df = chain.calls
        
        # 4. Filter for the desired strike
        opt_row = df[df['strike'] == float(strike)]
        if opt_row.empty:
            print(f"No option found for strike = {strike} and type = {option_type}")
            return None

        # 5. Extract fields
        last_price = opt_row['lastPrice'].values[0]
        implied_vol = opt_row['impliedVolatility'].values[0]
        bid = opt_row['bid'].values[0]
        ask = opt_row['ask'].values[0]

        return {
            'spot': current_spot,
            'strike': strike,
            'expiration': dt.datetime.strptime(self.expiry_date_str, '%Y-%m-%d'),
            'implied_volatility': implied_vol * 100.0,  # from e.g. 0.1783 to 17.83%
            'last_price': last_price,
            'bid': bid,
            'ask': ask
        }


if __name__ == "__main__":
    # Example usage
    ticker = "SPY"
    expiry_date_str = "2025-02-12"
    strike = 590
    option_type = "put"

    fetcher = fetch_option_data(ticker, expiry_date_str)
    result = fetcher.fetch_option_data(strike, option_type=option_type)

    if result:
        print("\nFetched option data:")
        for key, val in result.items():
            print(f"{key}: {val}")

        # Example of how you'd feed data back into your American‐option script:
        #
        # me_spy_gbm.add_constant('initial_value', result['spot'])
        # me_spy_gbm.add_constant('volatility', result['implied_volatility'])
        # me_spy_gbm.add_constant('final_date', result['expiration'])
        # me_spy_am_put.add_constant('strike', result['strike'])
        #
        # ... then run valuation_mcs_american, etc.
