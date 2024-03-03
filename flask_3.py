from flask import Flask, render_template, request, redirect, send_file
from extractors.berlin import BerlinStartupJobs
from extractors.wwr import Weworkremotely
from extractors.web3 import Web3

from file import save_to_file

app = Flask("JobScrapper")

db = {}

# decorator는 함수에 같이 사용해야 한다. 공백이나 다른게 있으면 해당 함수가 작동하지 않게 된다.
@app.route("/") # decorator
def home():
  return render_template("home.html", name="Kan")
# 템플릿 사용시 꼭 디렉토리명은 templates로 해야 한다. 아니면 flask에서 인식을 못한다.
# 변수로 지정하면 name이 home.html로 전달된다. html에서 받을때는 {{name}}으로 받는다.

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None: # keyword값이 없을때 None을 반환한다
    return redirect("/")
  
  if keyword in db:
    jobs = db[keyword]
  else:
    berlin = BerlinStartupJobs(keyword)
    berlin_jobs = berlin.get_all()

    wwr = Weworkremotely(keyword)
    wwr_jobs = wwr.get_all()
    
    web3 = Web3(keyword)
    web3_jobs = web3.get_all()

    jobs = berlin_jobs + wwr_jobs + web3_jobs
    db[keyword] = jobs
  
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  try:
    keyword = request.args.get("keyword")
    if keyword == None:
      return redirect("/")
    if keyword not in db:
      return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, db[keyword])
    return send_file(f"./save/{keyword}.csv", as_attachment=True)
  except:
    return redirect("/")

app.run("0.0.0.0")