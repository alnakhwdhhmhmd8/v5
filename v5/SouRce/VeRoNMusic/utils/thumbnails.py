import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch
from VeRoNMusic import app
from config import YOUTUBE_IMG_URL, OWNER_ID
import math
import textwrap
from googletrans import Translator

translator = Translator()      

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""    
    for i in list:
        if len(text1) + len(i) < 30:        
            text1 += " " + i
        elif len(text2) + len(i) < 30:       
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()     
    return [text1,text2]

def crop_center_circle(img, output_size, border, crop_scale=1.5):
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    larger_size = int(output_size * crop_scale)
    img = img.crop(
        (
            half_the_width - larger_size/2,
            half_the_height - larger_size/2,
            half_the_width + larger_size/2,
            half_the_height + larger_size/2
        )
    )
    
    img = img.resize((output_size - 2*border, output_size - 2*border))
    
    final_img = Image.new("RGBA", (output_size, output_size), "white")
    
    mask_main = Image.new("L", (output_size - 2*border, output_size - 2*border), 0)
    draw_main = ImageDraw.Draw(mask_main)
    draw_main.ellipse((0, 0, output_size - 2*border, output_size - 2*border), fill=255)
    
    final_img.paste(img, (border, border), mask_main)
    
    mask_border = Image.new("L", (output_size, output_size), 0)
    draw_border = ImageDraw.Draw(mask_border)
    draw_border.ellipse((0, 0, output_size, output_size), fill=255)
    
    result = Image.composite(final_img, Image.new("RGBA", final_img.size, (0, 0, 0, 0)), mask_border)
    
    return result

def create_rgb_neon_circle(image, center, radius, border_width, steps=30):
    draw = ImageDraw.Draw(image)
    
    for step in range(steps):
        red = int((math.sin(step / steps * math.pi * 2) * 127) + 128)
        green = int((math.sin((step / steps * math.pi * 2) + (math.pi / 3)) * 127) + 128)
        blue = int((math.sin((step / steps * math.pi * 2) + (math.pi * 2 / 3)) * 127) + 128)

        draw.ellipse([
            center[0] - radius - border_width + step, 
            center[1] - radius - border_width + step, 
            center[0] + radius + border_width - step, 
            center[1] + radius + border_width - step
        ], outline=(red, green, blue), width=border_width)

    return image

async def gen_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            title = re.sub("\W+", " ", title)
            title = title.title()
            test = await translator.translate(title, dest="en")
            title = test.text
            
            duration = result["duration"] if "duration" in result else "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result["viewCount"]["short"] if "viewCount" in result else "Unknown Views"
            channel = result["channel"]["name"] if "channel" in result else "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/qthumb{vidid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/qthumb{vidid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(8))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        draw = ImageDraw.Draw(background)
        arial = ImageFont.truetype("assets/font2.ttf", 30)
        font = ImageFont.truetype("assets/font.ttf", 30)
        title_font = ImageFont.truetype("assets/font3.ttf", 45)

        circle_thumbnail = crop_center_circle(youtube, 400, 20)
        circle_thumbnail = circle_thumbnail.resize((400, 400))
        circle_position = (120, 160)
        background.paste(circle_thumbnail, circle_position, circle_thumbnail)

        create_rgb_neon_circle(background, (circle_position[0] + 200, circle_position[1] + 200), 200, 20)

        text_x_position = 565

        title1 = truncate(title)
        draw.text((text_x_position, 180), title1[0], fill=(255, 255, 255), font=title_font)
        draw.text((text_x_position, 230), title1[1], fill=(255, 255, 255), font=title_font)
        draw.text((text_x_position, 320), f"{channel}  |  {views[:23]}", (255, 255, 255), font=arial)

        line_length = 580  

        red_length = int(line_length * 0.6)
        white_length = line_length - red_length

        start_point_red = (text_x_position, 380)
        end_point_red = (text_x_position + red_length, 380)
        draw.line([start_point_red, end_point_red], fill="red", width=9)

        start_point_white = (text_x_position + red_length, 380)
        end_point_white = (text_x_position + line_length, 380)
        draw.line([start_point_white, end_point_white], fill="white", width=8)

        circle_radius = 10 
        circle_position = (end_point_red[0], end_point_red[1])
        draw.ellipse([circle_position[0] - circle_radius, circle_position[1] - circle_radius,
                      circle_position[0] + circle_radius, circle_position[1] + circle_radius], fill="red")
        draw.text((text_x_position, 400), "00:00", (255, 255, 255), font=arial)
        draw.text((1080, 400), duration, (255, 255, 255), font=arial)

        play_icons = Image.open("assets/play_icons.png")
        play_icons = play_icons.resize((580, 62))
        background.paste(play_icons, (text_x_position, 450), play_icons)

        try:
            os.remove(f"cache/qthumb{vidid}.png")
        except:
            pass
        
        background.save(f"cache/{vidid}_qv4.png")
        return f"cache/{vidid}_qv4.png"
    except Exception as e:
        return YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    thumbnail = None  
    try:
        results = VideosSearch(url, limit=1)
        search_result = await results.next()
        if "result" in search_result and search_result["result"]:
            result = search_result["result"][0] 
            title = re.sub("\W+", " ", result.get("title", "Unsupported Title")).title()
            duration = result.get("duration", "Unknown Mins")
            if result["thumbnails"]:
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]  
            views = result.get("viewCount", {}).get("short", "Unknown Views")
            channel = result.get("channel", {}).get("name", "Unknown Channel")
        else:
            print("No results found.")
            return None 
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()   
        owner = int(OWNER_ID)
        wxyz = await app.download_media(
            (await app.get_users(owner)).photo.big_file_id,
            file_name=f"{owner}.jpg",
        )     
        try:
            wxy = Image.open(wxyz)
            youtube = Image.open(f"cache/thumb{videoid}.png")
        except OSError as e:
            print(f"Error opening image: {e}")
            return YOUTUBE_IMG_URL
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(20))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        radius = 170
        logo = wxy.resize((radius * 2, radius * 2), Image.LANCZOS)
        logo = logo.convert("RGBA")
        mask = Image.new("L", logo.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, radius * 2, radius * 2), fill=255)
        logo.putalpha(mask)
        Xcenter = (background.width - logo.width) // 2
        Ycenter = (background.height - logo.height) // 2
        background.paste(logo, (Xcenter, Ycenter), logo)   
        draw = ImageDraw.Draw(background)
        arial = ImageFont.truetype("assets/font2.ttf", 70)
        font2 = ImageFont.truetype("assets/font2.ttf", 70)
        font = ImageFont.truetype("assets/font.ttf", 30)
        draw.text(
            (425, 100),
            "VERON MUSIC",
            fill="white",
            stroke_width=2,
            stroke_fill="black",
            font=font2,
        )
        draw.text(
            (55, 560),
            f"{channel} | {views[:23]}",
            (255, 255, 255),
            font=font,
        )       
        draw.line(
           [(640, 660), (1220, 660)],
           fill="white",
           width=5,
        )
        draw.line(
           [(640, 650), (1220, 650)],
           fill="white",
           width=5,
        )
        draw.line(
          [(65, 70), (640, 70)],
          fill="white",
          width=5,
        )
        draw.line(
          [(65, 60), (640, 60)],
          fill="white",
          width=5,
        )
        draw.line(
            [(55, 70), (55, 360)],
            fill="white",
            width=5,
        )
        draw.line(
            [(65, 70), (65, 360)],
            fill="white",
            width=5,
        )
        draw.line(
            [(1220, 360), (1220, 650)],
            fill="white",
            width=5,
        )
        draw.line(
            [(1230, 360), (1230, 650)],
            fill="white",
            width=5,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL