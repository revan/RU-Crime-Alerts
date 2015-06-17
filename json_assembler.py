import json
import hashlib
from ugly_parser import getNextStory

data = []

for story in getNextStory():
	data.append({
		'text': story,
		'hash': hashlib.md5(story.encode()).hexdigest()
	})

with open('crimes.json', 'w') as out:
	json.dump(data, out, indent=2, sort_keys=True)
