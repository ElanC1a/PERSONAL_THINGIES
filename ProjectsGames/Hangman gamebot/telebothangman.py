import types
import telebot
from words import words
import random
from hangman_visual import lives_visual_dict
import string

bot=telebot.TeleBot("5456092600:AAEaIx2jZNofipUq6v9o69RVOpk5WGObuI0")

lives=7

def get_word(words):
    word=random.choice(words)  #choosing randomly the word
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()  

@bot.message_handler(commands=["about"])
def about(message):
    bot.send_message(message.chat.id, "Created by Murat A\nIt is a hangman game containing 2465 words\nThe list is being updated constantly")

@bot.message_handler(commands=["start"])
def start(message):
    global word,lives
    word=get_word(words)
    secret_word=set(word) #seperated letter in word
    alphabet=set(string.ascii_uppercase) #{'L', 'V', 'M', 'G', 'S', 'W', 'J', 'K', 'Q', 'A', 'E', 'R', 'U', 'N', 'D', 'H', 'I', 'Y', 'T', 'F', 'O', 'Z', 'C', 'X', 'B', 'P'}    
    used_letters=set()  #letters used by user
    
    #lives=7

    while len(secret_word)>0 and lives>0:
        word_list=[letter if letter in used_letters else "-" for letter in word] #W - A B
        bot.send_message(message.chat.id,(f"You have: {lives} lives left\nYou have used these letters: ", " ".join(used_letters)))
        
        bot.send_message(message.chat.id,f'. {lives_visual_dict[lives]}')
        bot.send_message(message.chat.id,("Current word: ", " ".join(word_list)))
        
        # keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_letter=bot.send_message(message.chat.id,("Guess a letter: ".upper()))  #reply_markup=keyboard
    
        if user_letter in alphabet-used_letters:  #why alphabet-used_letters
            used_letters.add(user_letter)
            if user_letter in secret_word:
                secret_word.remove(user_letter)
                bot.send_message(message.chat.id,"")
            else:
                lives=lives-1
                bot.send_message(message.chat.id,"\nThere is no such letter")
        elif user_letter in used_letters:
            bot.send_message(message.chat.id,"\nYou already used this letter")
        else:
            bot.send_message(message.chat.id,"\nSeriously? 😑\nINVALID INPUT!!!")
        
    if lives==0:
        bot.send_message(message.chat.id,f'. {lives_visual_dict[lives]}')
        bot.send_message(message.chat.id,"Too bad, you died\nThe word was: %s" %word)
    else:
        bot.send_message(message.chat.id,"Good job, Mr.Dictionary\nYou guessed the word: %s" %word)
bot.polling(non_stop=True)