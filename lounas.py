import requests
import json
import re
import datetime
import sys

piha = json.loads(requests.get(
    "https://www.ravintolapiha.fi/page-data/lounas/page-data.json").text)
pihaWeek = piha["result"]["data"]["contentfulPage"]["contentBlocks"].copy()

todayDate = datetime.datetime.now().strftime("%d.%m").lstrip("0")


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = re.sub("&#x26;", "\x26", cleantext)
    return cleantext


print("--------------------------------------------------")

for lunchOfTheDay in pihaWeek:

    startOfDateInfo = re.search(r"\d", str(lunchOfTheDay["title"])).start()
    endOfDateInfo = len(lunchOfTheDay["title"])
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-d" and str(lunchOfTheDay["title"])[startOfDateInfo: endOfDateInfo] == todayDate:
            print(lunchOfTheDay["title"])
            print(cleanhtml(lunchOfTheDay["body"]
                            ["childMarkdownRemark"]["html"]))
            print("--------------------------------------------------")
    else:
        print(lunchOfTheDay["title"])
        print(cleanhtml(lunchOfTheDay["body"]["childMarkdownRemark"]["html"]))
        print("--------------------------------------------------")
        print()
