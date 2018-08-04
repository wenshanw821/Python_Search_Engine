# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return index
    index.append([keyword,[url]])
    return index

def add_page_to_index(index,url,content):
    keyword = content.split()
    for element in keyword:
        add_to_index(index,element,url)

    return index

add_page_to_index(index,'fake.text',"This is a test")
print(index)
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
