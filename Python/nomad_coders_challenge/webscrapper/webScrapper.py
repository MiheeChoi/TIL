from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "java"
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("can't request website")
else:
  results = []
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = (soup.find_all('section', class_='jobs'))
  for job_section in jobs:
    post_list = job_section.find_all('li')
    post_list.pop(-1)
    for job_post in post_list:
      anchors = job_post.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_='company')
      title = anchor.find('span', class_='title')
      job_data = {
        'link': f"https://weworkremotely.com/{link}",
        'company': company.string,
        'kind': kind.string,
        'region': region.string,
        'position': title.string
      }
      results.append(job_data)
for result in results:
  print(result)
  print('/////')