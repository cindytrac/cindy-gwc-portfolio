from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("dogwalk.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

add = 0
counter = 0

for pix in image_list:
    add = pix[0]+ pix[1] + pix[2]

    if add < 182:
        pix = (darkBlue)
        recolored.append(pix)

    elif (add > 182) and (add < 364):
        pix = (red)
        recolored.append(pix)
    elif (add > 364) and (add < 546):
        pix = (lightBlue)
        recolored.append(pix)
    else:
        pix = (yellow)
        recolored.append(pix)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
