# Import libraries
from gazpacho import Soup

import undetected_chromedriver as UC

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


url_1 = "https://www.udemy.com/course/nextjs-web-dev-master-this-powerful-react-framework/?couponCode=FROLICINFIELDS"
url_2 = "https://www.udemy.com/course/git-github-for-beginners-from-start-to-star/?couponCode=SPRINGFLING"
url_3 = "https://www.udemy.com/course/mastering-bard-ai-googles-versatile-language-model/?couponCode=EASTERJOY"
# paid
url_4 = "https://www.udemy.com/course/javascript-practicals-crash-course/?couponCode=LETSLEARNNOW"

coupons_url = "https://www.udemyfreebies.com/course-category/development/1"

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36\
(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

soup = Soup.get(coupons_url)

cards = soup.find("div", {"class": "col-md-4 col-sm-6"}, partial=False, mode="all")

for card in cards:
    link = card.find("a", {"class": "button-icon "}, partial=False).attrs["href"].replace("free-udemy-course", "out")
      
    options = Options()
    options.add_argument("--lang=GB")

    driver = UC.Chrome(options=options)
    driver.get(link)

    schema = driver.find_element(By.ID, "schema_markup")

    script = schema.find_element(By.TAG_NAME, "script")

    print(script)

    


# TODO
# - Learn how to create xpaths
# - Create an xpath that works on the majority of courses

# possible way to find it:
# <div data-purpose="schema_markup" id="schema_markup">
# <script data-purpose="safely-set-inner-html:course-landing-page/seo-info" type="application/ld+json">
# </div>
# has a list of dictionaries and in one of them there is a key pair that contains the price value
# If the course is currently free, the key has a value of 0.00.
# it is the same in atleast 4 different courses, two courses that worked with the most commont xpath and two that don't
