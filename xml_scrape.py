import requests
from lxml import objectify
import os

os.system("cls")

param = "tavg"
period = 6
state = 44
div = 0
year = 2016
month = 7

url = requests.get("https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?" \
                        "param=" + str(param) \
                        + "&state=" + str(state) \
                        + "&div=" + str(div) \
                        + "&month=" + str(month) \
                        + "&periods[]=" + str(period) \
                        + "&year=" + str(year))

#objectify method
response = objectify.fromstring(url.content)

print "Username: efung"
print "value: %s" % response.data['value']
print "twentiethCenturyMean: %s" % response.data['twentiethCenturyMean']
print "lowRank: %s" % response.data['lowRank']
print "highRank: %s" % response.data['highRank']

"""
#etree method

tree = etree.fromstring(url.content)

element_dict = {}

data = tree.find("data")
for i in tree.find("data"):
    element_dict[i.tag] = i.text

print "Username: efung"
print "value: %s" % element_dict['value']
print "twentiethCenturyMean: %s" % element_dict['twentiethCenturyMean']
print "lowRank: %s" % element_dict['lowRank']
print "highRank: %s" % element_dict['highRank']
"""
