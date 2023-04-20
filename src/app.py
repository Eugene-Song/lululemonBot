import time
from bs4 import BeautifulSoup
import pyautogui
import pytesseract
import cv2
import webbrowser

# Replace these with your own credentials and target URL
product_url = "https://shop.lululemon.com/p/women-pants/Softstreme-HR-Pant/_/prod11020340?color=31382&sz=0&tasid=WiYzSApHiR&taterm=soft"
cvv = "123"

def check_stock_status():
    time.sleep(8)
    pyautogui.scroll(-8)
    time.sleep(1)

    location = pyautogui.locateCenterOnScreen("resource/addbag2.png")
    if location == None:
        print("Item perhaps not available...")
        location2 = pyautogui.locateCenterOnScreen("resource/outstock.png")
        if location2 != None:
            print("Item indeed unavailable!!!")
            return False
        return False
    return True

# def findDesiredProduct():
#     time.sleep(5)
#     print("found")
#     text_to_find = "/resource/size0.png"
#     location = pyautogui.locateOnScreen(text_to_find, screenshot)
#     pyautogui.click(location)
    
def add_bag():
    time.sleep(4)
    print("Trying to add to bag...")
    # Find the text "Add to Bag"
    text_to_find = "resource/addbag2.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    print("clicked")

def viewBagAndCheckout():
    time.sleep(4)
    print("Trying to view bag and checkout...")
    # Find the text "Add to Bag"
    text_to_find = "resource/viewbagcheck.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    print("clicked")

def checkout():
    time.sleep(4)
    print("Trying to checkout...")
    # Find the text "Add to Bag"
    text_to_find = "resource/checkout.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    print("clicked")
    
def nextStep():
    time.sleep(4)
    pyautogui.scroll(-600)
    time.sleep(1)

    print("Trying to go to next step...")
    # Find the text "Add to Bag"
    text_to_find = "resource/nextstep.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    print("clicked")

def reviewOrder():
    time.sleep(4)
    pyautogui.scroll(-600)
    time.sleep(1)

    print("Trying to go to next step...")
    # Find the text "Add to Bag"
    text_to_find = "resource/securitycode.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    pyautogui.write(cvv)
    
    text_to_find2 = "resource/revieworder.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find2, confidence=0.7)
    pyautogui.click(x/2, y/2, clicks=3, duration=0.5)
    print("clicked")

def placeOrder():
    time.sleep(4)
    pyautogui.scroll(-2)
    print("Trying to place order...")
    text_to_find2 = "resource/placeorder.png"
    x,y = pyautogui.locateCenterOnScreen(text_to_find2, confidence=0.7)
    print("clicked")

def purchase_item():
    add_bag()
    viewBagAndCheckout()
    checkout()
    nextStep()
    reviewOrder()
    # placeOrder()

try:
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # webbrowser.get(chrome_path).open_new_tab(product_url)
    webbrowser.open_new_tab(product_url)

    while True:
        in_stock = check_stock_status()
        if in_stock:
            print("Item in stock, proceeding to purchase...")
            purchase_item()
            print("addbag complete!")            
            break
        else:
            print("Item not in stock, waiting for 30 minutes before checking again...")
            time.sleep(3)  # Wait for 30 minutes before checking again
            pyautogui.hotkey('command', 'w')
            webbrowser.open_new_tab(product_url)

            # webbrowser.get(chrome_path).open_new_tab(product_url)

            

finally:
    print("Script terminated.")
