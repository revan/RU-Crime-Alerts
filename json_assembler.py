import json
import hashlib
from ugly_parser import getNextStory, extractDate

data = []

for story in getNextStory():
	date = extractDate(story)
	data.append({
		'text': story,
		'hash': hashlib.md5(story.encode()).hexdigest(),
		'date': date[0],
		'date_human': date[1]
	})

with open('crimes.json', 'w') as out:
	json.dump(data, out, indent=2, sort_keys=True)
