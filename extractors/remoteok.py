import requests
from bs4 import BeautifulSoup

def extract_remoteok_jobs(keyword):
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(url, headers={"User-Agent":"Unknown"})
  if request.status_code != 200:
    print("Can't request page")
  else:
    results = []
    soup = BeautifulSoup(request.text, "html.parser")
    jobsboard = soup.find('table', id='jobsboard')
    jobs = jobsboard.find_all('tr', class_='job')
    for job in jobs:
      info = job.find('td', class_='company position company_and_position')
      anchor = info.find('a', class_='preventLink')
      link = anchor['href']
      position = info.find('h2').string.strip('\n')
      company = info.find('h3').string.strip('\n')
      location = info.find('div').string.strip('\n')
      job_data = {
        'link' : f"https://remoteok.com{link}",
        'company' : company,
        'location' : location,
        'position' : position,
      }
      results.append(job_data)
  print("remoteok.com 스크랩 완료.")
  return results