# Simulated Annealing Algorithm

**Simulated Annealing** dựa trên việc mô phỏng quá trình làm nguội (annealing) trong kim loại, trong đó kim loại được nung nóng rồi làm nguội dần dần để tạo ra cấu trúc tinh thể ổn định. 
Thuật toán bắt đầu với một trạng thái ban đầu và thực hiện một loạt các biến đổi để tìm kiếm một trạng thái tốt hơn (tối ưu hóa)

Trong project này ta áp dụng thuật toán SA trong hai bài toán **Electricity Network** và **Travelling Salesman**

## 1. Electricity Network
Bài toán tối ưu hóa mạng lưới điện là một bài toán thực tế trong lĩnh vực quản lý hệ thống điện. 
Mục tiêu của bài toán là tìm cách cấu hình hệ thống mạng lưới điện sao cho chi phí vận hành của 
nó là thấp nhất

Trong mạng lưới điện, có nhiều thành phần như đường dây điện, trạm biến áp, hệ thống chiếu sáng 
và các thiết bị khác. Mỗi thành phần có công suất sử dụng và đơn giá năng lượng điện tương ứng. 
Chi phí vận hành của một thành phần được tính bằng sản phẩm giữa công suất sử dụng và giá thành 
của năng lượng điện

Bài toán tối ưu hóa mạng lưới điện nhằm tối thiểu hóa tổng chi phí vận hành của tất cả các thành 
phần trong hệ thống. Để giải quyết bài toán này, ta cần xác định cách cấu hình các thành phần trong 
mạng lưới điện sao cho hiệu quả từ mặt chi phí

Ta có thể điều chỉnh công suất sử dụng của các đường dây điện hoặc thay đổi loại bóng đèn 
được sử dụng trong hệ thống chiếu sáng. Các quyết định này sẽ ảnh hưởng đến chi phí vận hành của 
mạng lưới điện

Phương pháp tìm kiếm Simulated Annealing có thể được áp dụng để tìm cách cấu hình tối ưu cho bài
toán này. Giải thuật này sẽ tạo ra các trạng thái mới bằng cách thay đổi các thành phần trong 
mạng lưới điện và điều chỉnh nhiệt độ theo quy trình làm mát. Qua các bước lặp, giải thuật sẽ dần
dần di chuyển đến trạng thái tối ưu nhất với chi phí vận hành thấp nhất

## 2. Travelling Salesman
Bài toán Travelling Salesman (TSP) là một bài toán tối ưu hóa trong lĩnh vực lập lịch 
và quản lý tuyến. Bài toán đặt ra câu hỏi: "Một người bán hàng cần đi qua nhiều thành 
phố khác nhau và quay trở lại thành phố xuất phát, hãy xác định tuyến đường ngắn nhất mà 
người bán hàng có thể đi qua mỗi thành phố duy nhất một lần."

Mục tiêu của bài toán TSP là tìm tuyến đường ngắn nhất để người bán hàng đi qua tất cả 
các thành phố và quay trở lại thành phố xuất phát. Giải pháp tối ưu sẽ là một chuỗi các thành phố 
được sắp xếp sao cho tổng khoảng cách giữa các thành phố liên tiếp là nhỏ nhất
Phương pháp tìm kiếm Simulated Annealing có thể được áp dụng để giải quyết bài toán TSP 

Quá trình tìm kiếm sẽ bắt đầu bằng việc tạo ra một chuỗi ngẫu nhiên của các thành phố và 
dần dần cải thiện nó qua các vòng lặp. Trong mỗi vòng lặp, một trạng thái mới sẽ được tạo 
ra bằng cách hoán đổi vị trí của hai thành phố.Nếu trạng thái mới tốt hơn (tổng khoảng 
cách của nó nhỏ hơn), trạng thái mới sẽ được chấp nhận và cập nhật thành trạng thái hiện tại


