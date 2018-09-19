fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #print(pieces)
    if "@" not in pieces[1]: continue
    email = pieces.split("@")[-1]
    print(email)
