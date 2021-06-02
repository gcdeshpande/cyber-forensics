from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
pilImage=Image.open("C:\\Users\\gcdeshpande\\Desktop\\image.png")
ExifData = pilImage._getexif()
imgExif = ExifData.items()
print(imgExif)
