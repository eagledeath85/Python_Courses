for i in range(0, 100, 7):
    if i == 0:
        print(i)
        continue
    if i % 11 == 0:
        print(i)
        break
    print(i)

print("-" * 30)

for i in range(21):
    if i == 0:
        continue
    elif i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)
