from faker import Faker
from slugify import slugify
from snippets import job_html, base_html, bulma_html, bulma_job

fake = Faker()
Faker.seed(0)

BASE_URL = "https://martin-martin.github.io/fake-jobs"
jobs_list = ""

for i in range(1000):
    job = fake.job()
    if "engineer" in job.lower():
        # job_html.format(job_title, company_name, location, time)
        jobs_list += bulma_job.format(job,
                                      fake.company(), 
                                      f"{fake.city()}, {fake.military_state()}",
                                      fake.date(),
                                      f"{BASE_URL}/jobs/{slugify(job)}-{i}")

with open("index.html", "w") as fout:
    fout.write(bulma_html.format(jobs_list))