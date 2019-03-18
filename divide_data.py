from pathlib import Path
import numpy as np
import shutil

# https://1drv.ms/u/s!AtL739ZIpSoIgsJPIE-vWldVGBnGPw
# 를 다운받아 압축을 풀 것

p = Path('./rounds/')
train_ratio = 0.8

images = [img for img in p.glob('*.png')]

len_data = len(images)
shuffled_indices = list(np.random.permutation(len_data))
train_set_size = int(len_data * train_ratio)

for idx, image_idx in enumerate(shuffled_indices):
    copy_target = './rounds-train' if idx < train_set_size else './rounds-test'
    shutil.copy(str(images[image_idx]), copy_target)
