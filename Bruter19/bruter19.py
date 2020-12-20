import platform
from clint.textui import colored
import subprocess
from Brute import face
from Brute import face_tr
from Brute import insta
from Brute import insta_tr
from Brute import twitter
from Brute import twitter_tr
from banner import banner
import os
try:
    banner.bruter19_language()
    language=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
    if language=="1":
        banner.bruter19_wordlist_banner()
        wordlist=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
        if wordlist=="2" or wordlist=="no" or wordlist=="n":
            os.system("xterm -e python3 bruter19_cupp/cupp.py -i")
            os.system("zenity --info --text='Your Wordlist Has Been Generated In The Bruter19/ Directory'")
        banner.brute19banner()

        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"https://github.com/Hacksin5minutes")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Check /var/share/wordlists directory in order to see good wordlists.")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Be sure that you dont't have shorter than 6 character passwords in your wordlist.")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Let me know if the tool is not working properly[https://github.com/AzizKpln/Bruter19/issues].")
        choice=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
        if choice=="2":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Wrong Path For Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                face.fb_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C Detected Exiting..."))
                exit()
        elif choice=="1":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Be sure that you don't have shorter than 6 character passwords in your wordlist.")+colored.magenta("]\n"))
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number/Username")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Wrong Path For Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                insta.ig_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C Detected Exiting.."))
                exit()
        elif choice=="3":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Mail Address/Phone Number")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Path")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Wrong Path For Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                twitter.tw_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C Detected Exiting.."))
                exit()
    elif language=="2":
        banner.bruter19_wordlist_banner_tr()
        wordlist=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
        if wordlist=="2" or wordlist=="no" or wordlist=="no" or wordlist=="h":
            os.system("xterm -e python3 bruter19_cupp/cupptr.py -i")
            os.system("zenity --info --text='Dein Wordlist wurde im Bruter19/ Verzeichnis erstellt .'")
        banner.brute19bannertr()

        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"https://github.com/Hacksin5minutes")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Check /usr/share/wordlists ob da eine Wordlist ist .")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Sei dir sicher das du keine Passwörter unter 6 Buchstaben in der Wordlist hast ")
        print(colored.red("\n[")+colored.green("*")+colored.red("]")+"Sag mir wenn es geklappt hat [https://github.com/Hacksin5minutes/Bruter19/issues].")
        choice=input(colored.red("\n\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
        if choice=="2":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Email adresse/Telefon Nummer")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Pfad")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Falscher Dateipfad zur Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                face_tr.fb_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C zum beenden..."))
                exit()
        elif choice=="1":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Email adresse/Telefon Nummer")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Pfad")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Falscher Dateipfad zur Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                insta_tr.ig_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C zum beenden.."))
                exit()
        elif choice=="3":
            banner.normal_banner()
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Email adresse/Telefon Nummer/Username")+colored.magenta("]"))
            mail_address=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            print(colored.red("[")+colored.green("*")+colored.red("]")+colored.magenta("[")+colored.cyan("Wordlist Dateipfad")+colored.magenta("]"))
            try:
                pw_path=input(colored.red("\n[")+colored.blue("bruter19")+colored.yellow("@")+colored.cyan(platform.node())+colored.red("]") + colored.red(" - [") + colored.yellow("#") + colored.red("]"))
                with open(pw_path,"r",encoding="utf-8") as passwords:
                    pw=passwords.readlines()
            except:
                print(colored.red("[-]Falscher Dateipfad zur Wordlist!!!"))
                exit()
            print(" ")
            print(colored.red("-"*50))
            print(" ")
            try:
                twitter_tr.tw_brute(mail_address,pw)
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C zum beenden.."))
                exit()
except KeyboardInterrupt:
    print(colored.red("[-]CTRL+C DETECTED, EXITING.."))
