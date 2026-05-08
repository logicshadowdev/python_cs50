from PIL import Image, ImageDraw
import math

frames = []
width, height = 500, 500

for frame in range(100):
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)

    for x in range(width):
        y = int(height/2 + 100 * math.sin((x/50) + (frame * 0.2)))

        r = int(127 + 127 * math.sin(x/30))
        g = int(127 + 127 * math.sin(x/30 + 2))
        b = int(127 + 127 * math.sin(x/30 + 4))

        for thickness in range(17):
            draw.point((x, y + thickness), fill=(r, g, b))

    frames.append(img)

frames[0].save(
    "wave.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)

print("Wave GIF created.")