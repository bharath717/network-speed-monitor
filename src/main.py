print("Network Speed Monitor System - Initialized")
import time
# We will import the other modules later as the team finishes them
# from engine import get_speed_data 

def run_24_7_monitor():
    print("--- Network Speed Monitor Started ---")
    print("System is now monitoring 24/7. Press Ctrl+C to stop.")
    
    while True:
        try:
            # This is where the core logic will happen
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Checking speed...")
            
            # For now, we just simulate a wait. 
            # In the final version, this will wait 30 minutes (1800 seconds)
            time.sleep(10) 
            
        except KeyboardInterrupt:
            print("\nStopping the monitor. Goodbye!")
            break

if __name__ == "__main__":
    run_24_7_monitor()