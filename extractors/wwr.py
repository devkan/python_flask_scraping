import requests
from bs4 import BeautifulSoup


class Weworkremotely:
  def __init__(self, keyword):
    self.keyword = keyword
    self.url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={self.keyword}"
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
    jobs = soup.find_all("li", class_="feature")
    #print(jobs)

    for job in jobs:
      title = job.find("span", class_="title").get_text()
      company, position, _ = job.find_all("span", class_="company")
      url = job.find("div", class_="tooltip").next_sibling["href"]
      #print(title, " - ", company.text, "-", url)

      job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "url": f"https://weworkremotely.com/{url}"
      }
      self.all_jobs.append(job_data)


#berlin = Weworkremotely("javascript")
#berlin2 = Weworkremotely("java")
