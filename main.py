import undetected_chromedriver as UC

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import requests
import time

# Sets the minimum rating to filter the courses
minimum_rating = 3.7

coupons_url = "https://www.udemyfreebies.com/course-category/development/1"

coupons = requests.get(coupons_url)

coupons_soup = BeautifulSoup(coupons.content, "lxml")


try:
    cards = coupons_soup.find_all("div", class_="col-md-4 col-sm-6")

    for card in cards:
        rating_tag = card.find("i", class_= "fa-star").parent.text
        rating = float(rating_tag.split(":")[-1].split("/")[0])
        

        if rating > minimum_rating:
            course_url = card.find("a", class_="button-icon")["href"]

            course = requests.get(course_url)

            course_soup = BeautifulSoup(course.content, "lxml")

            udemy_url = course_soup.find("a", class_="button-icon")["href"]

            udemy = requests.get(udemy_url)


            


except Exception as e:
    print("Ratings was not found")
    print(e)








    # If the rating is higher than the minimum rating:
    """ if rating > minimum_rating:
        # Get the link to the page about the course
        course_link = course.find("a", class_="button-icon")["href"]

        # Creates a soup with it
        html_two = requests.get(course_link).text
        soup_two = BeautifulSoup(html_two, "lxml")

        # Get the link to the course in udemy
        udemy_link = soup_two.find("div", class_="text-center").a["href"]
     """