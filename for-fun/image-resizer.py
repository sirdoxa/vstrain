from PIL import Image

image_path = r'C:\Users\Mahdi\Desktop\bnar.png'

image = Image.open(image_path)

resized_image = image.resize((2560, 1440), Image.LANCZOS)

resized_image.save('bnar_2560x1440.png')

print('done!')
