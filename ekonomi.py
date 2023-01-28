from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from tabulate import tabulate
import os
from datetime import datetime

opt = Options()
opt.headless =True

chrome_driver_path = "C:\drivers\chromedriver"
driver = webdriver.Chrome(chrome_driver_path,chrome_options=opt)
driver.implicitly_wait(20)

url = "https://bigpara.hurriyet.com.tr/borsa/gunun-ozeti/"


driver.get(url)
while True:
    time.sleep(5)
    os.system('cls||clear')
    dolar = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[2]/a/span[1]/span[2]").text
    ydChange = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[2]/a/span[3]/span[1]").text 
    dChange1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[2]/a/span[3]/span[2]").text 
    euro = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[3]/a/span[1]/span[2]").text
    yeChange = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[3]/a/span[3]/span[1]").text
    eChange1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[3]/a/span[3]/span[2]").text 
    altin = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[4]/a/span[1]/span[2]").text
    yaChange = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[4]/a/span[3]/span[1]").text
    aChange1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/header/div[5]/div/ul/li[4]/a/span[3]/span[2]").text 
    named_tuple = time.localtime() 
    time_string = time.strftime("%m/%d/%Y \n %H:%M:%S", named_tuple)

    a="-"

    if ydChange.find(a) != -1:
        dIcon = "↓"
    else:
        dIcon = "↑"     
    if yeChange.find(a) != -1:
        eIcon = "↓"
    else:
        eIcon = "↑" 
    if yaChange.find(a) != -1:
        aIcon = "↓"
    else:
        aIcon = "↑"
    table = [['  DOLAR', '  EURO', '  ALTIN',"   TARİH"], [f"  {dolar} TL\n{dIcon} {dChange1}", f"  {euro} TL\n{eIcon} {eChange1}", f"  {altin} TL\n{aIcon} {aChange1}",time_string]]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))