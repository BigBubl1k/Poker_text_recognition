import pyautogui
from time import sleep
print(pyautogui.position())
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
#235  515

#открываем браузер и ссылку на юпитер ноутбук, копируем оттуда полученные данные
pyautogui.hotkey('Win')

pyautogui.typewrite('google chrome')
pyautogui.typewrite(['enter'])
pyautogui.typewrite('https://colab.research.google.com/drive/1uHoqEZejv53gtKR-0AFVmRnSZZvUcQcD?usp=sharing')
pyautogui.typewrite(['enter'])
sleep(7.5)
pyautogui.moveTo(400,400,1)
pyautogui.scroll(-8000,600,600)
pyautogui.moveTo(219,490, 1)
pyautogui.dragTo(100,347,1, button='left')
pyautogui.hotkey('ctrl', 'c')
#Открываем word и вставляем в него данные
pyautogui.hotkey('Win')
pyautogui.typewrite('word')
pyautogui.typewrite(['enter'])
sleep(4)
pyautogui.moveTo(759,250, 1)
pyautogui.click()
sleep(3)
pyautogui.hotkey('ctrl', 'v')
pyautogui.moveTo(28,14,1)
pyautogui.click()
#сохраняем word
pyautogui.moveTo(247,325,1)
pyautogui.click()
sleep(2)
pyautogui.typewrite('data from screenshot')
pyautogui.typewrite(['enter'])



   #pyautogui.click(194,50,duration = 0.5)





