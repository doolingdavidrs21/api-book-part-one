from swcpy import SWCClient
from swcpy import SWCConfig

# 1. Point the config to your new AWS URL
# Note: I removed the trailing slash '/' just to be safe, though most libs handle it.
aws_url = "https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com"

print(f"Attempting to connect to: {aws_url}...")

# 2. Initialize the client
config = SWCConfig(swc_base_url=aws_url, backoff=False)
client = SWCClient(config)

# 3. Try to fetch data
try:
    print("Fetching leagues...")
    leagues = client.list_leagues()

    print("\nSUCCESS! Here is the data from AWS:")
    print(leagues)

except Exception as e:
    print("\nERROR: Could not connect to AWS.")
    print(e)


# ... (keep previous code)

print("\n--- Testing Bulk Download ---")
try:
    # This uses the URL we fixed earlier
    csv_bytes = client.get_bulk_player_file()

    # Check if we got data back
    print(f"Success! Downloaded {len(csv_bytes)} bytes of player data.")

    # Optional: Save it to see if it's real
    with open("downloaded_players.csv", "wb") as f:
        f.write(csv_bytes)
    print("Saved to 'downloaded_players.csv'")

except Exception as e:
    print("Bulk download failed:", e)