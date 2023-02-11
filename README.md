# AffinityAnswers
Assessment for shortlisting

Assumptions:

The file of tweets is stored in the same directory as the Python script and is called tweets.txt.
The file of tweets is in plain text format and each tweet is on a separate line.
The racial slurs in the slurs list are case-insensitive.
The degree of profanity is indicated in a simple manner with the total count of the racial words in the tweet

In this program, the profanity_degree function takes a tweet and a list of words that indicate profanity as input, and returns the degree of profanity for that tweet. The function splits the tweet into words, and for each word, it checks if it is in the profanity list. If it is, it increments a counter for the number of profanity words in the tweet. The degree of profanity for the tweet is then calculated as the total number of racial words present in the tweet. 

This program can be easily modified to suit different requirements and can be improved to handle more complex scenarios, such as handling different types of slurs, using a more sophisticated method of calculating the degree of profanity, and so on.
