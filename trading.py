from basic_bot import BasicBot

def display_menu():
    print("\n" + "="*40)
    print("  CRYPTO TRADING BOT - TESTNET")
    print("="*40)
    print("1. Check Account Balance")
    print("2. Get Current Price")
    print("3. Place Market Order")
    print("4. Place Limit Order")
    print("5. Check Order Status")
    print("6. Exit")
    print("="*40)

def main():
    print("🚀 Starting Crypto Trading Bot...")
    
    try:
        # Initialize the bot
        bot = BasicBot(testnet=True)
        print("✅ Bot connected successfully!")
        
        # Show initial balance
        balance = bot.get_account_balance()
        print(f"💰 Current Balance: {balance} USDT")
        
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Check balance
                balance = bot.get_account_balance()
                print(f"💰 Current Balance: {balance} USDT")
            
            elif choice == '2':
                # Get current price
                symbol = input("Enter symbol (e.g., BTCUSDT): ").strip()
                price = bot.get_current_price(symbol)
                if price > 0:
                    print(f"💲 Current price of {symbol}: {price}")
                else:
                    print("❌ Could not get price")
            
            elif choice == '3':
                # Place market order
                print("\n📈 MARKET ORDER")
                symbol = input("Enter symbol (e.g., BTCUSDT): ").strip()
                side = input("Enter side (BUY/SELL): ").strip().upper()
                quantity = input("Enter quantity: ").strip()
                
                try:
                    quantity = float(quantity)
                    result = bot.place_market_order(symbol, side, quantity)
                    if result:
                        print(f"✅ Market order placed! Order ID: {result['orderId']}")
                    else:
                        print("❌ Market order failed")
                except ValueError:
                    print("❌ Invalid quantity")
            
            elif choice == '4':
                # Place limit order
                print("\n📊 LIMIT ORDER")
                symbol = input("Enter symbol (e.g., BTCUSDT): ").strip()
                side = input("Enter side (BUY/SELL): ").strip().upper()
                quantity = input("Enter quantity: ").strip()
                price = input("Enter price: ").strip()
                
                try:
                    quantity = float(quantity)
                    price = float(price)
                    result = bot.place_limit_order(symbol, side, quantity, price)
                    if result:
                        print(f"✅ Limit order placed! Order ID: {result['orderId']}")
                    else:
                        print("❌ Limit order failed")
                except ValueError:
                    print("❌ Invalid quantity or price")
            
            elif choice == '5':
                # Check order status
                print("\n🔍 CHECK ORDER STATUS")
                symbol = input("Enter symbol: ").strip()
                order_id = input("Enter order ID: ").strip()
                
                try:
                    order_id = int(order_id)
                    status = bot.get_order_status(symbol, order_id)
                    if status:
                        print(f"📋 Order Status: {status['status']}")
                        print(f"📊 Filled: {status.get('executedQty', 0)}")
                    else:
                        print("❌ Could not get order status")
                except ValueError:
                    print("❌ Invalid order ID")
            
            elif choice == '6':
                print("👋 Goodbye! Trading session ended.")
                break
            
            else:
                print("❌ Invalid choice. Please try again.")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your .env file and API credentials")

if __name__ == "__main__":
    main()