from extractors.indeed import extrac_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("what do you want to search for?")

indeed = extrac_indeed_jobs(keyword)
wwr = extrac_wwr_jobs(keyword)

jobs = indeed + wwr
for job in jobs:
  print(job)
  print("/////\n/////")