# Crypto Trading Bot - Binance Futures Testnet

A simple Python trading bot for Binance Futures Testnet that supports market orders, limit orders, and stop-limit orders.

## Features

- ✅ Market Orders (BUY/SELL)
- ✅ Limit Orders (BUY/SELL)
- ✅ Stop-Limit Orders (Bonus feature)
- ✅ Real-time price checking
- ✅ Order status monitoring
- ✅ Comprehensive logging
- ✅ User-friendly CLI interface

## Setup Instructions

### 1. Get Binance Testnet API Keys

1. Go to [Binance Testnet](https://testnet.binancefuture.com/)
2. Login with your Binance account
3. Navigate to API Management
4. Create new API key with futures trading permissions
5. Copy your API Key and Secret Key

### 2. Install the Bot

```bash
# Clone/download the project
mkdir crypto_trading_bot
cd crypto_trading_bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install python-binance==1.0.19 python-dotenv==1.0.0

# Create logs directory
mkdir logs
```

### 3. Configure API Keys

Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_actual_api_key_here
BINANCE_SECRET_KEY=your_actual_secret_key_here
```

**⚠️ Never commit the .env file to version control!**

### 4. Run the Bot

```bash
python main.py
```

## Usage Examples

### Basic Trading
1. Start the bot: `python main.py`
2. Check your balance
3. Get current price for a symbol (e.g., BTCUSDT)
4. Place market or limit orders
5. Monitor order status


## File Structure

```
crypto_trading_bot/
├── main.py              # Main application with CLI
├── basic_bot.py         # Core trading bot class
├── .env                 # API credentials (create this)
├── requirements.txt     # Dependencies
├── logs/                # Log files directory
│   ├── trading_bot_YYYYMMDD.log
│   └── orders_YYYYMMDD.json
└── README.md           # This file
```

## Logging

The bot creates detailed logs in the `logs/` directory:

- **trading_bot_YYYYMMDD.log**: Main application logs
- **orders_YYYYMMDD.json**: Order execution details in JSON format

## Safety Features

- ✅ **Testnet Only**: No real money at risk
- ✅ **Input Validation**: Validates all order parameters
- ✅ **Error Handling**: Comprehensive error catching
- ✅ **Logging**: All actions are logged for review

## Supported Order Types

### 1. Market Orders
- Executes immediately at current market price
- Use for quick entry/exit

### 2. Limit Orders
- Executes only at specified price or better
- Use for precise price control

### 3. Stop-Limit Orders (Bonus)
- Triggers a limit order when stop price is reached
- Use for risk management

## Example Trading Session

```
🚀 Starting Crypto Trading Bot...
✅ Bot connected successfully!
💰 Current Balance: 10000.0 USDT

========================================
  CRYPTO TRADING BOT - TESTNET
========================================
1. Check Account Balance
2. Get Current Price
3. Place Market Order
4. Place Limit Order
5. Check Order Status
6. Exit
========================================

Enter your choice (1-6): 2
Enter symbol (e.g., BTCUSDT): BTCUSDT
💲 Current price of BTCUSDT: 43250.5
```

## Troubleshooting

### Common Issues

1. **"API credentials not found"**
   - Make sure `.env` file exists
   - Check API key and secret are correct

2. **"Connection failed"**
   - Check internet connection
   - Verify testnet URL is accessible

3. **"Order failed"**
   - Check account balance
   - Verify symbol is correct (e.g., BTCUSDT)
   - Ensure quantity meets minimum requirements

### Getting Help

- Check the log files in `logs/` directory
- Verify API permissions on Binance Testnet
- Ensure you're using the testnet, not live trading

## Submission Files

For the job application, include:
- All source code files
- Sample log files from testing
- This README.md
- Screenshots of successful trades (optional)

## Disclaimer

This is a testnet trading bot for educational purposes only. No real money is involved. Always test thoroughly before any live trading.
