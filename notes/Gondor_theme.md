To change console to a gondor theme set PS1 value

```bash
PS1="[\\u@\e[1;36mGondor\e[0m \W]\$ "
```

Here's a breakdown of its components:
- [ and ]: Literal characters forming the start and end of the prompt display.
- \u: Displays the current username (e.g., root, user1).
- @: A literal '@' symbol.
- \e[1;36m: An ANSI escape sequence that sets the text color to bright cyan (bold).
- Gondor: The hostname of the machine.
- \e[0m: Resets text formatting back to default (turns off the color).
- \W: Shows the basename (last part) of the current working directory (e.g., ~ for home, docs for /home/user/docs).
- \$: Displays a $ if you're a normal user, or a # if you're the root user (super-user), indicating the prompt level.

this is better 
```bash
# --- Middle-earth Colors ---
export PS1='\[\e[38;5;94m\]\u@\h \[\e[38;5;136m\]\w \[\e[38;5;58m\]❯ \[\e[0m\]'
```
