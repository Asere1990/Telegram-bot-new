import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 Token del bot
TOKEN = '7898142673:AAHSHjtleMrgdi_ZOduDuRHc3V4x6B5KqAA'

# 🖼️ Imagen que se mostrará
IMAGE_URL = 'https://i.postimg.cc/MGQf6tKG/IMG-8234.jpg'

# 🔗 Enlace del botón "DESBLOQUEAR"
BOTON_URL = 'https://t.me/share/url?url=https://t.me/jineteras'

# Inicializar bot
bot = telebot.TeleBot(TOKEN)

# 🔘 Crear botonera
def crear_botonera():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url=BOTON_URL),
        InlineKeyboardButton("¿Cómo desbloquear?", callback_data="mostrar_info")
    )
    return markup

# 📩 Comando /start
@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    if message.chat.type == "private":
        bot.send_photo(
            message.chat.id,
            IMAGE_URL,
            caption=None,  # Sin texto debajo de la imagen
            reply_markup=crear_botonera()
        )

# 💬 Manejar botón "¿Cómo desbloquear?"
@bot.callback_query_handler(func=lambda call: True)
def manejar_callback(call):
    if call.data == "mostrar_info":
        bot.answer_callback_query(
            call.id,
            "𝐏𝐫𝐞𝐬𝐢𝐨𝐧𝐚 𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑 𝐲 𝐬𝐞𝐥𝐞𝐜𝐜𝐢𝐨𝐧𝐚 𝟑 𝐆𝐑𝐔𝐏𝐎𝐒 𝐆𝐑𝐀𝐍𝐃𝐄𝐒.",
            show_alert=True
        )

# 🟢 Mantener el bot corriendo
bot.infinity_polling()
