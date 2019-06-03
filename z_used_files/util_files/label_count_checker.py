f = open("labels.txt", 'r')
for l1 in f:
    for l2 in f:
        if(l1 == l2):
            print(l1+":"+l2)