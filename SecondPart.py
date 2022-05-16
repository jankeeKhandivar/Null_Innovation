# Second part ETL process of technical test

# Function for Extraction step
def reader(path):
    with open(path,"r+") as f: # open the file from any directory
        content = f.read()     # read the file into "content" variable
        f.close()
        print("Extract part is done.")    # notification
        return content

# Function for transformation step
def transformer2(content):
    content = content.lower()     # convert the content into lower case
    transformed_content = str()   # A variable for storing the transformed content
    lst = list()                  # A list of words
    for line in content.split():  # iterate through each line
        line = line.rstrip()
        words = line.split(" ")   # separate the words
        for word in words:
            if word in lst: continue     # Remove duplicates
            lst = lst + words
    for word in lst:             # iterate through words
        word_count = content.count(word)      # count the occurrences
        string1 = word + "->" + str(word_count)
        transformed_content = transformed_content + "\n" + string1
    print("Transform part is done.")    # notification
    return transformed_content

# Function for Load step
def writer(path, transformed_content):
    f = open(path, "r+")  # Open the file for writing the data
    f.truncate(0)  # clear the contents of the file (if any)
    f.write(transformed_content)  # write the transformed content into the file
    f.close()
    print("Load part is done.")  # notification

# main program
path1 = input("Provide the path of the file from which you want to extract the content:")
content = reader(path1)      # reader function is called
transformed_content = transformer2(content)      # Transformer2 function is called
path2 = input("Provide the path of the file in which you want to load the content:")
writer(path2, transformed_content)    # Writer function is called
