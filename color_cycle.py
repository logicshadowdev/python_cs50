from PIL import Image, ImageDraw
frames =[]
colors = ["red", "orange", "yellow", "blue", "green", "purple", "pink"]

for color in colors:
    img = Image.new("RGB", (500, 500), color="black")
    draw = ImageDraw.Draw(img)
    draw.ellipse([100, 100, 400, 400], fill=color, outline="white", width=5)

    frames.append(img)

frames[0].save(
    "color_cycle.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,
    loop=0
)

print("Color cycling GIF created.")