import requests

base = "https://jsonmock.hackerrank.com/api/football_matches"
def getNumDraws(year):
    # Write your code here
    goal = 0
    draw = 0
    while goal < 10:
        response = requests.get(f"{base}?year={year}&team1goals={goal}&team2goals={goal}").json()
        draw += response['total']
        goal += 1
        
    return draw

print(getNumDraws(2011))