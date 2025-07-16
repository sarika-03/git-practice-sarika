note = "hey i'm learing devops"

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved!")
