from faker import Faker
from snippets import job_html, base_html

fake = Faker()
Faker.seed(0)

jobs_list = ""

for _ in range(1000):
    job = fake.job()
    if "engineer" in job.lower():
        # job_html.format(job_title, company_name, location, time)
        jobs_list += job_html.format(job, fake.company(), f"{fake.city()}, {fake.military_state()}", fake.date())

with open("index.html", "w") as fout:
    fout.write(base_html.format(jobs_list))