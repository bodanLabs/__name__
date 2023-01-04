def upper_list_elements(my_list):
    new_list = []
    for item in my_list:
        new_list.append(item.upper())
    return new_list

if __name__ == "__main__":
    print("__name__=",__name__)
    upper_list = upper_list_elements(['bodan','python','coding'])
    print(upper_list)
if __name__ == "example_module":
    print("__name__=",__name__)
    print("you imported exmaple module")