from commands.message_template import Message_Template
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

DISABLE_WEB_PAGE_PREVIEW = None # True or False
REPLY_TO_MESSAGE_ID = None
DISABLE_NOTIFICATION = None 
PARSE_MODE = 'html'

COMMAND_TEXT_AUTHOR = 'Want to have your own bot? Write me: @grnbows'

REPLY_MARKUP = InlineKeyboardMarkup(row_width=1)

teleg_button = InlineKeyboardButton(text='@grnbows', url='https://t.me/grnbows')

REPLY_MARKUP.add(teleg_button)


def construct_message(message):
	if message.chat.type == 'private':
		msg = Message_Template(
				chat_id = message.chat.id,
				text = f'''Info about {message.chat.first_name} {message.chat.last_name} - @{message.chat.username}:

				user_id: {message.from_user.id}
				user_laguage_code: {message.from_user.language_code} 
				chat_id: {message.chat.id}
				chat_type: {message.chat.type}
				timestamp: {message.date}
				''', 

				disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW,
				reply_to_message_id=REPLY_TO_MESSAGE_ID, 
				reply_markup=REPLY_MARKUP,
				parse_mode=PARSE_MODE, 
				disable_notification=DISABLE_NOTIFICATION, 
				timeout=None
			)

	elif message.chat.type == 'group':
		msg = Message_Template(
				chat_id = message.chat.id,
				text = f'''Info about {message.chat.title}.\nCalled by {message.from_user.first_name} {message.from_user.last_name} - @{message.from_user.username}:

				chat_id: {message.chat.id}
				chat_type: {message.chat.type}
				called_user_id: {message.from_user.id}
				is_bot: {message.from_user.is_bot}
				user_laguage_code: {message.from_user.language_code} 
				all_members_are_administrators: {message.chat.all_members_are_administrators}
				timestamp: {message.date}
				''', 

				disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW,
				reply_to_message_id=REPLY_TO_MESSAGE_ID, 
				reply_markup=REPLY_MARKUP,
				parse_mode=PARSE_MODE, 
				disable_notification=DISABLE_NOTIFICATION, 
				timeout=None
			)

	return msg

