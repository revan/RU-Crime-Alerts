from secrets import ALCHEMY_KEY
import requests
import json
import re
from bs4 import BeautifulSoup


regexes = ['The Rutgers University Police Department asks .+?\.',
 'The Rutgers University Police Department is actively .+?\.',
 'The New Brunswick Police Department is actively .+?\.',
 'Anyone with information or who may have been .+?\.',
 'For more crime prevention information .+?html(/)?(\.)?',
 'For more crime prevention information .+?edu(/)?(\.)?',
 'The Rutgers University Police Department reminds .+?\.',
 'Follow the Rutgers Police Department .+?department/?\.?'
 ]

def getNextStory():

	soup = BeautifulSoup(requests.get('http://rupd.rutgers.edu/crime.php').text)

	clean = soup.get_text()
	splits = clean.split('Attention Rutgers Community:')

	itersplits = iter(splits)
	next(itersplits) #skip first
	for split in itersplits:
		target = split.replace('\r', '').replace('\n', '').replace('\t', '')

		for reg in regexes:
			target = re.sub(reg, '', target)

		target = target.split('Authority:')[0]

		yield target


def runEntityExtraction(story):
	response = requests.post('http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities',
		headers={'Content-Type': 'application/x-www-form-urlencoded'},
		params={'text': story, 'apikey': ALCHEMY_KEY, 'outputMode': 'json'})
	print(json.dumps(response.json(), indent=2))
	return response.json()