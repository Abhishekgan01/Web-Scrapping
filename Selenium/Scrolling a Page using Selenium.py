from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/abhis/OneDrive/Desktop/Selenium/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?sca_esv=1c9111ab037be726&rlz=1C1CHBF_enIN1019IN1019&sxsrf=ADLYWILwl1_XedaA-1gZpZpQKCXxjiGFWw:1723743758598&q=dhoni&udm=2&fbs=AEQNm0AMrUEM0u25RSHSP2GXBv1FqRTJXslv5T9cWPShXuZK-unDRtidhDD6MO07O664cf3rzCkRGzT6TOmIkWN6z59BEI_sG_WvMHTpzIDOeN0PG5PbQE-fUxh_CRmIjIVTMPZLqRLt8LEJmd-JeyXMTy_SsVO4Ripm82z6vpZhP9tO4TJ_Xc2C9SbcBfqKU5SUBcd-NfHrlEA0NtWnPbhLSCHG8iDz0g&sa=X&ved=2ahUKEwjk4qjzxfeHAxXw-jgGHb-4DLkQtKgLegQIDhAB&biw=1536&bih=695&dpr=1.25")


height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")