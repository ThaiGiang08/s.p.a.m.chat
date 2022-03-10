import pyautogui, pyperclip, random, time
print("Tool Spam by Thai Giang")
msg = input("Nhap noi dung spam:"). split(" || ")
n = int(input("Nhap so lan delay:"))
m = float(input ("Nhap thoi gian delay:"))

print ("Chuan bi")
for i in range(5,0, 1):
	print(i,end = "...",flush ='True')
print("Bat dau")

for i in range(n):
	pyperclip.copy(random.choice(msg))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(m)