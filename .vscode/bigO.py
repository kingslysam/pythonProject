from bigO import BigO
from bigO import algorithm
from random import randint
fname=input("Enter algorithm name:")
def fname(array):  # in-place, unstable
    '''
    Best : O(n^2) Time | O(1) Space
    Average : O(n^2) Time | O(1) Space
    Worst : O(n^2) Time | O(1) Space
    '''
    currentIndex = 0
    while currentIndex < len(array) - 1:
        smallestIndex = currentIndex
        for i in range(currentIndex + 1, len(array)):
            if array[smallestIndex] > array[i]:
                smallestIdx = i
        array[currentIndex], array[smallestIndex] = array[smallestIndex], array[currentIndex]
        currentIndex += 1
    return array

def TimeComplexity(functionname):
    lib = BigO()
    cmplx = lib.test(functionname, "random")
    cmplx = lib.test(functionname, "sorted")
    cmplx = lib.test(functionname, "reversed")
    cmplx = lib.test(functionname, "partial")
    cmplx = lib.test(functionname, "Ksorted")

TimeComplexity(fname)