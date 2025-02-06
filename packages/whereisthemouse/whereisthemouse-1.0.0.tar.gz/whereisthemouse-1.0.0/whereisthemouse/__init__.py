import pyautogui
import time
import pyperclip
import keyboard
def start():
    state = 0
    while True:
        if state==0:
            x,y=pyautogui.position()
            color=pyautogui.pixel(x,y)
            print(f"\r"+" "*100,end='')
            print(f"\r(x,y)=({x},{y}),color={color},(按alt複製位置)",end='')
            if keyboard.is_pressed("alt"):
                pyperclip.copy(f"{x},{y}")
                print(f"\r(x,y)=({x},{y}),color={color}\n位置已複製至剪貼簿....\n按1：繼續\n按2：複製顏色{color}並結束\n按3：複製{x},{y},color={color}並結束\n按4：結束",
                      end='')
                state=1
                time.sleep(1)
        else:
            if keyboard.is_pressed("1"):
                state = 0
                time.sleep(1)
            if keyboard.is_pressed("2"):
                pyperclip.copy(f"{color}");break
            if keyboard.is_pressed("3"):
                pyperclip.copy(f"{x},{y},color={color}");break
            if keyboard.is_pressed("4"):break
        time.sleep(0.01)



