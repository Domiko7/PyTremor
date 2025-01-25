import websocket
import json
import threading
import os
import ctypes
from playsound import playsound
from plyer import notification

def EEWsound(laungage, country):
    if laungage == 'English':
        playsound('sounds/Shaking(EN).mp3')
    elif laungage == 'Japanese':
        playsound('sounds/Shaking(JP).mp3')
    elif laungage == 'Chinese':
        playsound('sounds/Shaking(CH).mp3')
    elif laungage == 'Spanish':
        playsound('sounds/Shaking(ES).mp3')
    elif laungage == 'Korean':
        playsound('sounds/Shaking(SK).mp3')
    elif laungage == 'Polish':
        playsound('sounds/Shaking(PL).mp3')
    playsound('sounds/Emergency_Alert02-1.mp3')
    playsound('sounds/Emergency_Alert01-1.mp3')
    notification.notify(
        title="EARTHQUAKE ALERT! ({county} EEW)",
        message="drop cover and hold on",
        app_icon=None,  # Path to a custom icon file (.ico). Set to None for no icon.
        timeout=10  # Duration in seconds
    )

NoW=False
def on_message(ws, message):
    global toaster
    global NoW
    laungage = 'Chinese'
    data = json.loads(message)
    if data.get("type") == "jma_eew":
        if data.get("isFinal"):
            print("THIS IS THE FINAL REPORT")
        print("Earthquake Alert! (JAPAN EEW)")
        print(f"Title: {data.get('Title')}")
        print(f"Location: {data.get('Hypocenter')}")
        print(f"Magnitude: {data.get('Magunitude')}")
        print(f"Max Intensity: {data.get('MaxIntensity')}")
        print(f"Maximum earthquake intensity: {data.get('WarnArea').get('Shindo1')}")
        print(f"Orgin time: {data.get('OriginTime')}")
        print(f"Announced time: {data.get('AnnouncedTime')}")
        print(f"Depth: {data.get('Depth')}")
        print(f"Warning area arrival: {data.get('WarnArea').get('Arrive')}")
        print(f"Warning Areas: {data.get('WarnArea').get('Chiiki')}")
        print(f"Method: {data.get('isAssumption')}")
        EEWsound(laungage, 'Japan')
        NoW = False
        if data.get("isCancel"):
            for i in range(5):
                print('FALSE EEW ALARM')
    elif data.get("type") == "cwa_eew":
        print("Earthquake Alert! (CWA EEW)")
        print(f"Magnitude: {data.get('Magunitude')}")
        print(f"ID: {data.get('ID')}")
        print(f"Depth: {data.get('Depth')}")
        print(f"Time: {data.get('OrginTime')}")
        print(f"Location: {data.get('HypoCenter')}")
        print(f"Maximum intensity: {data.get('MaxIntensity')}")
        EEWsound(laungage, 'China')
        NoW = False
        print(f"ReportTIme: {data.get('ReportTime')}")
    elif data.get("type") == "sc_eew":
        print("Earthquake Alert! (SC EEW)")
        print(f"Magnitude: {data.get('Magunitude')}")
        print(f"ID: {data.get('ID')}")
        print(f"Depth: {data.get('Depth')}")
        print(f"Time: {data.get('OrginTime')}")
        print(f"Location: {data.get('hypoCenter')}")
        print(f"Maximum intensity: {data.get('MaxIntensity')}")
        EEWsound(laungage, 'China')
        NoW = False
    elif data.get("type") == "fj_eew":
        print("Earthquake Alert! (FJ EEW)")
        print(f"Magnitude: {data.get('Magunitude')}")
        print(f"ID: {data.get('ID')}")
        print(f"Depth: {data.get('Depth')}")
        print(f"Time: {data.get('OrginTime')}")
        print(f"Location: {data.get('HypoCenter')}")
        print(f"Maximum intensity: {data.get('maxIntensity')}")
        print(f"ReportTIme: {data.get('ReportTime')}")
        print(f"Final: {data.get('isFinal')}")
        EEWsound(laungage, 'China')
        NoW = False
    elif data.get("type") == "cenc_eqlist":
        print("Earthquake Alert! (CENC EQLIST)")
        for key, report in data.items():
            if key.startswith('No'):  
                print(f"Earthquake Report {key}:")
                print(f"Magnitude: {report.get('magnitude')}")
                print(f"Depth: {report.get('depth')}")
                print(f"Time: {report.get('time')}")
                print(f"Location: {report.get('location')}")
                EEWsound(laungage, 'China')
                NoW = False
    elif NoW == False:
        print("No EEW issued")
        notification.notify(
        title="NO EEW ISSUED",
        message=" ",
        app_icon=None,  # Path to a custom icon file (.ico). Set to None for no icon.
        timeout=10  # Duration in seconds
        )
        NoW = True

# Function for handling errors
def on_error(ws, error):
    print("Error:", error)

# Function for handling the closure of the connection
def on_close(ws, close_status_code, close_msg):
    print("Connection closed.")

# Function to execute when the connection is opened (DELETED FOR NOW)
def on_open(ws):
    global NoW
    print("WebSocket connection established.")

# Function to run a WebSocket connection in a separate thread
def run_websocket(ws_url):
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    #ws.on_open = on_open
    ws.run_forever()

# Dictionary to map the different data sources to their respective WebSocket URLs
ws_urls = {
    "jma_eew": "wss://ws-api.wolfx.jp/jma_eew",
    "cenc_eqlist": "wss://ws-api.wolfx.jp/cenc_eqlist",
    "cwa_eew": "wss://ws-api.wolfx.jp/cwa_eew",
    "sc_eew": "wss://ws-api.wolfx.jp/sc_eew",
    "fj_eew": "wss://ws-api.wolfx.jp/fj_eew"
}

# Create and start a separate thread for each WebSocket URL
threads = []
for source, url in ws_urls.items():
    thread = threading.Thread(target=run_websocket, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
