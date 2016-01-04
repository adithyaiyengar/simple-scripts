import re
from tkinter import filedialog

file_path = filedialog.askopenfilename(title="Choose file.", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
file_name = open(file_path, 'r')
formatted_file = re.sub("<[^>]*>", "\n", file_name.read())
with open("formatted.txt", "w") as form_file:
	form_file.write(formatted_file)