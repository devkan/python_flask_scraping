from extractors.berlin import BerlinStartupJobs
from extractors.wwr import Weworkremotely
from file import save_to_file

keyword = input("What do you want to search for? ")

berlin = BerlinStartupJobs(keyword)
berlin_jobs = berlin.get_all()

wwr = Weworkremotely(keyword)
wwr_jobs = wwr.get_all()

jobs = berlin_jobs + wwr_jobs
print(jobs)

save_to_file(keyword, jobs)