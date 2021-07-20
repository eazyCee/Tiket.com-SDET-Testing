from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
#Open tiket.com
driver.get('https://www.tiket.com/')
#Open tiket.com

#Search for tickets from Jakarta to Kuala Lumpur
origin = driver.find_element_by_id("productSearchFrom")
origin.clear()
origin.location_once_scrolled_into_view
origin.send_keys("Jakarta")
origin.send_keys(Keys.RETURN)
destination = driver.find_element_by_id("productSearchTo")
destination.clear()
destination.send_keys("Kuala Lumpur")
time.sleep(2)
destination.send_keys(Keys.RETURN)

time.sleep(2)
dateStart = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[4]/div/span")
dateStart.location_once_scrolled_into_view
dateStart.click()

dateEnd = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[7]/div/span")
dateEnd.location_once_scrolled_into_view
dateEnd.click()

passenger = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[3]/div[2]/div/div/div[3]/div/span")
passenger.location_once_scrolled_into_view
passenger.click()
time.sleep(2)

searchBtn = driver.find_element_by_class_name("product-form-search-btn")
searchBtn.click()

info = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]")
info.click()
#Search for tickets from Jakarta to Kuala Lumpur

#Select return flights
time.sleep(5)
flight = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div")
flight.click()

time.sleep(5)
returnFlight = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div")
returnFlight.click()
#Select return flights

# Testing Input Buyer Data
time.sleep(10)
title = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/input")
title.click()

time.sleep(1)
tuan = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[3]/ul/li[1]")
tuan.click()

name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/input")
name.send_keys("Cliff")

email = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div/input")
email.send_keys("clifftangel@gmail.com")

phone = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[3]/div[2]/div/input")
phone.send_keys("89689024886")
#Testing Input Buyer Data

#Testing Input Passenger Data
title2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input")
title2.location_once_scrolled_into_view
title2.click()

time.sleep(2)
tuan2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[3]/ul/li[1]")
tuan2.click()

namePassenger = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/input")
namePassenger.send_keys("Cliff")

lastNamePassenger = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/input")
lastNamePassenger.send_keys("Tangel")

nat = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/input")
nat.click()

indo = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[3]/div[2]/ul/li[1]")
indo.click()

birthDate = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div[1]")
birthDate.location_once_scrolled_into_view
birthDate.click()
time.sleep(2)
birthDateInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div[1]/div[1]/div/div[3]/ul/li[1]")
birthDateInput.click()
time.sleep(2)
birthMonthInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[6]/div")
birthMonthInput.location_once_scrolled_into_view
birthMonthInput.click()
time.sleep(2)
birthYearInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div[1]/div[5]/div/div[3]/ul/li[10]/div")
birthYearInput.location_once_scrolled_into_view
birthYearInput.click()

passportNum = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div/input")
passportNum.location_once_scrolled_into_view
passportNum.send_keys("A1234567")

yearIssued = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div/div[1]")
yearIssued.click()
time.sleep(2)
dayIssued = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div/div[1]/div[1]/div/div[3]/ul/li[2]/div")
dayIssued.click()
time.sleep(2)
monthIssued = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[1]")
monthIssued.click()
time.sleep(2)
yearIssued = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div/div[1]/div[5]/div/div[3]/ul/li[2]")
yearIssued.click()

issuingCountry = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div/div")
issuingCountry.click()

indoClick = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div/div/div[3]/div[2]/ul/li[1]")
indoClick.click()

expiryDate = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[2]/div/div[1]")
expiryDate.click()
time.sleep(2)
expiryDay = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[2]/div/div[1]/div[1]/div/div[3]/ul/li[2]/div")
expiryDay.click()
time.sleep(2)
expiryMonth = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[1]/div")
expiryMonth.click()
time.sleep(2)
expiryYear = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[2]/div/div[1]/div[5]/div/div[3]/ul/li[4]/div")
expiryYear.click()
#Testing Input Passenger Data

pay = driver.find_element_by_css_selector(".v3-btn")
pay.location_once_scrolled_into_view
pay.click()

confirm= driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[3]/div/div/div/div/div[3]/button[2]")
confirm.click()

print("Test complete!")