from selenium import webdriver
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument('--headless')
browser = webdriver.Chrome(r'E:\Downloads\Compressed\chromedriver_win32\\chromedriver.exe',options=None)
#browser.maximize_window()

'''i=40
while True:
    browser.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSeDdDvMEXFezI0RjJdfcPafnJiN1EmMYdALdS0sWIHsJV3iUQ/viewform?c=0&w=1')
    elem = browser.find_element_by_css_selector(f'#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(1) > div:nth-child(2) > div > content > div > label:nth-child({random.randrange(1,6)})')
    elem.click()
    elem = browser.find_element_by_css_selector(f'#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child({random.randrange(1,4)})')
    elem.click()
    elem = browser.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div.quantumWizTextinputPapertextareaEl.modeLight.freebirdFormviewerViewItemsTextLongText.freebirdThemedInput > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
    elem.send_keys('Internet connection should be much more consistent.')
    elem = browser.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div.quantumWizTextinputPapertextareaEl.modeLight.freebirdFormviewerViewItemsTextLongText.freebirdThemedInput > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
    elem.send_keys('Ethernet Cable should be provided to each room in the hostel and the placement rooms.')
    elem = browser.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div')
    elem.click()
    i+=1
    print(i)'''

i=j=30
while True:
    browser.get('http://stulish.com/tripti000')
    j+=1
    try:
        elem = browser.find_element_by_id('Text')
    except:
        continue
    greet = ['Hi','Hello','Hey']
    name = ['beautiful','girl']
    litter = ['I just want you to know that I care for you very much.', 'Can you guess who I am?',
              'The world is pretty dark.', 'You are doing a really great job.',
              'You are the most Beautiful girl.', 'I dont know what to tell you.', 'You have a bright future',
              'Ato makeup keno koro?',
              'Which dance you like the most ?', 'What do you choose: love marriage or arranged.',
              'Where are you staying in Saraswati Puja?', 'Do you have a boyfriend?',
              'star jolsha or zee bangla?', 'Live a healthy life.','See you soon.']
    animal = ['Bandor', 'Chagol', 'Goru', 'Gadha','ujbuk','bebun']

    text = random.choice(greet) + ' ' + random.choice(name) + ', ' + ' '.join(
        e for e in random.sample(litter, 5)) + Keys.ENTER + '          Your account has been hacked...("_")     I dare you to post this on facebook.'

    elem.send_keys(text)
    elem = browser.find_element_by_css_selector('#Container > form > div > div:nth-child(2) > button')
    elem.click()
    try:
        browser.switch_to_alert().accept()
    except:
        continue
    i+=1
    print(i)
    #browser.switch_to.alert().accept()