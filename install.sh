#!/bin/bash

mkdir -p ~/.config/nvim

# TODO: check for realpath, add alternative
ln -s $(realpath ./zshrc) ~/.zshrc
ln -s $(realpath ./init.vim) ~/.config/nvim/init.vim
ln -s $(realpath ./init.vim) ~/.vimrc
ln -s $(realpath ./tmux.conf) ~/.tmux.conf
ln -s $(realpath ./gitconfig) ~/.gitconfig

# TODO: add case for X
