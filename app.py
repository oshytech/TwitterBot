from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='D:\\Oshytech\\Codigo\\Python\\TwitterBotSelenium\\chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(2)

        email = bot.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        password = bot.find_element_by_xpath('//input[@name="session[password]"]')
        # limpiamos por si las moscas
        password.clear()
        email.clear()
        # cargamos los datos
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):

        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

        tweets = bot.find_elements_by_xpath('//a[@dir="auto" and not(@rel)]')
        tweets_url = [tweet.get_attribute('href') for tweet in tweets]

        for url in tweets_url:
            bot.get(url)
            try:
                time.sleep(3)
                likeButton = bot.find_element_by_xpath('//div[@data-testid="like"]')
                likeButton.click()
                time.sleep(15)
            except Exception as ex:
                print(url + " ya te gusta")
                time.sleep(20)

            time.sleep(2)



tb = TwitterBot('oshytest', 'RskTkkHq')
tb.login()
tb.like_tweet('webscraping')
