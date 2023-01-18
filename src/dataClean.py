import json

# function to extract message and response
def extract_conversation(line):
    conversation = {}
    line = line.strip()
    try:
        timestamp, message = line.split(" - ")
        conversation["prompt"] = message.split(":")[1].strip()
    except:
        pass
    return conversation

# Read the text file
with open("../data/raw/chat1.txt", "r", encoding="utf8") as file:
    lines = file.readlines()

    conversations = []
    prompt = ""

    # Iterate over the lines and extract message and response
    for line in lines:
        conversation = extract_conversation(line)
        if "prompt" in conversation:
            if prompt:
                conversation["response"] = prompt
            prompt = conversation["prompt"]
            conversations.append(conversation)

# Write the data to a JSON file
with open("../data/cleaned/chat1.json", "w") as file:
    json.dump(conversations, file, indent=4)