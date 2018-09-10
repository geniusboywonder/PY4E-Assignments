fname = input("Enter a file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print("File cannot be found: ", fname)
    quit()
fptotal = 0.00
icount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    iStart = line.find(":")
    iEnd = len(line)
    fpSpam = float(line[iStart+1:iEnd])
    fptotal = fptotal + fpSpam
    icount = icount + 1
    #print(line, iStart, iEnd, icount, fpSpam, fptotal, fptotal/icount)
print("Average spam confidence:", (fptotal/icount))
