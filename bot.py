import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from db import *



TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

# =============== START ===============

HELP_TEXT = """
<b>WELCOME</b> 🎉🎉🎉
Welcome to the demo bot of Yasserius!

My name is Yasser Aziz and I am a software developer.

If you wish to hire me, please feel free to contact me here:
https://t.me/yasseriiius

<b>DEMO BOT FEATURES</b>

/help or /hello - Get description of bot and all its commands

<b>TODO APP</b>
/add        - Add a todo for the bot to remember
/todos      - View a list of todos
/delete     - Delete a todo
"""

def help_command(bot, message):
    bot.send_message(message.chat.id, HELP_TEXT)

@bot.message_handler(commands=['start', 'help', 'hello'])
def start_command(message):
    help_command(bot, message)

# =============== OTHER ===============

def other_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Help", callback_data="cb_help"))
    return markup

# =============== CALLBACKS ===============

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print(call, '\n\n\n')
    # {'id': '7859808722370334414', 'from_user': {'id': 1830004323, 'is_bot': False, 'first_name': 'Yasser', 'username': 'yasseriiius', 'last_name': None, 'language_code': 'en', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}, 'message': {'content_type': 'text', 'id': 9011, 'message_id': 9011, 'from_user': <telebot.types.User object at 0x000001E0A698D330>, 'date': 1709350331, 'chat': <telebot.types.Chat object at 0x000001E0A698D360>, 'sender_chat': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': "*Here's how to use this bot*\n\n- Add an alert: /add 0xAddress...\n- See all alerts: /alerts", 'entities': [<telebot.types.MessageEntity object at 0x000001E0A698D4B0>, <telebot.types.MessageEntity object at 0x000001E0A698D450>], 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': <telebot.types.InlineKeyboardMarkup object at 0x000001E0A698D300>, 'message_thread_id': None, 'is_topic_message': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'users_shared': None, 'chat_shared': None, 'story': None, 'external_reply': None, 'quote': None, 'link_preview_options': None, 'giveaway_created': None, 'giveaway': None, 'giveaway_winners': None, 'giveaway_completed': None, 'forward_origin': None, 'boost_added': None, 'sender_boost_count': None, 'reply_to_story': None, 'json': {'message_id': 9011, 'from': {'id': 5777692794, 'is_bot': True, 'first_name': 'YeeeTestBot', 'username': 'yeee_test_bot'}, 'chat': {'id': 1830004323, 'first_name': 'Yasser', 'username': 'yasseriiius', 'type': 'private'}, 'date': 1709350331, 'text': "*Here's how to use this bot*\n\n- Add an alert: /add 0xAddress...\n- See all alerts: /alerts", 'entities': [{'offset': 46, 'length': 4, 'type': 'bot_command'}, {'offset': 82, 'length': 7, 'type': 'bot_command'}], 'reply_markup': {'inline_keyboard': [[{'text': 'Add alert', 'callback_data': 'cb_add'}], [{'text': 'See all alerts', 'callback_data': 'cb_alerts'}]]}}}, 'inline_message_id': None, 'chat_instance': '-7519837507589548955', 'data': 'cb_alerts', 'game_short_name': None, 'json': {'id': '7859808722370334414', 'from': {'id': 1830004323, 'is_bot': False, 'first_name': 'Yasser', 'username': 'yasseriiius', 'language_code': 'en'}, 'message': {'message_id': 9011, 'from': {'id': 5777692794, 'is_bot': True, 'first_name': 'YeeeTestBot', 'username': 'yeee_test_bot'}, 'chat': {'id': 1830004323, 'first_name': 'Yasser', 'username': 'yasseriiius', 'type': 'private'}, 'date': 1709350331, 'text': "*Here's how to use this bot*\n\n- Add an alert: /add 0xAddress...\n- See all alerts: /alerts", 'entities': [{'offset': 46, 'length': 4, 'type': 'bot_command'}, {'offset': 82, 'length': 7, 'type': 'bot_command'}], 'reply_markup': {'inline_keyboard': [[{'text': 'Add alert', 'callback_data': 'cb_add'}], [{'text': 'See all alerts', 'callback_data': 'cb_alerts'}]]}}, 'chat_instance': '-7519837507589548955', 'data': 'cb_alerts'}} 
    if call.data == "cb_help":
        help_command(bot, call.message)
    elif call.data == "cb_add":
        handle_new_todo(bot, call.message)
    elif call.data == "cb_todos":
        handle_show_todos(bot, call.message)
    elif call.data[:9] == "cb_delete":
        handle_delete_todo(bot, call.message, call.data)
    bot.answer_callback_query(call.id)

# =============== ADD ===============

def process_new_todo(message):
    todo_dict = {
        "telegram_id": message.chat.id,
        "text": message.text[:100]
    }
    add_new_todo(todo_dict)
    bot.reply_to(message, "Todo added. See /todos for all todos.")

def handle_new_todo(bot, message):
    msg = bot.reply_to(message, "Please provide the todo text:")
    bot.register_next_step_handler(msg, process_new_todo)

@bot.message_handler(commands=['add'])
def add_command(message):
    handle_new_todo(bot, message)

# =============== TODOS ===============

def add_todos_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Add todo", callback_data="cb_add"))
    return markup

def handle_show_todos(bot, message):
    todos = get_todos_by_telegram_id(message.chat.id)
    if todos:
        # print(todos)
        todos_strings = []
        for i, todo in enumerate(todos):
            todos_strings.append(f"{i+1}. {todo[2]}")
        message_str = """\
ALL TODOS:

{}""".format('\n\n'.join(todos_strings))
        bot.send_message(message.chat.id, message_str)
    else:
        bot.send_message(message.chat.id, "No todos found.", reply_markup=add_todos_markup())

@bot.message_handler(commands=['todos'])
def show_alerts(message):
    handle_show_todos(bot, message)

# =============== DELETE ===============

def delete_markup(todos):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for todo in todos:
        markup.add(InlineKeyboardButton(
            todo[2], 
            callback_data="cb_delete_{}".format(todo[0]))
        )
    return markup

@bot.message_handler(commands=['delete'])
def delete_command(message):
    todos = get_todos_by_telegram_id(message.chat.id)
    if todos:
        bot.send_message(
            message.chat.id, 
            "Which todo would you like to delete?", 
            reply_markup=delete_markup(todos)
        )
    else: 
        bot.send_message(message.chat.id, "No todos found. Add todos with /add command.")

def handle_delete_todo(bot, message, call_data):
    id = call_data.split('_')[-1]
    try:
        delete_todo_by_id(id, message.chat.id)
        bot.send_message(message.chat.id, "Todo deleted.")
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Oops! Something went wrong. Please try deleting todo again.')

# =============== OTHER ===============

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Not sure what you mean. Need help?", reply_markup=other_markup())

bot.infinity_polling()
