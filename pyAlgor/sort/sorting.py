'''
Bubble sort:
This sorting algorithm repeatedly steps through the input list, compare the adjacent elements and swaps them
if they are in the wrong order
Returns an list
'''
def bubble_sort(input):
    algorithmBusy  = True
    while algorithmBusy:
        algorithmBusy = False
        for i in range(len(input) - 1):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
                algorithmBusy = True    
    return input