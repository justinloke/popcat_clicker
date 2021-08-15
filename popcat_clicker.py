# import library
from selenium import webdriver
import time

# connect to Chrome driver and popcat.click website
driver = webdriver.Chrome()
driver.get("https://popcat.click/")


# automate the clicking
# kindly set total_pops to the no. of pops desired

total_pops = 1000
no_of_pops = 0

while no_of_pops < total_pops:
    driver.find_element_by_tag_name("div").click()
    no_of_pops += 1
    
    if no_of_pops%10 == 0:
        time.sleep(1)
    
    else:
        pass
    
else:
    print("Popping end")