# ieee_scraper
IEEE Xplore Digital Library Conference abstract scraping python script

# Dependencies
- Selenium
- lxml
- xlsxwriter

Please make sure to have the appropriate webdriver for Selenium.

# Install & Usage
```
pip install selenium
pip install lxml
pip install xlsxwriter
... (install webdriver) ...
scraper.py
```

Change line 7 to match the URL you are trying to scrape. You may need to add more rows with the tag &rowsPerPage=(NumElements).

After termination the xlsx writer will produce an Excel workbook with all of the abstracts.
