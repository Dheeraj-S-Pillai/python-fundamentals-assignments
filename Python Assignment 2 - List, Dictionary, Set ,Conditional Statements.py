#Python Assignment 2: Lists, Dictionaries, Sets & Conditional Statements

#  LISTS 

age_list = [24, 25, 26, 27, 28]
name_list = ["Arjun", "Meera", "Karthik", "Divya", "Rohan"]
print("1a.", age_list)
print("1b.", name_list)

name_list.append("Yazhini")
print("2a.", name_list)

age_list.insert(2, 30)
print("2b.", age_list)

name_list.remove("Yazhini")
print("2c.", name_list)

print("2d. popped:", age_list.pop(), "|", age_list)

age_list.extend([29, 30, 26])
print("2e.", age_list)

age_list.sort()
age_list.reverse()
print("2f.", age_list)

print("2g. max:", max(age_list), "min:", min(age_list), "sum:", sum(age_list))

print("3a.", name_list[0])
print("3b.", name_list[-1])
print("3c.", name_list[2:5])
print("3d.", name_list[::-1])

# DICTIONARY

student_marks = {"Arjun": 75, "Meera": 88, "Karthik": 65, "Divya": 92, "Rohan": 58}
print("4a.", student_marks)
print("4b. Meera:", student_marks["Meera"])

student_marks["Janani"] = 80
print("4c.", student_marks)

student_marks["Karthik"] = 82
print("4d.", student_marks)

print("4e. keys:", list(student_marks.keys()))
print("   values:", list(student_marks.values()))
print("   items:", list(student_marks.items()))

#  SETS 

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("5a.", my_set)
print("   Duplicates dropped — sets hold only unique, unordered elements.")


# Attempting my_set[4] = 's' would raise:
# TypeError: 'set' object does not support item assignment
# Sets are unordered and unindexed, so they don't support indexing like lists do.
# my_set[4] = 's'   

# Remedy: by using add() or remove()/discard() to modify a set instead of indexing
my_set.add('s')
print("5b. After add('s'):", my_set)
my_set.discard('s')
print("   After discard('s'):", my_set)



set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print("5c.", set1, set2)
print("5d. union:", set1 | set2)
print("   intersection:", set1 & set2)

# CONDITIONAL STATEMENTS 

score = float(input("\nEnter your score (0 to 10): "))
if score < 0 or score > 10:
    print("Invalid input. Score must be between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! You're performing really well, keep it up.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
