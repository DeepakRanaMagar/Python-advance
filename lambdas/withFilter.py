# takes in a function and a list as argument
# filter out all the elements of sequence, for which function return TRUE

# to find age eligible to vote
age = [10, 28, 18, 30, 60]

canVote = list(filter(lambda age: age >= 18, age))

print('Age can vote: ', canVote)

# to find even number of list

mylist = [5, 7, 22, 25, 30, 50]

even = list(filter(lambda x: (x%2!=0),mylist))
print("Even Number: ", even)