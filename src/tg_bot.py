import telebot

bot = telebot.TeleBot('6044258227:AAGQ7qgaB_Mcje2RcsGgtxnDu88RlHSEmig')
report_id = '-971539932'


def send_post(message):
    bot.send_message(report_id, message, parse_mode='html')
