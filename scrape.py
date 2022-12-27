#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

## List of Wikipedia Articles
targets = [
  "https://en.wikipedia.org/wiki/Gippsland_Lakes",
  "https://en.wikipedia.org/wiki/Lake_Hindmarsh",
  "https://en.wikipedia.org/wiki/Lake_Tyrrell",
  "https://en.wikipedia.org/wiki/Lake_Colac"
]

## Create driver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for t in targets:
  # Open target URL
  driver.get(t)

  # Find the Infobox table on the right of the page
  infobox = driver.find_element(By.CLASS_NAME, 'infobox')
  rows = infobox.find_elements(By.TAG_NAME, 'tr')

  for r in rows:
   print(r.text)

  # TODO: Find size, capacity, & gps data in the infobox
  # t_size = None
  # t_capacity = None
  # t_gps_lat = None
  # t_gps_lon = None
  
  # TODO: Package data and save in format to mimic rails fixture data
  # TODO: Write packaged data to YAML file in ./<NAME FROM URL>.yml (From here we append to our rails fixtures/seeds file)

## Cleanup

# Kill driver
driver.quit()

## Print done
print('done')
