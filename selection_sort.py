def selection_sort(array,sort_by_list):
     for sort_by in sort_by_list[-1::-1]:
        for x in range(len(array)):
            min_index = x
            for y in range(x, len(array)):
                if array[y][sort_by] < array[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                array[x], array[min_index] = array[min_index], array[x]



if __name__ == '__main__':
    elements = [
    {'First Name': 'Raj', 'Middle Name': 'Tim',  'Last Name': 'Nayyar'},
    {'First Name': 'Suraj','Middle Name': 'Andy',  'Last Name': 'Sharma'},
    {'First Name': 'Karan',  'Middle Name': 'Ben', 'Last Name': 'Kumar'}
]
    print(elements)

