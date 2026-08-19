#Basic structure of a dictionary
#dictionary_name {
 #   "key1": "value1",
 #   "key2": "value2",
 #   "key3": "value3"
#}



my_profile = {
    "name" : "Sunisha Raina",
    "age" : 25,
    "current_role" : "Software Engineer",
    "target_role" : "AI Engineer",
    "experience": 3}

print(my_profile)

print(my_profile["target_role"])
print(my_profile["name"])
print(my_profile["current_role"])

my_profile["target_role"] = "Senior AI Engineer"
print(my_profile)

my_profile["location"] = "Pune"
print(my_profile)

print(my_profile.keys())

print(my_profile.values())

print(my_profile.items()) #keys and value both will be printed in the form of tuples

#if my_profile.keys() != None:
 #   print(list(my_profile.keys()) + list(my_profile.values())) #this will give an error as keys and values are of different data types

for key, value in my_profile.items():
    print(key, ":",value)

my_profile.pop("location")
print(my_profile)   

payment = {
    "uetr" : "eefa0428-cff3-4844-8a08-fbb81c96571f",
    "amount" : 1000,
    "currency" : "AED",
    "status" : "COMPLETE",
    "sender" : "CITIAEADXXX"
}

print(payment)
print(payment["amount"])
payment["status"] = "REPAIR"
payment["receiver"] = "SCBLAEADXXX"
print(payment.keys())
print(payment.values())
payment.pop("sender")
print(payment)