from bs4 import BeautifulSoup
import requests
import csv

URL = 'https://www.faa.gov/air_traffic/publications/atpubs/cnt_html/chap3_section_3.html'

if __name__ == '__main__':
    r = requests.get(URL)
    scraped = []
    soup = BeautifulSoup(r.content, 'html.parser')

    tables = soup.find(id='main').find_all('table')
    for t in tables:
        rows = t.find('tbody').find_all('tr')
        for r in rows:
            cells = r.find_all('td')
            scraped.append(
                {
                    '3Ltr'      : cells[0].text.strip(),
                    'Company'   : cells[1].text.strip(),
                    'Country'   : cells[2].text.strip(),
                    'Telephony' : cells[3].text.strip(),
                }
            )
    
    with open('airlines.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['3Ltr', 'Company', 'Country', 'Telephony']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for i in scraped:
            writer.writerow(i)
