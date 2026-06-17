#“Write a program that saves a list of tasks (To‑Do List) in a text file.
# The program should also be able to read the tasks from the file and display them. Then convert the data to JSON format.”

import json
number_note = int(input("Enter number note: "))
text = input("Enter your note: ")

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write(f"{number_note}: {text} \n")

print("Note saved in text file.")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Content of text file:")
print(content)

note_list = [
    {
        "number_note" : number_note ,
        "your note": text
    }
]

with open("notes.json", "w", encoding="utf-8") as file:
    json.dump(note_list, file, ensure_ascii=False, indent=4)

print("Saved in JSON file")

with open("notes.json", "r", encoding="utf-8") as file:
    loaded_note = json.load(file)

print("Loaded from JSON:")
print(loaded_note)