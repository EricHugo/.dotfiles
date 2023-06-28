# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

export EDITOR="vim"
export CLICOLOR=yes

shopt -s histappend
HISTSIZE=10000
HISTFILESIZE=20000
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
shopt -s cdspell

case "$TERM" in
    xterm-color|*-256color|alacritty) color_prompt=yes;;
esac

if [ "$color_prompt" = yes ]; then
    PS1='\[\e[0m\]#\[\e[0m\][\[\e[0;1m\]\u\[\e[0m\]@\[\e[0;1;96m\]\h \[\e[0m\]\w\[\e[0m\]]\[\e[0m\]$\[\e[0m\]\n'
else
    pass
fi



if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
    alias rgrep='rgrep --color=auto' # GS added
fi
