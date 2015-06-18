import json
import hashlib
from ugly_parser import getNextStory, extractDate, extractLocation

data = []

for story in getNextStory():
	date = extractDate(story)
	locations = extractLocation(story)

	# location1 = locations[0] if len(locations) >= 1 

	data.append({
		'text': story,
		'hash': hashlib.md5(story.encode()).hexdigest(),
		'date': date[0],
		'date_human': date[1],
		'location1': locations[0] if len(locations) >= 1 else None,
		'location2': locations[1] if len(locations) >= 2 else None
	})

with open('crimes.json', 'w') as out:
	json.dump(data, out, indent=2, sort_keys=True)
