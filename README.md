# Rutgers Crime Alert API

A *very* rough API that scrapes the gross [RUPD Crime Alert page](http://rupd.rutgers.edu/crime.php),
strips it of HTML and bureaucratic boilerplate with regex, saving a json array to file.

Extracts time and location with regex.

[Map demo here!](http://vps.rsopher.com/crime.html)

## TODO
Since the structure of these alerts is so repetitive, it should be easy to extract structured data from them.
Might require some level of NLP and isn't strictly necessary, I suppose.

Notably: crime, perpetrator description.

Location extraction doesn't currently catch cases like `Mason and Pine Streets` or `on Robinson Street between Hamilton Street and Central Avenue`, reporting just `Pine Street` or `Robinson Street, Hamilton Street` respectively.

Also needs to load the local database and merge with new requests instead of clobbering in case RUPD takes down old alerts.

### Python Requirements:

```
requests
BeautifulSoup
dateutils
```