import os

def scrape(username, destination='temp'):
    MAX_POSTS = str(100)
    LOGIN_USER = "ENTER_YOUR_USERNAME"
    LOGIN_PASS = "ENTER_YOUR_PASSWORD"

    COMMAND = "instagram-scraper " + username + " -u " + LOGIN_USER + " -p " + LOGIN_PASS + " --destination " + destination + " --media-type image --media-metadata --maximum " + MAX_POSTS
    os.system(COMMAND)
    destination += '' if '/' in destination else '/'
