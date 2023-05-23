import tensorflow as tf
import os
import cv2
import PIL
from PIL import Image

dirs = ["train/dataset/nsfw", "train/dataset/sfw"]
ext_to_del = ["gif", "webp", "mp4", "svg"]

for dir in dirs:
    for file in os.listdir(dir):
        print(f"  Checking {file} from {dir}...")
        
        if file.endswith(tuple(ext_to_del)):
            os.remove(os.path.join(dir, file))
            print(f"        Removed {file} from {dir} (extension in {ext_to_del})")
            continue
        
        try:
            img = cv2.imread(os.path.join(dir, file), 0)
            height, width = img.shape[:2]
        
            if height < 64 or width < 64:
                os.remove(os.path.join(dir, file))
                print(f"        Removed {file} from {dir} (image under 64px)")
                continue
        except AttributeError:
            os.remove(os.path.join(dir, file))
            print(f"        Removed {file} from {dir} (image under 64px)")
            continue
        
        try:
            img = Image.open(os.path.join(dir, file))
            img.verify()
            img.close()
        except:
            print(f"        Removed {file} from {dir} (image corrupted)")
            os.remove(os.path.join(dir, file))
            continue
        
        with open(os.path.join(dir, file), 'rb') as f:
            check_chars = f.read()[-2:]
        if check_chars != b'\xff\xd9':
            print(f"        Removed {file} from {dir} (image not complete)")
            os.remove(os.path.join(dir, file))
            continue
        
        try:
            image = tf.keras.preprocessing.image.load_img(os.path.join(dir, file))
        except Exception as e:
            os.remove(os.path.join(dir, file))
            print(f"        Removed {file} from {dir}. Due to an error with keras : {e}")
            continue
        
        del image, img, height, width, check_chars
        
    print(f"Finished cleaning {dir} !")