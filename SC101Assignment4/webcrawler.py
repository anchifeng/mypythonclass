"""
File: webcrawler.py
Name: Feng An Chi
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.tbody.find_all('tr')
        male_n = 0
        female_n = 0
        for tag in tags:
            td = tag.find_all('td')
            if len(td) >= 5:
                male_n += int(digit(td[2].text))
                female_n += int(digit(td[4].text))
        print("Male Number: " + str(male_n))
        print("Female Number: " + str(female_n))


def digit(s):
    """
    param s (str): str remove comma
    """
    new_s = ''
    for ch in s:
        if ch.isdigit():
            new_s += ch
    return new_s


if __name__ == '__main__':
    main()
