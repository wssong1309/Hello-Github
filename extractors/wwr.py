from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='
  response = get(f"{base_url}{keyword}")
  
  if response.status_code != 200:
    print("Can't request website.")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop()
      for job_post in job_posts:
        anchors = job_post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, employment_type, region = anchor.find_all(class_='company')
        title = anchor.find(class_='title')
        job_data = {
          'link' : f"https://weworkremotely.com{link}",
          'company' : company.string.replace(",", ""),
          'location' : region.string.replace(",", ""),
          'position' : title.string.replace(",", "")
        }
        results.append(job_data)
    print("weworkremotely.com 스크랩 완료.")
    return results