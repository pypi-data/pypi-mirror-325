import time

import pypylon.pylon as py

from cadivi_analysis.settings import (
    camera99_consumer,
    camera27_consumer,
    camera55_consumer,
    logging,
)
from cadivi_analysis.utils.camera_utils import CameraUtils

# from cadivi_analysis.utils.image_utils import decode_base64_frame, write_frame


def main():
    tlf = py.TlFactory.GetInstance()
    devices = tlf.EnumerateDevices()

    # 27347 - Day to
    # camera_99 = CameraUtils(
    #     devices[0], offset_x=0, offset_y=130, exporsure_time=500
    # )
    # camera_27 = CameraUtils(
    #     devices[1], offset_x=0, offset_y=1064, exporsure_time=500
    # )
    # camera_55 = CameraUtils(
    #     devices[2], offset_x=0, offset_y=364, exporsure_time=500
    # )

    # Day nho
    camera_99 = CameraUtils(
        devices[0], offset_x=0, offset_y=342, exporsure_time=500
    )
    camera_27 = CameraUtils(
        devices[1], offset_x=0, offset_y=502, exporsure_time=500
    )
    camera_55 = CameraUtils(
        devices[2], offset_x=0, offset_y=292, exporsure_time=500
    )

    # Start Grabbing
    camera_99.start_grabbing(save=True, is_count_100=True)
    camera_27.start_grabbing(save=True, is_count_100=True)
    camera_55.start_grabbing(save=True, is_count_100=True)

    # Record the start time
    start_time = time.time()

    count = 0
    while True:
        if count > 99:
            break

        message_99 = camera99_consumer.poll()
        if not len(message_99.items()) == 0:
            for _, records in message_99.items():
                for rec in records:
                    # frame = decode_base64_frame(rec.value)
                    # write_frame(frame, f"linescan99_frame_{count:04d}")
                    print(rec.value)

        message_27 = camera27_consumer.poll()
        if not len(message_27.items()) == 0:
            # count += 1
            for _, records in message_27.items():
                for rec in records:
                    # frame = decode_base64_frame(rec.value)
                    # write_frame(frame, f"linescan27_frame_{count:04d}")
                    print(rec.value)

        message_55 = camera55_consumer.poll()
        if not len(message_55.items()) == 0:
            count += 1
            for _, records in message_55.items():
                for rec in records:
                    # frame = decode_base64_frame(rec.value)
                    # write_frame(frame, f"linescan55_frame_{count:04d}")
                    print(rec.value)

    # Record the end time
    end_time = time.time()

    # Stop Grabbing
    camera_99.stop_grabbing()
    camera_27.stop_grabbing()
    camera_55.stop_grabbing()

    elapsed_time = end_time - start_time
    logging.info(f"Elapsed time: {elapsed_time} seconds")
