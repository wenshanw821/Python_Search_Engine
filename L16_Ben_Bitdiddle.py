def add_to_index(index, keyword, url):
    print('Hello World!')
    # for entry in index:
    #     if entry[0] == keyword:
    #         entry[1].append(url)
    #         return
    # # not found, add new keyword to index
    # index.append([keyword, [url]])

    index.append([keyword, url])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

index = []
# print(add_to_index(index,'udacity','http://udacity.com'))
print(lookup(index,'udacity'))
