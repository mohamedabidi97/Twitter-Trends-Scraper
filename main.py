###### Import Packages ######

from selenium import webdriver
import pandas as pd
import csv


###### Open the link ######

driver = webdriver.Firefox()
driver.get('https://getdaytrends.com/united-states/')

###### Find Element By class and tag names ######

name = driver.find_element_by_class_name('inset').find_elements_by_tag_name('a')
num = driver.find_element_by_class_name('inset').find_elements_by_tag_name('span')

###### Trend Name######

names =[]
for x in name:
	names.append(x.text)
names = names[:15]

###### Number of Twitts ######

nums=[]
nums_final=[]
bad_words =['View details']
for x in num:
	nums.append(x.text)
for line in nums:
    if not any(bad_word in line for bad_word in bad_words):
        nums_final.append(line)
num_final = nums_final[:15]

###### Classification ######

Classification = list(range(1,16))

###### Export to csv file ######


with open('results.csv', 'w') as csvfile: # You can change the name of result file 'result.csv' 
		header = ['Classification', 'Trend Name', 'Number of tweets'] 
		writer1 = csv.writer(csvfile, delimiter=',')
		writer1.writerow(header)
		writer2 = csv.writer(csvfile, delimiter=':')
		for i in range(15):
		    	writer2.writerow([Classification[i],names[i],nums_final[i]])