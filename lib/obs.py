from config import OBSserver_url, OBSserver_password
import simpleobsws
#https://github.com/obsproject/obs-websocket/blob/4.x-current/docs/generated/protocol.md
#https://github.com/IRLToolkit/simpleobsws

obsws = simpleobsws.WebSocketClient(url=OBSserver_url, password=OBSserver_password)