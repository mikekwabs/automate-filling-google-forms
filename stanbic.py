from selenium import webdriver
import time

#Set webdriver path
driver = webdriver.Chrome('chromedriver.exe')

#Information about me
gmail = "mkoranteng007@st.ug.edu.gh"
gmail_password = 'abigispyworld5'
name = "Michael Koranteng"
schoolOfCompletion = "Presbyterian Senior High School, Osu"
address = 'Sowutuom,Accra'
phoneNumber = "0506691160"
comments = "I'm very excited to participate in this!"

#Website to fill forms
driver.get(
    'https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/edit'
)

#Set timer to 1 second so we can see the changes
time.sleep(1)

#Access the sign in prompt
sign_in_xpath = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
sign_in_xpath.click()

#Gmail Login
email_id = driver.find_element_by_id('identifierId').send_keys(gmail)
nextbutton_id = driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(60)
password = driver.find_element_by_name('password').send_keys(gmail_password)
passwordNextId = driver.find_element_by_id('passwordNext').click()

#details of form

name_xpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
)
time.sleep(1)
name_xpath.send_keys(name)

radio_gender_id = driver.find_element_by_id('i9').click()

email_id = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
)
email_id.send_keys(gmail)

submitButtonXpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
submitButtonXpath.click()

#Contact Information
school_xpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
)
time.sleep(1)
school_xpath.send_keys(schoolOfCompletion)

address_xpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'
)
address_xpath.send_keys(address)

phoneNumber_xpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
)
phoneNumber_xpath.send_keys(phoneNumber)

comments_xpath = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea'
)
comments_xpath.send_keys(comments)

finalSubmitButton = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()
