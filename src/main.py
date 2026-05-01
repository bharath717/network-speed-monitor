import time
# Importing the logic from your team's files
from engine import get_speed_metrics
from db_manager import init_db, save_log

def run_24_7_monitor():
    print("--- Network Speed Monitor Started ---")
    
    # Step 1: Initialize the database table
    init_db()
    
    print("System is now monitoring 24/7. Press Ctrl+C to stop.")
    
    while True:
        try:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting Speed Test...")
            
            # Step 2: Call the engine to get real speed
            results = get_speed_metrics()
            
            if results['status'] == 'Success':
                # Step 3: Save the results to the database
                save_log(results['download'], results['upload'], results['ping'])
                print(f"✅ Logged: {results['download']} Mbps Download / {results['upload']} Mbps Upload")
            else:
                print(f"❌ Error: {results.get('message')}")
            
            # Step 4: Wait before the next test
            # Set to 1800 for 30 minutes. Keeping it shorter for your testing.
            print("Waiting for next check...")
            time.sleep(60) 
            
        except KeyboardInterrupt:
            print("\nStopping the monitor. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_24_7_monitor()