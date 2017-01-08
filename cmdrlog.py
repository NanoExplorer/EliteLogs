import os,time,json
#import winclip
import signal
import sys
import time
import math
def writedict(filename, dictionary):
    """Given a filename and a dictionary (or list...), writes the dictionary to file as json.
    The dictionary can then be retrieved with the getdict function below.
    Setting pretty to false can make the file considerably smaller, at the cost of being almost unintelligable.
    """
    with open(filename,'w') as jsonfile:
        jsonfile.write(json.dumps(dictionary,
                                  sort_keys=True,
                                  indent=4, separators=(',', ': ')))
def getdict(filename):
    """Given the name of a json file, reads the file in and returns the object it contains
    """
    jsondict = None
    with open(filename,'r') as settings:
        jsondict = json.loads(settings.read())
        #reads the entire settings file with .read(), then loads it as a json dictionary, and stores it into jsondict
    return jsondict

def main():
    path_to_watch = "C:\\Users\\[example]\\Saved Games\\Frontier Developments\\Elite Dangerous\\"
    if path_to_watch == "C:\\Users\\[example]\\Saved Games\\Frontier Developments\\Elite Dangerous\\":
        print("To initialize this script, please edit the path_to_watch variable in the main() function to point to your commander log location.")
    print(path_to_watch)
    before= dict([(f,os.stat(path_to_watch+f).st_size) for f in os.listdir(path_to_watch)])
    with LogManager() as watcher:
        print("Starting...")
        while 1:
            after = dict ([(f, os.stat(path_to_watch+f).st_size) for f in os.listdir (path_to_watch)])
            added = [f for f in after if not f in before]
            removed = [f for f in before if not f in after]
            changed = [f for f in before if ((f in after) and (before[f] < after[f]))]
            if added: print("Added: ", ", ".join (added))
            if removed: print("Removed: ", ", ".join (removed))
            for full_filename in changed:
                with open(path_to_watch+full_filename,'r') as logfile:
                    logfile.seek(before[full_filename])
                    for line in logfile:#.read().split('\n'):
                        watcher.process_line(line.strip())
            before = after
            time.sleep(2)

class LogManager():
    def __init__(self):
        if not self.load():
            print("New save!")
            self.scandatabase=[]
        self.fuel=0
        self.route = ['LTT 16218', 'Nova Aquila No 3', 'COL 359 Sector NN-T E3-3', 'B133 Sector DB-X d1-30', 'Pru Euq JC-D D12-56', 'Swoiwns IT-F D12-31', 'Swoiwns JY-G D11-21', 'Swoiwns XV-C D13-18', 'Bleia Eohn ZJ-Z D6', 'Bleia Eohn KH-V D2-6', 'Bleia Eohn RT-R D4-0', 'Bleia Eohn YF-O D6-2', 'Aucopp VN-K D8-3', 'Aucopp EL-F D11-0', 'Aucopp PD-A D14-0', 'Drojeae IV-Y D4', 'Drojeae PH-V D2-5', 'Drojeae EG-O D6-0', 'Drojeae NY-I D9-3', 'Drojeae CX-B D13-3', 'Blae Drye FL-Y D3', 'Blae Drye OI-T D3-8', 'Blae Drye BW-N D6-3', 'Blae Drye II-K D8-3', 'Thailoi IB-F D11-7', 'Thailoi ST-Z D13-4', 'Pyraleau VX-U D2-5', 'Pyraleau AP-R D4-0', 'Pyraleau KH-M D7-16', 'Pyraleau VZ-G D10-5', 'Pyraleau EX-B D13-4', 'Nyeajaae CF-A D5', 'Nyeajaae KC-V D2-2', 'Nyeajaae UZ-P D5-21', 'Nyeajaae GN-K D8-8', 'Nyeajoa FL-F D11-16', 'Nyeajoa SY-Z D13-16', 'Flyiedge OB-X D1-22', 'Flyiedge ZT-R D4-22', 'Flyiedge KM-M D7-19', 'Flyiedge VE-H D10-3', 'Flyiedge FX-B D13-3', 'Skaude FQ-Y D16', 'Skaude ON-T D3-25', 'Skaude ZF-O D6-8', 'Skaude KY-I D9-3', 'Skaude XL-D D12-4', 'Prua Phoe LK-A D4', 'Prua Phoe JL-Y E9', 'Prua Phoe HV-P D5-52', 'Prua Phoe RN-K D8-2', 'Prua Phoe BQ-P E5-26', 'Prua Phoe NY-Z D13-97', 'Clooku HQ-Y D78', 'Clooku UT-R D4-165', 'Clooku QD-T E3-26', 'Clooku KY-I D9-266', 'Clooku MS-U F2-3', 'Nuekuae VO-A D110', 'Nuekuae GH-V D2-74', 'Stuelou GA-Q D5-149', 'Stuelou QS-K D8-12', 'Stuelou CL-F D11-165', 'Stuelou MD-A D14-24', 'Blua Eaec LB-X D1-243', 'Blua Eaec WT-R D4-206', 'Blua Eaec GM-M D7-332', 'Blua Eaec RE-H D10-4', 'Blua Eaec CW-N E6-275', 'Boelts WO-A D342', 'Boelts CL-Y E439', 'Boelts KX-U E2-13', 'Boeph VD-T E3-1415', 'Boeph DL-F D11-363', 'Boeph OD-A D14-979', 'Eoch Flyuae MB-X D1-147', 'Eoch Flyuae XT-R D4-200', 'Eoch Flyuae HM-M D7-961', 'Eoch Flyuae VJ-R E4-88', 'Eoch Flyuae YP-P E5-2654', 'Dryio Flyuae ZE-A E112', 'Dryio Flyuae JC-V D2-1910', 'Dryio Flyuae UU-P D5-877', 'Dryooe Flyou TS-K D8-1002', 'Dryooe Flyou FG-F D11-1923', 'Dryooe Flyou OD-A D14-201', 'Eol Prou NB-X D1-943', 'Eol Prou TN-T D3-430', 'Colonia']
        self.route = [x.lower() for x in self.route]
        self.times=[]
        self.lastjump = time.time()
        self.shipmass = 401
    def __enter__(self):
        return self
    def __exit__(self,exc_type, exc_value, traceback):
        self.save()
        print("You averaged {} sec/jump".format(sum(self.times)/len(self.times)))
    def load(self):
        if os.path.isfile('scandb.json'):
            print("loading!")
            self.scandatabase = getdict('scandb.json')
            self.fuel=0
            return(True)
        return(False)

    def save(self):
        print("Saving...")
        saveloc = "scandb.json"
        writedict(saveloc,self.scandatabase)
    def process_line(self,strin):
        info = json.loads(strin)
        events = {"LoadGame": self.LoadGame,
                  "FSDJump" : self.FSDJump,
                  "FuelScoop": self.FuelScoop,
                  "SupercruiseEntry": self.entersc,
                  "Rank": self.Rank,
                  "Progress": self.Progress,
                  "Location": self.Location,
                  "Scan": self.Scan,
                  "JetConeBoost":self.JetConeBoost
                  }
        try:
            events[info["event"]](info)
        except KeyError:
            print(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))
        print()
    def LoadGame(self,info):
        print("Welcome back, {Commander}. You're flying your {Ship} in {GameMode} and you \n\
have {Credits} credits.".format(**info))

    def FSDJump(self,info):
        pos = info["StarPos"]
        distancefromsol = math.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
        print("""You've arrived in the {} sector. You are {:.1f} L.Y. from Sol.""".format(info["StarSystem"],distancefromsol))
        if info["SystemAllegiance"] != "":
            print("This sector is under {} control.".format(info["SystemAllegiance"]))
        if info["SystemEconomy_Localised"] != "None":
            print("This system's primary economy is {}".format(info["SystemEconomy_Localised"]))
        print("""You used {FuelUsed:.3f} tonnes of fuel during your {JumpDist} L.Y. jump, and you
have {FuelLevel:.2f} tonnes remaining.""".format(**info))
        self.fuel=info["FuelLevel"]
        print("Your current range is {} ly".format(getrange(self.shipmass,self.fuel,1)))
        startingFuel=info["FuelUsed"]+info["FuelLevel"]
        #print("DEBUG: {} {} {}".format(info["JumpDist"],info["FuelUsed"],startingFuel))
        
        #if info["StarSystem"].lower() in self.route:
        #  print("You have arrived at your next waypoint!")
        #  print("Copying the next waypoint to clipboard...")
        #  nextwaypoint = self.route[self.route.index(info["StarSystem"].lower())+1]
        #  print("The next waypoint is {}".format(nextwaypoint))
        #  winclip.copy(nextwaypoint)
        #  #r.destroy()
        #  print(nextwaypoint)
        #  print(type(nextwaypoint))
        self.times.append(time.time()-self.lastjump)
        print("Jump time: {:.1f} seconds.".format(time.time()-self.lastjump))
        self.lastjump=time.time()
        
      
    def FuelScoop(self,info):
        print("You scooped {Scooped:.2f} tonnes of fuel and have {Total:.2f} tonnes available.".format(**info))
        self.fuel=info["Total"]
        print("Your current range is {} ly".format(getrange(self.shipmass,self.fuel,1)))

    def entersc(self,info):
        print("Supercruise jump complete! You're in the {StarSystem} system.".format(**info))

    def Rank(self,info):
        pass
        #print(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))

    def Progress(self,info):
        pass
        #print(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))

    def Location(self,info):
        print(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))

    def Scan(self,info):
        print(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))
        self.scandatabase.append(info)

    def JetConeBoost(self,info):
        print("""***********************************************************
* WARNING: MASSIVE ELECTROMAGNETIC INTERFERENCE DETECTED  *
*       Frame shift drive safety mechanisms offline       *    
* PERFORMING A FRAME SHIFT JUMP UNDER THESE CIRCUMSTANCES *
*                WILL VOID YOUR WARRANTY!                 *              
***********************************************************

*  Additionally, a FirmwareVerificationError was detected *


*******Starting NeutronHelper v1.3.4*******
Use of this software is not protected by
any warranties, explicit or implied.
USE AT YOUR OWN RISK.

Predicted Jump Range:
{} Light Years

*****Thank you for using NeutronHelper*****
******A Service of Nano Laboratories*******
""".format(getrange(self.shipmass,self.fuel,4) ))
#Fuel = 0.012 * (distance*mass/optimal mass)^2.45
#distance = 2.45root(fuel/0.012)*optimal mass/mass

def getrange(mass,fuel,mult):
    return mult*(5.279/0.012)**(1/2.45)*1560.9/(mass-32+fuel)
if __name__ == "__main__":
    main()

"""
  before = after
     activefiles[full_filename]=os.stat(full_filename).st_size

    if activefiles[full_filename] < os.stat(full_filename).st_size:
      with open(full_filename,'r') as logfile:
        logfile.seek(activefiles[full_filename])
        for line in logfile:#.read().split('\n'):
          print("BEGIN LINE: {}".format(line.strip()))
      activefiles[full_filename] = os.stat(full_filename).st_size
        
      

"""
