def my_generator(n):
    value = 0 # initialize counter
    while value < n:
        yield value  # produce current
        value += 1   # increment counter
        
if __name__ == "__main__":
        
    for item in my_generator(30):
        print(item)