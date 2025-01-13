#!/bin/python3

#################

# Browser Recon Platform

#################

from optparse import OptionParser
import sys
import readchar
import os.path
import os
import webbrowser
import time

#################### SETTINGS #####################

version_number = "1.0"

# default logging output directory
outdir = "C:\\Users\\<user>\\AppData\\Local\\Temp\\"

# Where is your browser, and what is it?

firefox_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path))
b = webbrowser.get('firefox')

# URL for search engine?  Rotating proxy recommended...

engine="https://www.google.com"
#engine="<fireprox URL"

###################################################

# add more to these lists if you want!

paste_sites = [
    "site:pastebin.com",
    "site:drive.google.com OR site:docs.google.com OR site:sheets.google.com",
    "site:docs.microsoft.com",
    "site:github.com",
    "site:www.filedropper.com OR site:FriendPaste.com",
    "site:CopyTaste.com OR site:Cl1p.net",
    "site:ShortText.com OR site:TextSave.de",
    "site:TextSnip.com OR site:TxtB.in",
    "site:jsfiddle.net OR site:stackoverflow.com",
    "site:beepingcomputer.com"
]

social_sites = [
    "site:facebook.com",
    "site:linkedin.com",
    "site:youtube.com",
    "site:twitter.com",
    "site:pinterest.com",
    "site:tumblr.com",
    "site:instagram.com",
    "site:flickr.com",
    "site:vimeo.com",
    "site:brighttalk.com",
    "site:tiktok.com"
]

filetype_list = [
    "filetype:pdf",
    "filetype:xls OR filetype:xlsx OR filetype:csv",
    "filetype:doc OR filetype:docx",
    "filetype:txt OR filetype:log OR filetype:rtf OR filetype:bak",
    "filetype:php OR filetype:apk",
    "filetype:env OR filetype:wsdl OR filetype:svc",
    "filetype:asmx OR filetype:asp OR filetype:aspx",
    "filetype:ppt OR filetype:pptx",
    "filetype:config OR filetype:yaml OR filetype:yml OR filetype:ini"
]

###################################################

def google_walker(sites,targetDomain,timer,targetName,topend,tabsOpen):

    cntinue = ""

    for site in sites:
        if cntinue == "a":
            break
        print("[+]   {}".format(site))
        b.open(engine + "/search?q=" + site + "+%22" + targetDomain + "%22")
        time.sleep(timer)
        b.open(engine + "/search?q=" + site + "+%22" + targetName + "%22")
        time.sleep(timer)
        tabsOpen +=2
        if tabsOpen == topend:
            print("<enter> to continue or <a>bort to return to test progression")
            cntinue = readchar.readkey()
            tabsOpen = 0
    return tabsOpen

def file_walker(filetypes,targetDomain,timer,targetName,topend,tabsOpen):

    cntinue = ""

    for type in filetypes:
        if cntinue == "a":
            break
        print("[+]   {}".format(type))
        b.open(engine + "/search?q=" + type + "+site:" + targetDomain + "%22")
        time.sleep(timer)
        b.open(engine + "/search?q=" + type + "+%22" + targetName + "%22")
        time.sleep(timer)
        tabsOpen +=2
        if tabsOpen == topend:
            print("<enter> to continue or <a>bort to return to test progression")
            cntinue = readchar.readkey()
            tabsOpen = 0
    return tabsOpen

def dorking(targetDomain,timer,targetName,maxtabs,tabsOpen):

    print ("[+]   " + engine + "/search?q=intitle:%22index%20of%22+%22last%20modified%22+%22parent%20directory%22+site:" + targetDomain)
    b.open(engine + "/search?q=intitle:%22index%20of%22+%22last%20modified%22+%22parent%20directory%22+site:" + targetDomain)
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:" + targetDomain + "+inurl:admin")
    b.open(engine + "/search?q=site:" + targetDomain + "+inurl:admin")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:" + targetDomain + "+inurl:login")
    b.open(engine + "/search?q=site:" + targetDomain + "+inurl:login")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:*." + targetDomain + "+-www")
    b.open(engine + "/search?q=site:*." + targetDomain + "+-www")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:*.*." + targetDomain + "+-www")
    b.open(engine + "/search?q=site:*.*." + targetDomain + "+-www")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:" + targetDomain + "+%22choose+file%22")
    b.open(engine + "/search?q=site:" + targetDomain + "+%22choose+file%22")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site%3Aopenbugbounty.org+inurl%3Areports+intext%3A%22" + targetDomain + "%22")
    b.open(engine + "/search?q=site%3Aopenbugbounty.org+inurl%3Areports+intext%3A%22" + targetDomain + "%22")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=site:" + targetDomain + "+%22internal%22+OR+%22confidential%22+OR+%22proprietary%22+OR+%22configuration%22+OR+%22admin%22")
    b.open(engine + "/search?q=site:" + targetDomain + "+%22internal%22+OR+%22confidential%22+OR+%22proprietary%22+OR+%22configuration%22+OR+%22admin%22")
    time.sleep(timer)
    print("[+]    " + engine + "/search?q=inurl:s3.amazonaws.com OR inurl:blob.core.windows" + "+%22" + targetDomain + "%22+" + targetName + "%22")
    b.open(engine + "/search?q=inurl:s3.amazonaws.com OR inurl:blob.core.windows" + "+%22" + targetDomain + "%22+" + targetName + "%22")
    tabsOpen = 8

    return tabsOpen

def sites_recon(targetDomain,timer,targetName,maxtabs,tabsOpen):
    tabsNow = google_walker(paste_sites,targetDomain,timer,targetName,maxtabs,tabsOpen)
    return tabsNow

def social_recon(targetDomain,timer,targetName,maxtabs,tabsOpen):
    tabsNow = google_walker(social_sites,targetDomain,timer,targetName,maxtabs,tabsOpen)
    return tabsNow

def filetype_recon(targetDomain,timer,targetName,maxtabs,tabsOpen):
    tabsNow = file_walker(filetype_list,targetDomain,timer,targetName,maxtabs,tabsOpen)
    return tabsNow

# taking arguments

if ((len(sys.argv) < 3 or len(sys.argv) > 12) and '-h' not in sys.argv):
    print("\nGeneral Recon Framework Version: {}".format(version_number))
    print("\nUsage:")
    print("\npython3 %s -d <target domain> -s <search string> -t (optional throttle) -m (optional maximum tabs fired) -a (optional autofire all tests) -o (optional output directory)\n" % sys.argv[0])
    print("Enclose complex strings in single quotes e.g. '/a/file/path' or 'Company Name'")
    print("Example:\n")
    print("python3 %s -d behind-bars.com -s 'Behind Bars' -t 2 -a -o '/tmp/engagement'\n" % sys.argv[0])
    sys.exit(1)

parser = OptionParser()
parser.add_option("-d", "--domain", help='Target domain e.g. \"behind-bars.com\" or \"gentex.com\"')
parser.add_option("-s", "--name", help='Target search phrase/name e.g. \"Behind Bars Bicycle Shop\" or \"Gentex\"')
parser.add_option("-t", "--throttle", help="Request throttling in seconds. 2.0 is standard, but defaults to 0 if no argument)")
parser.add_option("-a", "--autofire", help='Automatically runs all tests in sequence.  Only stops to promt when maximum tabs is met.',action="store_true")
parser.add_option("-o", "--outdir", help='Path to directory where output files will be written. Defaults to "/tmp/"')
parser.add_option("-m", "--maxtabs", help='Maximum number of tabs fired at your browser before prompting, with the expectation that you will close the browser.  Default is 10.  Best if it is an even number!')
(options, args) = parser.parse_args()

# argument processing, logging, and minimal dopey error checking

if options.outdir == None:
    print("[+]   Output directory path defaulting to {}".format(outdir))
else:
    try:
        os.mkdir(options.outdir)
        print("[+]   Creating {}".format(options.outdir))
    except:
        print("[+]   {} already exists".format(options.outdir))
    outdir = (options.outdir).rstrip('\\') + "\\"

log_file = outdir + options.domain + "-recon-log"

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(log_file, 'a')
    def write(self, text):
            self.terminal.write(text)
            self.log.write(text)
    def flush(self):
            pass
        
sys.stdout = Logger()

print("[+]   Application version: {}".format(version_number))
print("[+]   Logging stdout to {}".format(log_file))

targetDomain = options.domain
if targetDomain == None:
    print("[-]   No domain specified -- EXITING")
    quit()

targetName = options.name
if targetName == None:
    print("[-]   No search string specified -- EXITING")
    quit()

if (options.throttle) != None:
    timer = int(options.throttle)
else:
    timer = 0
    print("[+]   Throttle defaulting to 0")

autofire = options.autofire

if options.maxtabs == None:
    maxtabs = 10
    print("[+]   Maximum fired tabs defaulting to 10")
else:
    maxtabs = (int(options.maxtabs) // 2) * 2
    print("[+]   Maximum fired tabs = {}".format(maxtabs))
    if maxtabs == 0:
        print("[-]   Maximum fired tabs must be at least 2.")
        quit()

# logic to skip a module, or autofiring

def maybe_skip_this(subroutine,autofire,tabsOpen):

    if autofire == True:
        print("\n")
        tabsNow = subroutine(targetDomain,timer,targetName,maxtabs,tabsOpen)
        return tabsNow
    print("\n<enter> to continue or <s>kip operation ", end = '')
    cntinue = readchar.readkey()
    if cntinue == "s":
        return tabsOpen
    else:
        print("\n")
        tabsNow = subroutine(targetDomain,timer,targetName,maxtabs,tabsOpen)
        return tabsOpen

# test modules

subroutines = [
    ["\n\n[+]   Google dorking",dorking],
    ["\n\n[+]   Paste site enumeraton",sites_recon],
    ["\n\n[+]   Social media site enumeration",social_recon],
    ["\n\n[+]   Filetype enumeration",filetype_recon]
]

# calling modules

tabsOpen = 0
for subroutine in subroutines:
    print(subroutine[0])
    tabsOpen = maybe_skip_this(subroutine[1],autofire,tabsOpen)

print("\n")
