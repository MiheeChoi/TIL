from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-deb-shm-usage")
  browser = webdriver.Chrome(options=options)
  browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", attrs={"aria-label": "pagination"})
  if pagination == None:
    return 1
  pages = pagination.select("div a")
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count


def extrac_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  print("Found", pages, "pages")
  results = []
  for page in range(pages):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-deb-shm-usage")
    browser = webdriver.Chrome(options=options)
    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    print("requesting", final_url)

    browser.get(final_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)

    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link': f"https://kr.indeed.com/{link}",
          'company': company.string,
          'locaton': location.string,
          'position': title
        }
        results.append(job_data)

    for result in results:
      print(result, "\n////////")
  return results