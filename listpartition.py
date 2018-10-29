'''
TestCase:
1. [1, 1, 1, 2, 1]
2. [1,1,1,3]
3. [2,2,4]
4. [1, 2, 3, 1, 0, 1, 3]
5. [1]
6. [10,10]

'''

def find_index(array, n):

    left_sum = 0
    right_sum = 0
    right_index = n-1
    left_index = 0
    while left_index <= right_index:
            if left_sum <= right_sum:
                left_sum += array[left_index]
                left_index += 1

            else:
                right_sum += array[right_index]
                right_index -= 1

    if left_sum == right_sum:
        return right_index + 1
    else:
        return -1


if __name__ == '__main__':

    array = list(map(int, input("Enter N numbers seprated by space:").split()))
    n = len(array)
    if n > 1:
        index = find_index(array, n)
        if index == -1:
            print("List is not partitionable")
        else:
            print("List is partitionable")
            print(array[0:index], ' ', array[index:n])
    else:
        print("List is not partitionable")



