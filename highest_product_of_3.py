def highest_product_of_3(numbers):
    highest = numbers[0]
    highest_of_2 = highest * numbers[1]
    highest_of_3 = highest_of_2 * numbers[2]

    lowest = highest
    lowest_of_2 = highest_of_2

    for num in numbers:
        highest_of_3 = max(highest_of_3, highest_of_2*num, lowest_of_2*num)

        lowest_of_2 = min(lowest_of_2, highest*num, lowest*num)
        highest_of_2 = max(highest_of_2, highest*num, lowest*num)

        lowest = min(lowest, num)
        highest = max(highest, num)

    return highest_of_3
