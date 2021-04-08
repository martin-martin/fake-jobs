from pathlib import Path
from random import randint
from faker import Faker
from slugify import slugify
from snippets import job_html, base_html, bulma_html, bulma_job, job_detail_html

fake = Faker()
Faker.seed(0)

BASE_URL = "https://martin-martin.github.io/fake-jobs"
jobs_list = ""

job_loc = Path().cwd().joinpath("jobs")
job_loc.mkdir(exist_ok=True)

# customize the lorem generator to get some job talk going
word_list = ['job','professional','Python',
        'role','developer','Java',
        'agile','SCRUM','oversee',
        'Flask','Django','web application','dashboard' ]

for i in range(1000):
    job = fake.job()
    if "engineer" in job.lower():
        # job_html.format(job_title, company_name, location, time)
        description = fake.paragraph(nb_sentences=randint(5, 10), ext_word_list=word_list)
        slug_url = f"{slugify(job)}-{i}.html"
        company = fake.company()
        location = f"{fake.city()}, {fake.military_state()}"
        date = fake.date()
        jobs_list += bulma_job.format(job, company, location, date,
                                      f"{BASE_URL}/jobs/{slug_url}")
        with open(job_loc.joinpath(slug_url), "w") as detailpage:
            details = job_detail_html.format(job, company, location, date, description)
            detailpage.write(bulma_html.format(details))

with open("index.html", "w") as fout:
    fout.write(bulma_html.format(jobs_list))