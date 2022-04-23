# Import
from read import *
from write import *
from solver import *

# Giới hạn thời gian tìm lời giải tối đa 3 phút 
limited_time = 180

# Experimental Running
def run(test_cases):
    print("EXPERIMENTAL RUNNING IS STARTED !!!\n")
    time.sleep(5)

    for i in range(len(test_cases)):
        result = solve(test_cases.iloc[i], limited_time)
        # show(result)
        
        # Ghi lại thống kê kết quả của lời giải từng Test Cases
        write_the_statistics(test_cases.iloc[i], result)

    print("EXPERIMENTAL RUNNING HAS BE DONE!!!\n")

# Main
def main():
    # Lấy ngẫu nhiên 8 Test Cases từ bộ 12 nhóm Test Cases
    # copy_small_test_cases()

    # Đọc dữ liệu các Test Cases
    test_cases = read_test_cases()

    # Chạy thực nghiệm Test Cases
    run(test_cases)

if __name__ == '__main__':
    main()