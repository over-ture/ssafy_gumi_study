def solution(arg) :
    char_list = []
    char_number_list = []
    arg = arg.upper()
    for i in arg :
        if i not in char_list :
            char_list.append(i)
            char_number_list.append(1)
        else :
            char_number_list[char_list.index(i)] += 1
    
    max_val = max(char_number_list)
    max_char_index = char_list[char_number_list.index(max_val)]
    max_elements = [x for x in char_number_list if x == max_val]
    if len(max_elements) > 1 :
        return '?'
    else : 
        return max_char_index
    
Q = input()
print(solution(Q))