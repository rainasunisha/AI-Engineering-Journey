#Tuple: It is a collection of ordered elemennts which is immutable. It is defined by using parentheses ().
#Once created a tuple cannot be modified. It can contain duplicate elements and can hold different data types.

technologies = ("Python", "JavaScript", "SQL","SQL", "HTML", "CSS", "Payments", 0 , 4.5, True)
print(technologies)
print(technologies[0])
print(technologies[-1])

print(len(technologies))

#technologies[0] = "Java" - didn't work as tuple is immutable.

ai_learning = (
    "Python",
    "Machine Learning",
    "Deep Learning",
    "LLMs",
    "RAG"
)

print(ai_learning)
print(len(ai_learning))
print(ai_learning[1])
print(ai_learning[-1])