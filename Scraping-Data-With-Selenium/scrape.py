from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

    
#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('chromedriver.exe',desired_capabilities=dcap,service_args=service_args)

#access website
driver.get('https://www.tripadvisor.com/')

#find and click login icon
icon=driver.find_element_by_xpath('//*[@id="taplc_global_nav_action_profile_0"]/div/a[1]/span')
icon.click()

#find and switch to the popup frame
popup=driver.find_element_by_id('overlayRegFrame')
driver.switch_to.frame(popup)

#find and fill the email box
email=driver.find_element_by_id('regSignIn.email')
email.send_keys('emanueldiaz67@mail.com')

#find and fill the password box
pswd=driver.find_element_by_id('regSignIn.password')
pswd.send_keys('as8df79hkjA')

#find and click the login button
button=driver.find_element_by_xpath('//*[@id="regSignIn"]/div[3]')
button.click()

#find and click the Restaurants button
try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'global-nav-restaurants')))
except TimeoutException:
    print ("Loading took too much time!")

el=driver.find_element_by_id('global-nav-restaurants')
el.click()

#find and fill the search box
searchBox=driver.find_element_by_class_name('typeahead_input')
searchBox.send_keys('Hoboken')

#find and click the search button
button=driver.find_element_by_id('SUBMIT_RESTAURANTS')
button.click()

#wait until the page loads
try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'property_title')))
except TimeoutException:
    print ("Loading took too much time!")

#find all the restaurants in the first page and print their names
els=driver.find_elements_by_class_name('property_title')
for el in els:
    print (el.text)


