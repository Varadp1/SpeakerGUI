import tkinter as tk 
import pyttsx3


def speak(audio):
	engine = pyttsx3.init("sapi5")
	voices = engine.getProperty("voices")
	engine.setProperty('voice',voices[0].id)
	engine.say(audio)
	engine.runAndWait()

def speaker():
	t = entry.get()
	speak(t)
	print(type(entry))
	entry.delete(0,"end")

	

root = tk.Tk()
root.title("Speak")
root.geometry("500x270")
root.minsize(500,270)
root.maxsize(500,270)

entry = tk.Entry(root,font="lucida 12", relief="sunken",width=30)
entry.grid(row=0,column=1)
tk.Label(text="Write something: ").grid(row=0,column=0)
tk.Button(text="Press this to submit.",padx=20,pady=20,command=speaker).grid(row=1,column=1)

root.mainloop()