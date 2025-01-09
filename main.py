import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")
print(len(jobs))

for job in jobs:
    title = job.find("span", class_="title")
    company = job.find("span", class_="company")
    if title != None and company != None:
        print(title.text, "-------", company.text)
