import requests
import json
import re

piha = json.loads(requests.get("https://www.ravintolapiha.fi/page-data/lounas/page-data.json").text)
pihaWeek = piha["result"]["data"]["contentfulPage"]["contentBlocks"].copy()

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

for lunchOfTheDay in pihaWeek:
  print(lunchOfTheDay["title"])
  print(cleanhtml(lunchOfTheDay["body"]["childMarkdownRemark"]["html"]))
  print("--------------------------------------------------")

