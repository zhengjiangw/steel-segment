import os

import numpy as np
import cv2


def visiable(img_dir, label_path):

    with open(label_path, "r") as f:
        lines = f.readlines()
    # 去除标题
    lines = lines[1:]
    for line in lines:
        line = line[:-1]
        splits = line.split(",")
        img_name = splits[0]
        class_id = splits[1]
        mask_arr = np.array(splits[2].split(" ")).reshape(-1, 2).astype(np.int32)
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        h, w, _ = img.shape
        interger = mask_arr[:, 0] // w
        column = mask_arr[:, 0] - interger * w

        #starts from 0
        raw = interger + 1 - 1
        column_start = column - 1
        column_end = mask_arr[:, 1] + column_start

        for r, s, e in zip(raw, column_start, column_end):

            cv2.line(img, (s, r), (e, r), (255, 255, 0), 1)
        cv2.imshow("img", img)
        cv2.waitKey(0)


if __name__ == '__main__':

    img_dir = r"D:\dataset\severstal-steel-defect-detection\train_images"
    label_path = r"D:\dataset\severstal-steel-defect-detection\train.csv"
    visiable(img_dir, label_path)
