#TASK 1: Titanic Survival Prediction

#Author: Mohana Shree

#Domain: Data Science

#Aim: To build a titanic survival prediction model using python

import csv
import numpy as np
import matplotlib.pyplot as plt


with open("./Titanic-Dataset.csv","r") as f:
    rr = csv.reader(f)
    l=[]
    s = "PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked".split()
    d = {}
    for i in range(len(s)):
        d[s[i]]=i
    print(d)
    for i in rr:
        l.append(i[d["Sex"]])



# creating the dataset
data = {'Male':l.count("male"), 'Female':l.count("female")}
status = list(data.keys())
passengers = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(status, passengers, color ='blue', 
		width = 0.2)

plt.xlabel("Status")
plt.ylabel("No. of passengers")
plt.title("Titanic Survival graph")
plt.show()
