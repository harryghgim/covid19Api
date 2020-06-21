# get covid-19 data from postman api
# https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest

import requests, sys
from datetime import datetime

url = 'https://api.covid19api.com/summary'
r = requests.get(url)
rdata = r.json()
cdata = r.json()['Countries']
inputCodes = [x.lower() for x in sys.argv[1:]]

if len(sys.argv) < 2:
    print('Usage: \npython coronaSummary.py COUNTRYCODE#1 COUNTRYCODE#2 ...')
    print('For world data, put \'world\' as a COUNTRYCODE')
    print('To find out country code, run python spitCountryCode.py COUNTRY NAME')
    sys.exit()

gdata = r.json()['Global']
gdata.setdefault('Country', 'World')
gdata.setdefault('CountryCode', 'World')
cdata.insert(0, gdata)
spitData = []
for country in cdata:
    code    = country['CountryCode'].lower()

    # iterate each code
    for eachCode in inputCodes:
        if eachCode == code: spitData.append(country)

# set return order as same as inputCodes order
order = {key: i for i, key in enumerate(inputCodes)}
orderedspitData = sorted(spitData, key=lambda d: order[d['CountryCode'].lower()])

for e in orderedspitData:
    cases   = e['TotalConfirmed']
    name    = e['Country']
    code    = e['CountryCode']
    deaths  = e['TotalDeaths']
    nDeaths = e['NewDeaths']
    nCases  = e['NewConfirmed']
    date    = rdata['Date']
    d       = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    newDate = d.strftime('%m/%d')

    print(f'\n{code.upper()}: {name} {newDate}\nCases: {cases:,} New Cases: {nCases:,}\nDeaths: {deaths:,} New Deaths: {nDeaths:,}\nDeath Rate: {round(deaths/cases*100, 2)}%')

#TODO: no code found -> certain code not found print

