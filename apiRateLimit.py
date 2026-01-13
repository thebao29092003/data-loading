import requests
import time

# 2 đường link này đều thuộc hệ thống GitHub REST API,
# được sử dụng để tương tác với dữ liệu trên GitHub bằng mã lệnh (thay vì dùng giao diện web)

# Ngữ cảnh: Link này cực kỳ phổ biến trong khóa học Data Engineering Zoomcamp.[2][9] Học viên thường dùng nó như một nguồn dữ liệu (data source)
url = "https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp/events"
# response = requests.get(url)
# print(response.json())

# Đây là trang kiểm tra hạn ngạch (giới hạn) yêu cầu của bạn. GitHub quy định mỗi người dùng/IP chỉ được phép gọi API một số lần nhất định trong 1 giờ để tránh làm quá tải hệ thống.
url2 = "https://api.github.com/rate_limit"
remaining = requests.get(url2).json()['rate']['remaining']

if remaining == 0:
    time.sleep(30)