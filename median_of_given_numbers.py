l = []
x = int(input("Give me a number: "))
l =[x]
while x != 0:
    x = int(input("Give me a number: "))
    l.append(x)
else:
    sum = sum(l[:])
size = len(l)

for i in range(size):
    for j in range(0, size-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

if size % 2 == 0:
    M = (l[int((len(l)/2)-1)]+l[(int(len(l)/2))])/2
if size % 2 != 0:
    M = l[(int((len(l)+1)/2)-1)]

print(f"Before sorting: {l}")
print(f"After sorting:: {l}")
print(f"Median: {M}")