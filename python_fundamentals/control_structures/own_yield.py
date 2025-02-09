'''
Creation of a simple range functions showing the functionality of the yield keywork 
'''

def my_range(start, end):
    current = start
    while current < end:
        print("current on my range>", current)
        yield current
        current += 1


for num in my_range(0, 10):
    print("num on for>", num)
    print(num, end=" ")
