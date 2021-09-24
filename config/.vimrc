set nu
filetype plugin on
set encoding=utf-8
set fileencoding=utf-8
syntax enable
syntax on
set ts=4
set softtabstop=4
set shiftwidth=4
set showmatch
let g:pydiction_location='/home/asher/.vim/bundle/pydiction/complete-dict'
let g:pydiction_menu_height = 3

let Tlist_Auto_Highlight_Tag=1  
let Tlist_Auto_Open=1  
let Tlist_Auto_Update=1  
let Tlist_Display_Tag_Scope=1  
let Tlist_Exit_OnlyWindow=1  
let Tlist_Enable_Dold_Column=1  
let Tlist_File_Fold_Auto_Close=1  
let Tlist_Show_One_File=1  
let Tlist_Use_Right_Window=1  
let Tlist_Use_SingleClick=1  
nnoremap <silent> <F8> :TlistToggle<CR>
   
filetype plugin on  
autocmd FileType python set omnifunc=pythoncomplete#Complete  
   
set autoindent
set tabstop=4  
set shiftwidth=4  
set expandtab  
set number
