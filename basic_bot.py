import os
import logging
import json
from datetime import datetime
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from dotenv import load_dotenv

class BasicBot:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        # Load environment variables
        load_dotenv()
        
        # Setup logging first
        self.setup_logging()
        
        # Get API credentials
        self.api_key = api_key or os.getenv('BINANCE_API_KEY')
        self.api_secret = api_secret or os.getenv('BINANCE_SECRET_KEY')
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API credentials not found in .env file")
        
        # Initialize Binance client for testnet
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )
        
        self.logger.info("Trading bot initialized successfully")
    
    def setup_logging(self):
        """Setup logging to file and console"""
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        # Setup logging
        log_filename = f'logs/trading_bot_{datetime.now().strftime("%Y%m%d")}.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_account_balance(self):
        """Get account balance"""
        try:
            account = self.client.futures_account()
            balance = float(account['totalWalletBalance'])
            self.logger.info(f"Account Balance: {balance} USDT")
            return balance
        except Exception as e:
            self.logger.error(f"Error getting account balance: {e}")
            return 0.0
    
    def get_current_price(self, symbol):
        """Get current price for a symbol"""
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol.upper())
            price = float(ticker['price'])
            self.logger.info(f"Current price for {symbol}: {price}")
            return price
        except Exception as e:
            self.logger.error(f"Error getting price for {symbol}: {e}")
            return 0.0
    
    def place_market_order(self, symbol, side, quantity):
        """
        Place a market order
        symbol: Trading pair like 'BTCUSDT'
        side: 'BUY' or 'SELL'
        quantity: Amount to trade
        """
        try:
            self.logger.info(f"Placing market {side} order: {quantity} {symbol}")
            
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            
            self.logger.info(f"Market order successful! Order ID: {order['orderId']}")
            self.save_order_to_log(order)
            return order
            
        except BinanceOrderException as e:
            self.logger.error(f"Order failed: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return None
    
    def place_limit_order(self, symbol, side, quantity, price):
        """
        Place a limit order
        symbol: Trading pair like 'BTCUSDT'
        side: 'BUY' or 'SELL'
        quantity: Amount to trade
        price: Limit price
        """
        try:
            self.logger.info(f"Placing limit {side} order: {quantity} {symbol} at {price}")
            
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            
            self.logger.info(f"Limit order successful! Order ID: {order['orderId']}")
            self.save_order_to_log(order)
            return order
            
        except BinanceOrderException as e:
            self.logger.error(f"Order failed: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return None
    
    def get_order_status(self, symbol, order_id):
        """Check order status"""
        try:
            order = self.client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )
            self.logger.info(f"Order {order_id} status: {order['status']}")
            return order
        except Exception as e:
            self.logger.error(f"Error getting order status: {e}")
            return None
    
    def save_order_to_log(self, order):
        """Save order details to JSON log file"""
        order_data = {
            'timestamp': datetime.now().isoformat(),
            'orderId': order.get('orderId'),
            'symbol': order.get('symbol'),
            'side': order.get('side'),
            'type': order.get('type'),
            'quantity': order.get('origQty'),
            'price': order.get('price'),
            'status': order.get('status')
        }
        
        # Save to JSON log file
        log_file = f'logs/orders_{datetime.now().strftime("%Y%m%d")}.json'
        with open(log_file, 'a') as f:
            json.dump(order_data, f)
            f.write('\n')