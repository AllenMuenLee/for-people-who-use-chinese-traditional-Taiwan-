import pyautogui, time, subprocess, os
import win32con, win32gui, win32api
import ctypes

LID = {0x0404: "Chinese (Traditional) (Taiwan)"}
word = input("輸入忘記按shift的文字:")


open = subprocess.Popen("notepad.exe")
hwnd = 0
while(hwnd == 0):
	hwnd = win32gui.FindWindow(None, "Untitled - Notepad")
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, int(pyautogui.size()[0] / 2 - pyautogui.size()[0] / 10 * 3), int(pyautogui.size()[1] / 2 - pyautogui.size()[1] / 10 * 3), int(pyautogui.size()[0] / 10 * 6), int(pyautogui.size()[1] / 10 * 6),win32con.SWP_SHOWWINDOW)
pyautogui.moveTo(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)
pyautogui.click()

result = win32api.SendMessage(hwnd, win32con.WM_INPUTLANGCHANGEREQUEST, 0, 0x0404)

if result != 0:
	print("無法設定語言")
	quit()

time.sleep(0.1)
for i in word: 
	pyautogui.press(i)

print("輸入結束")

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

print("複製完成")

quit()