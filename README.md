# Rutgers Crime Alert API

A *very* rough API that scrapes the gross [RUPD Crime Alert page](http://rupd.rutgers.edu/crime.php),
strips it of HTML and bureaucratic boilerplate with regex, saving a json array to file.

## TODO
Since the structure of these alerts is so repetitive, it should be easy to extract structured data from them.
Notably: time, location, crime, perpetrator description.

Also needs to load the local database and merge with new requests (each alert has a hash for this purpose)
in case RUPD takes down old alerts.

### Python Requirements:

```
requests
BeautifulSoup
```