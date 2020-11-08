def has_negatives(a):

    a_dict = { a[i] : 0 for i in range(0, len(a) ) }

    result = []

    for key in a_dict:
        if key > 0 and key * -1 in a_dict:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
