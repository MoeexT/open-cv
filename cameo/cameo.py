#! py -3
# -*- coding: utf-8 -*-

import cv2
import filters
from managers import CaptureManager, WindowManager


class Cameo(object):
    def __init__(self):
        self._window_manager = WindowManager('Cameo', self.on_keypress)
        self._capture_manager = CaptureManager(cv2.VideoCapture(0), self._window_manager, True)

        # @这是滤波器
        # self._curve_filter = filters.FindEdgesFilter4()

    def run(self):
        """main loop"""
        self._window_manager.create_window()
        while self._window_manager.is_window_created:
            self._capture_manager.enter_frame()
            frame = self._capture_manager.frame
            # TUDO(yuwan) filter the frame (chapter 3)
            # @这是滤波器方法
            # filters.stroke_edges(frame, frame)
            # self._curve_filter.apply(frame, frame)

            self._capture_manager.exit_frame()
            self._window_manager.process_events()

    def on_keypress(self, key_code):
        """
        handle a keypress
        space  -> take a screen_shot
        tab    -> start/stop recording a screen_cast
        escape -> quit
        :param key_code:
        :return:
        """
        if key_code == 32:  # space
            self._capture_manager.write_image("filtered_images/screen_shot.png")
        elif key_code == 9:  # tab
            if not self._capture_manager.is_writing_video:
                self._capture_manager.start_writing_video("screen_cast.avi")
            else:
                self._capture_manager.stop_writing_video()
        elif key_code == 27:  # escape
            self._window_manager.destroy_window()


if __name__ == "__main__":
    Cameo().run()
