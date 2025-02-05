from enum import Enum

class PantoneColor(Enum):
    CERULEAN = 2000  # 蔚蓝色, Pantone 15-4020
    FUCHSIA_ROSE = 2001  # 紫红玫瑰, Pantone 17-2031
    TRUE_RED = 2002  # 正红, Pantone 19-1664
    AQUA_SKY = 2003  # 水色天空, Pantone 14-4811
    TIGERLILY = 2004  # 虎皮百合, Pantone 17-1456
    BLUE_TURQUOISE = 2005  # 蓝绿松石, Pantone 15-5217
    SAND_DOLLAR = 2006  # 沙金色, Pantone 13-1106
    CHILI_PEPPER = 2007  # 辣椒红, Pantone 19-1557
    BLUE_IRIS = 2008  # 鸢尾蓝, Pantone 18-3943
    MIMOSA = 2009  # 含羞草黄, Pantone 14-0848
    TURQUOISE = 2010  # 松石绿, Pantone 15-5519
    HONEYSUCKLE = 2011  # 忍冬红, Pantone 18-2120
    TANGERINE_TANGO = 2012  # 探戈橘, Pantone 17-1463
    EMERALD = 2013  # 翡翠绿, Pantone 17-5641
    RADIANT_ORCHID = 2014  # 璀璨紫兰花, Pantone 18-3224
    MARSALA = 2015  # 玛萨拉酒红, Pantone 18-1438
    ROSE_QUARTZ = 2016  # 玫瑰石英粉红, Pantone 13-1520
    SERENITY = 2016  # 宁静粉蓝, Pantone 15-3919
    GREENERY = 2017  # 草木绿, Pantone 15-0343
    ULTRA_VIOLET = 2018  # 紫外光色, Pantone 18-3838
    LIVING_CORAL = 2019  # 珊瑚橘, Pantone 16-1546
    CLASSIC_BLUE = 2020  # 经典蓝, Pantone 19-4052
    ULTIMATE_GRAY = 2021  # 极致灰, Pantone 17-5104
    ILLUMINATING = 2021  # 亮丽黄, Pantone 13-0647
    VERY_PERI = 2022  # 长春花蓝, Pantone 17-3938
    VIVA_MAGENTA = 2023  # 非凡洋红, Pantone 18-1750
    PEACH_FUZZ = 2024  # 柔和桃, Pantone 13-1023

# 示例用法
print(PantoneColor.CLASSIC_BLUE.name, PantoneColor.CLASSIC_BLUE.value)
