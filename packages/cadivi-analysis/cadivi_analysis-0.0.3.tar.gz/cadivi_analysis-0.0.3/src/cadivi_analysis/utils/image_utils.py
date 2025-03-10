# import base64

import numpy as np
import cv2


# Function to decode base64 frame
def decode_base64_frame(encoded_frame):
    np_data = np.frombuffer(encoded_frame, np.uint8)
    return cv2.imdecode(np_data, cv2.IMREAD_COLOR)


# Function to encode frame to base64
def encode_frame_base64(frame):
    _, buffer = cv2.imencode(".jpg", frame)
    return buffer.tobytes()


def write_frame(img, image_file):
    cv2.imwrite(
        f"{image_file}.png",
        img,
    )
