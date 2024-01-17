name = "Sean Park"
language = "Python"
message = f"Hello, {name}! Would you like to learn some {language} today?"

print(name.lower())
print(name.upper())
print(name.title())

# f-string

name = "Steve Jobs"
quote = "Stay hungry, stay foolish."
print(f"{name} once said, \"{quote}\"")

famous_person = "Steve Jobs"
message = f"{famous_person} once said, \"{quote}\""
print(message)

name = " Sean Park "
print(f"\t{name}")
name.lstrip()
print(name)

file_name = "python_work/Chapter2/learning_python.txt"
file_name = file_name.removesuffix(".txt")
print(file_name)