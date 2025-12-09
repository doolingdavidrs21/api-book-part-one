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