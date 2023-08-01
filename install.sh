#!/bin/bash

mkdir -p ~/.config/nvim
mkdir ~/zsh

# TODO: check for realpath, add alternative
ln -sf $(realpath ./zshrc) ~/.zshrc
ln -sf $(realpath ./alacritty.yml) ~/.config/alacritty/alacritty.yml
ln -sf $(realpath ./init.vim) ~/.config/nvim/init.vim
ln -sf $(realpath ./init.vim) ~/.vimrc
ln -sf $(realpath ./tmux.conf) ~/.tmux.conf
ln -sf $(realpath ./gitconfig) ~/.gitconfig
ln -sf $(realpath ./zsh_config) ~/zsh/zsh_config
ln -sf $(realpath ./zsh/zsh_config) ~/zsh/zsh_config

# TODO: add case for X
#cp ./udevmon.yaml /etc/interception/udevmon.d
#cp ./interception_mappings.yaml /etc/interception/interception_mappings.yaml
