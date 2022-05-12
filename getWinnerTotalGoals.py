import requests

base = "https://jsonmock.hackerrank.com/api/football_competitions"
base1 = "https://jsonmock.hackerrank.com/api/football_matches"
def getWinnerTotalGoals(competition, year):
    # Write your code here
    data = requests.get(f"{base}?name={competition}&year={year}").json()
    winner = data.get('data')[0].get('winner')
    
    data1 = requests.get(f"{base1}?competition={competition}&year={year}&team1={winner}").json()
    totalPage1 = data1.get('total_pages')
    page1 = 1
    total = 0
    while page1 <= totalPage1:
        response = requests.get(f"{base1}?competition={competition}&year={year}&team1={winner}&page={page1}").json()
        mydata = response.get('data')      
        for i in range(len(mydata)):
            total += int(mydata[i].get('team1goals'))
        page1 += 1
    
        
    data2 = requests.get(f"{base1}?competition={competition}&year={year}&team2={winner}").json()
    totalPage2 = data2.get('total_pages')
    page2 = 1
    while page2 <= totalPage2:
        response = requests.get(f"{base1}?competition={competition}&year={year}&team2={winner}&page={page2}").json()
        mydata = response.get('data')      
        for i in range(len(mydata)):
            total += int(mydata[i].get('team2goals'))
        
        page2 += 1
            
    return total

print(getWinnerTotalGoals('English Premier League', 2014))