from tkinter import *
from tkinter import ttk
import os
import customtkinter as ctk


# main window
root=ctk.CTk()
root.title('Create a Config file')

# the main frame
mainframe = ctk.CTkFrame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# input path entry
input_path = StringVar()
input_entry = ctk.CTkEntry(mainframe, width=300, textvariable=input_path,)
input_entry.grid(column=1, row=2, sticky=(W, E))
input_path = str(input_path)


# input path text
text1 = 'Input Path(Remember to use \'/\' instead of \'\\\')'
input_path_txt = ctk.CTkLabel(mainframe,text=text1)
input_path_txt.grid(column = 1, row = 1,sticky=(W,E))

# output path entry
output_path = StringVar()
output_entry = ctk.CTkEntry(mainframe, width=300, textvariable=output_path)
output_entry.grid(column=1, row=4, sticky=(W, E))
output_path = str(output_path)


# output path text
text2= 'Output Path(Remember to use \'/\' instead of \'\\\')'
output_path_txt = ctk.CTkLabel(mainframe,text=text2)
output_path_txt.grid(column=1,row=3,sticky=(W,E))

render_overworld = True
overworld_chkbox = ctk.CTkCheckBox(root, text = 'Render Overworld', variable = None)
overworld_chkbox.grid(row = 5, column = 1)

#start main loop
root.mainloop()
