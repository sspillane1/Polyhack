import json


# Get array and turn into json #
def createjson(st):
    x = json.dumps(st)
    with open("data.json", "w") as write_file:
        json.dump(x, write_file)
    print(json.dumps(x))

if __name__ == "__main__":
    #comment out
    #st = "Hey there guy"
    #createjson(st)
