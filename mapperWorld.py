#Made by DiXiao
import os
from PIL import Image

if not os.path.exists("outWorld"):
    os.makedirs("outWorld")

SIZE = 1024

mapimg = Image.open("./mapWorld.png")

img_list = [[0, 2, '8a6d9dbf-BC7_UNORM.png'], [0, 3, 'd88684d4-BC7_UNORM.png'], [0, 4, '6491a25b-BC7_UNORM.png'], [1, 2, '85138956-BC7_UNORM.png'], [1, 3, '87720353-BC7_UNORM.png'], [1, 4, 'b1b5a69d-BC7_UNORM.png'], [1, 5, '686ae7f2-BC7_UNORM.png'], [1, 6, 'e19d75e6-BC7_UNORM.png'], [1, 7, '5e51bfe4-BC7_UNORM.png'], [10, 0, '033546bd-BC7_UNORM.png'], [10, 1, '7bac48e0-BC7_UNORM.png'], [10, 10, 'e14b665f-BC7_UNORM.png'], [10, 2, '60d1c4c0-BC7_UNORM.png'], [10, 3, '38d5acc0-BC7_UNORM.png'], [10, 4, '8e4bdc93-BC7_UNORM.png'], [10, 5, '640c6d82-BC7_UNORM.png'], [10, 6, 'ab30a5a3-BC7_UNORM.png'], [10, 7, '1b2bb745-BC7_UNORM.png'], [10, 8, 'eb089502-BC7_UNORM.png'], [10, 9, '5a2dffd8-BC7_UNORM.png'], [11, 0, 'f26707cb-BC7_UNORM.png'], [11, 1, '43a9eeea-BC7_UNORM.png'], [11, 10, '7196a13d-BC7_UNORM.png'], [11, 2, 'f6f7b285-BC7_UNORM.png'], [11, 3, 'a4358833-BC7_UNORM.png'], [11, 4, '2b047746-BC7_UNORM.png'], [11, 5, '73853f17-BC7_UNORM.png'], [11, 6, '6a013fab-BC7_UNORM.png'], [11, 7, 'd43f6f23-BC7_UNORM.png'], [11, 8, 'f3182a0d-BC7_UNORM.png'], [11, 9, '125fbe2b-BC7_UNORM.png'], [12, 2, '35c0ca43-BC7_UNORM.png'], [12, 3, '4d3dcb59-BC7_UNORM.png'], [12, 4, 'c9bc1170-BC7_UNORM.png'], [12, 5, '455ab2e4-BC7_UNORM.png'], [12, 6, 'b0ed7a0a-BC7_UNORM.png'], [12, 7, '6219c7d9-BC7_UNORM.png'], [12, 8, 'dfa95cd0-BC7_UNORM.png'], [12, 9, 'd7954578-BC7_UNORM.png'], [13, 3, 'a4ed2da1-BC7_UNORM.png'], [13, 4, '0c46151c-BC7_UNORM.png'], [13, 5, '4187a910-BC7_UNORM.png'], [13, 6, '11740b61-BC7_UNORM.png'], [13, 7, '8f007d44-BC7_UNORM.png'], [13, 8, '33a74dca-BC7_UNORM.png'], [13, 9, '5ea42503-BC7_UNORM.png'], [2, 2, '11f69b55-BC7_UNORM.png'], [2, 3, '669bc790-BC7_UNORM.png'], [2, 4, '341fb98a-BC7_UNORM.png'], [2, 5, 'dc9479cc-BC7_UNORM.png'], [2, 6, '34f608b8-BC7_UNORM.png'], [2, 7, '51dc1e5f-BC7_UNORM.png'], [3, 2, '80ae79d8-BC7_UNORM.png'], [3, 3, '86da5f1c-BC7_UNORM.png'], [3, 4, '1923e119-BC7_UNORM.png'], [3, 5, '449508a6-BC7_UNORM.png'], [3, 6, '813ea556-BC7_UNORM.png'], [3, 7, '5145040d-BC7_UNORM.png'], [4, 2, '15fa88a5-BC7_UNORM.png'], [4, 3, 'da744c0b-BC7_UNORM.png'], [4, 4, '6daab02f-BC7_UNORM.png'], [4, 5, 'c8c1f396-BC7_UNORM.png'], [4, 6, 'dd4dcb9e-BC7_UNORM.png'], [4, 7, '88a819b8-BC7_UNORM.png'], [5, 0, '7c69dff4-BC7_UNORM.png'], [5, 1, '203f7dd6-BC7_UNORM.png'], [5, 2, 'f8bc8813-BC7_UNORM.png'], [5, 3, '66303bc3-BC7_UNORM.png'], [5, 4, '5f5dfccb-BC7_UNORM.png'], [5, 5, '80d3508e-BC7_UNORM.png'], [5, 6, '1af5a274-BC7_UNORM.png'], [5, 7, '1765a7fe-BC7_UNORM.png'], [6, 0, 'fc2d9433-BC7_UNORM.png'], [6, 1, 'ac841dc9-BC7_UNORM.png'], [6, 2, '09f7f9e0-BC7_UNORM.png'], [6, 3, '169a55dd-BC7_UNORM.png'], [6, 4, 'ceaad758-BC7_UNORM.png'], [6, 5, '3cb58cfa-BC7_UNORM.png'], [6, 6, '5f7d9e14-BC7_UNORM.png'], [6, 7, 'c85edf9f-BC7_UNORM.png'], [7, 0, '8f877a3c-BC7_UNORM.png'], [7, 1, '25833a56-BC7_UNORM.png'], [7, 2, 'abd441af-BC7_UNORM.png'], [7, 3, 'c9a9b7b6-BC7_UNORM.png'], [7, 4, '10b3a440-BC7_UNORM.png'], [7, 5, '93a426ae-BC7_UNORM.png'], [7, 6, '9719938d-BC7_UNORM.png'], [7, 7, 'dee1dc86-BC7_UNORM.png'], [7, 8, 'd2b9b85e-BC7_UNORM.png'], [8, 0, '28c0683d-BC7_UNORM.png'], [8, 1, 'd4555f08-BC7_UNORM.png'], [8, 2, 'd2efeea1-BC7_UNORM.png'], [8, 3, '0376a1b1-BC7_UNORM.png'], [8, 4, '81f4dcb8-BC7_UNORM.png'], [8, 5, '2646d960-BC7_UNORM.png'], [8, 6, '83d5feb5-BC7_UNORM.png'], [8, 7, 'f794fd58-BC7_UNORM.png'], [8, 8, '9f73fe62-BC7_UNORM.png'], [9, 0, '239e5b2e-BC7_UNORM.png'], [9, 1, '420491cf-BC7_UNORM.png'], [9, 10, '6190362a-BC7_UNORM.png'], [9, 2, '0153aa78-BC7_UNORM.png'], [9, 3, '126345f5-BC7_UNORM.png'], [9, 4, 'eeb5a406-BC7_UNORM.png'], [9, 5, 'b780f35f-BC7_UNORM.png'], [9, 6, 'e7519354-BC7_UNORM.png'], [9, 7, 'b7acb60a-BC7_UNORM.png'], [9, 8, '0a21d70b-BC7_UNORM.png'], [9, 9, '4aea4dde-BC7_UNORM.png']]

for img in img_list:
    row = img[0]
    col = img[1]
    out_name = img[2]
        
    crop_img = mapimg.crop((row*SIZE,col*SIZE,(row+1)*SIZE,(col+1)*SIZE))
    
    trans_img = crop_img.transpose(method=Image.FLIP_TOP_BOTTOM)
    
    trans_img.save(f"./outWorld/{out_name}")