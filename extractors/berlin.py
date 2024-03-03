import requests
from bs4 import BeautifulSoup



# https://berlinstartupjobs.com/?s=python&page=1
class BerlinStartupJobs:
  def __init__(self, keyword):
    self.keyword = keyword
    self.url = f"https://berlinstartupjobs.com/skill-areas/{self.keyword}/"
    self.header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    #self.total_pages = self.get_pages()
    #self.page = 1
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
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
    #print(jobs)

    
    for job in jobs:
      title = job.find("h4", class_="bjs-jlid__h").get_text()
      company = job.find("a", class_="bjs-jlid__b").text # get_text()대신에 text를 사용해도 된다. 함수 아님 주의

      url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
      description = job.find("div", class_="bjs-jlid__description").text.strip() # /t,/n을 제거하기 위해 strip()을 사용한다.

      #print(title, " - ", company, "-", url)
      job_data = {
        "title": title,
        "company": company,
        "description": description,
        "url": url
      }
      
      self.all_jobs.append(job_data)


  def get_pages(self):
    response = requests.get(self.url, headers=self.header)
    soup = BeautifulSoup(response.content, "html.parser")
    
    return len(soup.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers"))
    # len은 배열의 길이를 반환하고, find_all은 배열을 반환한다. 그래서 len(find_all())을 사용한다.


#berlin = BerlinStartupJobs("javascript")
#berlin2 = BerlinStartupJobs("java")
