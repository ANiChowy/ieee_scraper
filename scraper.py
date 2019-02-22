from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import xlsxwriter

browser = webdriver.Firefox()
url = "https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?filter=issueId%20EQ%20%228460178%22&rowsPerPage=1000&pageNumber=1&resultAction=REFINE&resultAction=ROWS_PER_PAGE"
browser.get(url)
innerHTML = browser.execute_script("return document.body.innerHTML")

htmlElem = html.document_fromstring(innerHTML)

base_href = "https://ieeexplore.ieee.org"

#print(htmlElem)
list_of_links = []
row = 1
col = 0
workbook = xlsxwriter.Workbook('Abstracts.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Title', bold)
worksheet.write('B1', 'Abstract', bold)
for elem in htmlElem.iterlinks():
    link = elem[2]
    if link.startswith("/document/") and link.endswith("/") and link not in list_of_links:
        list_of_links.append(link)
        nurl = base_href + link
        print('Travelling to ... ' + nurl)
        #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        browser.get(nurl)

        ninnerHTML = browser.execute_script("return document.body.innerHTML")
        nhtmlElem = html.document_fromstring(ninnerHTML)

        title = nhtmlElem.cssselect(".document-title > span:nth-child(1)")

        for elem in title:
            tText = elem.text_content()
            print(tText)
            worksheet.write(row, col, tText)

        abstract = nhtmlElem.cssselect(".abstract-text > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")

        for elem in abstract:
            aText = elem.text_content()
            print(aText)
            worksheet.write(row, col+1, aText)
        row += 1
        #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

workbook.close()