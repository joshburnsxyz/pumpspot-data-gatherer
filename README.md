# pumpspot-data-gatherer
This script was written to specifically scrape the Wikipedia articles of Lakes, and other bodies of water
to extract information like GPS coordinates, capacity, salt or fresh water, and other data. This data was
used to build a project called "Pumpspot". It was an interactive map of water sources that could be used
by Emergency Services, Survivalists and anyone else who needed access to water.

The Project never reached a public deployment and this script remains. There may be no immediate use for
anyone to use it as-is. But it may hold value for someone one day.


## Usage:

### Requirements

- Google Chrome (to run Selenium webdriver)

First off run the following command to install python dependencies from PyPi.

```shell
$ pip install -r ./requirements.txt
```

Then create a `urls.txt` (or modify the existing one) file with a
new URL on each line. Each URL should point to a Wikipedia article
about a particular Lake,River,Body of Water - As long as the
article follows the same general template that script has been
designed for the data will be extracted from the page correctly.

Run the script with the following command

```shell
$ python3 ./scrape.py
```

An `output.yml` file will be created containing the data from the article
formatted for use in the main pumpspot app.
