import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 Token del bot
TOKEN = '7898142673:AAHSHjtleMrgdi_ZOduDuRHc3V4x6B5KqAA'
# 🖼️ Imagen que se mostrará
IMAGE_URL = 'https://i.postimg.cc/MGQf6tKG/IMG-8234.jpg'
# 🔗 Enlace del botón "DESBLOQUEAR"
BOTON_URL = 'https://t.me/share/url?url=https://t.me/jineteras'

bot = telebot.TeleBot(TOKEN)

# 🔘 Botonera con texto personalizado
def crear_botonera():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url=BOTON_URL),
        InlineKeyboardButton("¿Cómo desbloquear?", callback_data="mostrar_popup")
    )
    return markup

# ▶️ Manejo del comando /start en privado
@bot.message_handler(commands=['start'])
def comando_start(message):
    if message.chat.type != 'private':
        return  # Ignora grupos y canales

    argumentos = message.text.split()
    parametro = argumentos[1] if len(argumentos) > 1 else None

    if parametro == "como_desbloquear":
        bot.send_photo(
            chat_id=message.chat.id,
            photo=IMAGE_URL,
            reply_markup=crear_botonera()  # 👈 sin caption
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Bienvenido. Presioná el botón desde el canal para ver cómo desbloquear el contenido."
        )

# 📩 Acción del botón de ayuda
@bot.callback_query_handler(func=lambda call: call.data == "mostrar_popup")
def mostrar_popup(call):
    if call.message.chat.type == 'private':
        bot.answer_callback_query(
            callback_query_id=call.id,
            text="Presione DESBLOQUEAR y únase a 3 grupos grandes.",
            show_alert=True
        )

# ▶️ Ejecutar el bot
print("✅ Bot iniciado correctamente.")
bot.polling()
