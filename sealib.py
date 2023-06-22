import time, random, pyautogui, rich, tkinter as tk, os, pyttsx3, platform, wget, webbrowser, sys
from tkinter import Tk

class SeaFun:
    """This class have random functions!"""
    def __init__(self):
        pass

    def RNDnumber(a:int = 10, b:int = 1000):
        """Print random number! (You can use a number from a function using a variable: randomnumber)"""
        global randomnumber
        randomnumber = random.randint(a, b)
        print(randomnumber)
        pass
    pass

class SeaDEV:
    """Developing Functions"""
    def __init__(self):
        pass

    def Say(text:str = 'Test'):
        """RECOGNIZE TEXT"""
        engine = pyttsx3.init()
        engine.say(text=text)
        engine.runAndWait()
        pass

    def SayToSave(filename:str = 'recognize.mp3', text:str = 'recognize test, Sealib super amazing library!'):
        """SAVE RECOGNIZE TEXT"""
        engine = pyttsx3.init()
        engine.save_to_file(text=text, filename=filename)
        engine.runAndWait()
        pass

    pass

class SeaRich:
    """Rich"""
    def __init__(self):
        pass
    pass

class SeaBrowser:
    """Browser Commands"""
    def __init__(self):
        pass

    def open(link:str):
        """Open Link in the WEB"""
        webbrowser.open(url=link)
        pass

    def search(question:str = 'Python'):
        """Search in the WEB"""
        # question = input('search: ')
        webbrowser.open(f'https://www.google.com/search?q={question}')
        pass

    def download(link:str):
        """Download File With Link"""
        wget.download(url=link)
        pass
    pass

class SeaOS:
    """System commands"""
    def __init__(self):
        pass
        
    def sleep(sec:float = 2):
        """Example: sleep(5), Stop code on 5 seconds!"""
        time.sleep(sec)
        pass

    def exit():
        """STOP CODE"""
        sys.exit()
        pass

    def System():
        """System info"""
        print(platform.system())
        print(platform.win32_ver())
        print(platform.processor())
        print(platform.machine())
        pass
    
    def cmd(command:str = 'start'):
        """cmd command"""
        os.system(command=command)
        pass
    pass

class SeaMacro:
    """Pyautogui"""
    def __init__(self):
        pass

    def click(button:str = 'left'):
        """Mouse click"""
        pyautogui.click(button=button)
        pass

    def write(text:str = 'Hello World!'):
        """Write text"""
        pyautogui.typewrite(message=text)
        pass

    def press(button:str = 'enter'):
        """Press key"""
        pyautogui.press(button)
        pass

    def hotkey(*args:str):
        """Hotkeying keys"""
        pyautogui.hotkey(args=args)
        pass

    pass

class SeaTkinter:
    """Easy Tkinter commands"""
    def __init__(self):
        pass



    def WINCreate(title:str, geometry:str = "400x330"):
        """Create window as Tkinter"""
        global win
        win = Tk()
        win.title(title)
        win.geometry(geometry)
        win.resizable(width=True, height=True)
        pass

    def WINLabel(text:str, bg:str, fg:str, justify:str):
        """pick Label on window"""
        global label
        label = tk.Label(win, justify=justify, text=text, bg=bg, fg=fg)
        pass

    def WINPackLabel():
        """Confirm Label on window"""
        label.pack()
        pass

    def example1():
        """EXAMPLE"""
        win.title('EXAMPLE')
        win.config(bg='white')
        win.geometry('400x400')
        win.resizable(width=True, height=True)
        label = tk.Label(win, justify='center', text='Example', bg='White', fg='Black')
        label.pack()
        win.mainloop()
        pass

    def mainloop():
        """Open window and start LOOP"""
        win.mainloop()
        pass
    pass

if __name__ == '__main__':
    print('This is library!')
    SeaOS.exit()
else: print('Sealib Imported!')