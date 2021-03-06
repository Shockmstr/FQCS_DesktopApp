from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QFileDialog, QWidget, QMessageBox
import cv2
import os
from app_models.detector_config import DetectorConfig
from app_constants import ROOT_DIR
import trio
import asyncio
import numpy as np


def sync_func(func, *args):
    if asyncio.iscoroutinefunction(func):
        if (len(args) > 0):
            return trio.run(func, *args)
        else:
            return trio.run(func)
    else:
        if (len(args) > 0):
            return func(*args)
        else:
            return func()


def file_chooser_open_directory(parent) -> QUrl:
    dialog = QFileDialog(parent)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    url = dialog.getExistingDirectoryUrl()
    return url


def file_chooser_open_file(parent, f_filter=None):
    dialog = QFileDialog(parent)
    url = dialog.getOpenFileUrl(filter=f_filter)
    return url


def concat_images(images, label_w, label_h):
    dim = (label_w, label_h)
    final_img = None
    for idx, img in enumerate(images):
        height, width, _ = images[idx].shape
        scale = label_h / height
        width *= scale
        if final_img is None:
            final_img = cv2.resize(images[idx], (int(width), label_h))
        else:
            final_img = np.concatenate(
                (final_img, cv2.resize(images[idx], (int(width), label_h))),
                axis=1)
    if final_img.shape[1] > label_w:
        final_img = cv2.resize(final_img, dim)
    return final_img


def get_all_camera_index(num=10):
    # checks the first 10 indexes.
    index = 0
    arr = []
    while num > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        num -= 1
    return arr


def hide_all_children(widget):
    for ch in widget.children():
        if hasattr(ch, 'hide'):
            ch.hide()


def show_all_children(widget):
    for ch in widget.children():
        if hasattr(ch, 'show'):
            ch.show()


def show_message(text, title="Message", icon=QMessageBox.Information):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(text)
    msg.setWindowTitle(title)
    choice = msg.exec_()
    return choice