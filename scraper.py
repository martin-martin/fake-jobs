import requests
from bs4 import BeautifulSoup

URL = 'https://martin-martin.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# print(results.prettify())

# job_elems = results.find_all('div', class_='card-content')
# python_jobs = results.find_all('p', string='Python Developer')
python_job_title_elems = results.find_all('h2', string=lambda text: 'python' in text.lower())

python_jobs = [je.parent.parent.parent for je in python_job_title_elems]

for job_elem in python_jobs:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('h3', class_='company')
    location_elem = job_elem.find('p', class_='location')
    apply_link = job_elem.find_all('a')[1]['href']
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(apply_link)
    print()