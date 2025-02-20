Nếu muốn clone về máy: git clone https://github.com/Duck095/XO.git

Di chuyển vào thư mục repository: cd XO

Lấy danh sách nhánh từ xa: git fetch

Kiểm tra nhánh hiện tại: git branch

Kiểm tra tất cả nhanh hiện tại có: git branch -r

chuyển sang nhánh cần làm việc: git checkout <tên_nhánh>


Lấy từng file từ nhánh A sang B
- đảm bảo rằng bạn đang ở nhánh B: git checkout B
- 
- Xem danh sách file trong nhánh A: git ls-tree -r origin/A --name-only
- 
- liệt kê các file có trong A nhưng không có trong B: git diff --name-only B origin/A

- lấy tất cả các file mới từ A mà không ảnh hưởng đến file đã có trong B: git checkout origin/A -- $(git diff --name-only B origin/A)
- Ví dụ: Giả sử:
B có: file1.txt, file2.txt
A có: file1.txt, file2.txt, file3.txt, file4.py
Sau khi chạy lệnh trên, bạn sẽ chỉ lấy file3.txt và file4.py, còn file1.txt và file2.txt vẫn giữ nguyên.

- Lấy từng file từ A về B (chỉ những file chưa có hoặc bị thay đổi):
  +: git checkout origin/A -- file3.txt
  +: git checkout origin/A -- file4.py

- Lấy nhiều file: git checkout origin/A -- file1.txt file2.py folder/file3.js

- Lấy toàn bộ thư mục: git checkout origin/A -- src/

- Lấy tất cả file từ trung nhưng không merge(hợp nhất): git checkout origin/A -- .


- Sau khi đã lấy file xong, bạn cần commit và push lên GitHub(push lên nhánh của bạn):
  + git add .
  + git commit -m "Lấy file chưa có từ nhánh A"
  + git push origin B

- Tạo Pull Request (PR) để merge code vào repository chính
- Sau khi đẩy code lên GitHub, bạn cần mở Pull Request để chủ repository xem xét và hợp nhất code của bạn vào nhánh main:
  + Truy cập vào repository trên GitHub.
  + Bạn sẽ thấy thông báo "Compare & pull request", nhấp vào đó.
  + Viết mô tả về thay đổi của bạn.
  + Nhấn "Create pull request".
  + Chủ repository sẽ xem xét, có thể yêu cầu chỉnh sửa hoặc chấp nhận thay đổi của bạn.

