file_name = "filename.jar"
extension_type = ""
for index in range(len(file_name) -1 ):
    if file_name[index] == '.':
        extension_type = file_name[index:]
print(extension_type)