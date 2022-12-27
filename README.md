# pumpspot-data-gatherer
Web scraper to automate data retrieval for pumpspot

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
