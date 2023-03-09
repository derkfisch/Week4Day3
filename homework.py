#question 1

words = ['this' , 'is', 'a', 'sentence', '.']
#creating a reverse function
def reverse(words):
    #default start, default stop, step from back to front of string 1 word at a time
    return words[::-1]

print(reverse(words))

#question 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def Distinct_words(a_text):
    #need a dictionary for words: count
    word_count = {}

    # Create a loop that goes over the words split by space
    # For every word in string 'a_text', split by space
    for word in a_text.split():
        # If that word exists in the dictionary
        if word in word_count:
            # add 1 to word's count in dictionary word_count
            word_count[word] += 1
        else:
            # if word doesn't exist, add word to word_count with a count of starting count of 1
            word_count[word] = 1

    return word_count

print(Distinct_words(a_text))

#question 3

nums_list = [10,23,45,70,11,15]
target = 70

# If number is not present return -1
def linear_search(nums_list, target):
    nums_list = [10,23,45,70,11,15]
    target = 70
    
    #creating a for loop for every number in range of 6 index spots of nums_list
    for num in range(6):
        #if the number in that index of nums_list is equal to the target
        if nums_list[num] == target:
            #return the index that the target was found
            return num
    #if the numbers have looped through and the target wasnt found, return -1
    return -1

print(linear_search(nums_list, target))