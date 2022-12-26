#!/usr/bin/env python3

from selenium import webdriver

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
  # Open target URL
  driver.get(t)

  # Find the Infobox table on the right of the page
  infobox = driver.find_element_by_class_name("infobox")
  infobox_txt = infobox[0].text

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