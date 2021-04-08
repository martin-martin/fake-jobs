import requests
from bs4 import BeautifulSoup

URL = "https://www.pythonjobshq.com/jobs/search?q=python&l=usa"
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
results = soup.find('ul', class_='jobList')
# print(results.prettify())

job_elems = results.find_all('li', class_='job-listing')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('a', class_='jobList-title').find('strong')
    company_elem = job_elem.find('ul', class_='jobList-introMeta').find('li')
    # location_elem = job_elem.find('div', class_='location')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    # print(location_elem.text.strip())
    print()

print("--------------- PARTNER RESULTS ---------------")
partner_results = soup.find('div', id="load-backfill-ajax")
partner_job_elems = partner_results.find_all('li', class_='job-listing')

for job_elem in partner_job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('a', class_='jobList-title').find('strong')
    company_elem = job_elem.find('ul', class_='jobList-introMeta').find('li')
    # location_elem = job_elem.find('div', class_='location')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    # print(location_elem.text.strip())
    print()