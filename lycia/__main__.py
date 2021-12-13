from lycia.Lycia import start, lycia, lyciainline
from pyrogram import filters
from lycia import API_ID , API_HASH , TOKEN

LYCIA = Client(
        ':memory:', 
         api_id=API_ID, 
         api_hash=API_HASH,
         bot_token=TOKEN)

if __name__ == "__main__":
    LYCIA.run()
