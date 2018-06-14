#!/usr/bin/env python

import tornado.ioloop 
import tornado.web 
import time
import asyncio
import websockets
import tornado.platform.asyncio
tornado.platform.asyncio.AsyncIOMainLoop().install()

#Web app starts
#use the web server if you want! In case you use, use a different index.html

class MainHandler(tornado.web.RequestHandler):
        def get(self):
                self.render("views/index.html", title = "GPS")

def make_app():
        return tornado.web.Application([
                (r"/", MainHandler),
        ])


app = make_app()
app.listen(8888)

#web app ends

print("APP is listening on *8888")

clients = set()
#socket server starts
async def hello(websocket, path):
        global clients
        clients.add(websocket)
        try:
            while True:
                name = await websocket.recv()
                #print("< {}".format(name))
                print(name)
                
                print(clients)
                greeting = name
                
                await asyncio.wait([ws.send(greeting) for ws in clients])
                print(greeting)
                time.sleep(10)
        finally:
            clients.remove(websocket)

                
                
start_server = websockets.serve(hello, 'localhost', 8765)
print("Listening on *8765")
#socket app ends

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
