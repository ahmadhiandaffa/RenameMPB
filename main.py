import shutil
import os
import csv
import tkinter
import patoolib
import tkinter

# Show message dialog for choosing files
submission_file = tkinter.filedialog.askopenfilename(title="Pilih file submission (.zip)")
grader_file     = tkinter.filedialog.askopenfilename(title="Pilih file grader")
extract_dir     = tkinter.filedialog.askdirectory(title="Pilih folder untuk extract")

# Unzip submission file
shutil.unpack_archive(filename, extract_dir)

# Remove unnecessary folder name part
folders = os.listdir(extract_dir)
for folder in folders:
    old_name = folder
    old_path = os.path.join(extract_dir, old_name)
    new_name = folder.split("_")[0]
    new_path = os.path.join(extract_dir, new_name)
    os.rename(old_path, new_path)

# Read grader file
with open(grader_file) as fp:
    reader = csv.reader(fp)
    next(reader, None)  # skip the headers
    student_list = [row for row in reader]

# Add NRP & grader to folder name
for student in student_list:
    nrp, name, grader = student

    old_name = name
    old_path = os.path.join(extract_dir, old_name)
    new_name = grader + "_" + nrp[-3:] + "_" + name 
    new_path = os.path.join(extract_dir, new_name)
    os.rename(old_path, new_path)

# Extract file in each folder
folders = os.listdir(extract_dir)
for folder in folders:
    folder_path = os.path.join(extract_dir, folder)
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        _, extension = os.path.splitext(file)
        if extension == ".zip":
            print(file)
            shutil.unpack_archive(file_path, format="zip", extract_dir=folder_path)
            os.remove(file_path) 
        else:
            continue