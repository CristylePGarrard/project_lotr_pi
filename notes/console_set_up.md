#### install font libraries

```bash
sudo apt update && sudo apt upgrade
```

```bash
sudo apt install fonts-firacode fonts-jetbrains-mono
```

Update settins to font

#### update console settings

```bash
# --- Middle-earth Colors ---
export PS1='\[\e[38;5;94m\]\u@\h \[\e[38;5;136m\]\w \[\e[38;5;58m\]❯ \[\e[0m\]'
```

Color meanings:
- 94 → aged parchment
- 136 → gold
- 58 → dark forest green/brown

Update bashrc file

```bash
source ~/.bashrc
```

#### Greeting at opening of console

#### figlet and lolcat

```bash
sudo apt install figlet lolcat
```

```bash
vim ~/.motd_lotr
```

```bash
#!/bin/bash
figlet "Middle Earth" | lolcat
echo ""
echo " ✨ Elen síla lúmenn’ omentielvo ✨"
echo " --------------------------------"
echo " The road goes ever on and on..."
echo ""
echo "—— Imladris Terminal ——"
```

```bash
chmod +x ~/.motd_lotr
```

add ```bash ~/.motd_lotr```to ~/.motd_lotr file


#### fun aliases

update .bashrc

```bash
# --- Middle-earth Aliases ---
alias fellowship='htop'
alias lembas='sudo apt update && sudo apt upgrade'
alias mordor='cd /'
alias shire='cd ~'
alias gandalf='echo "A wizard is never late, nor is he early."'
```


