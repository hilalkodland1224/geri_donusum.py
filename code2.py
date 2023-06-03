import discord
from discord.ext import commands
import os
import random
import requests



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


images_icindeki_resimler = os.listdir(r'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\images')
cat_images_icindeki_resimler = os.listdir(r'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\cat_images')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is ready to launch :D')


@bot.command()
async def mem(ctx):
    rastgele_resim = random.choice(images_icindeki_resimler)
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\images\{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem_cat(ctx):
    rastgele_resim_cat = random.choice(cat_images_icindeki_resimler)
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\cat_images\{rastgele_resim_cat}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)




@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def kagit_atik(ctx):
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\geri_donusum _kutulari\kagitatik.jpg',"rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
@bot.command()
async def plastik_atik(ctx):
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\geri_donusum _kutulari\plastikatik.jpg',"rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def cam_atik(ctx):
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\geri_donusum _kutulari\camatik.jpg',"rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def evsel_atik(ctx):
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\geri_donusum _kutulari\evselatik.webp',"rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def maske_eldiven_atik(ctx):
    with open(rf'C:\Users\BuyukSef\Desktop\kodland ders kodları\M2L1\geri_donusum _kutulari\maskeveeldivenatik.webp',"rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
   

bot.run('TOKEN BURADA OLACAK')



