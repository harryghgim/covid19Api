import requests, sys, pprint

url = 'https://api.covid19api.com/summary'
r = requests.get(url)
countryData = r.json()['Countries']
countryDict = {}

for countryEntry in countryData:
    key = countryEntry['Country'].lower()
    value = countryEntry['CountryCode'].lower()
    countryDict.setdefault(key, value)

lowList = [x.lower() for x in sys.argv[1:]]
userInput = ' '.join(lowList)

if len(sys.argv) < 2:
    print('Usage:')
    print('run python spitCountryCode.py COUNTRY NAME')
    print('To see all codes, run python spitCountryCode.py all')
    sys.exit()

if sys.argv[1] == 'all':
    pprint.pprint(countryDict)
    sys.exit()

try:
    print(userInput + ' : '+ countryDict[userInput])
except KeyError:
    results = {}
    for name in countryDict.keys():
        if userInput in name:
            results.setdefault(name, countryDict[name])

    if results != {}:
        print('Did you mean...')
        pprint.pprint(results)
    else:
        print('Not Found')

