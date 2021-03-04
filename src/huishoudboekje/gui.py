import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text="Hello, huishoudboekje!",
    background="#34A2FE",
    width=100,
    height=10
)

label = tk.Label(text="Name: ")
entry = tk.Entry(fg="yellow", bg="#34A2FE", width=100)

button = tk.Button(
    text="Click me!",
    width=100,
    height=5,
    bg="#34A2FE",
    fg="yellow",
)

name = entry.get()
print(name)

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()



greeting.pack()
label.pack()
entry.pack()
button.pack()



window.mainloop()

#Label 	    A widget used to display text on the screen
#Button 	A button that can contain text and can perform an action when clicked
#Entry 	    A text entry widget that allows only a single line of text
#Text 	    A text entry widget that allows multiline text entry
#Frame 	    A rectangular region used to group related widgets or provide padding between widgets