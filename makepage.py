from pathlib import Path
from random import randint, choice
from faker import Faker
from slugify import slugify
from snippets import job_html, base_html, job_detail_html


fake = Faker()
Faker.seed(0)

BASE_URL = "https://martin-martin.github.io/fake-jobs"
jobs_list = ""

job_loc = Path().cwd().joinpath("jobs")
job_loc.mkdir(exist_ok=True)

# customize the lorem generator to get some job talk going
word_list = ['job','professional','Python', 'no experience', 'curious', 'willing to learn',
        'role','developer','Java', 'support', 'collaborate', 'include', 'communities',
        'agile','SCRUM','oversee', 'oversea', 'relocation', 'remote', 'distributed',
        'Flask','Django','web application','dashboard','software developer', 'programs',
        'build', 'coordinate', 'explore', 'growth opportunity', 'talented', 'motivated',
        'grit', 'CSS', 'HTML', 'employ', 'discussions', 'inclusive', 'open-minded',
        'detail-oriented', 'fast-growing', 'responsible tech', 'educational',
        'environmentally friendly', 'teamwork', 'asset', 'company']

python_jobs = ["Python Developer", "Senior Python Developer", "Back-End Web Developer (Python, Django)",
               "Python Internship", "Software Developer (Python)", "Python Programmer (Entry-Level)",
               "Software Engineer (Python)"]

for i in range(100):
    if i % 10 == 0:  # Create 10 jobs titled as Python jobs with software dev ipsum
        job = choice(python_jobs)
        description = fake.paragraph(nb_sentences=randint(5, 10), ext_word_list=word_list)
    else:
        job = fake.job()
        description = fake.paragraph(nb_sentences=randint(5, 10))
    slug_url = f"{slugify(job)}-{i}.html"
    company = fake.company()
    location = f"{fake.city()}, {fake.military_state()}"
    date = fake.date_between(start_date='-2m', end_date='today')
    jobs_list += job_html.format(job, company, location, date,
                                    f"{BASE_URL}/jobs/{slug_url}")
    with open(job_loc.joinpath(slug_url), "w") as detailpage:
        details = job_detail_html.format(job, company, location, date, description)
        detailpage.write(base_html.format(details))

with open("index.html", "w") as fout:
    fout.write(base_html.format(jobs_list))
