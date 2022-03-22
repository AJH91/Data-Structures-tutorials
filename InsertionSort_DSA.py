def insertion_sort(elements):

    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1





if __name__ == '__main__':
    elements = [2,1,5,7,2,0,5]
    insertion_sort(elements)
    print(elements)