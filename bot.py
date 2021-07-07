import discord
from discord.ext import commands
import random
import aiohttp
import os
import json
import asyncio

bot = commands.Bot(command_prefix='*')





@bot.command()
async def p(ctx):
    await ctx.send(f'@everyone')

@bot.command()
async def плюс(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def хелпПЛЮС(ctx):
    await ctx.send ('```*ПЛЮС 1 число 2 число```')

@bot.command()
async def умн(ctx, a: int, b: int):
    await ctx.send (a * b)

@bot.command()
async def ХЕЛПУМН(ctx):
    await ctx.send ('```*УМН 1 число 2 число```')

@bot.command()
async def мин(ctx, a: int, b: int):
    await ctx.send (a - b)

@bot.command()
async def хелпМИН(ctx):
    await ctx.send ('```*МИН 1 число 2 число```')

@bot.command()
async def дел(ctx, a: int, b: int):
    await ctx.send (a // b)

@bot.command()
async def хелпДЕЛ(ctx):
    await ctx.send ('```*ДЕЛ 1 число 2 число```')

@bot.command()
async def хелп(ctx):
    await ctx.send('```*умн 1 число 2 число \n*дел 1 число 2 число \n*мин 1 число 2 число \n*плюс 1 число 2 число\n*anime показывает рандомную картинку\n*hentai показывает рандомное хентай изображение```')

@bot.command()
async def аниме(ctx):
    imgs = [
        "https://c.wallhere.com/images/4a/47/f2a9464ba6d875df6cf33cc5535c-1543221.jpg!d",
        "https://im0-tub-ru.yandex.net/i?id=9671df1f0773ef3e6bb3b6d08ff21630&ref=rim&n=33&w=213&h=150",
        "https://im0-tub-ru.yandex.net/i?id=63f8a706c03fa48a59b4eed9acbf6315&ref=rim&n=33&w=267&h=150",
        "https://thumbs.gfycat.com/GrandioseZestyIbex-size_restricted.gif"
    ]
    await ctx.send(random.choice(imgs))

@bot.command()
async def gif(ctx):
    imgs4 = [
        "https://media1.tenor.com/images/efb20dfc8abed06d3d2ceef313bbd40b/tenor.gif?itemid=19510299",
        "https://thumbs.gfycat.com/CalculatingGreenDanishswedishfarmdog-max-1mb.gif",
        "https://thumbs.gfycat.com/LikelyDismalBobcat-size_restricted.gif",
        "https://delovoymir.biz/res/images/uploaded/columns/dop/15320.gif"
    ]
    await ctx.send(random.choice(imgs4))



@bot.command()
async def among(ctx):
    amogus = [
        "https://images.smash.gg/images/user/1289184/image-5f6c95d7d032ca2ba1c92042971acb8e.gif",
        "https://media.sketchfab.com/models/04f3d7452bac4799bcab779e21d60f16/thumbnails/db11e90c20c6436b806fd0f6affeded2/0b13f55572fb4a67ba27df72272fe3e2.jpeg",
        "http://risovach.ru/upload/2020/11/mem/a_255260244_orig_.jpg",
        "https://static.wikia.nocookie.net/34227392-b6b6-4874-911d-49c9bbe73655/scale-to-width/755",
        "https://i.ytimg.com/vi/JCxb690uSbM/maxresdefault.jpg"
    ]
    await ctx.send(random.choice(amogus))




client = discord.Client()



from asyncio import sleep
@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("Я БОТ А ВЫ"))
          await sleep(5)
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("ЧЕЛОВЕКИ"))
          await sleep(5)







@bot.command()
async def хентай(ctx):
    imgs1 = [
        "https://2.bp.blogspot.com/-3L/CJnAOZzdE/VCe8QQstlUI/AAAAAAAAHPc/6Fv3wGOJsJY/s1600/anichcicks_bondage+(20)",
       "https://im0-tub-ru.yandex.net/i?id=e6d15eef835fd16d1a016a64536bdcad&ref=rim&n=33&w=256&h=150",
        "https://im0-tub-ru.yandex.net/i?id=ca13dd43b0952796331781cff8ce25a5&ref=rim&n=33&w=267&h=150"




    ]
    await ctx.send(random.choice(imgs1))





@bot.command()
async def hentai(ctx):
    imgs2 = [
        "https://2.bp.blogspot.com/-3L/CJnAOZzdE/VCe8QQstlUI/AAAAAAAAHPc/6Fv3wGOJsJY/s1600/anichcicks_bondage+(20)",
        "https://im0-tub-ru.yandex.net/i?id=e6d15eef835fd16d1a016a64536bdcad&ref=rim&n=33&w=256&h=150",
        "https://im0-tub-ru.yandex.net/i?id=ca13dd43b0952796331781cff8ce25a5&ref=rim&n=33&w=267&h=150"




    ]

    if ctx.channel.is_nsfw():
     await ctx.send(random.choice(imgs2))
    else:
       await ctx.send("Прости, но эту команду можно использовать только в канале NSFW")



bot.run('ODQxNzExMzk0ODc3NjAzODYw.YJqu0g.EbuE27LV81_J_AUBQ_tEA2k6fF4')
