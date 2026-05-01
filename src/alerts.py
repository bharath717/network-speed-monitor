def check_thresholds(download_speed):
    # Set a minimum threshold, e.g., 10 Mbps
    THRESHOLD = 10.0
    if download_speed < THRESHOLD:
        print(f"⚠️ ALERT: Network speed is low! ({download_speed} Mbps)")
        # In the future, Member 6 can add email logic here