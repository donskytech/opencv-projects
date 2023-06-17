from importlib import import_module
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from qr_scanner import QRScanner
from camera_opencv import Camera

myDataDB = ["123456", "223344"]

app = Flask(__name__)
app.config["SECRET_KEY"] = "DonskyTech Rocks!"
socketio = SocketIO(app, cors_allowed_origins="*")

qr_code_scanner = QRScanner()

def generate_frames(camera):
    while True:
        is_granted, is_denied = False, False
        image = camera.get_frame()

        result = QRScanner.read_qr_code(image)
        if len(result) == 0:
            socketio.emit(
                "scan_result",
                {"status": "scan", "message": "Please scan your QR Code"},
            ) 

        for barcode in result:
            myData = barcode.data.decode("utf-8")
            if myData in myDataDB:
                socketio.emit(
                    "scan_result",
                    {"status": "granted", "message": "Access Granted"},
                )
                is_granted = True
            else:
                print("Not found in the database!")
                socketio.emit(
                    "scan_result", {"status": "denied", "message": "Access Denied"}
                )
                is_denied = True
            QRScanner.add_box_to_qr_code(image, barcode)

        if is_granted:
            image = qr_code_scanner.get_access_granted_img()
        elif is_denied:
            image = qr_code_scanner.get_access_denied_img()
        

        frame = QRScanner.encode(image)

        if is_granted or is_denied:
            for _ in range(2):
                yield (b"--frame\r\n" + b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
        else:
            yield (b"--frame\r\n" + b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(
        generate_frames(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
