fname = input("Enter a file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be found: ", fname)
    quit()
for line in fh:
    print(strip(line.upper())
