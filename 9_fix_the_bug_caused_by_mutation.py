# Explain the relationship between aliasing, mutation, and cloning. Briefly explain each concept.

"""
Aliasing:

Aliasing means giving another name to an existing object. 
We can understand that using this analogy. 
The vocabulary differences are different words used to name the same object; 
we are not changing the object but the name, for example(biscuit/cookie). 
So… the same happens with aliasing, we are giving new names to the same object.

Mutation:

To understand the concept of mutation let’s think about humans having babies, 
each time a human has babies what happens is that they are creating a mutation of their DNA, 
and creating a special and unique person (yeah folk, you are special and unique… or well, according to genetics you are… just joking, you truly are?); 
maybe we look like the same and even identical as our biological relatives, 
but at DNA level we are unique within our own personal mutations.

Cloning: 
Let's bring again this genetic stuff, remember Dolly the sheep? We can clone a sheep, 
and both sheep will have the same DNA and will look the same, 
but both sheep are completely different because they are unique as living organisms.
"""

# With your knowledge of aliasing, mutation, and cloning, modify the functions in the following program so that the original list is not mutated.

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
    new_data = data[:]
 
    for item in data:
        if item == target:
            new_data.remove(target)
 
    return new_data
 
def get_product(data):
    total = 1
 
    for i in range(len(data)):
        total *= data[i]
 
    return total
 
remove_elem(c, 3)
print(get_product(b))
print(a)