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
        try:
            rating_tag = card.find("i", class_="fa-star").parent.text
            rating = float(rating_tag.split(":")[-1].split("/")[0])


        except Exception as f:
            print("\n Something went wrong with this course. Pass")
            pass

       
        else:
            if rating > minimum_rating:
                course_url = card.find("a", class_="button-icon")["href"]

                course = requests.get(course_url)

                course_soup = BeautifulSoup(course.content, "lxml")

                udemy_url = course_soup.find("a", class_="button-icon")["href"]

                options = Options()
                options.add_argument("--lang=GB")

                driver = UC.Chrome(options=options)
                driver.get(udemy_url)

                # Most typical path (8/12)
                udemy_price_xpath = "//*[@id='main-content-anchor']/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/span[2]"
                # Example: https://www.udemy.com/course/capture-edit-render-create-uhd-screen-videos-with-nvidia/?couponCode=MAR-2024-A

                # Own path
                try:
                    udemy_price = driver.find_element(By.XPATH, udemy_price_xpath)
                

                    if udemy_price.text == "Free":
                        print("\n", udemy_price.text)
                        print("The course is Free!")
                        print(udemy_url)
                        driver.close()
                    else:
                        print("\n", udemy_price.text)
                        print("it is not free")

                        driver.close()

                except Exception:
                    print("Element not found")
                    pass
                    

                # ! GET SELENIUM TO CLICK ON THE LINK TO ENROLL, INPUT THE EMAIL AND PASSWORD DATA, AND CLICK ENROLL AGAIN



except Exception as e:
    print("Global exception")
    pass
