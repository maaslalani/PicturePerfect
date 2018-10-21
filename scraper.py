import os

def scrape(username, destination='temp'):
    MAX_POSTS = str(100)
    LOGIN_USER = "jonathangin52"
    LOGIN_PASS = "mBbf^8Kq2sc8"

    COMMAND = "instagram-scraper " + username + " -u " + LOGIN_USER + " -p " + LOGIN_PASS + " --destination " + destination + " --media-type image --media-metadata --maximum " + MAX_POSTS
    os.system(COMMAND)
    destination += '' if '/' in destination else '/'
