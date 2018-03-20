
with open('data.txt','r') as myfile:
	data = myfile.read()
lim=80
for sentence in data.split("\n"): 
    if sentence == "": print 
    w=0 
    l = []
    for word in sentence.split():		
        if w + len(word) + 1 <= lim:
            l.append(word)
            w += len(word) + 1 
        else:
            print " ".join(l).center(lim," ")
            l = [word] 
            w = len(word)
    if (len(l)): print " ".join(l).center(lim," ")
