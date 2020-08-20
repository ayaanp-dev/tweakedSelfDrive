import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy', allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

w = []
a = []
s = []
d = []
wa = []
wd = []
sa = []
sd = []
nk = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0,0,0,0,0,0]:
        w.append([img,choice])
        
    elif choice == [0,1,0,0,0,0,0,0,0]:
        a.append([img,choice])
        
    elif choice == [0,0,1,0,0,0,0,0,0]:
        s.append([img,choice])
        
    elif choice == [0,0,0,1,0,0,0,0,0]:
        d.append([img,choice])
        
    elif choice == [0,0,0,0,1,0,0,0,0]:
        wa.append([img,choice])
        
    elif choice == [0,0,0,0,0,1,0,0,0]:
        wd.append([img,choice])
        
    elif choice == [0,0,0,0,0,0,1,0,0]:
        sa.append([img,choice])
        
    elif choice == [0,0,0,0,0,0,0,1,0]:
        sd.append([img,choice])
        
    elif choice == [0,0,0,0,0,0,0,0,1]:
        nk.append([img,choice])

    else:
        print("no matches")


##w = w[:len(s)][:len(a)][:len(d)][:len(wa)][:len(wd)][:len(sa)][:len(sd)]
##s = s[:len(w)]
##a = a[:len(w)]
##d = d[:len(w)]
##wa = wa[:len(w)]
##wd = wd[:len(w)]
##sa = sa[:len(w)]
##sd = sd[:len(w)]
##nk = nk[:len(w)]

final_data = w + a + s + d + wa + wd + sa + sd + nk
shuffle(final_data)

np.save('balanced_data.npy', final_data)
