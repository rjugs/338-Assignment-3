import sys

def main():
    # Create an empty list (dynamic array)
    myList = []
    # Find the capactiy to begin with
    prev_capacity = sys.getsizeof(myList)
    print("Size of the list: ", prev_capacity)

    # Testing from 0 to 64 list elements
    for i in range(0, 64):
        # Add an item to the list every iteration
        myList.append(i)
        # Find the updated size after appending
        curr_capacity = sys.getsizeof(myList)

        # If the updated size is greater than the previous size, print the change in size at element i.
        if curr_capacity > prev_capacity:
            print(f"List capacity is changed at {i} elements: {prev_capacity} bytes -> {curr_capacity} bytes")
            # Make the previous capacity the new one for the next iteration.
            prev_capacity = curr_capacity


if __name__== '__main__':
    main()