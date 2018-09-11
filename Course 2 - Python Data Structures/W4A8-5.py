fname = input("Enter a file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print("File cannot be found: ", fname)
    quit()

icount = 0
lst = list()

for line in fh:
    if len(line) < 3 or not line.startswith("From ") : continue
    words = line.rstrip().split()
    print(words[1])
    icount = icount + 1
print("There were", icount, "lines in the file with From as the first word")
