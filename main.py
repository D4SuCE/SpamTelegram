from telethon import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
import os
import asyncio
import time

creds = []

if os.path.exists("config.data"):
    file = open("config.data", "r")
    for line in file:
        creds.append(line.strip())
    file.close()
else:
    creds.append(input("Введите id: "))
    creds.append(input("Введите hash: "))
    file = open("config.data", "w")
    file.write(creds[0] + "\n")
    file.write(creds[1])
    file.close()

#message = input("Введите сообщение: ")

message = "Привет, если у тебя нет денег, то вступай к нам в чат, с нами ты найдешь актуальные советы по обналу и кардингу, у нас самая лучшая аудитория. https://t.me/+PUHqymbdgE5lYWQy"

client = TelegramClient("Spam_" + creds[0].strip(), creds[0].strip(), creds[1].strip())

#nicknames = []
#file = open('accounts.txt', 'r')
#for line in file:
#    nicknames.append(line.strip())
#file.close()

async def main():
    file = open('accounts.txt', 'r')
    for nickname in file:
        try:
            await client.send_message(nickname.strip(), message)
            print("Сообщение отправлено: " + nickname.strip())
            time.sleep(1)
        except PeerFloodError:
            print("[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
            client.disconnect()
        except Exception as ex:
            print(ex)
            #print("Не найден: " + nickname)
    file.close()
    print("Рассылка завершена!")
    
with client:
    client.loop.run_until_complete(main())
