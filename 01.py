# Advent of Code 2024!
# Day 1

# Reads two columns of numbers from a text file and stores them in separate lists (with each list sorted from smallest to largest)
def read_lists_from_input(filename):
    num_list_1 = list()
    num_list_2 = list()
    with open(filename) as f:
        for line in f.readlines():
            line_nums = line.split()
            num_list_1.append(int(line_nums[0]))
            num_list_2.append(int(line_nums[1]))
    num_list_1.sort()
    num_list_2.sort()
    return num_list_1, num_list_2

# Assigns min and max to two numbers, calculates difference between the two
def compare_nums(num1, num2):
    bigger_num = max(num1, num2)
    smaller_num = min(num1, num2)
    diff = bigger_num - smaller_num
    sum_of_diffs.append(diff)
    return sum_of_diffs

# Calculate similarity score by multiplying a number from a list by the number of times it appears in a second list, then adding the score to a running total
def similarity_score(nums1, nums2):
    running_total = list()
    for i in nums1:
        count = nums2.count(i)
        running_total.append(i * count)
    return sum(running_total)

# Initialize variables
sum_of_diffs = list()
sum_of_similarity_scores = list()

# Get input filename
input_file = input("Enter input filename: ")

# Create number lists from input
num_list_1, num_list_2 = read_lists_from_input(filename=input_file)

# Compare lists of numbers
for i in range(0, len(num_list_1)):
    sum_of_diffs = compare_nums(num_list_1[i], num_list_2[i])

print("Distance between lists:", sum(sum_of_diffs))

sum_of_similarity_scores = similarity_score(num_list_1, num_list_2)

print("Similarity score of lists:", sum_of_similarity_scores)