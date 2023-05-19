from selenium import webdriver

# initialize the Chrome webdriver
driver = webdriver.Chrome()

# navigate to the webpage
driver.get("https://www.thehindu.com/elections/karnataka-assembly/bjp-releases-first-list-of-189-candidates-for-karnataka-assembly-elections/article66726191.ece")

# take a screenshot and save it to a file
driver.save_screenshot("screenshot.png")

# close the webdriver
driver.quit()