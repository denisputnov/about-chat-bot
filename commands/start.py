from commands.message_template import Message_Template
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

DISABLE_WEB_PAGE_PREVIEW = None # True or False
REPLY_TO_MESSAGE_ID = None
DISABLE_NOTIFICATION = None 
PARSE_MODE = 'html'

COMMAND_TEXT_PRIVATE = 'Hi, use /info to get full info about this chat.\nI can work not only in personal chats. Add me in group chat to get info about this one.'
COMMAND_TEXT_GROUP = 'Hi, use /info to get full info about this chat.\nI can work not only in group chats. Just write me personally to get all info about your account.'

REPLY_MARKUP = None

def construct_message(msg):
	if msg.chat.type == 'private':
		message = Message_Template(
				chat_id = msg.chat.id,
				text = COMMAND_TEXT_PRIVATE, 

				disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW,
				reply_to_message_id=REPLY_TO_MESSAGE_ID, 
				reply_markup=REPLY_MARKUP,
				parse_mode=PARSE_MODE, 
				disable_notification=DISABLE_NOTIFICATION, 
				timeout=None
			)

	elif msg.chat.type == 'group':
		message = Message_Template(
				chat_id = msg.chat.id,
				text = COMMAND_TEXT_GROUP, 

				disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW,
				reply_to_message_id=REPLY_TO_MESSAGE_ID, 
				reply_markup=REPLY_MARKUP,
				parse_mode=PARSE_MODE, 
				disable_notification=DISABLE_NOTIFICATION, 
				timeout=None
			)

	return message
