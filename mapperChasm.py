#Made by DiXiao
import os
from PIL import Image

if not os.path.exists("outChasm"):
    os.makedirs("outChasm")

SIZE = 1024

mapimg = Image.open("./mapChasm.png")

img_list = [[0, 0, '710d5495-BC7_UNORM.png'], [0, 1, '297d9531-BC7_UNORM.png'], [0, 2, '5c752444-BC7_UNORM.png'], [1, 0, 'ffc3437f-BC7_UNORM.png'], [1, 1, '6ec3ca70-BC7_UNORM.png'], [1, 2, 'ecceab34-BC7_UNORM.png'], [2, 0, 'e2e2328c-BC7_UNORM.png'], [2, 1, 'e46a20f8-BC7_UNORM.png'], [2, 2, '376b5295-BC7_UNORM.png']]

for img in img_list:
    row = img[0]
    col = img[1]
    out_name = img[2]
        
    crop_img = mapimg.crop((row*SIZE,col*SIZE,(row+1)*SIZE,(col+1)*SIZE))
    
    trans_img = crop_img.transpose(method=Image.FLIP_TOP_BOTTOM)
    
    trans_img.save(f"./outChasm/{out_name}")