'''
NEWS AGGREGATOR

- Daily request is sent that scrapes BBC headlines
- Headlines are linked to their articles
- Links are injected into Obsidian daily note
- Section prepared for when the file is opened
'''

import requests
from bs4 import BeautifulSoup
import datetime


def scrape_bbc():
    url = 'https://www.bbc.co.uk/news'
    bbc = requests.get(url)
    bbc_content = bbc.text

    soup = BeautifulSoup(bbc_content, 'html.parser')
    headlines = soup.find_all('h3')

    daily = {}
    for headline in headlines[:10]:
        text = headline.text.strip()

        if text.startswith("Live"):
            continue

        link = headline.find('a')
        if link and 'href' in link.attrs:
            req = link['href']
            daily[text] = req

    return daily


def open_dailynote(daily):
    format = "%d.%m.%y"
    today = (datetime.datetime.today()).strftime(format)
    path = 'your_path_to_Obsidian_note'
    print(today)

    with open(path + f"/{today}.md", "r+") as dn:
        lines = dn.readlines()
        dn.seek(0)

        heading_index = None

        for index, line in enumerate(lines):
            if line.strip() == "## Headlines":
                heading_index = index
                break

        if heading_index is not None:
            for i in range(heading_index + 1):
                dn.write(lines[i])

            dn.write("\n")

            for text, url in daily.items():
                dn.write(f"[{text}](https://www.bbc.co.uk{url})\n")

            for i in range(heading_index + 1, len(lines)):
                dn.write(lines[i])

            for i in range(heading_index + 1, len(lines)):
                dn.write(lines[i])
        else:
            print("Heading not in file!")


def main():
    daily = scrape_bbc()
    open_dailynote(daily)
    exit()


if __name__ == "__main__":
    main()
