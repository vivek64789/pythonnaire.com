# =======================================================================
# ========================Sorting started================================
# =======================================================================

def sort_by_start(self, events):
    if self.sort_by.get() == "Sort by":
        self.sort_button.configure(command=self.sort_by_id_ascending)
        self.sort_by_id_ascending()

    if self.sort_by.get() == "Batch ID" and self.sort_in.get() == "Ascending Order":
        self.sort_button.configure(command=self.sort_by_id_ascending)
        self.sort_by_id_ascending()

    if self.sort_by.get() == "Batch ID" and self.sort_in.get() == "Descending Order":
        self.sort_button.configure(command=self.sort_by_id_descending)
        self.sort_by_id_descending()

    if self.sort_by.get() == "Batch Name" and self.sort_in.get() == "Ascending Order":
        self.sort_button.configure(command=self.sort_by_name_ascending)
        self.sort_by_name_ascending()

    if self.sort_by.get() == "Batch Name" and self.sort_in.get() == "Descending Order":
        self.sort_button.configure(command=self.sort_by_name_descending)
        self.sort_by_name_descending()

    if self.sort_by.get() == "Date" and self.sort_in.get() == "Ascending Order":
        self.sort_button.configure(command=self.sort_by_registration_ascending)
        self.sort_by_registration_ascending()

    if self.sort_by.get() == "Date" and self.sort_in.get() == "Descending Order":
        self.sort_button.configure(command=self.sort_by_registration_descending)
        self.sort_by_registration_descending()


def sort_by_id_ascending(self):
    query = "select * from batch;"
    data = self.db_connection.select(query)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list)
    sorted_list = self.bubble_sort_ascending(sort_list)
    # messagebox.showinfo("Sorted", "Data is sorted in Ascending order by ID")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def bubble_sort_ascending(self, list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    print('the sorted list is ', list)
    return list


def sort_by_id_descending(self):
    query = "select * from batch;"
    data = self.db_connection.select(query)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list)
    sorted_list = self.bubble_sort_descending(sort_list)
    # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By ID")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def bubble_sort_descending(self, list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    print('the sorted list is ', list)
    return list


def sort_by_name_ascending(self):
    # print("I am in sort by name in ascending order")
    query = "select * from batch;"
    data = self.db_connection.select(query)
    print(data)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list[0])
    sorted_list = self.bubble_name_ascending(sort_list)
    # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def sort_by_name_descending(self):
    # print("i am in sort by name in descending order")
    query = "select * from batch;"
    data = self.db_connection.select(query)
    print(data)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list[0])
    sorted_list = self.bubble_name_descending(sort_list)
    # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def bubble_name_ascending(self, list):
    print("Success")
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i][1].upper() > list[i + 1][1].upper():
                list[i], list[i + 1] = list[i + 1], list[i]
    print('the sorted list is ', list)
    return list


def bubble_name_descending(self, list):
    print("Success")
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i][1].upper() < list[i + 1][1].upper():
                list[i], list[i + 1] = list[i + 1], list[i]
    print('the sorted list is ', list)
    return list


def sort_by_registration_ascending(self):
    query = "select * from batch;"
    data = self.db_connection.select(query)
    print(data)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list[0])
    sorted_list = self.bubble_registration_ascending(sort_list)
    # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def sort_by_registration_descending(self):
    # print("i am in sort by name in descending order")
    query = "select * from batch;"
    data = self.db_connection.select(query)
    print(data)
    sort_list = []
    for values in data:
        sort_list.append(values)
    # print(sort_list[0])
    sorted_list = self.bubble_registration_descending(sort_list)
    # messagebox.showinfo("Sorted", "Data is Sorted in Descending order By Name")
    if len(sorted_list) != 0:
        self.batch_tree.delete(*self.batch_tree.get_children())
        for values in sorted_list:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.batch_tree.insert('', END, values=data_list)


def bubble_registration_ascending(self, list):
    # print("Success")
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i][4].upper() > list[i + 1][4].upper():
                list[i], list[i + 1] = list[i + 1], list[i]
    # print('the sorted list is ', list)
    return list


def bubble_registration_descending(self, list):
    # print("Success")
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i][4].upper() < list[i + 1][4].upper():
                list[i], list[i + 1] = list[i + 1], list[i]
    # print('the sorted list is ', list)
    return list

# =======================================================================
# ========================Sorting Ended==================================
# =======================================================================
