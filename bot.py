import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "pv lfc bot test v0.1")

	return r

def run_bot(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "coutinho" in comment.body:
			comment.reply("Hello")		


r = bot_login()
run_bot(r)