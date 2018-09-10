fname = input("Enter a file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be found: ", fname)
    quit()

sword = input("Enter a search word: ")

for line in fh:
  line = line.rstrip()
  if not line.startswith(sword) :  continue
  words = line.split()
  print(words[1])
