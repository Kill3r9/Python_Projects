
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
            str = " ".join(l)
	    length = len(str)
	    b = lim-length
	    print " "*int(b/2) + str + " "*int(b/2)
            l = [word] 
            w = len(word)
    if (len(l)): 
		str1 = " ".join(l)
	    	lengt = len(str1)
	    	bl = lim-lengt
	    	print " "*int(bl/2) + str1 + " "*int(bl/2)
	
