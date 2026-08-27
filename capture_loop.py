import threading
import time
import mss
from PIL import Image
import io
from config import load_config

class CaptureThread(threading.Thread):
    def __init__(self, api_client, stop_event):
        super().__init__()
        self.api_client = api_client
        self.stop_event = stop_event
        self.daemon = True

    def run(self):
        config = load_config()
        interval = config.get('interval_sec', 3.0)
        region = config.get('region', {'x': 200, 'y': 150, 'width': 640, 'height': 400})
        
        monitor = {
            "left": region['x'], 
            "top": region['y'], 
            "width": region['width'], 
            "height": region['height']
        }

        with mss.mss() as sct:
            while not self.stop_event.is_set():
                try:
                    # 1. Capture only the region
                    screenshot = sct.grab(monitor)
                    
                    # 2. Convert to PNG bytes
                    img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
                    buf = io.BytesIO()
                    img.save(buf, format='PNG')
                    img_bytes = buf.getvalue()
                    
                    # 3. Send to cloud
                    self.api_client.send_frame(img_bytes)
                    
                except Exception as e:
                    print(f"Capture error: {e}")
                
                time.sleep(interval)
