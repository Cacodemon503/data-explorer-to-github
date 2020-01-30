import csv
import requests
from tqdm import tqdm
from collections import defaultdict

#--------------------------CSV READER----------------------------#
columns = defaultdict(list) 

with open("{}.csv".format(str(input("File name: ")))) as f:
    reader = csv.DictReader(f)
    for row in reader: 
        for (k,v) in row.items(): 
            columns[k].append(v) 

#------------------VARS NAMES & LIST TO APPEND-------------------#
names = columns[str(input("Column name: "))]
git_names = []

#-----------------GITHUB CHECKER & LIST APPENDER-----------------#
for i in tqdm(names):
    print("Checking if user exists on GitHub ...")
    token = open("token.txt" , "r").read() 
    headers = {"Authorization": "token " + token}
    URL = "https://api.github.com/users/" + i
    r = requests.get(url = URL, headers = headers)
    data = r.json()
    keys = list(data.keys())
    
    if keys[0] != "message":
        git_names.append(i)

#--------------------------NEW CSV WRITER-------------------------#        
with open("{}.txt".format(str(input("Enter file name: "))), "w", encoding = "utf-8") as filename:
    writer = None
    for i in tqdm(git_names):
        URL = "https://api.github.com/users/" + i
        r = requests.get(url = URL, headers = headers)
        data = r.json()
            
        URL = "https://api.github.com/users/" + i + "/repos"
        r = requests.get(url = URL, headers = headers)
        user_repos = r.json()
        languages = [i["language"] for i in user_repos if i["language"] != None if i["language"] != "Makefile"] # add more langs != if needed
        languages_counted = {i: f"{round(languages.count(i)/len(languages)*100, 2)}%" for i in set(languages)}
        readout = {'Username': data['login'], 'Full Name': data['name'], 'Email': data['email'],
                    'Location': data['location'], 'Company': data['company'], 'Hireable Status': data['hireable'],
                    'Languages': languages_counted, 'Profile Summary': 'https://profile-summary-for-github.com/user/' + data['login']}
        if not writer:
            writer = csv.DictWriter(filename, delimiter=';', fieldnames=readout.keys())
        writer.writerow(readout)
    
    print ("Writing completed")