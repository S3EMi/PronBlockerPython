"""
Welcome to PronBlocker! Your first step to curing you pron addiction.
Peek the code all you want! This should be a simple "host" file editing program.
Dire problems requires dire solutions.
"""
import os

hosts_file = open("C:\Windows\System32\drivers\etc\HOSTS","a")
pronList = open("sitesList.txt","r" )
listLen = len(pronList.readlines())

def pause():
    input("\n Press any button to continue...")

def checkFile():
    try: 
        open("C:\Windows\System32\drivers\etc\HOSTS")
    except Exception:
        print("--An error occurred while opening HOSTS file! Please run the file as ADMIN.--")

def openWrite():
    pronList = open("sitesList.txt","r" )
    progress = 0

    for i in pronList:
        hosts_file.write(i)
        progress += 1
        pBar = (progress/listLen) * 100
        print("Blocking websites... %.4s%%" %(pBar))
    print("\nDONE! -- Finished adding sites to HOST!")

def closeFiles():
    pronList.close()
    hosts_file.close()
    print("\nFinished closing files!")

def main():
    print("--- Welcome to PronBlocker! You're one step closer to greatness! ---")
    print("If you want to revert changes, run the 'REVERT CHANGES' file on the folder.")
    input("Make sure that the file is running as admin. Once you have, press any button...")
    checkFile()
    openWrite()
    closeFiles()
    pause()
main()
