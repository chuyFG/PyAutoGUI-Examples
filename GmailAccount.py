import pyautogui, time, webbrowser

#PyAutoGUI Settings
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print('Press Ctrl-C to quit.')

#Open URL in Default Browser
URL='http://www.gmail.com'
webbrowser.open(URL, new=1, autoraise='true')
time.sleep(1)

#Open multiple URL in Default Browser
##URLlist=[
##    'http://cnn.com',
##    'http://money.cnn.com',
##    'http://marketwatch.com',
##    'http://www.google.com/search?q=mexico&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiXiq3DmcbtAhXgB50JHdZXAdUQ_AUoAXoECBMQAw&biw=1280&bih=881',
##    'http://www.google.com/search?source=hp&ei=q4rTX9egFMO0tAaH15eABw&q=dollar+peso&oq=dollar+peso&gs_lcp=CgZwc3ktYWIQAzILCAAQsQMQgwEQyQMyAggAMggIABCxAxCDATICCAAyAggAMgIIADICCAAyAggAMgIIADIECAAQCjoLCC4QsQMQxwEQowI6AgguOggILhDHARCjAjoOCC4QsQMQxwEQowIQkwI6DgguELEDEIMBEMcBEKMCOgUILhCxAzoICAAQsQMQyQM6BQgAEJIDOgUIABCxAzoOCC4QsQMQxwEQrwEQkwJQxU9YiVlgiVpoAnAAeACAAVWIAfQFkgECMTGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=psy-ab&ved=0ahUKEwiXorP1mcbtAhVDGs0KHYfrBXAQ4dUDCAk&uact=5',
##    'http://twitter.com/JohnLegere?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor',
##    'http://www.google.com/search?q=ergen&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiJia-smsbtAhUEWs0KHXmfDiMQ_AUoAXoECBIQAw&biw=1280&bih=881',
##    'http://www.google.com/search?biw=1280&bih=881&tbm=nws&ei=H4vTX9GAN9uztAaClpDABA&q=directv&oq=directv&gs_l=psy-ab.3..0i433k1j0j0i433k1l4j0l4.5518.6321.0.6432.7.6.0.1.1.0.82.409.6.6.0....0...1c.1.64.psy-ab..0.7.411...0i433i131k1j0i3k1.0.flCvvQTOyns',
##    'http://www.google.com',
##    ]
##for item in URLlist:
##    webbrowser.open(item, new=2, autoraise='true')

#get mouse position
#x, y = pyautogui.position()
#positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#print(positionStr)

#click mouse at position - main display - sign in with diff account
pyautogui.click(788,258, button='left')
time.sleep(1)

#get mouse position
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr)

#click mouse at position - main display - different account
pyautogui.click(788,700, button='left')
time.sleep(1)

#click mouse at position - main display - create account
pyautogui.click(688,700, button='left')
time.sleep(1)

#click mouse at position - main display - for myself
pyautogui.click(688,750, button='left')
time.sleep(1)

#FirstName, LastName, Username, Password
Account=[{'FirstName':'DishHW','LastName':'Test','Username':'DishHWtest02','Password':'text','Password2':'text'}]
#print(Account[0]['FirstName'])
#print(Account[0]['LastName'])
#print(Account[0]['Username'])
#print(Account[0]['Password'])

#Type in FirstName
pyautogui.typewrite(Account[0]['FirstName'] + '\t')
time.sleep(1)

#Type in LastName
pyautogui.typewrite(Account[0]['LastName'] + '\t')
time.sleep(1)

#Type in Username
pyautogui.typewrite(Account[0]['Username'] + '\t')
time.sleep(1)

#Type in extra Tab
pyautogui.typewrite('\t')
time.sleep(1)

#Type in Password
pyautogui.typewrite(Account[0]['Password'] + '\t')
time.sleep(1)

#Type in Password Confirm
pyautogui.typewrite(Account[0]['Password2'] + '\t')
time.sleep(1)

#Type in Space - checkbox
pyautogui.press('space')
time.sleep(1)

#Type in tab-tab-enter
pyautogui.typewrite('\t'+'\t'+'\n')
time.sleep(1)
