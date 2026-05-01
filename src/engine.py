import speedtest

def get_speed_metrics():
    """
    This function performs the actual network test.
    Returns a dictionary with the results.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server() # Finds the fastest server near you
        
        print("Testing Download speed...")
        download = st.download() / 1_000_000  # Convert bits to Megabits (Mbps)
        
        print("Testing Upload speed...")
        upload = st.upload() / 1_000_000      # Convert bits to Megabits (Mbps)
        
        ping = st.results.ping
        
        return {
            "download": round(download, 2),
            "upload": round(upload, 2),
            "ping": ping,
            "status": "Success"
        }
    except Exception as e:
        return {"status": "Error", "message": str(e)}

# For local testing by Member 2
if __name__ == "__main__":
    print("Running local test...")
    print(get_speed_metrics())