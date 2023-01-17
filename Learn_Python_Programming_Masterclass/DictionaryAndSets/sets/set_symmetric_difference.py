# Symmetric difference is the opposite of intersection
# It produces the set of items that are in one set or the other, but not in both

morning_courses = {"python", "java", "C#", "C", "ruby"}
afternoon_courses = {"lisp", "java", "C#", "C", "ruby"}

# Using the symmetric_difference() method
excluded_courses = morning_courses.symmetric_difference(afternoon_courses)
print(excluded_courses)

# Using the operator
possible_courses = morning_courses ^ afternoon_courses
print(possible_courses)