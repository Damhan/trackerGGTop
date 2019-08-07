from selenium import webdriver
import csv

#Start up a new chrome driver
driver = webdriver.Chrome()
#Get our desired URL
driver.get('https://tracker.gg/tft/leaderboards/stats/all/default?page=1&region=EUW')
print("Opening Web Page..")

#grab the table
table = driver.find_element_by_css_selector('#app > div.trn-wrapper > div.trn-container > div > main > div.leaderboards > div.content > div > div > div.board > table')
print("Getting leaderboard table..")
#Open our CSV file.
with open('results.csv', 'w', newline='') as csvFile:
    wr = csv.writer(csvFile)
    print("Creating a CSV file..")
    #Iterate throw each row, writing to our CSV.

    for row in table.find_elements_by_css_selector('tr'):
        wr.writerow([cell.text for cell in row.find_elements_by_css_selector('td')])

    print("Finished writing to results file.")
    csvFile.close