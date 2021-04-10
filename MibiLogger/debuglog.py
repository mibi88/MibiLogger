from colorama import Fore, Back, Style

def startlog(description=None):
   print(Style.BRIGHT + Fore.GREEN + Back.BLUE + "[DEBUG LOG]", end = "")
   print(Style.RESET_ALL + "\n")
   if description != None:
      print(Style.BRIGHT + Back.RED + Fore.WHITE + "Debug For : ", end = "")
      print(Style.BRIGHT + Back.WHITE + Fore.BLUE + str(description), end = "")
      print(Style.RESET_ALL + "\n\n")
# startlog("MibiLogger")
def errorlog(test_name, tagtype, value):
   msg = "[ERROR] Error : " + str(test_name) + "    Type : #" + str(tagtype) + "    Value : " + str(value)
   print(Style.BRIGHT + Fore.RED + Back.WHITE + msg, end = "")
   print(Style.RESET_ALL, "")
# errorlog("Errorlog test", "test", "True")
def infolog(test_name, tagtype, value):
   msg = "[INFO] Info : " + str(test_name) + "    Type : #" + str(tagtype) + "    Value : " + str(value)
   print(Style.BRIGHT + Fore.BLUE + Back.WHITE + msg, end = "")
   print(Style.RESET_ALL, "")
# infolog("Errorlog test", "test", "True")
def warninglog(test_name, tagtype, value):
   msg = "[WARNING] Warning : " + str(test_name) + "    Type : #" + str(tagtype) + "    Value : " + str(value)
   print(Style.BRIGHT + Fore.YELLOW + Back.WHITE + msg, end = "")
   print(Style.RESET_ALL, "")
# warninglog("Errorlog test", "test", "True")
