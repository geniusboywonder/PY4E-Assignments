fname = input("Enter a file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be found: ", fname)
    quit()
lst = list()
for line in fh:
    words = line.rstrip().split()
    for w in range(len(words)) :
        word = words[w]
        if word in lst : continue
        lst.append(word)
slst = sorted(lst)
print(slst)
