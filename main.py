import glob
import os
from PIL import Image

output_dir = "output"


def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    if os.path.exists(output_dir) is False:
        os.mkdir(output_dir)
    frame_one.save(output_dir + "/result.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0, transparency=0, disposal=2)


if __name__ == "__main__":
    make_gif("input")
