from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get("https://www.thesparksfoundationsingapore.org")
print(driver.title)

# Checking Logo (1)
search= driver.find_elements_by_class_name("navbar-brand")
if search:
    print("Logo is present")
else:
    print("Logo is not present")

# Checking if Youtube video is playing (2)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
play=driver.find_element_by_xpath("//button[@aria-label='Play']")
play.click()
state=driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
if (state!=-1):
    print("Player state:", state,"Video sucessfully playing")
time.sleep(5)
pause=driver.find_element_by_class_name("video-stream")
pause.click()
time.sleep(4)
driver.switch_to.parent_frame()

# Clicking on About Us
nav=driver.find_elements_by_class_name("dropdown-toggle")
nav[0].click()
time.sleep(4)


# (Page 2) Checking if Expert Mentors has been updated (3)
nav_ele=driver.find_elements_by_xpath('//ul[@class="dropdown-menu"]//li/a')
try:
    for ele in nav_ele:
        eleval=ele.get_attribute("innerHTML")
        if (eleval=="Expert Mentors"):
            ele.click()
            info=driver.find_element_by_class_name("wthree_banner_info_grid")
            if("Page Not Yet Ready!" in info.text):
                print("Expert Mentors page not updated yet!")
except StaleElementReferenceException:
    if (ele not in nav_ele):
        raise 
time.sleep(4)

# Clicking on Policies and Code
nav=driver.find_elements_by_class_name("dropdown-toggle")
nav[1].click()
time.sleep(4)

# Page 3 Checking if navbar is present on Policies Page (4)
nav_ele=driver.find_elements_by_xpath('//ul[@class="dropdown-menu"]//li/a')
try:
    for ele in nav_ele:
        eleval=ele.get_attribute("innerHTML")
        if (eleval=="Policies"):
           

            ele.click()
            navbar= driver.find_element_by_class_name("nav")
            if navbar:
                print("Navbar is present on Policies page")
            else:
                print("Navbar is not present on Policies page")

except StaleElementReferenceException:
    if (ele not in nav_ele):
        raise 

# Checking if copyright claim is present (5)
time.sleep(4)
driver.execute_script("window.scrollTo(0, 2500)") #Scrolling to bottom of page
time.sleep(2)
copy=driver.find_element_by_class_name("copyright-wthree")
if copy:
    print("Copy-right is present")
else:
    print("It is not present")

# Checking if back to top button works (6)
totop=driver.find_element_by_id("toTopHover")
totop.click()
time.sleep(4)
if (driver.execute_script("return window.pageYOffset"))==0:
    print("At the start of page; Back to top works!")
else:
    print("Not at the start of page; Back to top doesn't work!")
time.sleep(4)

# Clicking on Programs
nav=driver.find_elements_by_class_name("dropdown-toggle")
nav[2].click()
time.sleep(4)

# Page 4 Checking for quote in Student mentorship (7)
nav_ele=driver.find_elements_by_xpath('//ul[@class="dropdown-menu"]//li/a')
try:
    for ele in nav_ele:
        eleval=ele.get_attribute("innerHTML")
        if (eleval=="Student Mentorship Program"):
           

            ele.click()
            navbar= driver.find_element_by_class_name("para-w3-agile")
            if navbar:
                print("Quote is present on Student Mentorship page")
            else:
                print("Quote is not present on Student Mentorship page")

except StaleElementReferenceException:
    if (ele not in nav_ele):
        raise 
time.sleep(4)

# Checking if Student SOS button works (8)
sos=driver.find_elements_by_class_name("button-w3layouts")
sos[2].click()
if(driver.find_element_by_class_name("inner-tittle-w3layouts").text=="Student SOS Program"):
    print("You are on the Student SOS Program Page")
else:
    print("The Student SOS button is broken :(")
time.sleep(4)


# Page 5 Checking for address in Contact Us (9)
contact=driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a')
contact.click()
add= driver.find_element_by_class_name("agilew3_contact")
if add:
    print("Address is present")
else:
    print("Address is not present")

time.sleep(4)

# Checking if "The Sparks Foundation leads to home page" (10)
driver.execute_script("window.scrollTo(0, 2500)")
print('Clicking on "The Sparks Foundation"')
time.sleep(4)
home=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/h6/a")
home.click()
if (driver.current_url=="https://www.thesparksfoundationsingapore.org/"):
    print ("Back to the homepage!")
else:
    print("Nope!")