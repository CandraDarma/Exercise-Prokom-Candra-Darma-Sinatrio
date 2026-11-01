def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(f"Sending: {message}")
        sent_messages.append(message)


messages = ["Halo!", "Apa kabar?", "Sampai jumpa."]
sent_messages = []

send_messages(messages[:], sent_messages)   # kirim salinan list
print(messages)          # list asli tetap utuh
print(sent_messages)
