import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key=""
)
def is_last_message_from_sender(chat_log,sender_name=""):
  #split the chatlog into indivisual messages
  messages = chat_log.strip().split("/2025] ")[-1]
  if sender_name in messages:
    return True
  return False



# Step 1: Click on the icon
pyautogui.click(1158,1063 )
time.sleep(1)

while True:
  # Give user time to switch to the right screen
  time.sleep(2)

  # Step 2: Drag to select text
  pyautogui.moveTo(1459, 487)
  pyautogui.dragTo(1436,863 , duration=1, button='left')
  time.sleep(2)

  # Step 3: Copy the selected text
  pyautogui.hotkey('ctrl', 'c')
  time.sleep(2)
  pyautogui.click(1409,849)

  # Step 4: Get text from clipboard
  chat_History = pyperclip.paste()

  print(chat_History)
  
  if is_last_message_from_sender(chat_History):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
        {"role": "user", "content": ""},
        {"role": "user", "content": chat_History }
      ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)

    #Step 5: click at the coordinates
    pyautogui.click(1619, 801)
    time.sleep(1)

    # Step 6: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Step 7: Press send
    pyautogui.hotkey('ctrl', 'enter')
