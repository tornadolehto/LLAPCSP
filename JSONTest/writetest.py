import json

data = {}
quit = None

while quit != 'y':

    x = input("1")
    data[x] = input('2')
        
    print(data)
    with open("data.json","w") as f:
            json.dump(data,f,indent=4)
    
    quit = input("Quit?")



    