two_dim_array = [
    [1,2,3,4,5,6,7,8,9],
    [10,11,12,99,14,15,16,17,18,19],
    [20,21,22,23,24,25,26,27,28,29]
    ]

def locateLargest(lst):
    location = []
    max_value = 0
    max_row_index = 0
    max_col_index = 0
    for row_index in range(0,len(lst)):
        for col_index in range(0,len(lst[row_index])):
            if lst[row_index][col_index] > max_value:
                max_row_index = row_index
                max_col_index = col_index
                max_value = lst[row_index][col_index]
    location.append(max_row_index)
    location.append(max_col_index)
    return location
                  
def main():
    print(f'The location of the largest element is at {locateLargest(two_dim_array)}')
  
main()        