import tkinter as tk
from tkinter import scrolledtext
from assistant_client import client, assistant, create_thread, send_message
from prompt_formatter import format_prompt
from openai import AssistantEventHandler

class MnemoroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mnemoro Copilot Prototype")
        self.thread = create_thread()

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80)
        self.chat_display.pack(padx=10, pady=10)

        self.chat_display.tag_configure("user", foreground="blue")
        self.chat_display.tag_configure("mnemoro", foreground="green")

        self.entry = tk.Entry(root, width=80)
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.send)

        self.send_button = tk.Button(root, text="Enviar", command=self.send)
        self.send_button.pack()

    def send(self, event=None):
        user_msg = self.entry.get()
        if not user_msg.strip():
            return

        self.chat_display.insert(tk.END, f"\nVocê > {user_msg}\n")
        self.entry.delete(0, tk.END)

        prompt = format_prompt(user_msg)
        send_message(self.thread.id, prompt)

        with client.beta.threads.runs.stream(
            thread_id=self.thread.id,
            assistant_id=assistant.id,
            instructions="Você é o assistente virtual da startup Mnemoro...",
            event_handler=GUIEventHandler(self.chat_display),
            top_p=0.2
        ) as stream:
            stream.until_done()

        self.thread = create_thread()

class GUIEventHandler(AssistantEventHandler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def on_text_created(self, text):
        self.text_widget.insert(tk.END, "\nMNEMORO ASSISTANT > ")

    def on_text_delta(self, delta, snapshot):
        self.text_widget.insert(tk.END, delta.value)
        self.text_widget.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MnemoroGUI(root)
    root.mainloop()
