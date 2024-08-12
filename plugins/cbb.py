#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b><blockquote>╭───────────⍟
├➤ ᴏᴡɴᴇʀ : <a href='t.me/'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/outlawbots>ᴏᴜᴛʟᴀᴡ ʙᴏᴛs</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ : <a href=https://t.me/ifeelscam>ᯓ ɪɴᴠᴀʟɪᴅ ᡣ𐭩</a>
├➤ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me/ifeelscam>ʜᴀᴍᴢᴀ</a>
╰───────────────⍟</blockquote></b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data ="source"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , callback_data = "main")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ sʜᴏʀᴛs 𝟷𝟾+ ᴠɪᴅᴇᴏs", url = "https://t.me/UnseenRobot/shorts")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
        
    elif query.data == "plan":
        btn = [[
            InlineKeyboardButton(' Send Payment Screenshot (ADMIN)', url="t.me/UnseenAdmin")
        ],[
            InlineKeyboardButton(' ᴄʟᴏꜱᴇ ', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(btn)
        await query.message.reply_photo(
            photo=("https://graph.org/file/30f2719bec632aad4e5be.jpg"),
            caption=message_content.format(
                first = query.from_user.mention, 
                second = query.from_user.mention
        ),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "main":
        await query.message.edit_text(
            text=f"<blockquote>ʜᴇʟʟᴏ ᴍʏ ᴜsᴇʀs ᴍʏ ᴜᴘᴅᴀᴛᴇ & ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/InkaLinks"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url = "t.me/outlawbots")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"), 
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"<b><blockquote>👋 Hey {query.from_user.mention}\n\nI'm advance bot of providing videos for @InkaLinks Channel!!..</blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton(text="🏖️", callback_data="about"),
                    InlineKeyboardButton(text="🍂", callback_data="about"),
                    InlineKeyboardButton(text="⚠️", callback_data="me"),
                    InlineKeyboardButton(text="💸", callback_data="about"),
                    InlineKeyboardButton(text="🎭", callback_data="about"),
                ],[ InlineKeyboardButton( "ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", callback_data = "main" ),
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", callback_data = "source")
                ], [ InlineKeyboardButton("ᴡᴀᴛᴄʜ sʜᴏʀᴛs 𝟷𝟾+ ᴠɪᴅᴇᴏs", url = "http://t.me/UnseenRobot/shorts") ],
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>ᴛʜɪs sᴇᴄᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs & ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [  InlineKeyboardButton("ᴅᴇᴠʟᴏᴘᴇʀ",url= "t.me/ifeelscam"),
                         InlineKeyboardButton("ᴀᴅᴍɪɴ",url = "t.me/UnseenAdmin")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    elif data == "source":
        await query.message.edit_text(
            text=f"<b><blockquote>ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ\nɪɴ ᴛᴡᴏ ᴡᴀʏs\n★ <a herf='https://publicearn.com/GitHub'>ɢɪᴛʜᴜʙ</a> \n★ <a herf='https://t.me/+Yy9O2e_eJwU3NjRl'>ᴢɪᴘ ғɪʟᴇ </a></blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ɢɪᴛʜᴜʙ ", url="https://publicearn.com/GitHub"),
                        InlineKeyboardButton("ᴢɪᴘ ғɪʟᴇ",url="https://t.me/+Yy9O2e_eJwU3NjRl")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ" , callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
