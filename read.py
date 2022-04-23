### Import Libraries
import random
import pandas as pd
import time

### Folders
groups = [
    '00Uncorrelated', '01WeaklyCorrelated', '02StronglyCorrelated',
    '03InverseStronglyCorrelated', '04AlmostStronglyCorrelated', '05SubsetSum',
    '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', '08SpannerWeaklyCorrelated',
    '09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated', '11ProfitCeiling',
    '12Circle'
    ]
number_of_items = ['n00050', 'n00100', 'n00200', 'n00500', 'n01000', 'n02000', 'n05000', 'n10000']
value_ranges = ['R01000', 'R10000']

### Read the Test Cases
def read_test_cases():
    df = pd.DataFrame(columns=["group", "path", "n", "capacity", "values", "weights"])
    for group in groups:
        for n in number_of_items:
            # Chọn ngẫu nhiên một trong 2 phạm vi giá trị của test case (1000 hoặc 10000)
            idx_value_range = random.randint(0, 1)
            
            # Chọn ngẫu nhiên test case (Từ test case s000.kp đến test case s099.kp)
            idx_file = str(random.randint(0, 9)) + str(random.randint(0, 9))

            # Đọc dữ liệu test case với giá trị values và weights
            path = "test-cases/" + group + "/" + n + "/" + value_ranges[idx_value_range] + "/s0" + idx_file + ".kp"
            with open(path) as f:
                f.readline()
                n = int(f.readline())
                capacity = int(f.readline())
                values = []
                weights = []

                f.readline()
                lines = f.readlines()
                for line in lines:
                    temp = line.replace('\n', '').split(' ')
                    values.append(temp[0])
                    weights.append(temp[1])
                
                temp_df = pd.DataFrame({
                    "group": group, 
                    "path": path,
                    "n": n, 
                    "capacity": capacity, 
                    "values": [values], 
                    "weights": [weights]
                    })
                df = pd.concat([df, temp_df], ignore_index = True, axis = 0)

    return df

print("THE TEST CASES AS DATA FRAME:\n")
print(read_test_cases())
time.sleep(5)