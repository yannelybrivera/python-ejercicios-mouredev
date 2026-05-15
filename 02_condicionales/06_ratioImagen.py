import requests
from PIL import Image
from io import BytesIO
import math


url ="https://i.pinimg.com/1200x/fe/ca/65/feca654c61d5df237a6d35702c57e225.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))
width, height = img.size

mcd = math.gcd(width, height)

ratio_w = width // mcd
ratio_h = height // mcd

math.gcd(width, height)

print(f"Resolución: {width}x{height}")
print(f"Aspect Ratio: {ratio_w}:{ratio_h}")