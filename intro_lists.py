def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    save_first_element = list_one[0]
    list_one[0] = list_one[-1]
    list_one[-1] = save_first_element
    return (list_one)# make sure to remove this line before beginning work on this function

print("\033(1m Swap first and last elements of a list \033[0m")
myList = [1,2,3,4,5,6]
print("My list is:",myList)
print("Swapping first and last:", swap(myList))
print()
def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    pass # make sure to remove this line before beginning work on this function


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    pass # make sure to remove this line before beginning work on this function