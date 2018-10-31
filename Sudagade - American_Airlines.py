from bs4 import BeautifulSoup # A Library that makes it easy to scrape information from web pages
import requests # Library that lets you makes HTTP requests
import sys #
import pandas as pd 

# In this program, we give the company's CIK, Filing Type, and Submission Date to get the SEC Filing from EDGAR.
# Once we get the XBRL link, Python will read it and save all Tags that start with us-gaap
# I am save the result as an array and saving it to a CSV File as well

# Access page
cik = '0000006201'
type = '10-K'
dateb = '20171231'
 
# Obtain HTML for search page
base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}&dateb={}"
edgar_resp = requests.get(base_url.format(cik,type,dateb))
edgar_str = edgar_resp.text

# Find the document link
doc_link = ''
soup = BeautifulSoup(edgar_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile2')
rows = table_tag.find_all('tr')
for row in rows:
  cells = row.find_all('td')
  if len(cells) > 3:
    if '2016' in cells[3].text:
      doc_link = 'https://www.sec.gov' + cells[1].a['href']

# Exit if document link couldn't be found
if doc_link == '':
  print("Couldn't find the document link")
  sys.exit()

# Obtain HTML for document page
doc_resp = requests.get(doc_link)
doc_str = doc_resp.text

# Find the XBRL link
xbrl_link = ''
soup = BeautifulSoup(doc_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile', summary='Data Files')
rows = table_tag.find_all('tr')
for row in rows:
  cells = row.find_all('td')
  if len(cells) > 3:
    if 'INS' in cells[3].text:
      xbrl_link = 'https://www.sec.gov' + cells[2].a['href']

# Obtain XBRL text from document
xbrl_resp = requests.get(xbrl_link)
xbrl_str = xbrl_resp.text

# Find and print stockholder's equity
soup = BeautifulSoup(xbrl_str, 'lxml')
tag_list = soup.find_all()
tagname = list()
tagtext = list()
for tag in tag_list:
  if (tag.name[0:7] == "us-gaap"):
    tagname.append(tag.name)
    tagtext.append(tag.text)
d = {"Tag Name": pd.Series(tagname),
     "Data": pd.Series(tagtext)}
df = pd.DataFrame(d)
array = df.values
print(array)
df.to_csv('American_Airlines.csv')
