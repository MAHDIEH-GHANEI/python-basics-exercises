#Write a function that takes a list of dictionaries and sorts the list based on a specific dictionary key 
# (which is passed as a second argument). Use a lambda function to perform the sorting

def process_deictionary(list_of_dic, sort_key):
    sort_list= sorted(list_of_dic, key=lambda d:d.get(sort_key, ""))
    return sort_list

my_data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
]

sorted_by_name = process_deictionary(my_data, "name")
print("order by name: ")
print(sorted_by_name)

sorted_by_age = process_deictionary(my_data, "age")
print("order by age")
print(sorted_by_age)