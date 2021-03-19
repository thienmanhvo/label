import glob2
import math
import os
import numpy as np

files = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
    image_files = glob2.glob(os.path.join("data", ext))
    print(len(image_files))
    for img in image_files:

        if os.path.exists(img[:-3] + "txt"):
            files.append(img)

# files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#     image_files = glob2.glob(os.path.join("thienGray/", ext))
#     files += image_files


nb_val = math.floor(len(files) * 0.3)
rand_idx = np.random.choice(len(files), size=nb_val, replace=False)
train_idx = [x for x in np.arange(len(files)) if x not in rand_idx]

print(rand_idx)
print(train_idx)

print(len(files))
print(len(train_idx))
print(len(rand_idx))

# Tạo file train.txt
with open("train.txt", "w") as f:
    for idx in np.arange(len(files)):
        if idx in train_idx and (os.path.exists(files[idx][:-3] + "txt")):
            f.write(files[idx] + '\n')

# Tạo file vali.txt
with open("val.txt", "w") as f:
    for idx in np.arange(len(files)):
        if (idx in rand_idx) and (os.path.exists(files[idx][:-3] + "txt")):
            f.write(files[idx] + '\n')