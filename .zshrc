# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi

NEWLINE=$'\n'
#PROMPT="[%F{214}%n%f@%B%F{32}%m%f%b %~]$ ${NEWLINE}"

eval "$(oh-my-posh init zsh --config ~/zsh/theme.omp.json)"

