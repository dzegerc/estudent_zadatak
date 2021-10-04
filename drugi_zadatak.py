rijeci = "alpha beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
s = rijeci.split()
l = []

for i in s:
    if (rijeci.count(i)>=1 and (i not in l)):
        l.append(i)

print(' '.join(l))