from app import create_app
from flask_socketio import SocketIO
from app import config

app = create_app()
if __name__ == '__main__':
    socketio = SocketIO(app, async_mode=None)
    socketio.run(app, config.HOST, config.PORT)