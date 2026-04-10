from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# ====== CẤU HÌNH PROFILE ======
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\huy20\AppData\Local\Google\Chrome\User Data\Profile 1")
chrome_options.add_argument(r"--profile-directory=Default")  # đổi nếu cần

# ====== DANH SÁCH WEBSITE ======
urls = [
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://mail.google.com"
]đ

drivers = []

for url in urls:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get(url)
    drivers.append(driver)

time.sleep(5)

# ====== TỰ ĐỘNG CLICK VIDEO YOUTUBE ======
try:
    yt_driver = drivers[0]
    video = yt_driver.find_element(By.ID, "video-title")
    video.click()
except:
    print("Không tìm thấy video")

input("Nhấn Enter để đóng...")

for driver in drivers:
    driver.quit()