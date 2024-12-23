import random

# Define the story with placeholders for user input
story = "Once upon a time, there was a {} {} who lived in a {} {}. One day, the {} {} decided to {} to {}."

# Define lists of words for each placeholder
adjectives = ["happy", "sad", "angry", "excited", "sleepy"]
nouns = ["cat", "dog", "bird", "fish", "monkey"]
locations = ["forest", "desert", "ocean", "mountain", "city"]
actions = ["dance", "sing", "run", "jump", "swim"]

# Ask the user to input a word for each placeholder
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
location1 = input("Enter a location: ")
location2 = input("Enter another location: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
action = input("Enter an action: ")
location3 = input("Enter a final location: ")

# Fill in the story with the user input
filled_story = story.format(adjective1, noun1, location1, location2, adjective2, noun2, action, location3)

# Print the filled-in story
print(filled_story)
