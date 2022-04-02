from PIL import Image
import os.path
import glob

root_path = "./pic/*.png"
dst_path = "./images/A"
def converted(file_name, outdir, width=224, height=224):
    img = Image.open(file_name)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(file_name)))
    except Exception as e:
        print(f"error:{e}")

for file_name in glob.glob(root_path):
    converted(file_name, dst_path)
