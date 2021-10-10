from PIL import Image
import os

# allChamps = os.listdir('champs')
# ahriD = r'C:/Users/F3Lx/PycharmProjects/InstaLock/champs/Ahri.png'
# ahri = Image.open(ahriD)
# width, height = ahri.size
# left = 10
# top = 10
# right = 105
# bottom = 105
# ahri = ahri.crop((left, top, right, bottom))
# ahri.show()

# for champDir in allChamps:
#     champDir = f'champs/{champDir}'
#     if '.png' in champDir:
#         champ = Image.open(champDir)
#         print('png file')
#         if champ.size == (120, 120):
#             print(f'resizing {champ}')
#             champ = champ.crop((left, top, right, bottom))
#             champ.save(champDir)

# path = 'champs/'
#
# for file in os.listdir(path):
#     os.rename(path + file, path + file.lower())
#
# then = os.listdir(path)
# print(then)