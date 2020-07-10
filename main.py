import apiworks
import pets
import requests
import webbrowser

#f = apiworks.api()
#f.refresh()
#f.getMiles()
name = input()
pet = pets.pet(name)
var = True
while(var):
    print('1. status, 2. simulate 1 hour, 3. feed, 4. buy toy')
    i = input()
    if (i == '1'):
        print(pet.getStatus())
    elif (i == '2'):
        pet.hourPasses()
    elif(i == '3'):
        pet.feed()
    elif(i == '4'):
        pet.buyToy()
    else:
        break
print('done')
