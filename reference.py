PLACEHOLDER = "[NAME]"

#
# with open("letter_1.txt") as names_file:
#     names = names_file.readlines()
#
# with open("letter_3.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
# #

with open('letter_3.txt', 'r') as file :
  filedata = file.read()
print(filedata)
# Replace the target string
filedata = filedata.replace(PLACEHOLDER, 'abcd')

# Write the file out again
with open('letter_3.txt', 'w') as file:
  file.write(filedata)


print(filedata)



# # creating a variable and storing the text
# # that we want to search
# search_text = "dummy"
#
# # creating a variable and storing the text
# # that we want to add
# replace_text = "replaced"
#
# # Opening our text file in read only
# # mode using the open() function
# with open(r'SampleFile.txt', 'r') as file:
#     # Reading the content of the file
#     # using the read() function and storing
#     # them in a new variable
#     data = file.read()
#
#     # Searching and replacing the text
#     # using the replace() function
#     data = data.replace(search_text, replace_text)
#
# # Opening our text file in write only
# # mode to write the replaced content
# with open(r'SampleFile.txt', 'w') as file:
#     # Writing the replaced data in our
#     # text file
#     file.write(data)
#
# Printing Text replaced
if month in dataset['month'].values and day in dataset['day'].values:
  ds = dataset[(dataset['month'] == month) & (dataset['day'] == day)]
  a = ds.to_dict('records')
  for i in a:
    ram = random.choice(lists)
    s = i['name']
    y = i['email']
    with open(ram, 'r') as file:
      filedata = file.read()
    filedata = filedata.replace(PLACEHOLDER, s)
    with open('letter_3.txt', 'w') as file:
      file.write(filedata)
      print(filedata)
    sendmail(y, filedata)
    ########################################################################
    with open(ram, 'r') as file:
      filedata = file.read()
    filedata = filedata.replace(s, PLACEHOLDER)
    with open('letter_3.txt', 'w') as file:
      file.write(filedata)
    print(s, y)
