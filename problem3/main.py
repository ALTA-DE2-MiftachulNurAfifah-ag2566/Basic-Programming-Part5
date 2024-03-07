def join_array_remove_duplicate(arrayA, arrayB):
    array = list(dict.fromkeys(arrayA + arrayB))
    # array1 = list(set(arrayA))
    # array2 = list(set(arrayB))
    # array = [i for i in array1 + array2 if i in array1 or i in array2]
    return array

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
