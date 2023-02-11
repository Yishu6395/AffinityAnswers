import re

# Define a list of racial slurs
slurs = set(["racial_slur_1", "racial_slur_2", "racial_slur_3", ...])

# Open the file of tweets
with open("tweets.txt", "r") as file:
    tweets = file.readlines()

# Iterate through each tweet
for tweet in tweets:
    profanity_level = 0
    words = tweet.split()
    
    # Check if each word in the tweet is a racial slur
    for word in words:
        if word in slurs:
            profanity_level += 1
    
    # Indicate the degree of profanity for each tweet
    if profanity_level == 0:
        print(f"The tweet '{tweet}' is not profane.")
    else :
        print(f"The tweet '{tweet}' has a '{profanity_level}' degree of profanity.") 

