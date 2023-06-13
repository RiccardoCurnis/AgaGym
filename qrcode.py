import qrcode
img= qrcode.make("Hello World, Ciao Simone!")
img.save("mycode.png")