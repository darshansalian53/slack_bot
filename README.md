Bots are a useful way to interact with chat services such as Slack. If you have never built a bot before, 
this post provides an easy starter tutorial for combining the Slack API with Python to create your first bot.

We will walk through setting up your development environment, obtaining a Slack API bot token and coding our simple bot in Python.

Tools We Need
Our bot, which we will name "StarterBot", requires Python and the Slack API. To run our Python code we need:

Either Python 2 or 3
pip and virtualenv to handle Python application dependencies
Free Slack account - you need to be signed into at least one workspace where you have access to building apps.
It is also useful to have the Slack API docs handy while you're building this tutorial.


Establishing Our Environment
We now know what tools we need for our project so let's get our development environment set up. 
Go to the terminal (or Command Prompt on Windows) and change into the directory where you want to store this project.
Within that directory, create a new virtualenv to isolate our application dependencies from other Python projects.

virtualenv starterbot
source starterbot/bin/activate


The official slackclient API helper library built by Slack can send and receive messages from a Slack channel.
Install the slackclient library with the pip command:
pip install slackclient==1.3.2



Slack APIs and App Configuration
We want our Starter Bot to appear like any other user in your team - it will participate in conversations inside channels, groups, and DMs.
In a Slack App, this is called a bot user, which we set up by choosing "Bot Users" under the "Features" section. After clicking "Add a Bot User",
you should choose a display name, choose a default username, and save your choices by clicking "Add Bot User". You'll end up with a page that looks like the following:

Added a bot user to the Slack App

The slackclient library makes it simple to use Slack's RTM API and Web API. 
We'll use both to implement Starter Bot, and they each require authentication. Conveniently, 
the bot user we created earlier can be used to authenticate for both APIs.

Click on the "Install App" under the "Settings" section. 
The button on this page will install the App into our Development Workspace. Once the App is installed, 
it displays a bot user oauth access token for authentication as the bot user.


A common practice for Python developers is to export secret tokens as environment variables.
Back in your terminal, export the Slack token with the name SLACK_BOT_TOKEN:
export SLACK_BOT_TOKEN='your bot user access token here'

