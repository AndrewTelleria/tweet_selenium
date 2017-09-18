#! python3

"""
twitter.py - Takes a command line argument that has a username, password, and tweet - it will login to twitter and write the tweet for you.

e.g.

$ python3 twitter.py "username" "password" "Hello, world!"

Do not forget the quotes on the command line argument because without them sys.argv will think they are a single string with not spaces between the words.

The script will check to see if the maximum characters are breached and if they are not it will proceed to write the tweet and post the tweet for you.

"""

from selenium import webdriver
import sys, webbrowser


tweet = sys.argv[3]
username = sys.argv[1]
password = sys.argv[2]

def write_tweet(tweet, username, password):

	characters = tweet.replace(" ", "")
	list_chars = list(characters)
	if len(list_chars) > 140:
		print("Your tweet has to many characters - 140 characters is the max.")
	else:
		browser = webdriver.Chrome()
		browser.get('https://twitter.com/')
		login = browser.find_element_by_css_selector('.EdgeButton.EdgeButton--transparent.EdgeButton--medium.StreamsLogin.js-login')
		login.click()
		uname = browser.find_element_by_css_selector('div.LoginForm-input.LoginForm-username input')
		uname.send_keys(username)
		pword = browser.find_element_by_css_selector('div.LoginForm-input.LoginForm-password input')
		pword.send_keys(password)
		login_submit = browser.find_element_by_css_selector('.EdgeButton.EdgeButton--primary.EdgeButton--medium.submit.js-submit')
		login_submit.click()
		tweet_box = browser.find_element_by_id('tweet-box-home-timeline')
		tweet_box.send_keys(tweet)
		tweet_button = browser.find_element_by_css_selector('div.TweetBoxToolbar-tweetButton.tweet-button button')
		tweet_button.click()
		webbrowser.open(browser.current_url)



write_tweet(tweet, username, password)