def get_products_of_all_ints_except_at_index(numbers):
    result = [None] * len(numbers)

    product_so_far = 1
    for i in range(len(numbers)):
        result[i] = product_so_far
        product_so_far *= numbers[i]

    product_so_far = 1
    for i in range(len(numbers)-1, -1, -1):
        result[i] *= product_so_far
        product_so_far *= numbers[i]

    return result
