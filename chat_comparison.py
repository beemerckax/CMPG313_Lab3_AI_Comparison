import tkinter as tk
from tkinter import scrolledtext

def compare_chats():
    user_msg = entry.get()
    if not user_msg:
        return
    
    # ELIZA side logic (Rule-based)
    eliza_display.insert(tk.END, f"You: {user_msg}\n")
    if "mother" in user_msg.lower():
        eliza_display.insert(tk.END, "ELIZA: Who else in your family is strict?\n\n")
    elif "tired" in user_msg.lower():
        eliza_display.insert(tk.END, "ELIZA: Did you come to me because you are tired?\n\n")
    else:
        eliza_display.insert(tk.END, "ELIZA: Please elaborate on that.\n\n")

    # LLM side logic (Generative)
    llm_display.insert(tk.END, f"You: {user_msg}\n")
    if "mother" in user_msg.lower():
        llm_display.insert(tk.END, "LLM: Having a strict parent can be difficult.\n\n")
    elif "tired" in user_msg.lower():
        llm_display.insert(tk.END, "LLM: I understand. Rest is crucial for health.\n\n")
    else:
        llm_display.insert(tk.END, "LLM: That is interesting. Tell me more about your thoughts.\n\n")
    
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Past vs Present AI - ELIZA vs LLM")

main_label = tk.Label(root, text="AI Comparison Lab: ELIZA vs LLM", font=("Arial", 14, "bold"))
main_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

eliza_frame = tk.LabelFrame(frame, text=" [ ELIZA (Past AI) ] ")
eliza_frame.pack(side=tk.LEFT, padx=10)
eliza_display = scrolledtext.ScrolledText(eliza_frame, width=30, height=15)
eliza_display.pack()
eliza_display.insert(tk.END, "ELIZA ready.\n\n")

llm_frame = tk.LabelFrame(frame, text=" [ LLM (Present AI) ] ")
llm_frame.pack(side=tk.LEFT, padx=10)
llm_display = scrolledtext.ScrolledText(llm_frame, width=30, height=15)
llm_display.pack()
llm_display.insert(tk.END, "LLM ready.\n\n")

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)
tk.Label(entry_frame, text="Type your message here:").pack(side=tk.LEFT)
entry = tk.Entry(entry_frame, width=40)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(entry_frame, text="Compare", command=compare_chats).pack(side=tk.LEFT, padx=2)
tk.Button(entry_frame, text="Clear", command=lambda: [eliza_display.delete('1.0', tk.END), llm_display.delete('1.0', tk.END)]).pack(side=tk.LEFT, padx=2)

root.mainloop()
