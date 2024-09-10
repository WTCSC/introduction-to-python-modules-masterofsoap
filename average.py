from text_utils import count_words # Imports the code from the text_utils.py module I made
import sys # Imports the code from a preset module that is a list of directories and provides access to some variables

def average_words_per_line(file_path): # Creates our main variable
    with open(file_path, 'r') as file: # Opens the given file
        lines = file.readlines() # Counts the number of lines

    if lines: # Checks to make sure the list of lines is not empty
        total_words = sum(count_words(line) for line in lines) # Defines total words by using the count_words function from my test_utils module to cound the ammount of words
        average =  total_words / len(lines) # Calculates the average words per line
        print(f"Average words per line: {average:.0f}") # Prints the output
    else:
        average = 0 # If there are no lines, set the average to 0

if __name__ == "__main__": # Checks if the script is being run directly (Not as a module)
    if len(sys.argv) > 1: # Checks if a file path arguement was provided
        average_words_per_line(sys.argv[1]) # Calls the the function with the provided file path and stores the result
    else:
        print("Usage: python3 average.pv <file_path>") # I mostly needed something for the else statement. This prints the proper instructions if no file path is found