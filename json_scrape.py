import requests, os

os.system('cls')

url = 'http://buckets.peterbeshai.com/api/players.php?player=201939&season=2015'

username = 'efung'

response = requests.get(url,headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

jump_shots = int(response.json()['TOTAL_FGA'])
made_shots = int(response.json()['TOTAL_FGM'])
percentage = float(made_shots) / float(jump_shots)

print "Username: %s" % username
print "Total FGA: %i" % jump_shots
print "Total FGM: %i" % made_shots
print "Percentage made: %.2f%%" % (percentage * 100)
