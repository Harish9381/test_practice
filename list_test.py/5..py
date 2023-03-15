l = int(input())
even = 0
for i in range(len(l)):
    if i % 2 == 0:
        even += l[i]
print(f"sum of even_indexed elements{even}")