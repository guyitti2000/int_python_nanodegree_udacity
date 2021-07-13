
def people():
people_ = {}
prompt = input("Would you like to add a person to the list? (Y/N): ")
while prompt.lower() == "y":
    qs = dict(name='first name', surname='last name')
    print(qs)
    index = f"person_{len(people_) + 1}"
    people_[index] = {}
    for key, value in qs.items():
        name = input('Please enter your {}: '.format(value))
        people_[index][key] = name
        print(people_)
    prompt = input("Another person? (Y/N): ")
print(people_)
return people_


'''
def people():
    people = {}
    prompt = input("Would you like to add a person to the list? (Y/N): ")
    while prompt.lower() == "y":
        qs = dict(name='first name', surname='last name')
        for key, value in qs.items():
            name = input('Please enter your {}: '.format(value))
            people[key] = name
            print(people)
        prompt = input("Another person? (Y/N): ")
    print(people)
    return people


people()
'''
