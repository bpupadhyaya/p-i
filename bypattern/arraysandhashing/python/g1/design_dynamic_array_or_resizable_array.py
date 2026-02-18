"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java
or a vector in C++.
Your DynamicArray class should support the following operations:
-DynamicArray(int capacity) will initialize an empty array with a capacity of capacity,
where capacity > 0.
-int get(int i) will return the element at index i. Assume that index i is valid.
-void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
-void pushback(int n) will push the element n to the end of the array.
-int popback() will pop and return the element at the end of the array. Assume that the
array is non-empty.
-void resize() will double the capacity of the array.
-int getSize() will return the number of elements in the array.
-int getCapacity() will return the capacity of the array.

If we call void pushback(int n) but the array is full, we should resize the array first.
Example 1:
Input:
["Array", 1, "getSize", "getCapacity"]
Output:
[null, 0, 1]

Example 2:
Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
Output:
[null, null, 1, null, 2]
"""


class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set n at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            # Soft delete the last element
            self.length -= 1
        # Return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity *= 2
        new_arr = [0] * (self.capacity)
        # Copy element to new array
        for i in range(self.capacity):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def get_size(self) -> int:
        return self.length

    def get_capacity(self) -> int:
        return self.capacity


def main():
    # T1
    # ["Array", 1, "getSize", "getCapacity"]
    # my_array = DynamicArray(1)
    # print(my_array)
    # print(my_array.get_size())
    # print(my_array.get_capacity())

    # T2
    # ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
    my_array2 = DynamicArray(1)
    print(my_array2.pushback(1))
    print(my_array2.get_capacity())
    print(my_array2.pushback(2))
    print(my_array2.get_capacity())


if __name__ == "__main__":
    main()

