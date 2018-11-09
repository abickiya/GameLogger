
from igdb_api_python.igdb import igdb

igdb = igdb("99b931869c35e813e368d974594713f5")

result = igdb.games({
    'search': "persona 5",
    'fields': 'name'})

for game in result.body:
    print("Retrieved: " + game["name"])