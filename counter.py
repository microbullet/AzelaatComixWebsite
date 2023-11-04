import os

folder_path = './comics'  # Replace with the actual folder path

files = os.listdir(folder_path)
file_count = len(files)

with open('file_count.txt', 'w') as file:
    file.write(str(file_count))