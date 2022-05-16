# first part ETL process of technical test

# Function for Extraction step
def reader(path):
    with open(path, "r+") as f:  # open the file from any directory
        content = f.read()  # read the file into "content" variable
        f.close()
        print("Extract part is done.")  # notification
        return content


# Function for transformation step
def transformer1(content):
    transformed_content = content.upper()  # Convert the content into Uppercase (Capitalize)
    print("Transform part is done.")  # notification
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
transformed_content = transformer1(content)      # Transformer1 function is called
path2 = input("Provide the path of the file in which you want to load the content:")
writer(path2, transformed_content)    # Writer function is called
