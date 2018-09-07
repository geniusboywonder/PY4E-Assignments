fname = input("Enter a filename: ")
try:
    fhand = open(fname)
    # finp = fhand.read()
except:
    print("File cannot be found: ", fname)
    quit() #or break or continue

count = 0
for line in fhand:
    if not line.startswith("Subject:") :
        continue
    count = count + 1
print("There were", count, " subjects lines in ", fname)
