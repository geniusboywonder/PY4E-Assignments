name = input("Enter a file name: ")
if len(name) < 1 : name = "mbox-short.txt"

try:
    fh = open(name)
except:
    print("File cannot be found: ", name)
    quit()

counts = dict()
lst = list()

for line in fh:
    if len(line) < 3 or not line.startswith("From ") : continue
    words = line.rstrip().split()
    time = words[6]
    hour = time[:2]
    print(words)
    counts[words[6].]

#
#     for word in words:
#         if "@" not in word : continue
#         counts[word] = counts.get(word,0) + 1
#
# sendercount = None
# sender = None
#
# for k,v in counts.items() :
#     if sendercount is None or v > sendercount :
#         sender = k
#         sendercount = v
#
# print(sender, sendercount)