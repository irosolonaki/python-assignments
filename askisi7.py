import urllib.request
import json
import datetime
from datetime import date, timedelta

#βρίσκουμε την τωρινή ημερομηνία
d = date.today()
year = d.year
month = d.month
f = datetime.date(year,month,1)
current = d - f
curr = current.days

#αρχικοποιούμε τον πίνακα με το κενό για να εισάγουμε τις κληρώσεις
pin = []
for i in range(0,82):
    pin.append(0) 

kl=0
for k in range(0, curr+1):
    for j in range(0,82):
        pin[j]=0
    before = (d-timedelta(days=k)).isoformat()
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id".format(before,before) #βρίσκουμε τις κληρώσεις τις προηγούμενης μέρας
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)
    f = data[0] #πρώτη κλήρωση της μέρας
    l = data[-1] #τελευταία κλήρωση της μέρας
    print(f)
    print(l) #τις εμφανίζουμε
    url2 = "https://api.opap.gr/draws/v3.0/1100/draw-id/{}/{}".format(f,l) 
    r2 = urllib.request.urlopen(url2)
    html2=r2.read()
    html2=html2.decode()
    data2=json.loads(html2, strict=False)
    for i in data2["content"]:
        w = i["winningNumbers"]["list"] #βρίσκουμε όλους τους ενδιάμεσους συνδυασμούς
        w.sort()
        pin.extend(w) #τους προσθέτουμε στον πίνακα pin 
        print(pin)
        set(pin)
        res = max(set(pin), key = pin.count) #βρίσκουμε τον αριθμό με την μεγαλυτερη συχνότητα 
        print("Element with highest frequency:\n",res)




