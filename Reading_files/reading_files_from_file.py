
file_path = "C:\\Users\\Acer\\OneDrive\\Desktop\\3111Final\\Reading_files\\reading_files_from_file.txt"
line_data = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace("\n", "")
        line_dat = line.split(" ")
        line_data.append(line_dat)

print(line_data)