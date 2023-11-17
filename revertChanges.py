"""
Why are you doing this man... Don't give in bro... :(
"""
import os

replaceHosts = open("hosts","r")

def pause():
    input("\nPress any button to coninue...")

hosts_file = open("C:\Windows\System32\drivers\etc\HOSTS","w")

def openWrite():
    replaceHosts = open("hosts","r")

    for i in replaceHosts:
        hosts_file.write(i)
    print("\nDone... HOSTS file is reverted back.")

def closeFiles():
    hosts_file.close()
    replaceHosts.close()
    print("\nFinished closing files!")

def main():
    print("Don't do it lil bro, you'll just go back to that miserable life of yours... And you will make me sad :(")
    input("Make sure that the file is running as admin. Once you have, press any button...")
    openWrite()
    closeFiles()
    pause()
main()