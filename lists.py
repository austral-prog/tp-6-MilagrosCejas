def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >=3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False



def list_of_lists(list_of_lists_to_modify):
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]

        return list_of_lists_to_modify
