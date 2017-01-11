import queue
import json
try:
    import requests
except:
    import pip
    print("Performing first-time setup...")
    pip.main(['install','pillow','requests'])
def input_worker(input_queue):
    while True:
        inp = input()
        if inp == "ship":
            input_queue.put({"cmd":"ship","data":makeship()})
        elif inp == "exit":
            print("Exiting...")
            input_queue.put({"cmd":"exit"})
        elif len(inp) > 6 and inp[0:5] == "cargo":
            try:
                cargo = int(inp[6:])
                input_queue.put({"cmd":"cargo","data":cargo})
                print("Setting cargo amount...")
            except:
                print("Invalid cargo amount")
        elif len(inp) > 7 and inp[0:6] == 'origin':
            try:
                origin = getOrigin2(inp[7:])
                input_queue.put({"cmd":"origin","data":origin})
            except:
                print("There was an error finding the system {}.".format(inp[7:]))
        elif inp == "help":
            print("""Available commands are:
ship
    -Asks for and sets information about your ship, used for calculating jump range.
    
cargo [number]
    -Sets the amount of cargo tonnage you are currently hauling.
    
origin [system name]
    -Sets the system to display distances relative to. i.e. after `origin Merope` on FSD jump
     it might say "you've arrived in the Pleiades xy-z 3834 system and are 32 light years from Merope".
     
help
    -Lists available commands ;)
    
exit
    -Quits the program""")
        else:
            print("Invalid command:", inp)


def makeship():
    print("Please input the following information about your ship:")
    ship = {"currentfuel":0,
    "cargo":0,
    "unladenmass":getfloat("Ship unladen mass (includes full fuel tank, as output by coriolis.edcd.io): "),
    "fuelcapacity":getfloat("Ship fuel tank maximum capacity: "),
    "fsdrating":getrating("Frame shift drive rating (A-E): "),
    "fsdclass":getclass("Frame shift drive class (2-8): "),
    "fsdmaxfuel":getfloat("FSD maximum fuel use per jump: "),
    "fsdoptmass":getfloat("FSD optimal mass: ")}
    return ship
fsdclasses = {2: 2,
              3: 2.15,
              4: 2.3,
              5: 2.45,
              6: 2.6,
              7: 2.75,
              8: 2.9,
              }
fsdratings = {'A': 12,
              'B': 10,
              'C': 8,
              'D': 10,
              'E': 11,
              }

def getOrigin():
    print("Input a star that you want to see your distance to on each jump.")
    print("Press return (leave blank) to use Sol.")
    return getOrigin2(input())

def getOrigin2(starName):
    if starName == "":
        return ('Sol',0,0,0)
    else:
        r = requests.get("https://www.edsm.net/api-v1/system",params={"systemName":starName,"showCoordinates":1})
        starinfo = json.loads(r.text)
        starcoords = (starinfo["name"],starinfo["coords"]["x"],starinfo["coords"]["y"],starinfo["coords"]["z"])
        print("The coordinates of {} are ({}, {}, {})".format(*starcoords))
        return starcoords
    
def getfloat(prmpt):
    while True:
        try:
            num = float(input(prmpt))
            assert(num>0)
            return num
        except:
            print("Invalid number, please try again.")

def getclass(prmpt):
    while True:
        try:
            clas = int(input(prmpt))
            assert(clas < 9)
            assert(clas > 1)
            return fsdclasses[clas]
        except:
            print("Invalid class, please enter a number between 2 and 8.")
def getrating(prmpt):
    while True:
        try:
            rating = input(prmpt)
            rating = rating.upper()
            assert(len(rating)==1)
            assert(ord(rating) > 64)
            assert(ord(rating) < 70)
            return fsdratings[rating]
        except:
            print("Invalid rating, please enter a letter between A and E")
            
