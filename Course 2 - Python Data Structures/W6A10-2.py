name = input("Enter a file name: ")
if len(name) < 1 : name = "mbox-short.txt"

try:
    fh = open(name)
except:
    print("File cannot be found: ", name)
    quit()

counts = dict()
countsort = list()
lst = list()

# read each line of the file
for line in fh:
    if len(line) < 3 or not line.startswith("From ") : continue
    # split each line into words
    words = line.rstrip().split()
    # find the "time" word
    time = words[5]
    # strip out the hour
    hour = time[:2]
    # count the number of occurances of each hour
    counts[hour] = counts.get(hour,0) + 1

# put the dictionary into a list so it can be sorted
for v,k in counts.items() :
    lst = (str(v), k)
    countsort.append(lst)

#sort the list
countsort = sorted(countsort)

# print each tuple on a new line
for v,k in countsort :
    print(v,k)
