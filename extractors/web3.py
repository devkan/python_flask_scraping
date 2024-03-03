import requests
from bs4 import BeautifulSoup


class Web3:
  def __init__(self, keyword):
    self.keyword = keyword
    self.url = f"https://web3.career/{self.keyword}-jobs"
    self.header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    self.all_jobs = []
    
    self.scrapping()


  def get_all(self):
    return self.all_jobs

  def scrapping(self):
    self.scrape_page()
    #for page in range(self.total_pages):
      #self.page += 1
      

  def scrape_page(self):
    #scrape_url = f"{self.url}&page={self.page + 1}"
    scrape_url = f"{self.url}"

    response = requests.get(self.url, headers=self.header)
    #print(response.content)

    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("table", class_="table-borderless").find("tbody").find_all("tr")
    #print(jobs)

    for job in jobs:
      title = job.find("div", class_="job-title-mobile").text
      company = job.find("td", class_="job-location-mobile").text
      url = job.find("div", class_="job-title-mobile").find("a")["href"]
      #print(title, " - ", company, "-", url)

      job_data = {
        "title": title,
        "company": company,
        "url": f"https://web3.career{url}"
      }
      self.all_jobs.append(job_data)


#web3 = Web3("javascript")
