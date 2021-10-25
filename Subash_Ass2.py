from selenium import webdriver
import time
import pandas as pd
import html5lib
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path=r"C:\DRIVERBIN\chromedriver.exe", options=options)

#driver = webdriver.Chrome()

driver.get("https://www.imdb.com/chart/top/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)

table = pd.read_html('https://www.imdb.com/chart/top/', match='Rank & Title')
df = table[0]
df1 = df[['Rank & Title']]
df2 = df1.rename(columns = {'Rank & Title':'Name Year'})
df2['Name Year'] =  df2['Name Year'].apply(lambda x: x.replace('(','').replace(')',''))
print(df2.head())