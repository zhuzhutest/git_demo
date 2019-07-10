

##################################################
# words = ["w","wo", "worldas","worlds","wor"]
# words=["a", "ad", "adu", "adul", "adult", "adulb"]
words=["f", "fa", "fab", "fabr", "fabri", "fabrica", "fabrication"]
# words=["b", "be", "bea", "beas", "beast", "beasty"]
# words=["cable","ork","camel","cabin", "cabiny"]

def test():
	dict1={}
	for i in range(len(words)):
		dict1[i]=len(words[i])
	maxindex = list(dict1.keys())[list(dict1.values()).index(max(dict1.values()))]
	return max(dict1.values()),maxindex,words[maxindex]

def test2():
	maxlength,maxindex,word=test()
	minlist = []
	maxword=""
	for i in range(len(words)):
		if i<maxlength and words[i] in word:
			minlist.append(words[i])

		elif i>=maxlength:
			print i
			print maxlength
			if i>maxindex:
				maxindex=i
				word=words[i]
			print "Output1: "+word
			print "minlist:"
			print minlist
			break
		else:
			print "Output3: "+word
			print "minlist:"
			print minlist
			break
	print "Output3: "+word
	print "minlist:"
	print minlist	

#######################################################
# test2()
a=3913
for i in range(240):
	a = a-9
	print a





# print "true"
# print "false"