from dataclasses import dataclass
import re
from PIL import Image, ImageDraw, ImageFont
from types import SimpleNamespace

@dataclass
class BaseColor:
    hex: str = None
    rgb: tuple[int, int, int] = None
    cmyk: tuple[int, int, int, int] = None

    def __post_init__(self):
        """Automatically complete missing color formats"""
        if self.hex:
            self.rgb = self.hex_to_rgb(self.hex)
            self.cmyk = self.rgb_to_cmyk(self.rgb)
        elif self.rgb:
            self.hex = self.rgb_to_hex(self.rgb)
            self.cmyk = self.rgb_to_cmyk(self.rgb)
        elif self.cmyk:
            self.rgb = self.cmyk_to_rgb(self.cmyk)
            self.hex = self.rgb_to_hex(self.rgb)
        else:
            raise ValueError("At least one of HEX, RGB, or CMYK must be provided")

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """Convert HEX to RGB"""
        hex_color = hex_color.lstrip("#")
        if re.fullmatch(r"[0-9A-Fa-f]{6}", hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        raise ValueError("Invalid HEX color format")

    @staticmethod
    def rgb_to_hex(rgb_color: tuple[int, int, int]) -> str:
        """Convert RGB to HEX"""
        if not all(0 <= c <= 255 for c in rgb_color):
            raise ValueError("RGB values must be in the range 0-255")
        return "#{:02X}{:02X}{:02X}".format(*rgb_color)

    @staticmethod
    def rgb_to_cmyk(rgb_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
        """Convert RGB to CMYK"""
        r, g, b = [x / 255.0 for x in rgb_color]
        k = 1 - max(r, g, b)
        if k == 1:
            return 0, 0, 0, 100  # Pure black
        c = (1 - r - k) / (1 - k) * 100
        m = (1 - g - k) / (1 - k) * 100
        y = (1 - b - k) / (1 - k) * 100
        k *= 100
        return int(c), int(m), int(y), int(k)

    @staticmethod
    def cmyk_to_rgb(cmyk_color: tuple[int, int, int, int]) -> tuple[int, int, int]:
        """Convert CMYK to RGB"""
        if not all(0 <= c <= 100 for c in cmyk_color):
            raise ValueError("CMYK values must be in the range 0-100")
        c, m, y, k = [x / 100.0 for x in cmyk_color]
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)
        return int(r), int(g), int(b)
    
    def canvas(self):
        """Display the color with a side color bar and annotated text"""
        width, height = 300, 100  # Canvas size
        color_bar_width = 100  # Width of the color bar

        # Create a blank white image
        canvas = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(canvas)

        # Draw the color bar
        draw.rectangle([(width - color_bar_width, 0), (width, height)], fill=self.rgb)

        # Prepare text information
        text_lines = [
            f"HEX: {self.hex}",
            f"RGB: {self.rgb}",
            f"CMYK: {self.cmyk}"
        ]
        
        # Load a default font
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            font = ImageFont.load_default()

        # Draw text on the left side
        text_x, text_y = 10, 20
        for line in text_lines:
            draw.text((text_x, text_y), line, fill="black", font=font)
            text_y += 30  # Spacing between lines
        return canvas
    
    def show(self):
        """Display the color and information"""
        self.canvas().show()

class Color(SimpleNamespace):
    RED = BaseColor(hex="#FF0000")         # 红色
    GREEN = BaseColor(hex="#00FF00")       # 绿色
    BLUE = BaseColor(hex="#0000FF")        # 蓝色
    YELLOW = BaseColor(hex="#FFFF00")      # 黄色
    CYAN = BaseColor(hex="#00FFFF")        # 青色
    MAGENTA = BaseColor(hex="#FF00FF")     # 品红
    WHITE = BaseColor(hex="#FFFFFF")       # 白色
    BLACK = BaseColor(hex="#000000")       # 黑色
    GRAY = BaseColor(hex="#808080")        # 灰色
    ORANGE = BaseColor(hex="#FFA500")      # 橙色
    PURPLE = BaseColor(hex="#800080")      # 紫色
    PINK = BaseColor(hex="#FFC0CB")        # 粉色
    BROWN = BaseColor(hex="#A52A2A")       # 棕色
    
    PRUSSIAN_BLUE = BaseColor(hex="#003153")  # 普鲁士蓝色
    KLEIN_BLUE = BaseColor(hex="#002FA7")     # 克莱因蓝色
    MARRS_GREEN = BaseColor(hex="#01847F")    # 马尔斯绿色
    SCHONBRUNNER_GELB = BaseColor(hex="#FBD26A")  # 申布伦黄色
    BURGUNDY_RED = BaseColor(hex="#470024")  # 勃艮第红色
    
    
if __name__ == "__main__":    
    color = Color.MARRS_GREEN
    color.show()


