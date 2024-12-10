def process_unstructured_data(lines):
    knowledge_list = []
    for line in lines:
        # Replace underscores with spaces and split into components
        knowledge_list.extend([entry.replace("_", " ") for entry in line.split(" ")])
    return knowledge_list

# Example unstructured data

address="raw/"

name="dev.src"
# Process the data into a list
with open(address+name,"r") as f:
    lines = [line.rstrip('\n') for line in f]
knowledge_list = process_unstructured_data(lines)

input_file = address+name+"fa.txt"
output_file = address+name+"1"+"txt"

with open(address+name+"fa.txt", 'w') as file:
    # Join the list elements into a single string with a newline character
    data_to_write = '\n'.join(knowledge_list)

    # Write the data to the file
    file.write(data_to_write)

# with open(input_file, "r") as file:
#     lines = file.readlines()
#
# with open(output_file, "w") as file:
#     for line in lines:
#         if line.strip():  # Checks if the line is not empty
#             file.write(line)
#
# # Using "with open" syntax to automatically close the file
#
# with open(output_file ,"r") as f:
#      lines = [line.rstrip('\n') for line in f]
#
# setlines=set(lines)
# lines=list(setlines)
# #lines = list(dict.fromkeys(lines))
# with open(output_file+".txt", "w") as file:
#     for line in lines:
#         if line.strip():  # Checks if the line is not empty
#             file.write(line+"\n")
