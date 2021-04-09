import requests
from bs4 import BeautifulSoup

URL = 'https://martin-martin.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elems = results.find_all('div', class_='card-content')
# python_jobs = results.find_all('p', string='Python Developer')
python_jobs = job_elems.find_all('p', class_="title",
                               string=lambda text: 'python' in text.lower())

for job_elem in python_jobs:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('p', class_='title')
    company_elem = job_elem.find('p', class_='company')
    location_elem = job_elem.find('p', class_='location')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()