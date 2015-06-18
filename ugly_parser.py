import requests
import json
import re
import dateutil.parser as dateparser
from bs4 import BeautifulSoup


regexes = ['The Rutgers University Police Department asks .+?\.',
 'The Rutgers University Police Department is actively .+?\.',
 'The New Brunswick Police Department is actively .+?\.',
 'The New Brunswick Police Department asks that anyone .+?\.',
 'The investigation is ongoing and the New Brunswick Police Department asks .+?\.',
 'Anyone with information or who may have been .+?\.',
 'For more crime prevention information .+?html(/)?(\.)?',
 'For more crime prevention information .+?edu(/)?(\.)?',
 'The Rutgers University Police Department reminds .+?\.',
 'Follow the Rutgers Police Department .+?department/?\.?'
]


date_regex = '(?:January|February|March|April|May|June|July|August|September|October|November|December)\s[1-3]?\d,\s\d{4}'
location_regex = '\w+\s(?:Street|Avenue|Place|Drive|St\.)'

def getNextStory():
	soup = BeautifulSoup(requests.get('http://rupd.rutgers.edu/crime.php').text)

	clean = soup.get_text()
	splits = clean.split('Attention Rutgers Community:')

	itersplits = iter(splits)
	next(itersplits) #skip first
	for split in itersplits:
		target = split.replace('\r', '').replace('\n', '').replace('\t', '').replace('\u00a0', ' ')

		for reg in regexes:
			target = re.sub(reg, '', target)

		target = target.split('Authority:')[0]

		yield target.strip()

def extractDate(text):
	matches = re.findall(date_regex, text)
	if len(matches) > 0:
		return (int(dateparser.parse(matches[0]).timestamp()), matches[0])

def extractLocation(text):
	return re.findall(location_regex, text)
