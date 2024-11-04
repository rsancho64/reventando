# [0,1,2,3,4,5]
#  * 
# [0,1,2,3,4,5]
#    *
# [0,1,2,3,4,5]
#      *
# [0,1,2,3,4,5]
#        *
# [0,1,3,3,4,5]
#          *  
# [0,1,3,6,4,5]
#             *
# [0,1,3,6,10,5]

# [0,1,3,6,10,15]

# oops. 
# lista = list(range(1000000000))
# print(lista)
# print(len(lista))

def my_generator(n):
    value = 0 # initialize counter
    while value < n:
        yield value  # produce current
        value += 1   # increment counter
        
if __name__ == "__main__":
        
    for item in my_generator(1000000000):
        print(item)

# lista = list(range(1000000000))
# print(lista)
# print(len(lista))

# for pos in range(len(lista)):
#     print(pos)
#     if pos == 0:
#         pass
#     else:
#         lista[pos] += lista[pos-1]

# print(lista)

