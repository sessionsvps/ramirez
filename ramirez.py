from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(24406776)
    api_hash = "61589051c184c7fda6c96d6f4564ba47"
    phone_number = "51934595550"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spam481516", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4243049748")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spam481516", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["spam 2024", "Spam 2024","Tienda streaming ramirez","Stream","𝙍𝙀𝙁𝙀𝙍𝙀𝙉𝘾𝙄𝘼𝙎 𝘿𝙀 𝙑𝘼𝙉𝙎","WORLD AUTH","「𝘿𝙖𝙧𝙘𝙠 𝙈𝙖𝙨𝙩𝙚𝙧」","𝐇𝐎𝐏𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🌩️","💥𝐑𝐄𝐅𝐄𝐑𝐄𝐍𝐂𝐈𝐀𝐒 𝐋𝐃𝐁𝐌","𝐑𝐄𝐅𝐄𝐑𝐄𝐍𝐂𝐈𝐀𝐒","Videos Diseños Streaming","𝐀𝐫𝐤𝐡𝐚","#! 𝐔𝐧𝐤𝐧𝐨𝐰𝐧 𝐂𝐚𝐫𝐝❜𝐬","𝗙𝗠𝗩𝗧𝗭","ELITE BINS","𝐊𝐢𝐧𝐠 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ⌞🜲⌝","APK BASENEXUS","⚡️𝐅⊗𝐑𝐙𝐀⚡️","QUEMANDO ESTAFADORES","【B】 В I N N E R 'S 【B】","🎩𝕂𝕀ℕ𝔾𝕊𝕄𝔸ℕ 𝔹𝕀ℕ𝕊 🎩","𝐊𝐢𝐧𝐠 𝐁𝐢𝐧𝐧𝐞𝐫𝐬 ⌞🜲⌝","𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓𝐒","𝐇𝐚𝐝𝐞𝐬 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ⌞🜲⌝","𝙊𝙣𝙮𝙭 𝙪𝙥𝙙𝙖𝙩𝙚𝙨!","𝗗𝗢𝗫 𝗗𝗔𝗧𝗔 - 𝗖𝗔𝗡𝗔𝗟","CUENTAS GRATIS PARA TODOS","🌕 [𝕄𝕆𝕆ℕ𝕃𝕀𝔾ℍ𝕋 ℂ𝔸ℕ𝔸𝕃] ✨","BIN Y CUENTAS"," ͟͟͞͞➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","𝗩𝗔𝗞 𝗦ú𝗽𝗲𝗿 𝗴𝗶𝗳𝘁𝘀⛥","🩸𝐆𝐎𝐉𝐎 𝐌𝐄𝐓𝐎𝐃𝐎𝐒🩸","Al Fondo Hay Sitio 11 Nueva Temporada 2024 Afhs11","⌜☬ᴼᴺᴱ⌟ Aɴᴏɴɪᴍᴜs","𝕃𝕚𝕠𝕟𝕤 𝔸𝕔𝕔𝕠𝕦𝕟𝕥 ℂ𝕙𝕒𝕟𝕟𝕖𝕝","「 𝗦𝗛𝗔𝗗𝗢𝗪 𝗕𝗜𝗡𝗦 ↯」","𝕴𝖓𝖈𝖔𝖕𝖓𝖎𝖙𝖔𝖘","╰•𝘽𝙞𝙣𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙂𝙧𝙖𝙩𝙞𝙨•╯","• 𝙇𝙐𝙈𝙄𝙉𝙊𝙐𝙎 𝙎𝙏𝘼𝙍 •","𝙎𝙇𝙊𝙏𝙎","𝙎𝙋𝘼𝙍𝙏𝘼𝙉 𝘽𝙄𝙉𝙎↯","𝙎𝙖𝙣𝙘𝙩𝙪𝙖𝙧𝙮","REFERENCIAS TON","@MeaTkTk referencias♥️🦋🫦","Expertos Testimonios","Plantita refes","🍀𝐑𝐞𝐟𝐞𝐫𝐞𝐧𝐜𝐢𝐚𝐬 𝐌𝐞𝐢 𝐌𝐞𝐢","𝐑𝐞𝐟𝐞𝐫𝐞𝐧𝐜𝐢𝐚𝐬 𝐌𝐚𝐢𝐥𝐨","DJANGO REFES😈","Referidos de César Carrillo.","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝘿𝙀𝙎𝘾𝘼𝙉𝙎𝙊 𝙈𝙀𝘿𝙄𝘾𝙊","🩸𝙏𝙐𝙏𝙊𝙍𝙄𝘼𝙇 𝘽𝙐𝙎𝙌𝙐𝙀𝘿𝘼𝙎","[MÉTODOS] PERÚTIM","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","🩸𝙈𝙀𝙏𝙊𝘿𝙊","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝙋𝙍𝙄𝙈𝙀","@Jimzxz7","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝙏𝙄𝘿𝘼𝙇","『𝙰𝚜𝚝𝚛𝚊 𝚅𝙸𝙿』","Referencias","MÉTODO IZIPAY","🩸𝙐𝙎𝙀𝙍 𝘿𝙀 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼𝙎","• 𝙇𝙐𝙈𝙄𝙉𝙊𝙐𝙎 𝙎𝙏𝘼𝙍 •","╰•𝘽𝙞𝙣𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙂𝙧𝙖𝙩𝙞𝙨•╯","𝕽𝖊𝖋𝖊𝖗𝖊𝖓𝖈𝖎𝖆𝖘 ","ℝ𝔼𝔽𝔼ℝ𝔼ℕℂ𝕀𝔸𝕊 𝗜𝘇𝘂𝗸𝘂👁","ZYDE7 BINS","BINTAKER™ 💳","Referencias Senior Flag","𝑪𝑨𝑵𝑺𝑬𝑹 𝛹2Ƥ","𝑪𝑨𝑴 ✞ 𝑩𝑰𝑵𝑺 𝛹2𝑷","𝐄𝐲𝐬𝐕𝐦 𝐂𝐡𝐚𝐧𝐧𝐞𝐥","Referencias Elmer 💸","𝕽𝖔𝖞𝖆𝖑 𝕭𝖎𝖓𝖘 𝕮𝖍𝖆𝖓𝖓𝖊𝖑","𝐙𝐞𝐮𝐬 𝐁𝐢𝐧𝐬 ⌞🜲⌝","DEMON 「BINS↯」☘","〽️𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","𝙏𝙊𝙈𝙈𝙔 𝙍𝙀𝙁𝙀𝙍𝙀𝙉𝘾𝙄𝘼𝙎🥀▪️","𝘽𝙞𝙣𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙂𝙧𝙖𝙩𝙞𝙨","Diseños Streaming Vip","𝙂𝙤𝙡𝙙 𝘼𝙣𝙤𝙣𝙮𝙢𝙤𝙪𝙨","• 𝘿𝙄𝘼𝙈𝙊𝙉𝘿 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 •","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝙍𝙀𝘾𝘼𝙍𝙂𝘼𝙎","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝙍𝙀𝘾𝘼𝙍𝙂𝘼𝙎","Senior Referencias","𝑺𝑾𝑨𝑫𝑫𝒀 𝑩𝑰𝑵𝑺 ⛧","🔥 𝗟𝗘𝗢𝗡𝗦 𝗕𝗜𝗡𝗡𝗘𝗥𝗦 🔥","¡𝗩𝗘𝗥𝗦𝗔𝗖𝗘!","𝗕𝗜𝗡𝗦 𝟮𝗠𝗚","💳 𝘽1𝙉𝙉𝙀𝙍𝙎 🍿","𝗔𝟮𝗔𝘀𝘀𝗶𝗮𝗱","𝐕𝐭𝐫𝐒𝐲𝐱","🩸𝙈𝙀𝙏𝙊𝘿𝙊 𝙋𝙍𝙄𝙈𝙀 𝙑𝙄𝘿𝙀𝙊","ONE PICE CUENTAS","SCAM+SCRAPP SALDOX","𝑊𝐴𝐾𝐴𝑁𝐷𝐴 𝐹𝑂𝑅𝐸𝑉𝐸𝑅","𝘼𝙮𝙖𝙣𝙤𝙠𝙤𝙟𝙞 CC'S !𓆰𓆪¡"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.send_message(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spam481516", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spam481516", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(5)
                        if j==3: break
            await client.send_message("@spam481516", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(600) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())