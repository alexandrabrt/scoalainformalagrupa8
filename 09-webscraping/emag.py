from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

# find_element = browser.find_element(by=By.ID, value="card_grid")
# print(find_element.text.split('\n'))
# for i in range(1, 62):
#     find_element = browser.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]')
#     print(find_element.text)
#     print('++++++++++++++++++++++++++++++++++++')
# //*[@id="card_grid"]/div[62]
find_element = browser.find_elements(by=By.XPATH, value='//div[contains(@id,"card_grid")]//a[contains(@class,"card-v2-title")]')
print(find_element)
# for i in find_element:
#     print(i.get_attribute(''))
# //div[contains(@id,"card_grid")]//a[contains(@class,"card-v2-title")]
# //*[@id="card_grid"]/div[63]

