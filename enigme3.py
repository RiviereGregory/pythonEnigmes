def maximum_in_pile(pile_in, k):
    maxi = pile_in[k]
    j = k
    for i in range(k, len(pile_in)):
        if pile_in[i] > maxi:
            maxi = pile_in[i]
            j = i
    return j


def return_part_of_pile_between_k_and_end_pile(pile_modified, k):
    length_pile = len(pile_modified)
    for i in range((length_pile - k) // 2):
        temp = pile_modified[k + i]
        pile_modified[k + i] = pile_modified[length_pile - 1 - i]
        pile_modified[length_pile - 1 - i] = temp


def sorting_the_crepe_maker_on_pile(pile_modified):
    for i in range(len(pile_modified)):
        j = maximum_in_pile(pile_modified, i)
        return_part_of_pile_between_k_and_end_pile(pile_modified, j)
        return_part_of_pile_between_k_and_end_pile(pile_modified, i)


if __name__ == '__main__':
    pile = [7, 6, 1, 3, 2, 8, 9, 5, 4]
    print(pile)
    sorting_the_crepe_maker_on_pile(pile)
    print(pile)
