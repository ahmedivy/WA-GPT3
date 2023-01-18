import json
import re

# Open the file for reading
with open("data/raw/chat1.txt", "r", encoding="utf-8") as f:
    # Read all the lines in the file
    lines = f.readlines()
    ignores = [
        "Messages to this group are now secured with end-to-end encryption. Tap for more info.",
        "<Media omitted>",
        "You deleted this message",
    ]
    conversation = {}
    conversations = []
    
    for line in lines:
        try:
            date, time, name, message = re.findall(r"(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2}\s[AP]M) - (\S+): (.*)", line)[0]
            if message not in ignores:
                print(f'{date} {time} {name} {message}')
        except:
            print(line)



# Read the text file
# with open("../data/raw/chat1.txt", "r", encoding="utf8") as file:
#     lines = file.readlines()

#     conversations = []
#     prompt = ""
#     response = ""

#     for line in lines:
#         date, time, name, message = line.split(" ", 3)

# # Write the data to a JSON file
# with open("../data/cleaned/chat1.json", "w") as file:
#     json.dump(conversations, file, indent=4)