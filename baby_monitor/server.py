import time

from fastapi import FastAPI
from starlette.responses import StreamingResponse, HTMLResponse
from .camera import gen_frames

app = FastAPI()

# camera = Camera()

# async def stream_video():
#     while True:
#         frame = camera.get_frame()
#         print(f'{time.time()} got frame')
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get('/')
async def index():
    return HTMLResponse('<html><body><center><img src="/video"></center></body></html>')


@app.get('/video')
async def video():
    return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')
