import webbrowser
base="https://api.whatsapp.com/send?text="
text=input("pleasse enter text to send\n")
webbrowser.open(base+text)