import random
import math

x = int(input("Δώσε x: "))
y = int(input("Δώσε y: "))
if y==x:
    print("Λάθος διαστάσεις!") #θέλουμε ορθογώνιο
    x = int(input("Δώσε x: "))
    y = int(input("Δώσε y: ")) 
syn_pl=0
for k in range(0,101): #έχουμε 100 επαναλήψεις - συνδυασμούς
    array = [] #ο μεγάλος πίνακας που θα περιέχει όλα τα sos
    pinsos = [] #ο εμφωλευμένος πίνακας που δημιουργούμε με τυχαίους συνδυασμούς sos
    m = math.ceil(x*y/2) #στρογγυλοποίηση προς τα πάνω για να μπει στην επανάληψη

    #γεμίζει μισά με s και μισά με o
    for i in range(m):
        pinsos.append("s")
        pinsos.append("o")
    s=0
    o=0
    while s==o: #αν κάποιο πλήθος s/o διαφέρει σταματάει η επανάληψη
        for i in range(y):
            gr = [] #δημιουργούμε τον εμφωλευμένο πίνακα sos γραμμή γραμμή
            for j in range(x):
                synd = random.choice(pinsos) #δημιουργούμε τυχαίους συνδυασμού με τα s και o
                gr.append(synd) #προσθέτουμε τους συνδυασμούς σε κάθε γραμμή

                #ο έλεγχος γίνονται για να βεβαιωθούμε ότι θα είναι μισά μισά
                if synd == "s":
                    s+=1 
                elif synd == "o":
                    o+=1
            array.append(gr) #οι γραμμές προσθέτονται στον μεγάλο τελικό πίνακα
    
    orizontia = 0
    katheta = 0
    diagwnia = 0
    for i in range(y):
        for j in range(x):
            if j < x-2: #χρησιμοποιούμε αυτόν τον έλεγχο για να μην βγούμε απο τα όρια του πίνακα ανά γραμμή
                if (array[i][j]=="s") and (array[i][j+1]=="o") and (array[i][j+2]=="s"):
                    orizontia+=1 #υπολογισμός οριζόντιων sos
                            

            if i < y-2: #χρησιμοποιούμε αυτόν τον έλεγχο για να μην βγούμε απο τα όρια του πίνακα ανά στήλη
                if array[i][j]=="s" and (array[i+1][j]=="o") and (array[i+2][j]=="s"):
                    katheta+=1 #υπολογισμός κάθετων sos
                            
            if y>=2 and x>=2: #χρησιμοποιούμε αυτόν τον έλεγχο για να μην βγούμε απο τα όρια του πίνακα ανά στήλη και γραμμή
                if(i<y-2) and (j>1):
                    if array[i][j]=="s" and (array[i+1][j-1]=="o") and (array[i+2][j-2]=="s"):
                        diagwnia+=1 #υπολογισμός διαγώνιων sos
                                
    pl = orizontia + katheta + diagwnia #πλήθος sos κάθε επανάληψης
    syn_pl = syn_pl + pl #συνολικό πλήθος όλων των επαναλήψεων
    

mo_sos = syn_pl/100 #μέσος όρος τριάδων sos μετά απο 100 επαναλήψεις
print("Ο μέσος όρος των τριάδων sos είναι: ", mo_sos)