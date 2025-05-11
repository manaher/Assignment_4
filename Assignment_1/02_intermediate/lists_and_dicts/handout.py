# PROBLEM: 1 List practice

# fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
# # printing length
# print(len(fruit_list))
# # Adding mango
# fruit_list.append("mango")
# print(fruit_list)

# *********************************************************************************************

#  PROBLEM: 2
# Accessing elements

# def func_list_index(list, index):
#     try:
#         return list[index]
#     except IndexError:
#         return "Index out of range"
    
# print(func_list_index(['zara', 1 , 'ali', 2 , 'hamzah'], 2))

# ***************************************************************************************

# # Modifying element
# def modify_element(lst, index, new_value):
#     try:
#         lst[index] = new_value
#         return lst
#     except IndexError:
#         return "Index out of range"

    
# print(modify_element(['zara', 1 , 'ali', 2 , 'hamzah'], 2, "ahmed"))

# ********************************************************************************

# # SLICING ELEMENTS
# def slice_list(lst, start_index, end_index):
#     try:
#         return lst[start_index:end_index]
#     except IndexError:
#         return "Index out of range"

    
# print(slice_list(['zara', 1 , 'ali', 2 , 'hamzah'], 0, 4))

# *********************************************************************************


# GAME
def access(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range"

def modify(my_list, index, new_value):
    try:
        my_list[index] = new_value
        return my_list
    except IndexError:
        return "Index out of range"

def slice_list(my_list, start_index, end_index):
    try:
        return my_list[start_index:end_index]
    except IndexError:
        return "Index out of range"

# Main Game Logic
my_list = ['a', 'b', 'c', 'd', 'e']

choice = input("Enter an option from the following: \n1. access \n2. modify \n3. slice \n").lower()

if choice == "access":
    index = int(input("Enter the index to access: "))
    print("Result:", access(my_list, index))

elif choice == "modify":
    index = int(input("Enter the index to modify: "))
    new_value = input("Enter the new value: ")
    print("Updated List:", modify(my_list, index, new_value))

elif choice == "slice":
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    print("Sliced List:", slice_list(my_list, start_index, end_index))

else:
    print("Invalid option selected.")
