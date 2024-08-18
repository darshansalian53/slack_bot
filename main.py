from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
from datetime import date
import time

# Load environment variables from a .env file
env_path = ".env"
load_dotenv(env_path)

# Initialize the Slack client
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

try:
    # Send a message to the Slack channel
    response = client.chat_postMessage(
        channel="test", 
        text="The current date is " + str(date.today()) + " " + str(current_time)
    )
except SlackApiError as e:
    print(f"Error sending message: {e.response['error']}")
