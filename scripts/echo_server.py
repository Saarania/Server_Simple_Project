import socket
from tkinter import *
"""
HOST = ''  # Standard loopback interface address (localhost)
PORT = 45662        # Port to listen on (non-privileged ports are > 1023)

received_text  = "";

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("Received ",repr(data))
            received_text += repr(data)
            if not data:
                break
            conn.sendall(data)

"""
app = Tk()

label = Label(app, text='<!--  saved from url=(0014)about:internet  -->\n<letter>\n  \n<title maxlength="10"> Quote Letter </title>\n  \n<salutation limit="40">Dear Daniel,</salutation>\n  \n<text>\nThank you for sending us the ', font=('bold',10), pady=20)
label.grid(row=0,column= 0, sticky=W)

app.title("XML tranfer application")
app.geometry("1000x400")
app.mainloop()