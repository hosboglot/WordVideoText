from PIL import Image, ImageDraw, ImageFont
import textwrap


def write_text(text, speed):
    sample = Image.open('Resources/sample.png')
    sample = sample.resize((720, 360))
    frames = [sample]

    text = textwrap.fill(text, 37, max_lines=13, placeholder='')
    for text in [text[:j] for j in range(1, len(text) + 1)]:
        if text[-1] in (' ', '\n'):
            continue
        with sample.copy() as frame:
            draw_text = ImageDraw.Draw(frame)
            draw_text.multiline_text((190, 70), text, '#000000', ImageFont.truetype('Resources/times.ttf', 18))
            frames.append(frame)
    frames.extend([frames[-1]] * 5)
    frames[0].save('output.gif', save_all=True, append_images=frames[1:], optimize=True, duration=(6-speed) * 150)


if __name__ == '__main__':
    write_text('Hello, world!', 2)
