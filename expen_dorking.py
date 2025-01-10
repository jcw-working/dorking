#!/bin/python3

import webbrowser
import time
import readchar

##################################################################################

# Where is your browser, and what is it?

firefox_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path))
b = webbrowser.get('firefox')

##################################################################################

# add more to these lists if you want!

paste_sites = [
    "pastebin.com",
    "drive.google.com OR site:docs.google.com OR site:sheets.google.com",
    "docs.microsoft.com",
    "github.com",
    "www.filedropper.com OR site:FriendPaste.com",
    "CopyTaste.com OR site:Cl1p.net",
    "ShortText.com OR site:TextSave.de",
    "TextSnip.com OR site:TxtB.in",
    "jsfiddle.net OR site:stackoverflow.com",
    "beepingcomputer.com"
]

social_sites = [
    "facebook.com",
    "linkedin.com",
    "youtube.com",
    "twitter.com",
    "pinterest.com",
    "tumblr.com",
    "instagram.com",
    "flickr.com",
    "vimeo.com",
    "brighttalk.com",
    "tiktok.com",
]

filetype_list = [
    "pdf",
    "xls OR filetype:xlsx OR filetype:csv",
    "doc OR filetype:docx",
    "txt OR filetype:log OR filetype:rtf OR filetype:bak",
    "php",
    "env OR filetype:wsdl OR filetype:svc",
    "asmx OR filetype:asp OR filetype:aspx",
    "ppt OR filetype:pptx",
    "config OR filetype:yaml OR filetype:yml OR filetype:ini"
]

def google_walker(sites,targetDomain,timer,targetName,topend):

    counter = 0
    cntinue = ""

    for site in sites:
        if cntinue == "a":
            break
        print("[+]   {}".format(site))
        b.open("https://google.com/search?q=site:" + site + "+%22" + targetDomain + "%22")
        time.sleep(timer)
        b.open("https://google.com/search?q=site:" + site + "+%22" + targetName + "%22")
        time.sleep(timer)
        counter +=1
        if counter == topend:
            print("<enter> to continue or <a>bort to return to test progression")
            cntinue = readchar.readkey()
            counter = 0

def file_walker(filetypes,targetDomain,timer,targetName,topend):

    counter = 0
    cntinue = ""

    for type in filetypes:
        if cntinue == "a":
            break
        print("[+]   {}".format(type))
        b.open("https://google.com/search?q=filetype:" + type + "+site:" + targetDomain + "%22")
        time.sleep(timer)
        b.open("https://google.com/search?q=filetype:" + type + "+%22" + targetName + "%22")
        time.sleep(timer)
        counter +=1
        if counter == topend:
            print("<enter> to continue or <a>bort to return to test progression")
            cntinue = readchar.readkey()
            counter = 0

def dorking(variable_list):

    targetDomain = variable_list[0]
    timer = variable_list[1]

    b.open("https://www.google.com/search?q=filetype:bak%20inurl:%22htaccess\|passwd\|shadow\|htusers%22+site:" + targetDomain)
    time.sleep(timer)
    b.open("https://www.google.com/search?q=intitle:%22index%20of%22+%22last%20modified%22+%22parent%20directory%22+site:" + targetDomain)
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site:" + targetDomain + "+inurl:admin")
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site:" + targetDomain + "+inurl:login")
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site:*." + targetDomain + "+-www")
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site:*.*." + targetDomain + "+-www")
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site:" + targetDomain + "+%22choose+file%22")
    time.sleep(timer)
    b.open("https://www.google.com/search?q=site%3Aopenbugbounty.org+inurl%3Areports+intext%3A%22" + targetDomain + "%22")
    time.sleep(timer)

def sites_recon(variable_list):

    targetDomain = variable_list[0]
    timer = variable_list[1]
    targetName = variable_list[2]
    topend = variable_list[3]

    google_walker(paste_sites,targetDomain,timer,targetName,topend)

def social_recon(variable_list):

    targetDomain = variable_list[0]
    timer = variable_list[1]
    targetName = variable_list[2]
    topend = variable_list[3]

    google_walker(social_sites,targetDomain,timer,targetName,topend)

def filetype_recon(variable_list):

    targetDomain = variable_list[0]
    timer = variable_list[1]
    targetName = variable_list[2]
    topend = variable_list[3]

    file_walker(filetype_list,targetDomain,timer,targetName,topend)