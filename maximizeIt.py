class Top_Number:

    def __init__(self):
        self.topNum = 0

    def set_top_num(self, new_top):
        self.topNum = new_top
        return self.topNum

class Number_List:

    def __init__(self, num_list, list_name):
        self.num_list = num_list
        self.name = list_name
        self.tail_index = len(num_list) - 1
        self.current_index = 0

    def increment_index(self):
        if self.is_max_index() == True:
            self.current_index = 0
        else:
            self.current_index += 1

    def is_max_index(self):
        return self.current_index == self.tail_index


def get_input_list():
    in_list = []
    stop_flag = 0

    while stop_flag == 0:
        try:
            temp_num_list = []
            str_input = input().split(" ")

            for i in str_input:
                temp_num_list.append(int(i))

            in_list.append(temp_num_list)
        except EOFError:
            stop_flag = 1

    return in_list


def pop_list(num_stream):

    M = num_stream[0][1]
    del(num_stream[0])

    allLists = []

    for i in num_stream:
        allLists.append(i[1:])

    return allLists, M


def get_list_dict(allLists):

    list_dict = {}
    list_number = 1

    for i in allLists:
        list_dict["List" + str(list_number)] = Number_List(i, "List" + str(list_number))
        list_number += 1

    return list_dict


def get_max_number(list_dict, num_object, denominator, iter=0):

    def update_list_indexes(list_num, list_object):
        if list_object.is_max_index() == True:
            list_object.increment_index()
            list_num -= 1
            if list_num == 0:
                return 0
            update_list_indexes(list_num, list_dict["List" + str(list_num)])
        else:
            list_object.increment_index()
        return 0

    K = len(list_dict)
    tempNum = 0

    for i in list_dict:
        indx = list_dict[i].current_index
        tempNum += (list_dict[i].num_list[indx] ** 2)

    if tempNum % denominator > num_object.topNum:
        num_object.set_top_num(tempNum)

    index_ticker = []
    index_max = []

    for i in list_dict:
        index_ticker.append(list_dict[i].current_index)

    for i in list_dict:
        index_max.append(list_dict[i].tail_index)

    update_list_indexes(K, list_dict["List" + str(K)])

    iter += 1
    
    if index_ticker != index_max:
        get_max_number(list_dict, num_object, denominator, iter)

    return num_object


# def maximum_number(list_dict, num_object, denominator):
#     current_max_number = 0
#     current_list_count = 


# num_stream = get_input_list()

# num_stream = [[3, 1000], [2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]] 

### Testing
x = []
x.append("7 159".split(" "))
x.append("7 868344 5702470 4164686 6909034 9938057 2325752 2873259".split(" "))
x.append("7 3281382 6656834 2949466 8313351 1693510 3531625 7965124".split(" "))
x.append("7 6170425 3484246 2039180 761139 2069051 3570668 2348921".split(" "))
x.append("7 9698787 37364 8030130 6391829 6969085 1247325 1978995".split(" "))
x.append("7 8416661 9855125 6534506 9285004 8073946 3215543 6194037".split(" "))
x.append("7 8012002 5541294 1583648 3809736 4714479 7049465 4639438".split(" "))
x.append("7 6407988 3097441 2604562 5094765 6581687 7160093 5855903".split(" "))

num_stream = []
for i in x:
    y = []
    for j in i:
        y.append(int(j))
    num_stream.append(y)        
###



return_values = pop_list(num_stream)

allLists = return_values[0]
M = return_values[1]

list_dictionary = get_list_dict(allLists)

num_object = Top_Number()

num_object = get_max_number(list_dictionary, num_object, M)

print(type(num_object.topNum))



