file = open('image.jpg', "rb")

image = file.read()
file.close()

image = bytearray(image)
key = 48

for i,j in enumerate(image):
	image[i]=j^key

file = open("encrypted.jpg","wb")
file.write(image)
file.close()
