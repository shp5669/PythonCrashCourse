guests = ['Tanya', 'Alliya', 'Martina', 'Gabi', 'Ozlem', 'Sean']

for guest in guests:
    print(f"Hi {guest}, I would like to invite you to dinner.")

guests.insert(0, 'Yujin')
guests.insert(3, 'Jenny')
guests.append('Jin')


for guest in guests:
    print(f"Hi {guest}, I would like to invite you to dinner.")

guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(guests)

del guests[0]
del guests[0]

print(guests)