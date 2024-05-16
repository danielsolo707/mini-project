print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("What does BIOS stand for? ", "basic input/output system"),
    ("What does HDD stand for? ", "hard disk drive"),
    ("What does SSD stand for? ", "solid state drive"),
    ("What does LAN stand for? ", "local area network"),
    ("What does WAN stand for? ", "wide area network"),
    ("What does URL stand for? ", "uniform resource locator"),
    ("What does HTML stand for? ", "hypertext markup language"),
    ("What does HTTP stand for? ", "hypertext transfer protocol"),
    ("What does FTP stand for? ", "file transfer protocol"),
    ("What does DNS stand for? ", "domain name system"),
    ("What does IP stand for? ", "internet protocol")
]

for question, answer in questions:
    user_answer = input(question)
    if user_answer.lower() == answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/len(questions)) * 100) + "%.")
