#Tuples questions

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B",
                "progressive rock", "disco")

print'Create a tuple genres_tuple:', genres_tuple

print'The length of genres_tuple is', len(genres_tuple)

print'the element with index 3 is', genres_tuple[3]

print'the elements with index 3,4 and 5 are', genres_tuple[3:6]

print'the first two elements of the tuple genres_tuple are', genres_tuple[0:2]

print'the frist index of disco is', genres_tuple.index('disco')

C_tuple=(-5,1,-3)

C_list=sorted(C_tuple)

print'sorted list from C_tuple is', C_list

#Lists questions:

a_list=[1,'hello',[1,2,3],True]

print 'the value stored at index 1 of a_list is', a_list.index(1)

print 'the elements stored at index 1 and 2 of a_list are', a_list[1:3]

A=[1,'a']

B=[2,1,'d']

print 'concatenate of list A and B is', A+B
