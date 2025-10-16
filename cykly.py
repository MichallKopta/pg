def my_range(start, stop, step=1):
    range = [start]
    while start+step < stop:
        start += step
        range.append(start)
    return range

#def my_enumerate()

def while_enumerate(iterable, start=0):
    index = 0
    result = []
    while index <= len(iterable):
        result.append((start + index , iterable[index]))
        index += 1
    return result

def for_enumerate(iterable, start=0):
    result = []
    index = 0
    for index in range(len(iterable)):
        result.append((start + index , iterable[index]))
    return result
    

#def my_zip():
    


if __name__ == "__main__":
    text = "abcdef"
    #print(list(enumerate(text, 1)))
    #print(text[3])
    #print(my_range(1,5))
    #print(while_enumerate(text,100))
    print(for_enumerate(text,100))
    