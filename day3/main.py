import argparse
import math

invalid_ids = []

def find_duplicates(id_range:str):
    
    sum = 0
    start, end = id_range.split("-")
    start = int(start)
    end = int(end)
    for i in range(start, end+1):
        number = str(i)

        if len(number) % 2 == 0:
            midpoint = int(len(number)/2)
            print(midpoint)
            first_half = number[:midpoint]
            second_half = number[midpoint:]
            print(midpoint, " : ", first_half, " - ", second_half)
            if first_half == second_half:
                invalid_ids.append(i)
                sum += i
                
    return sum

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()

    file_path = args.path
    id_ranges = []
    with open(file_path, "r") as f:
        output = f.read()
        id_ranges = output.split(",")
        
    total_sum = 0
    for range in id_ranges:
        total_sum += find_duplicates(range)
    
    print(total_sum)
    
if __name__ == "__main__":
    main()
    
    
