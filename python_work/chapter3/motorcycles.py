motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # This line replaces the first item in the list with 'ducati'
print(motorcycles)

motorcycles.append('ducati') # This line adds 'ducati' to the end of the list
print(motorcycles)

motorcycles = [] # This line creates an empty list
motorcycles.append('honda') # This line adds 'honda' to the list
motorcycles.append('yamaha') # This line adds 'yamaha' to the list
motorcycles.append('suzuki') # This line adds 'suzuki' to the list
print(motorcycles)

motorcycles.insert(0, 'ducati') # This line adds 'ducati' to the beginning of the list
print(motorcycles)

del motorcycles[0] # This line deletes the first item in the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # This line removes the last item in the list and stores it in the variable 'popped_motorcycle'
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() # This line removes the last item in the list and stores it in the variable 'last_owned'
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
first_owned = motorcycles.pop(0) # This line removes the first item in the list and stores it in the variable 'first_owned'
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') # This line removes 'ducati' from the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati' # This line stores 'ducati' in the variable 'too_expensive'
motorcycles.remove(too_expensive)   # This line removes the value stored in the variable 'too_expensive' from the list

print(f"\nA {too_expensive.title()} is too expensive for me.") # This line prints the value stored in the variable 'too_expensive'
