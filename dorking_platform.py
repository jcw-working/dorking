#!/bin/python3

#################

# Dorking Framework

#################

from optparse import OptionParser
import sys
import readchar
import os.path
import os

from expen_dorking import dorking,sites_recon,social_recon,filetype_recon

###################################################

version_number = "Resolve/Platform Supplementary Browser Recon"

# default logging output directory
outdir = "C:\\Users\\jwilkes\\AppData\\Local\\Temp\\"

###################################################

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
parser.add_option("-a", "--autofire", help='Automatically runs all tests in sequence.  Does not open browser for site checks.',action="store_true")
parser.add_option("-o", "--outdir", help='Path to directory where output files will be written. Defaults to "/tmp/"')
parser.add_option("-m", "--maxtabs", help='Maximum number of tabs fired at your browser before prompting.  Default is 10.  Best if it is an even number!')
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
    maxtabs = 5
    print("[+]   Maximum fired tabs defaulting to 10")
else:
    maxtabs = int(options.maxtabs) // 2

variable_list = [targetDomain,timer,targetName,maxtabs]

# logic to skip a module, or autofiring

def maybe_skip_this(subroutine,variable_list,autofire):

    if autofire == True:
        print("\n")
        subroutine(variable_list)
        return
    print("\n<enter> to continue or <s>kip operation ", end = '')
    cntinue = readchar.readkey()
    if cntinue == "s":
        return
    else:
        print("\n")
        subroutine(variable_list)

# test modules

subroutines = [
    ["\n\n[+]   Google dorking",dorking],
    ["\n\n[+]   Paste site enumeraton",sites_recon],
    ["\n\n[+]   Social media site enumeration",social_recon],
    ["\n\n[+]   Filetype enumeration",filetype_recon]
]

# calling modules

for subroutine in subroutines:
    print(subroutine[0])
    maybe_skip_this(subroutine[1],variable_list,autofire)

print("\n")