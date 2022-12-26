#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## List of Wikipedia Articles
targets = [
  "https://en.wikipedia.org/wiki/Gippsland_Lakes",
  "https://en.wikipedia.org/wiki/Lake_Hindmarsh",
  "https://en.wikipedia.org/wiki/Lake_Tyrrell",
  "https://en.wikipedia.org/wiki/Lake_Colac"
]
## Create driver instance
driver = webdriver.Chrome('./chromedriver')

for t in targets:
  driver.get(t)
  infobox = driver.find_element_by_class_name("infobox")
  print(infobox)