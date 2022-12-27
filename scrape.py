#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import yaml

## List of Wikipedia Articles
targets = [
  "https://en.wikipedia.org/wiki/Gippsland_Lakes",
  "https://en.wikipedia.org/wiki/Lake_Wendouree",
  "https://en.wikipedia.org/wiki/Lake_Tyrrell",
  "https://en.wikipedia.org/wiki/Lake_Hindmarsh",
  "https://en.wikipedia.org/wiki/Lake_Colac",
  "https://en.wikipedia.org/wiki/Lake_Corangamite",
  "https://en.wikipedia.org/wiki/Lake_Coorong",
  "https://en.wikipedia.org/wiki/Tarago_Reservoir"
]

## Create driver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Create results list
results = []

for t in targets:
  # Initialize empty variables
  t_name = None
  t_size = None
  t_capacity = None
  t_gps_lat = None
  t_gps_lon = None
 
  # Open target URL
  driver.get(t)

  # Find the Infobox table on the right of the page
  infobox = driver.find_element(By.CLASS_NAME, 'infobox')
  rows = infobox.find_elements(By.TAG_NAME, 'tr')

  # Extract Name
  t_name = rows[0].text

  print(f"Processing {t_name}")

  for r in rows:
    # Split label from actual data
    p = r.text.split(" ", 1)

    # Extract coordiants
    if r.text.startswith("Coordinates: "):
      parsed_coords = p[1].split(" ")
      t_gps_lat = parsed_coords[0]
      t_gps_lon = parsed_coords[1]

    # Extract coordiants (fallback)
    if r.text.startswith("Coordinates"):
      parsed_coords = p[1].split("\n", 1)[0].split(" ")
      t_gps_lat = parsed_coords[0]
      t_gps_lon = parsed_coords[1]

    # Extract size (surface area)
    if r.text.startswith("Surface area"):
      t_size = p[1].split(" ")[1]

  datarec = {
    "name": t_name,
    "size": t_size,
    "capacity": t_capacity,
    "gps_lat": t_gps_lat,
    "gps_lon": t_gps_lon
  }
  results.append(datarec)

yamldump = yaml.dump(results, allow_unicode=True)
print(yamldump)

# Kill driver
driver.quit()

## Print done
print('done')
quit()
