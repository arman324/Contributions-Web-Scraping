#
#  webScraping.py
#  Created by Arman Riasi on 6/10/20.
#  Copyright © 2020 Arman Riasi. All rights reserved.
#
import requests
from bs4 import BeautifulSoup
import re
import calendar
import matplotlib.pyplot as plt
import numpy as np


date_ = []
date_HTML = []
contribution_HTML = []
contribution_ = []

s = " "
s2 = " "

Monday = 0
Tuesday = 0
Wednesday = 0
Thursday = 0
Friday = 0
Saturday = 0
Sunday = 0

Username = " "

URL = "https://github.com/"
Username = input("please enter your github username: ")

result = requests.get(URL+Username)

soup = BeautifulSoup(result.text,'html.parser')

date = soup.find_all('rect',attrs={'class':'day'})
contribution = soup.find_all('rect',attrs={'class':'day'})

for i in date:
    date_HTML.append(str(i))

for j in contribution:
    contribution_HTML.append(str(j))


for i in date_HTML:
    date_.append(s.join(re.findall(r"data-date=\"(.*?)\"",i)))

for j in contribution_HTML:
    contribution_.append(s2.join(re.findall(r"data-count=\"(.*?)\"",j)))


for j in range(0,len(contribution_)):
    if contribution_[j] == "0":
        continue
    year = int(date_[j][0:4])
    month = int(date_[j][5:7])
    day = int(date_[j][8:10])
    DayOfTheWeek = calendar.weekday(year, month, day)
    if DayOfTheWeek == 0:
        Monday += int(contribution_[j])

    if DayOfTheWeek == 1:
        Tuesday += int(contribution_[j])

    if DayOfTheWeek == 2:
        Wednesday += int(contribution_[j])

    if DayOfTheWeek == 3:
        Thursday += int(contribution_[j])

    if DayOfTheWeek == 4:
        Friday += int(contribution_[j])

    if DayOfTheWeek == 5:
        Saturday += int(contribution_[j])

    if DayOfTheWeek == 6:
        Sunday += int(contribution_[j])


print("\nIt's your result (%s):" %Username)
print("\n")

print("Monday = %s" %Monday)
print("Tuesday = %s" %Tuesday)
print("Wednesday = %s" %Wednesday)
print("Thursday = %s" %Thursday)
print("Friday = %s" %Friday)
print("Saturday = %s" %Saturday)
print("Sunday = %s" %Sunday)

print("\n\n")

y_ = []
y_.append(Monday)
y_.append(Tuesday)
y_.append(Wednesday)
y_.append(Thursday)
y_.append(Friday)
y_.append(Saturday)
y_.append(Sunday)

myX = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


x = np.array([0,1,2,3,4,5,6])
y = np.array(y_)

# plotting the points
plt.plot(x, y, color='green', linestyle='-', linewidth = 5,
         marker='o', markerfacecolor='blue', markersize=12)


plt.title('Your commits in last year!')

my_xticks = myX

plt.xticks(x, my_xticks)
plt.yticks(y_)
plt.plot(x, y)
plt.show()
