import time
import datetime
from selenium import webdriver as wd
from selenium.webdriver.common.by import By


# Opens Chrome and goes to the UO Knight Library Group Study Room Reservation page
wd = wd.Chrome()
wd.implicitly_wait(10)
wd.get("https://uoregon.libcal.com/reserve/knightgroupstudy")

# Clicks an Open rooms and Time button
def get_exact_date():
        date = datetime.datetime.now()
        time = str(date)

        weekday = date.weekday()
        if weekday == 0:
                weekday = "Monday"
        elif weekday == 1:
                weekday = "Tuesday"
        elif weekday == 2:
                weekday = "Wednesday"
        elif weekday == 3:
                weekday = "Thursday"
        elif weekday == 4:
                weekday = "Friday"
        elif weekday == 5:
                weekday = "Saturday"
        elif weekday == 6:
                weekday = "Sunday"

        year = time[0:4]

        month = str(time[5:7])
        if month == "01":
                month = "January"
        elif month == "02":
                month = "February"
        elif month == "03":
                month = "March"
        elif month == "04":
                month = "April"
        elif month == "05":
                month = "May"
        elif month == "06":
                month = "June"
        elif month == "07":
                month = "July"
        elif month == "08":
                month = "August"
        elif month == "09":
                month = "September"
        elif month == "10":  
                month = "October"
        elif month == "11":
                month = "November"
        elif month == "12":
                month = "December"

        day = int(time[8:10])
        hour = int(time[11:13])
        am_pm = "am"
        if hour > 12:
                hour = hour - 12
                hour = str(hour)
                hour = hour
                am_pm = "pm"
        else:
                hour = str(hour)
                hour = hour
        minute = int(time[14:16])
        if minute >= 30:
                minute = "00"
                hour = int(hour)+1
        else:
                minute = "30"
        return str(f"{hour}:{minute}{am_pm} {weekday}, {month} {day}, {year} - Knight 219 - Available")

open_rooms = wd.find_element(By.XPATH, f"//a[@title='{get_exact_date()}']")
open_rooms.click()

#Clicks the Submit button
submit = wd.find_element(By.XPATH, "//button[@id='submit_times']")
submit.click()

#Clicks the Continue button
continue_button = wd.find_element(By.XPATH, "//button[@id='terms_accept']")
continue_button.click()

#Fills out the form
name = wd.find_element(By.XPATH, "//input[@id='fname']")
name.send_keys("Paul")
name = wd.find_element(By.XPATH, "//input[@id='lname']")
name.send_keys("Selhorst")
email = wd.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("selhorst@uoregon.edu")
event_title = wd.find_element(By.XPATH, "//input[@id='nick']")
event_title.send_keys("Study Group, Math/CS/GLBL/WR")

#Clicks the Submit my Booking button
submit_booking = wd.find_element(By.XPATH, "//button[@id='btn-form-submit']")
submit_booking.click()

time.sleep(10)

