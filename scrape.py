#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from rich.progress import track
import yaml
import re

def dms2dd(dms):
  """
  Convert DMS style GPS Coordinates to DD style coordinates
  """
  dmsreg = re.split('[°\'"]', dms)
  deg = dmsreg[0]

  minutes_p = dmsreg[1][-2:]
  if minutes_p == "′S":
    minutes = dmsreg[1][0:2]
  else:
    minutes = dmsreg[1]

  try:
    seconds = dmsreg[2]
  except:
    seconds = 00

  dd = int(deg) + float(minutes)/60 + float(seconds)/3600
  return dd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
results = []
target_url_file = open("urls.txt")
output_file = open("output.yml", "w+")
targets = target_url_file.readlines()

for t in targets:
  # Open target URL
  driver.get(t)

  # Find the Infobox table on the right of the page
  infobox = driver.find_element(By.CLASS_NAME, 'infobox')
  rows = infobox.find_elements(By.TAG_NAME, 'tr')

  # Extract Name
  t_name = rows[0].text

  for r in track(rows, description=t_name):
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

  datarec = {
    "name": t_name,
    "category": 5, # Category 5 = Lake
    "designation": "PLACEHOLDER",
    "salt_water": None,
    "size": None,
    "capacity": None,
    "gps_lat": dms2dd(t_gps_lat),
    "gps_lon": dms2dd(t_gps_lon)
  }
  results.append(datarec)

# Write formatted YAML data to output_file
yaml.dump(results, output_file, allow_unicode=True)

# cleanup
driver.quit()
target_url_file.close()
output_file.close()
quit()
