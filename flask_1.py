from extractors.berlin import BerlinStartupJobs
from extractors.wwr import Weworkremotely

keyword = input("What do you want to search for? ")

berlin = BerlinStartupJobs(keyword)
berlin_jobs = berlin.get_all()

wwr = Weworkremotely(keyword)
wwr_jobs = wwr.get_all()

jobs = berlin_jobs + wwr_jobs
print(jobs)

file = open(f"./save/{keyword}.csv", mode="w", encoding="utf-8")
file.write("Title,Company,URL\n")

for job in jobs:
  file.write(f"{job['title']},{job['company']},{job['url']}\n")
  
file.close()  