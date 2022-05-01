from PIL import Image, ImageDraw, ImageFont


class ProcessImage:
    def __init__(self, names_txt, certificate, location, font, font_size=50):
        self.location = location
        self.certificate = Image.open(certificate).convert(mode='RGB')
        self.width = self.certificate.width
        self.font = ImageFont.truetype(font, font_size)

        with open(names_txt, 'r') as f:
            self.names = [line.strip() for line in f]

    def generate_certificates(self):
        for i, name in enumerate(self.names):
            img = self.certificate.copy()
            draw = ImageDraw.Draw(img)
            print(f'Generating certificate for {name}...')

            if self.location[0] != 'center':
                draw.text(self.location, f"{name}", fill=(0, 0, 0), font=self.font)
            else:
                draw.text((self.__get_center(name, draw)), f"{name}", fill=(0, 0, 0), font=self.font)
            img.save(f"certs/{i}_{name}.jpeg")

    def __get_center(self, name, draw):
        text_len = draw.textlength(name, self.font)
        x = (self.width / 2) - (text_len / 2)
        return x, self.location[1]
