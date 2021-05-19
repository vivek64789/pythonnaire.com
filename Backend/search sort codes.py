# # # # def find(l, target):
# # # #     start = 0
# # # #     end = len(l) - 1
# # # #
# # # #     while start <= end:
# # # #         middle = (start + end) // 2
# # # #         midpoint = l[middle]
# # # #         if midpoint > target:
# # # #             end = middle - 1
# # # #         elif midpoint < target:
# # # #             start = middle + 1
# # # #         else:
# # # #             return midpoint
# # # #
# # # #
# # # # Ls = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"]  # Needs to be sorted.
# # # #
# # # # print(find(Ls, "Joe"))
# # #
# # #
# # # # # Python program to implement Selection Sort for
# # # # # array of strings
# # # #
# # # # # Function defined for sorting the array of strings
# # # # def Selection(arr, n):
# # # #     # One by one move boundary of unsorted subarray
# # # #     for i in range(n):
# # # #         min_index = i
# # # #         min_str = arr[i]
# # # #
# # # #         # Find the minimum element in unsorted subarray
# # # #         for j in range(i + 1, n):
# # # #
# # # #             # If min_str is greater than arr[j]
# # # #             if min_str > arr[j]:
# # # #                 # Make arr[j] as min_str and update min_index as j
# # # #                 min_str = arr[j]
# # # #                 min_index = j
# # # #
# # # #             # Swap the found minimum element with the first element
# # # #         if min_index != i:
# # # #             # Store the first element in temp
# # # #             temp = arr[i]
# # # #
# # # #             # Place the min element at the first position
# # # #             arr[i] = arr[min_index]
# # # #
# # # #             # place the element in temp at min_index
# # # #             arr[min_index] = temp
# # # #
# # # #         # Return the sorted array
# # # #     return arr
# # # #
# # # #
# # # # arr = ["GeeksforGeeks", "Practice.GeeksforGeeks", "GeeksQuiz"]
# # # #
# # # # print("Given array is")
# # # # for i in range(len(arr)):
# # # #     print(i, ":", arr[i])
# # # #
# # # # print("\nSorted array is")
# # # # for i in range(len(Selection(arr, len(arr)))):
# # # #     print(i, ":", Selection(arr, len(arr))[i])
# # # #
# # # # # This code is contributed by Manish KC
# # # # # profile: mkumarchaudhary06
# # #
# # #
# # # # Python program to implement Selection Sort for
# # # # array of strings
# # #
# # #
# # # def selection_sort_ascending(_list, n):
# # #     """Function defined for sorting the list of strings"""
# # #     # One by one move boundary of unsorted sublist
# # #     for i in range(n):
# # #         min_index = i
# # #         min_str = _list[i]
# # #
# # #         # Find the minimum element in unsorted sublist
# # #         for j in range(i + 1, n):
# # #
# # #             # If min_str is greater than arr[j]
# # #             if min_str > _list[j]:
# # #                 # Make _list[j] as min_str and update min_index as j
# # #                 min_str = _list[j]
# # #                 min_index = j
# # #
# # #             # Swap the found minimum element with the first element
# # #         if min_index != i:
# # #             # Store the first element in temp
# # #             temp = _list[i]
# # #
# # #             # Place the min element at the first position
# # #             _list[i] = _list[min_index]
# # #
# # #             # place the element in temp at min_index
# # #             _list[min_index] = temp
# # #
# # #         # Return the sorted list
# # #     return _list
# # #
# # #
# # # # data_list = ["Joe", "Brian", "Lois", "Stewie", "Meg", "Peter"]
# # # data_list = [7, 2, 3, 4, 5, 6]
# # # print("\nSorted list is")
# # # sorted_list = selection_sort_ascending(data_list, len(data_list))
# # # print(sorted_list)
# # # #
# # #
# # # def binary_search(l, target):
# # #     start = 0
# # #     end = len(l) - 1
# # #
# # #     while start <= end:
# # #         middle = (start + end) // 2
# # #         midpoint = l[middle]
# # #         if midpoint > target:
# # #             end = middle - 1
# # #         elif midpoint < target:
# # #             start = middle + 1
# # #         else:
# # #             return midpoint
# # #
# # #
# # # find = binary_search(sorted_list, "Peter")
# # # print(f"User {find} found")
# # #
# # #
# # # def search_by_id(self):
# # #     self.search_start()
# # #     self.search_button.configure(command=self.search_by_id_start)
# # #
# # #
# # # def search_by_id_start(self):
# # #     # print("I am in search by id")
# # #     try:
# # #         obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
# # #         self.db_connection.create(obj_student_database.get_database())
# # #
# # #         query = "select * from students;"
# # #         data = self.db_connection.select(query)
# # #         # print(data)
# # #         # self.student_tree.delete(*self.student_tree.get_children())
# # #         search_list = []
# # #         for values in data:
# # #             data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
# # #                          values[8],
# # #                          values[9], values[10], values[11], values[12], values[13], values[14]]
# # #             # print(data_list[0])
# # #             search_list.append(data_list[0])
# # #         # print(search_list)
# # #         output = self.binary_search(search_list, int(self.search_entry.get()))
# # #         # print(output)
# # #         if output:
# # #             messagebox.showinfo("Found", f"Student having id {output} found")
# # #             val_list = []
# # #             for child in self.student_tree.get_children():
# # #                 val = self.student_tree.item(child)["values"]
# # #                 val_list.append(val)
# # #
# # #
# # #
# # #         else:
# # #             messagebox.showerror("Error", " ID Not found")
# # #
# # #     except BaseException as msg:
# # #         print(msg)
# # #
# # #
# # #
# # # # print("I am in search by id")
# # #         # try:
# # #         #     obj_student_database = Model_class.student_registration.GetDatabase('use cms;')
# # #         #     self.db_connection.create(obj_student_database.get_database())
# # #         #
# # #         #     query = "select * from students;"
# # #         #     data = self.db_connection.select(query)
# # #         #     # print(data)
# # #         #     # self.student_tree.delete(*self.student_tree.get_children())
# # #         #     search_list = []
# # #         #     for values in data:
# # #         #         data_list = [values[0], values[4], values[5], values[2], values[6], values[7],
# # #         #                      values[8],
# # #         #                      values[9], values[10], values[11], values[12], values[13], values[14]]
# # #         #         # print(data_list[0])
# # #         #         search_list.append(data_list[0])
# # #         #     # print(search_list)
# # #         #     output = self.binary_search(search_list,int(self.search_entry.get()))
# # #         #     # print(output)
# # #         #     if output:
# # #         #         messagebox.showinfo("Found",f"Student having id {output} found")
# # #         #         val_list= []
# # #         #         for child in self.student_tree.get_children():
# # #         #             val= self.student_tree.item(child)["values"]
# # #         #             val_list.append(val)
# # #         #
# # #         #
# # #         #
# # #         #     else:
# # #         #         messagebox.showerror("Error"," ID Not found")
# # #         #
# # #         # except BaseException as msg:
# # #         #     print(msg)
# #
# #
# #
# # def selection_sort_list_ascending(_list, n):
# #     """Function defined for sorting the list of strings"""
# #     # One by one move boundary of unsorted sublist
# #     for i in range(n):
# #         # print(i)
# #         min_index = i
# #         min_str = _list[i][1]
# #         print(min_str)
# #
# #         # Find the minimum element in unsorted sublist
# #         for j in range(i + 1, n):
# #             # print(j)
# #
# #             # If min_str is greater than arr[j]
# #             if min_str > _list[j][1]:
# #                 # Make _list[j] as min_str and update min_index as j
# #                 min_str = _list[j][1]
# #                 min_index = j
# #
# #             # Swap the found minimum element with the first element
# #         if min_index != i:
# #             # Store the first element in temp
# #             temp = _list[i]
# #
# #             # Place the min element at the first position
# #             _list[i] = _list[min_index]
# #
# #             # place the element in temp at min_index
# #             _list[min_index] = temp
# #
# #         # Return the sorted list
# #     return _list
# #
# #
# # data_list = [["Joe", "Brian"], ["Meg", "Peter"], ["Lois", "Stewie"]]
# #
# # print("\nSorted list is")
# # sorted_list = selection_sort_list_ascending(data_list, len(data_list))
# # # print(sorted_list)
# # #
#
#
# def bubble_name_descending(list):
#     for j in range(len(list) - 1):
#         for i in range(len(list) - 1):
#             if list[i][1] > list[i + 1][1]:
#                 list[i], list[i + 1] = list[i + 1], list[i]
#     print('the sorted list is ', list)
#     return list
#
#
# bubble_name_descending([["Joe", "zrian"], ["Meg", "Aeter"], ["Lois", "Stewie"]])
#
#
# def selection_sort_ascending(self, _list, n):
#     """Method defined for sorting the list of data in ascending order"""
#     # One by one move boundary of unsorted sublist
#     for i in range(n):
#         min_index = i
#         min_str = _list[i]
#
#         # Find the minimum element in unsorted sublist
#         for j in range(i + 1, n):
#
#             # If min_str is greater than arr[j]
#             if min_str > _list[j]:
#                 # Make _list[j] as min_str and update min_index as j
#                 min_str = _list[j]
#                 min_index = j
#
#             # Swap the found minimum element with the first element
#         if min_index != i:
#             # Store the first element in temp
#             temp = _list[i]
#
#             # Place the min element at the first position
#             _list[i] = _list[min_index]
#
#             # place the element in temp at min_index
#             _list[min_index] = temp
#
#         # Return the sorted list
#     return _list
#
#
# def selection_sort_descending(self, _list, n):
#     """Method defined for sorting the list of data in descending order"""
#     # One by one move boundary of unsorted sublist
#     for i in range(n):
#         min_index = i
#         min_str = _list[i]
#
#         # Find the minimum element in unsorted sublist
#         for j in range(i + 1, n):
#
#             # If min_str is greater than arr[j]
#             if min_str > _list[j]:
#                 # Make _list[j] as min_str and update min_index as j
#                 min_str = _list[j]
#                 min_index = j
#
#             # Swap the found minimum element with the first element
#         if min_index != i:
#             # Store the first element in temp
#             temp = _list[i]
#
#             # Place the min element at the first position
#             _list[i] = _list[min_index]
#
#             # place the element in temp at min_index
#             _list[min_index] = temp
#
#         # Return the sorted list
#     return _list
#
# query="select * from people where"+str(self.search_by.get())+'=' +str(self.search_txt.get())""

# query="select * from people where"+str(self.search_by.get())+"=" '%"+str(self.search_txt.get())+"%'
#


#



# Python code to demonstrate
# to find strings with substrings
# using list comprehension

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print ("The original list is : " + str(test_list))

# initializing substring
subs = 'ek'

# using list comprehension
# to get string with substring
res = [i for i in test_list if subs in i]

# printing result
print ("All strings with given substring are : " + str(res))
