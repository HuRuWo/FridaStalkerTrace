import os

import frida, sys


# https://frida.re/docs/examples/android/
# send('onClick'); 消息发送
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


script_file = os.path.join(os.path.dirname(__file__), "frida_stalker.js")
try:
    script = open(script_file, encoding='utf-8').read()
    process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
    script = process.create_script(script)
    script.on('message', on_message)
    print('[*] Running CTF')
    script.load()
    sys.stdin.read()
except Exception as e:
    raise Exception("Read script error.")
