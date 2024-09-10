def count_chars(text): # Defines the character count variable
    return len(text) # Returns the count of each character

def count_words(text): # Defines the word count variable
    return len(text.split()) # Splits each sentence and returns the word count

def count_sentences(text): # Defines the sentence count variable
    sentence_endings = '.?!' # Defines what ends a sentence
    count = 0 # Sets up the count variable
    for char in text: #                } \
        if char in sentence_endings: # } --> Looks at each set of words and looks for ?, ., or ! then when it finds one, it adds one to the count.
            count += 1 #               } /
    
    return count # Returns the count of sentences