dic={'jibi':1,'aysha':2,'marva':3}
l=list(dic.items())
l.sort()
d=dict(l)
print("Ascending is:",d)
l=list(dic.items())
l.sort(reverse=True)
d=dict(l)
print("Descending is",d)