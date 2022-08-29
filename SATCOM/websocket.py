import asyncio
import pathlib
import ssl
import websockets

root_ca = pathlib.Path("/app/Certs/isrgrootx1.pem")
dev_cert = pathlib.Path("/app/Certs/fullchain.pem")
dev_key = pathlib.Path("/app/Certs/privkey.pem")


def ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(root_ca)
    ssl_context.load_cert_chain(dev_cert,dev_key)
    return ssl_context

def readFlag():
    file = open("flag.txt","r")
    flag = file.read()
    file.close()
    return flag

async def hello(url,port):
    scheme = "wss://"
    uri = scheme + url + ":" + str(port)
    # server_hostname='', Dont worry,if you dont have any domain
    async with websockets.connect(uri, ssl=ssl_context(),server_hostname='') as websocket:
        name = "Welcome to Winja CTF!!!"
        await websocket.send(name)

        server_command = await websocket.recv()
        if server_command == "flag":
            await websocket.send("Here is the flag:{}".format(readFlag()))


def connectServer(url,port):
    asyncio.run(hello(url,port))
