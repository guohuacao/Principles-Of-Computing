"""
Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    for element in list1:
        if element not in new_list:
            new_list.append(element)
    #new_list.sort()
    #print new_list
    return new_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    for element in list1:
        if element in list2:
            new_list.append(element)
    #new_list.sort()
    #print new_list
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    res_list = []
    idx_i = 0;
    idx_j = 0;
    res_list = [];
    while idx_i < len(list1) and idx_j < len(list2):
        if list1[idx_i] <= list2[idx_j]:
            res_list.append(list1[idx_i])
            idx_i += 1
        else:
            res_list.append(list2[idx_j])
            idx_j += 1
    while idx_i < len(list1):
        res_list.append(list1[idx_i])
        idx_i += 1
    while idx_j < len(list2):
        res_list.append(list2[idx_j])
        idx_j += 1
    return res_list;


def swap(list_2):
    """
    len == 2, return sorted list
    """
    if (list_2[0] < list_2[1]):
        return list_2
    else:
        temp = list_2[0]
        list_2[0] = list_2[1]
        list_2[1] = temp
        return list_2


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if (len(list1) <= 1):
        return list1
    if (len(list1) == 2):
        return swap(list1)
    mid = len(list1)/2
    list_left = merge_sort(list1[0:mid])
    list_right = merge_sort(list1[mid:])
    result = merge(list_left, list_right)
    return result
# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]  #easy to bug: return []
    first_letter = word[0:1]
    rest_result = gen_all_strings(word[1:])
    rest_result_copy = list(rest_result)
    for each in rest_result_copy:
        for index in range(len(each)):
            new_word = each[:index] + first_letter + each[index:]
            rest_result.append(new_word)
        rest_result.append(each + first_letter)
    return rest_result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    res = []
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    for line in netfile.readlines():
        res.append(line[:-1])
    return res


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

#remove_duplicates([0, 1, 3, 2, 2]);
print merge_sort([9,3,5,1])
