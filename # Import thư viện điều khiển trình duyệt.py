# Import thư viện điều khiển trình duyệt (Chrome)
from selenium import webdriver

# Import cấu hình cho Chrome (chạy ẩn, full màn hình, v.v.)
from selenium.webdriver.chrome.options import Options

# Import cách tìm phần tử HTML (theo tag, id, class...)
from selenium.webdriver.common.by import By
import threading
# Import thư viện xử lý thời gian (delay, sleep)
import time


# URL trang web chứa video bạn muốn test
URL = "https://www.youtube.com/"


# Khởi tạo cấu hình cho Chrome
options = Options()

# Mở trình duyệt ở chế độ full màn hình
options.add_argument("--start-maximized")


# Khởi tạo trình duyệt Chrome với cấu hình ở trên
driver = webdriver.Chrome(options=options)


try:
    # Mở trang web
    driver.get(URL)

    # Chờ 5 giây để trang load xong (video + JS)
    time.sleep(5)

    # Tìm tất cả thẻ <video> trong trang
    videos = driver.find_elements(By.TAG_NAME, "video")

    # Nếu không tìm thấy video nào
    if not videos:
        print("Khong tim thay the video")

    else:
        # Lấy video đầu tiên trong danh sách
        video = videos[0]

        # Dùng JavaScript để bấm play video
        driver.execute_script("arguments[0].play();", video)

        # Chờ 10 giây để video chạy
        time.sleep(10)


# Dù có lỗi hay không vẫn đóng trình duyệt
finally:
    driver.quit()