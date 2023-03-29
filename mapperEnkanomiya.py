#Made by DiXiao
from PIL import Image

SIZE = 1024

mapimg = Image.open("./mapEnkanomiya.png")

img_list = [[0, 0, '8bfdb7a5-BC7_UNORM.png'], [0, 1, '32595b37-BC7_UNORM.png'], [0, 2, '1913e1e6-BC7_UNORM.png'], [1, 0, '0e5ed7b8-BC7_UNORM.png'], [1, 1, 'a41e6fc5-BC7_UNORM.png'], [1, 2, '326eb5c6-BC7_UNORM.png'], [2, 0, '53c943e0-BC7_UNORM.png'], [2, 1, 'c6d473d2-BC7_UNORM.png'], [2, 2, 'd4594270-BC7_UNORM.png']]

for img in img_list:
    row = img[0]
    col = img[1]
    out_name = img[2]
        
    crop_img = mapimg.crop((row*SIZE,col*SIZE,(row+1)*SIZE,(col+1)*SIZE))
    
    trans_img = crop_img.transpose(method=Image.FLIP_TOP_BOTTOM)
    
    trans_img.save(f"./outEnkanomiya/{out_name}")