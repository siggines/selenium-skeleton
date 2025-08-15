from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import tempfile
import shutil
import time
import os
import requests
import sys
invalid_chars = '/\\:*?"<>|'

service = Service('./geckodriver')

user_prof = open("firefox_profile.txt").read()
if user_prof == "":
    print("hint: Go to about:profiles in firefox.")
    print("example where fgybejjt is the profile ID: fgybejjt.default")
    user_prof = input("Enter your firefox non-release profile ID:\n").strip()
    open("firefox_profile.txt", "w").write(str(user_prof))
else:
    print(f"Running on profile: {user_prof}")
if os.name == "nt":
    path = os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
    profile_path=path/{user_prof}.default
    cache = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'selenium_firefox_cache')
elif os.name == "posix":
    profile_path=os.path.expanduser(f"~/.mozilla/firefox/{user_prof}.default")
    cache = os.path.expanduser('~/.cache/selenium_firefox_cache')
if os.path.exists(cache):
    shutil.rmtree(cache)
    os.makedirs(cache, exist_ok=True)
else:
    os.makedirs(cache, exist_ok=True)

profile = FirefoxProfile(profile_path)
options = Options()
options.profile = profile
profile.set_preference("browser.cache.disk.enable", True)
profile.set_preference("browser.cache.disk.parent_directory", cache)
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(10)

MAIN_URL = "https://google.com"
driver.get(MAIN_URL)
time.sleep(1)

#
#
#

driver.quit()
shutil.rmtree(cache)
sys.exit()
