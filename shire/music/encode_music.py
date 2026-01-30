from urllib.parse import quote

with open("shire_music.js") as f:
    code = f.read()

print(quote(code))

