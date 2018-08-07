# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(list):

    if len(list) <= 0:
        return None
    else:
        long = list[0]
        new_list = [[long]]

        for i in list[1:]:
            if i == long:
                new_list[-1].append(i)
            else:
                long = i
                new_list.append([i])

        max = len(new_list[0])
        result = new_list[0][0]

        for entry in new_list:
            if len(entry) > max:
                result = entry[0]
                max = len(entry)
        return result

#For example,

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1,2,3,4,5]))
# 1

print(longest_repetition([]))
# None
