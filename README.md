# covid19Api
Get Covid-19 summary for each country using Postman COVID19 Api.

## Usage

### 1. Get corona summary
```
python coronaSummary.py COUNTRYCODE
```

Example:
```
python coronaSummary.py kr

KR: Korea (South) 06/21
Cases: 12,421 New Cases: 48
Deaths: 280 New Deaths: 0
Death Rate: 2.25%
```

To see more than one country of Corona summary, put more country code followed by whitespace:
```
python coronaSummary.py COUNTRYCODE#1 COUNTRYCODE#2 ...
```

Example:
```
python coronaSummary.py kr jp hr

KR: Korea (South) 06/21
Cases: 12,421 New Cases: 48
Deaths: 280 New Deaths: 0
Death Rate: 2.25%

JP: Japan 06/21
Cases: 17,725 New Cases: 67
Deaths: 955 New Deaths: 4
Death Rate: 5.39%

HR: Croatia 06/21
Cases: 2,299 New Cases: 19
Deaths: 107 New Deaths: 0
Death Rate: 4.65%
```

Country code to put is case-insensitive.

### 2. Get country code
Not sure about country code? No problem. Simply run ```python spitCountryCode.py COUNTRY NAME```. Country name doesn't have to be exactly the same. One keyword should do the work. For example, run ```python spitCountryCode.py united```, and you will see something like this:
```
python spitCountryCode.py united

Did you mean...
{'tanzania, united republic of': 'tz',
 'united arab emirates': 'ae',
 'united kingdom': 'gb',
 'united states of america': 'us'}
```
Now you know the country code you were looking for.

#### Not Found
This program provides 186 countries' Covid-19 data, however, there might be some countries whose data are not available. If you put a country name whose data are not available(North Korea) or simply wrong name(Alibaba), ```Not Found``` message will be printed.
```
python spitCountryCode.py Alibaba

Not Found
```

To see all available countries, run ```python spitCountryCode.py all```:
```
python spitCountryCode.py all

{'afghanistan': 'af',
 'albania': 'al',
 'algeria': 'dz',
 'andorra': 'ad',
 'angola': 'ao',
 'antigua and barbuda': 'ag',
...
```

Country name or keyword to put is case-insensitive.

To find out more about Postman Covid19 Api, [visit COVID19 API Pages](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest).

## Requirements
This python script uses [requests module](https://requests.readthedocs.io/en/master/). Use ```pip install requests``` in your local or virtual environment, or simply run ```pip install -r requirements.txt``` to install all the dependencies written in ```requirement.txt```.
