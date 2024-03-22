# Doesn't work
url_1 = "https://www.udemy.com/course/data-analytics-visualization-acquire-demanded-tech-skills/?couponCode=FB573A1A219A48EA7ADE"
url_2 = "https://www.udemy.com/course/coding-basics-gentle-intro-to-coding-for-beginners/?couponCode=ST14MT3"
# Works
url_3 = "https://www.udemyfreebies.com/out/the-complete-wordpress-developer-course-w"

# Import libraries 
from bs4 import BeautifulSoup 
import requests 
  
# set the url to perform the get request 
page = requests.get(url_3) 
  
# load the page content 
text = page.content 
  
# make a soup object by using 
# beautiful soup and set the markup as html parser 
soup = BeautifulSoup(text, "html.parser") 
  
# open the file in w mode 
# set encoding to UTF-8 
with open("url_3.html", "w", encoding = 'utf-8') as file: 
    
    # prettify the soup object and convert it into a string 
    file.write(str(soup.prettify())) 

# TODO
# - Learn how to create xpaths
# - Create an xpath that works on the majority of courses