import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002447990145")) # তোমার DB Channel ID দাও
    SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
    SHORTLINK_API = os.environ.get('SHORTLINK_API')
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    # এখানে ভুল ছিল: যদি চ্যানেল পাবলিক হয় তবে @ দিয়ে নাম দাও, নাহলে ID দাও
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002251392657") 
    
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002251392657")
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
    
    # এটি খালি থাকলে অনেক সময় এরর দেয়, তাই [] ডিফল্ট রাখা ভালো
    OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
    
    ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too.

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Developer:** [Jeet](https://t.me/allfreecoursesforfree) 
│
├🔹 **Bot Support:** [Support](https://t.me/allfreecoursesforfree)
│
├🔸 **Bot Updates:** [Channel](https://t.me/allfreecoursesforfree)
│
╰──────[ 😎 ]───────────⍟
"""
    
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** [Jeet](https://t.me/allfreecoursesforfree)
 
I am here to provide the best free courses and files.
"""

    HOME_TEXT = """
Hello, [{}](tg://user?id={})

This is a Permanent **FileStore Bot**.

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited.
"""
