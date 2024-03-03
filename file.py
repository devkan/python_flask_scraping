def save_to_file(file_name, jobs):
  file = open(f"./save/{file_name}.csv", mode="w", encoding="utf-8")
  file.write("Title,Company,URL\n")

  for job in jobs:
    file.write(f"{job['title']},{job['company']},{job['url']}\n")
    
  file.close()    