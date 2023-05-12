import os
from PIL import Image

# liverディレクトリ内のPNG画像を変換
for filename in os.listdir("liver_mask"):
    if filename.endswith(".png"):
        im = Image.open(os.path.join("liver_mask", filename))
        im = im.point(lambda x: 255 if x == 1 else 0)
        save_path = os.path.join("liver_mask_255", filename)
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        im.save(save_path)

# lesionディレクトリ内のPNG画像を変換
for filename in os.listdir("tumor_mask"):
    if filename.endswith(".png"):
        im = Image.open(os.path.join("tumor_mask", filename))
        im = im.point(lambda x: 255 if x == 1 else 0)
        save_path = os.path.join("tumor_mask_255", filename)
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        im.save(save_path)