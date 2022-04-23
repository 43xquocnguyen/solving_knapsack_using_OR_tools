import os.path

def write(test_case, result):
    group = test_case['group']
    path = test_case['path']
    n = test_case['n']
    capacity = test_case['capacity']

    with open("results/running_results.csv", "a+") as f:
        f.write(group + ",")                                    # Group of Test Cases                  
        f.write(path.replace("\n", "") + ",")                   # Test Case            
        f.write(str(n) + ",")                                   # Number of Items
        f.write(str(capacity) + ",")                            # Capacity
        f.write(str(result['total_value']) + ",")               # Total Value
        f.write(str(result['total_weight']) + ",")              # Total Weight
        f.write(str(result['time']).replace("s", "") + "\n")    # Total Time to Found
        f.close()
    
# Write the Statistics
def write_the_statistics(test_case, result):
    group = test_case['group']
    path = test_case['path']
    n = test_case['n']
    capacity = test_case['capacity']

    if os.path.exists("results/running_results.csv"):
        write(test_case, result)
    else:
        # Tạo thư mục
        with open("results/running_results.csv", "a+") as f:
            f.write("group,test_case,n,capacity,total_value,total_weight,time\n")
            f.close()
        write(test_case, result)