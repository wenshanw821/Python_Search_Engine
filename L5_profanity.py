from urllib import request
from urllib import parse

def read_text():
    string = (r"C:\Users\Wenshan Wang\OneDrive\Documents\Online Learning"
        r"\Udacity\Programming Fundations with Python"
        r"\Proj_profanity_check\data_scientist_weekly.txt") # use \ or parenthesis to break the long line
    quotes = open(string)
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):

    # check each word:
    text_string = text_to_check.split('.')
    # print(text_string)

    for word in text_string:
        # print('Checking ...', word)
        if check_profanity_word(word):
            print('Please check the word - ', word)
            return


def check_profanity_word(text_to_check):
    # in Python version 3, parsing the string is required in order to send the website a request.
    url = "http://www.wdylike.appspot.com/?q="
    query = parse.quote(text_to_check)

    #open the url and read the output
    connection = request.urlopen(url+query)
    output = connection.read()
    output_str = bytes.decode(output)
    connection.close()

    if output_str == 'true':
        return True
    else:
        return False

read_text()
