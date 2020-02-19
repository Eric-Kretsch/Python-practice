#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and space with and inserted before the last item.

def toString(arr):
    s = ''
    for i in range(len(arr)):
        if i > 0:
            if i == len(arr) - 1:
                #last item
                s = s + ' and '
            else:
                s = s + ', '
        s = s + arr[i];
    return s

toString(['apples', 'bananas', 'tofu', 'cats'])
