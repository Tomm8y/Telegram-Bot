# Created By t.me/Tomm8yy .

import telebot

# Initialize the bot with your API key
bot = telebot.TeleBot("BOT-TOKEN-ID")

# Define inline keyboard buttons
button1 = telebot.types.InlineKeyboardButton("Write our button name 1", url="https://t.me/Tomm8yy") 
            # Put in instead "Write our button name 1" bytton name. ,  #Put in instead "Hi I'm TommY" what is you want url when touch "Connection" button.   
button2 = telebot.types.InlineKeyboardButton("Write Your button name 2", callback_data="Write Your button name 2")
            # Put in instead "Write our button name 2" bytton name. 
button3 = telebot.types.InlineKeyboardButton("Write your button name 3", callback_data="Write Your button name 3")
            # Put in instead "Write our button name 3" bytton name.

# Define inline keyboard markups
markup1 = telebot.types.InlineKeyboardMarkup(row_width=1)
markup1.add(button1, button2, button3)

# Define reply keyboard markups
key_markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
key_markup1.add("created", "by", "TommY") # Write your keyboard button name instead  "created", "by", "TommY" . 

# Handle callback queries
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Write Your button name 2":  #Put in instead "Created By t.me/Tomm8yy" what is you want call back when touch "Write Your button name 2" button.
        bot.send_message(call.message.chat.id, "Created By t.me/Tomm8yy")
    elif call.data == "Write Your button name 3":
        bot.send_message(call.message.chat.id, """
██████████████████████████████████
█─▄─▄─█─▄▄─█▄─▀█▀─▄█▄─▀█▀─▄█▄─█─▄█
███─███─██─██─█▄█─███─█▄█─███▄─▄██
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▀▀""")

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, I'm t.me/Tomm8yy", reply_markup=key_markup1) #Write what do you want when call "strt" cammand.


# Handle /data command
@bot.message_handler(commands=['data'])
def send_data(message):
    bot.reply_to(message, "Write what do you want when call data cammand.", reply_markup=markup1)
#                         "Write what do you want when call data cammand."

# Define a command handler for /sendphoto
@bot.message_handler(commands=['sendphoto'])
def send_photo(message):
    chat_id = message.chat.id
    photo_path1 = r"C:\...jpg"  # Replace with the path to your photo
    photo_path2 = r"C:\...png"

    with open(photo_path1, 'rb') as photo:
        bot.send_photo(chat_id, photo)
    with open(photo_path2, 'rb') as photo:
        bot.send_photo(chat_id, photo)

# Define a command handler for /sendfile
@bot.message_handler(commands=['sendfile'])
def send_file(message):
    chat_id = message.chat.id
    file_path1 = r"O:\...iso"  # Replace with the path to your file
    file_path2 = r"O:\...txt"

    # Open the file in binary mode and send it
    with open(file_path1, 'rb') as file:
        bot.send_document(chat_id, file)
    with open(file_path2, 'rb') as file:
        bot.send_document(chat_id, file)

# Define a command handler for /sendaudio
@bot.message_handler(commands=['sendaudio'])
def send_audio(message):
    chat_id = message.chat.id
    audio_path1 = r"O:\...mp3"  # Replace with the path to your audio
    audio_path2 = r"O:\...mp3"

    with open(audio_path1, 'rb') as audio:
        bot.send_audio(chat_id, audio)
    with open(audio_path2, 'rb') as audio:
        bot.send_audio(chat_id, audio)    

# Define a command handler for /sendvideo
@bot.message_handler(commands=['sendvideo'])
def send_video(message):
    chat_id = message.chat.id
    video_path1 = r"O:\...mp4"  # Replace with the path to your video
    video_path2 = r"O:\...mp4"

    with open(video_path1, 'rb') as video:
        bot.send_video(chat_id, video)
    with open(video_path2, 'rb') as video:
        bot.send_video(chat_id, video)


# Handle regular text messages
@bot.message_handler()
def handle_message(message):
    if message.text == "created":
        bot.send_message(message.chat.id, "Hi, I'm TommY")  # Put in instead "Hi I'm TommY" what is you want when touch "created" keyboard button . 
    elif message.text == "by":
        bot.send_message(message.chat.id, "Hi, I'm TommY")  # Put in instead "Hi I'm TommY" what is you want when touch "by" keyboard button .
    elif message.text == "TommY":
        bot.send_message(message.chat.id, "Hi, I'm TommY")  # Put in instead "Hi I'm TommY" what is you want when touch "TommY" keyboard button .
    
   
# Start polling
bot.infinity_polling()
# Created By TommY.