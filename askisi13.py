#εισάγετε το αρχείο
filename = input("Εισάγετε όνομα αρχείου: ")
with open(filename, 'r',encoding='utf-8') as f:
    text = f.read().replace('\n', '') #το διαβάζουμε και το εκχωρούμε στην μεταβλητή text 

#αφαιρούμε όλα τα σημεία στίξης από το κείμενο
punct=['0','1','2','3','4','5','6','7','8','9','.',',','!','[',']','(',')','/','-',';','"', '“','”','*']
for char in punct:
    text=text.replace(char,' ')

#χωρίζουμε το κείμενο σε λέξεις
words=[]
words=text.split()

#αρχικά δημιουργούμε λίστα με εμφωλευμένες λίστες που περιέχουν τις λέξεις και το μήκος τους
w=[[wrd,len(wrd)] for wrd in words]

#και μετά την μετατρέπουμε σε λεξικό
d = dict(w)
print(d)

#έλεγχος για συνδυασμό λέξεων που το μήκος τους είναι ίσο με 20
flag=False
for i in range (1,11):
    lst=[]
    for k_1,v_1 in d.items():
        if int(v_1)==i:
            for k_2,v_2 in d.items():
                if k_1!=k_2 and int(v_1)+int(v_2)==20:
                    print(k_1.lower()+k_2.lower())
                    d[k_1]=100
                    d[k_2]=100
                    flag=True
                    break

if flag==False:
    print('Δεν βρέθηκε ζευγάρι λέξεων με μήκος 20.')

