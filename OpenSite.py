import pyautogui, time, webbrowser

#PyAutoGUI Settings
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print('Press Ctrl-C to quit.')

#Open URL in Default Browser
URL='http://www.google.com'
webbrowser.open(URL, new=1, autoraise='true')

#Open multiple URL in Default Browser
#URLlist=[
#    'http://cnn.com',
#    'http://money.cnn.com',
#    'http://marketwatch.com',
#    'http://www.google.com/search?q=mexico&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiXiq3DmcbtAhXgB50JHdZXAdUQ_AUoAXoECBMQAw&biw=1280&bih=881',
#    'http://www.google.com/search?source=hp&ei=q4rTX9egFMO0tAaH15eABw&q=dollar+peso&oq=dollar+peso&gs_lcp=CgZwc3ktYWIQAzILCAAQsQMQgwEQyQMyAggAMggIABCxAxCDATICCAAyAggAMgIIADICCAAyAggAMgIIADIECAAQCjoLCC4QsQMQxwEQowI6AgguOggILhDHARCjAjoOCC4QsQMQxwEQowIQkwI6DgguELEDEIMBEMcBEKMCOgUILhCxAzoICAAQsQMQyQM6BQgAEJIDOgUIABCxAzoOCC4QsQMQxwEQrwEQkwJQxU9YiVlgiVpoAnAAeACAAVWIAfQFkgECMTGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=psy-ab&ved=0ahUKEwiXorP1mcbtAhVDGs0KHYfrBXAQ4dUDCAk&uact=5',
#    'http://twitter.com/JohnLegere?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor',
#    'http://www.google.com/search?q=ergen&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiJia-smsbtAhUEWs0KHXmfDiMQ_AUoAXoECBIQAw&biw=1280&bih=881',
#    'http://www.google.com/search?biw=1280&bih=881&tbm=nws&ei=H4vTX9GAN9uztAaClpDABA&q=directv&oq=directv&gs_l=psy-ab.3..0i433k1j0j0i433k1l4j0l4.5518.6321.0.6432.7.6.0.1.1.0.82.409.6.6.0....0...1c.1.64.psy-ab..0.7.411...0i433i131k1j0i3k1.0.flCvvQTOyns',
#    'http://www.google.com',
#    ]
#for item in URLlist:
#    webbrowser.open(item, new=2, autoraise='true')

#get mouse position
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr)

#click mouse at position - main display
pyautogui.click(596,443)

#type in something in browser
pyautogui.typewrite('mexico')
pyautogui.typewrite('\n')




