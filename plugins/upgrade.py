from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """
𝐁𝐮𝐲   𝐏𝐥𝐚𝐧   𝐀𝐜𝐜.   𝐓𝐨   𝐘𝐨𝐮𝐫   𝐍𝐞𝐞𝐝 !!!


𝟏.   𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 ɢʙ
👉     ꜰʀᴇᴇ
𝟐.   𝐁𝐚𝐬𝐢𝐜  𝐏𝐥𝐚𝐧
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 30/ᴍᴏɴᴛʜ.</a> 
𝟑.   𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝  𝐏𝐥𝐚𝐧 
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 60/ᴍᴏɴᴛʜ.</a>  
𝟒.   𝐏𝐫𝐞𝐦𝐢𝐮𝐦  𝐏𝐥𝐚𝐧 
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 90/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

𝐍𝐎𝐓𝐄 :  ᴀꜰᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ꜱᴇɴᴅ  ꜱᴄʀᴇᴇɴꜱʜᴏᴛ  ᴛᴏ  ᴏᴡɴᴇʀ.
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('sᴇɴᴅ sᴄʀᴇᴇɴ sʜᴏᴛ  ❣️',url='https://t.me/Priyanka_samrottbot')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg')
            ],
                    [
                        InlineKeyboardButton('🔮  ʜᴇʟᴘ',url='https://t.me/Priyanka_samrottbot'),
                        InlineKeyboardButton("🏠   ʜᴏᴍᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await update.message.edit(text = text, disable_web_page_preview=True, reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """
𝐁𝐮𝐲   𝐏𝐥𝐚𝐧   𝐀𝐜𝐜.   𝐓𝐨   𝐘𝐨𝐮𝐫   𝐍𝐞𝐞𝐝 !!!


𝟏.   𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 ɢʙ
👉     ꜰʀᴇᴇ
𝟐.   𝐁𝐚𝐬𝐢𝐜  𝐏𝐥𝐚𝐧
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 30/ᴍᴏɴᴛʜ.</a> 
𝟑.   𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝  𝐏𝐥𝐚𝐧 
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 60/ᴍᴏɴᴛʜ.</a>  
𝟒.   𝐏𝐫𝐞𝐦𝐢𝐮𝐦  𝐏𝐥𝐚𝐧 
👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg'>₹ 90/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

𝐍𝐎𝐓𝐄 :  ᴀꜰᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ꜱᴇɴᴅ  ꜱᴄʀᴇᴇɴꜱʜᴏᴛ  ᴛᴏ  ᴏᴡɴᴇʀ.
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('sᴇɴᴅ sᴄʀᴇᴇɴ sʜᴏᴛ  ❣️',url='https://t.me/Priyanka_samrottbot')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://telegra.ph/file/c7cfd97c873659fe9284e.jpg')
            ],
                    [
                        InlineKeyboardButton('🔮  ʜᴇʟᴘ',url='https://t.me/Priyanka_samrottbot'),
                        InlineKeyboardButton("🏠   ʜᴏᴍᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await message.reply_text(text = text, disable_web_page_preview=True, reply_markup = keybord)
