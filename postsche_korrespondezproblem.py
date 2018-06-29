import copy
import functools
import random

min_elements = 66

xs = ["001", "01", "01", "10"]
ys = ["0", "011", "101", "001"]

used_xs = [False, False, False, False]
used_ys = [False, False, False, False]

indizes_x = []
indizes_y = []

def test_if_is_begin(arr_el, test, lazy=False):
    if not lazy:
        return arr_el.find(test) == 0
    else:
        print("test lazy", arr_el, test)
        return test.find(arr_el) == 0


def get_pos(arr, arr_el):
    ind = arr.index(arr_el)
    arr[ind] = ""
    return ind


def gen_index(is_matching):
    return is_matching


def startswith(arr, test):
    clone_arr = copy.deepcopy(arr)
    temp = list(filter(lambda el: gen_index(test_if_is_begin(el, test)), arr))
    if len(temp) == 0:
        temp = list(filter(lambda el: gen_index(test_if_is_begin(el, test, lazy=True)), arr))
    return map(lambda x: get_pos(clone_arr, x), temp)


def get_rand_el(inp):
    print("Get Rand El", inp)
    return inp[random.randint(0, len(inp) - 1)]


def get_shortest_el(enumerate):
    if(len(enumerate) == 1):
        return enumerate[0]
    shortest = enumerate[0]
    for e in enumerate:
        if(len(e[1]) < len(shortest[1])):
            shortest = e
    return shortest


def get_best_el(indexes, elements, used):
    filtered = filter(lambda (it, x): indexes.count(it) > 0, enumerate(elements))

    if not is_ready(used):
        temp = filter(lambda x: not used[x[0]], filtered)
        if(len(temp) > 0):
            filtered = temp

    short_el = get_shortest_el(filtered)
    len_short_el = len(short_el[1])
    temp = filter(lambda x: len(x[1]) == len_short_el, filtered)
    res = temp[random.randint(0, len(temp) - 1)]
    print("res", str(res[0]), res[1])
    return res[0], res[1]


def inspect(x):
    print(x)
    return x


def update_used(used_data, arr, el):
    clone_arr = copy.deepcopy(arr)
    clone_arr = list(map(lambda (it, x): "" if inspect(x) else clone_arr[it], enumerate(used_data)))
    print(arr, clone_arr, used_data)
    print(clone_arr.index(el))
    print(clone_arr.index(el))
    if clone_arr.__contains__(el):
        used_data[get_pos(clone_arr, el)] = True
    return used_data


def is_ready(bool_array):
    return functools.reduce(lambda x, y: x and y, bool_array)


def filter_pipes(str):
    res = functools.reduce(lambda x, y: x + y, str.split("|"))
    return res


def main(start_el, x_str="|", y_str="|", start_with_x=True):
    current_mode_is_x = start_with_x
    iterations = 0
    if current_mode_is_x:
        ind_el = xs.index(start_el)
        used_xs[ind_el] = True
        indizes_x.append(ind_el)
        x_str = x_str + start_el
    else:
        ind_el = ys.index(start_el)
        used_ys[ind_el] = True
        indizes_y.append(ind_el)
        y_str = y_str + start_el

    print(x_str, y_str)
    complete = False
    while iterations < 1000 and (len(filter_pipes(x_str)) == len(filter_pipes(y_str)) and not complete) or len(
            filter_pipes(x_str)) != len(filter_pipes(y_str)):
        if len(filter_pipes(x_str)) == len(filter_pipes(y_str)):
            if random.random < 0.5:
                indizes = [x for x in range(0,len(xs))]
                ind_el, el = get_best_el(indizes,xs, used_xs)
                used_xs[ind_el] = True
                x_str = x_str + "|" + el
                indizes_x.append(ind_el)
            else:
                indizes = [x for x in range(0, len(ys))]
                ind_el, el = get_best_el(indizes, ys, used_ys)
                used_ys[ind_el] = True
                y_str = y_str + "|" + el
                indizes_y.append(ind_el)


        current_mode_is_x = True if len(filter_pipes(x_str)) < len(filter_pipes(y_str)) else False
        if current_mode_is_x:
            find = filter_pipes(y_str)[len(filter_pipes(x_str)):]
            print("find", find)
            add_to_x = startswith(xs, find)
            if (len(add_to_x) == 0):
                return -1
            selected_el_ind, selected_el = get_best_el(add_to_x, xs, used_xs)
            used_xs[selected_el_ind] = True
            indizes_x.append(selected_el_ind)
            x_str = x_str + "|" + selected_el
        else:
            find = filter_pipes(x_str)[len(filter_pipes(y_str)):]
            print("find", find)
            add_to_y = startswith(ys, find)
            if (len(add_to_y) == 0):
                return -1
            selected_el_ind, selected_el = get_best_el(add_to_y, ys, used_ys)
            used_ys[selected_el_ind] = True
            indizes_y.append(selected_el_ind)
            y_str = y_str + "|" + selected_el
        iterations += 1
        complete = is_ready(used_ys) and is_ready(used_xs) and (len(indizes_x) >= min_elements or len(indizes_y) >= min_elements)
        print(used_xs, used_ys)
        print(iterations, complete, len(filter_pipes(x_str)), len(filter_pipes(y_str)))
    print(x_str, y_str)
    print(filter_pipes(x_str), filter_pipes(x_str).find(filter_pipes(y_str)))
    print(filter_pipes(y_str), filter_pipes(y_str).find(filter_pipes(x_str)))
    print("indizes_x", indizes_x, "len:", len(indizes_x))
    print("indizes_y", indizes_y, "len:", len(indizes_y))

    pass


pass

main("01")
