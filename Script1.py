from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

class test():

    driver = webdriver.Chrome(executable_path=r"C:/Users/Deeksha/Selenium/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()


    driver.get("https://www.flipkart.com/")
    print(driver.title)
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()


    action = ActionChains(driver)
    hover = driver.find_element_by_class_name("_3Ep39l")
    action.move_to_element(hover).perform()

#//button[@class='_2AkmmA _29YdH8']
#driver.find_element_by_class_name("_3Ep39l").click()
    driver.find_element_by_class_name("_1Q5BxB").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys("7842984606")
    driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("IamNmbr1#")
    driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c' and .//span[contains(., 'Login')]]").click()
    time.sleep(5)
    element = driver.find_element_by_xpath("//div[@class='_3buEbR' and text()='Hello']")
    print(element.is_displayed())

    try:
        hover1 = driver.find_element_by_xpath("//div[@class='_1jA3uo']")
        action.move_to_element(hover1).perform()
    except:
        pass

    logout = driver.find_element_by_xpath("//div[@class='_3NNJZh row']/span[text()='Logout']")
    logout.click()

    driver.close()
    driver.quit()
    print("Test Done")



