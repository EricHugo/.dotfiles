call plug#begin()
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
Plug 'nanotech/jellybeans.vim'
Plug 'scrooloose/syntastic'
Plug 'vim-airline/vim-airline'
Plug 'scrooloose/nerdcommenter'
Plug 'valloric/youcompleteme'
Plug 'tpope/vim-repeat'
Plug 'raivivek/vim-snakemake'
Plug 'lukas-reineke/indent-blankline.nvim'
Plug '~/git/simplechecklist.vim'
"Plug 'erichugo/simplechecktlist.vim'
call plug#end()

let g:NERDCreateDefaultMappings = 1

set mouse=a
set history=1000
set wildmenu
set smartcase
set backspace=eol,start,indent
set whichwrap+=<,>,h,l
set showmatch
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4

set noerrorbells
set novisualbell
set t_vb=
set tm=500

set encoding=utf8
set ffs=unix,dos,mac

filetype plugin on
filetype indent on
syntax enable

map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l
map 0 ^
map <SPACE> <Nop>
let mapleader="\<SPACE>"

" Delete trailing white space on save
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun

if has("autocmd")
    autocmd BufWritePre *.txt,*.js,*.py,*.wiki,*.sh,*.coffee :call CleanExtraSpaces()
endif

" Return to last edit position when opening files 
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
" Set to auto read when a file is changed from the outside
set autoread
au FocusGained,BufEnter * checktime

" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
    set wildignore+=.git\*,.hg\*,.svn\*
else
    set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif

if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif

try
    colorscheme jellybeans
catch
endtry

" Set extra options when running in GUI mode
if has("gui_running")
    set guioptions-=T
    set guioptions-=e
    set t_Co=256
    set guitablabel=%M\ %t
endif

