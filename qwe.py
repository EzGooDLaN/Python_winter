from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "lightblue")
draw = ImageDraw.Draw(image)

draw.ellipse((100, 100, 300, 300), fill="white", outline="black")
draw.ellipse((125, 50, 275, 150), fill="white", outline="black")

draw.ellipse((180, 80, 195, 95), fill="black")
draw.ellipse((205, 80, 220, 95), fill="black")

draw.polygon([(200, 100), (215, 125), (185, 125)], fill="orange")

draw.ellipse((190, 170, 210, 190), fill="black")
draw.ellipse((190, 200, 210, 220), fill="black")

draw.line((125, 180, 100, 160), fill="black", width=4)
draw.line((275, 180, 300, 160), fill="black", width=4)

draw.ellipse((-50, 250, 150, 450), fill="white", outline="black")
draw.ellipse((250, 250, 450, 450), fill="white", outline="black")

draw.ellipse((0, 0, 100, 100), fill="yellow", outline="yellow")
draw.line((10, 50, 120, 50), fill="yellow", width=3)
draw.line((55, 10, 55, 120), fill="yellow", width=3)
draw.line((20, 20, 110, 110), fill="yellow", width=3)

image.show()

