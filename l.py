from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(3)

driver.get("https://youtube.com/shorts/n5C5iR_uZXM?feature=share") #replace with your required youtube shorts link

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[1]/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#2 account click 

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

#3 account click 

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer/tp-yt-paper-icon-item/div').click()

#4th account click 

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt 

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

#5th account click 

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer/tp-yt-paper-icon-item/div').click()

#6th account click

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

#7th account click

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

#8th account click

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

#9th account click

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click()

#10th account click

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)
#click on id
driver.find_element_by_id("avatar-btn").click()

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_class_name("yt-spec-button-shape-with-label ").click() #like button

time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()

time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(3)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click()

time.sleep(10)




