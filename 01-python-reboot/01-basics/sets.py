skills = {"Python", "SQL", "Python", "AI", "Python"}
print(skills)

#A set is a collection of values, but its biggest feature is:
#Sets automatically remove duplicate values.

skills.add("Machine Learning")
print(skills)

skills.remove("SQL")
print(skills)

#union of two sets
skills1 = {"Python" , "JavaScript", "SQL", "HTML", "CSS", "Payments"}
skills2 = {"JIRA", "Testing", "Python", "AI", "Python"}
all_skills = skills1.union(skills2)
print(all_skills)

#intersection of two sets
backend = {"Python", "SQL", "Java", "C++"}
frontend = {"HTML", "CSS", "JavaScript", "Python"}
common_skills = backend.intersection(frontend)
print(common_skills)