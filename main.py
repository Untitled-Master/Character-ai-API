import playwright
from characterai import PyCAI

client = PyCAI('Token(value)')
client.start()    # add this - REN
char = 'Char key'

# Save tgt and history_external_id 
# to avoid making a lot of requests
chat = client.chat.get_chat(char)

#history_id = chat['external_id'] #not needed anymore - REN
participants = chat['participants']

# In the list of "participants",
# a character can be at zero or in the first place
if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

while True:
    message = input('You: ')

    data = client.chat.send_message(
        #char, message, history_external_id=history_id, tgt=tgt
        chat['external_id'], tgt, message # modified args - REN
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    print(f"{name}: {text}")
