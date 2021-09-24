
##  Go 环境

### [配置go环境](https://learnku.com/articles/24924#01ba0b)

####  1. 安装
- 1.1 下载包
```console 
wget https://dl.google.com/go/go1.12.linux-amd64.tar.gz
sudo tar xzvf go1.12.linux-amd64.tar.gz -C /usr/local/
```
- 1.2 配置环境
配置 PATH 及 GOPATH#

``` console
mkdir -p /export/go/{bin,pkg,src}
export GOPATH=/export/go
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

####  2. [vim配置]()

```console
"==============================================================================
" vim 内置配置
"==============================================================================

" 设置 vimrc 修改保存后立刻生效，不用在重新打开
" 建议配置完成后将这个关闭
autocmd BufWritePost $MYVIMRC source $MYVIMRC

" 关闭兼容模式
set nocompatible

set nu " 设置行号
set cursorline "突出显示当前行
" set cursorcolumn " 突出显示当前列
set showmatch " 显示括号匹配

" tab 缩进
set tabstop=4 " 设置Tab长度为4空格
set shiftwidth=4 " 设置自动缩进长度为4空格
set autoindent " 继承前一行的缩进方式，适用于多行注释

" 定义快捷键的前缀，即<Leader>
let mapleader=";"

" ==== 系统剪切板复制粘贴 ====
" v 模式下复制内容到系统剪切板
vmap <Leader>c "+yy
" n 模式下复制一行到系统剪切板
nmap <Leader>c "+yy
" n 模式下粘贴系统剪切板的内容
nmap <Leader>v "+p

" 开启实时搜索
set incsearch
" 搜索时大小写不敏感
set ignorecase
syntax enable
syntax on                    " 开启文件类型侦测
filetype plugin indent on    " 启用自动补全

" 退出插入模式指定类型的文件自动保存
au InsertLeave *.go,*.sh,*.php write
```
#### 3. [go升级到最新](https://github.com/lichengshuang/go/blob/main/tools/updatego.sh)
```console
#!/bin/bash
###在进行有些工作的时候 他们要求go的版本比较go
### 假如在命令行里加 脚本后加 update 那就升级
go version

line=$1

function dnsfile()
    {
    ### 因为dns的问题有时候下面域名解析出问题
cat >/etc/resolv.conf <<EOF
options timeout:2 attempts:3 rotate single-request-reopen
nameserver 119.29.29.29
nameserver 223.5.5.5
EOF

    }

function removego()
    {
    ##升级需要卸载旧的go
    apt-get -y --purge remove golang* ||  yum -y remove golang
    }
###先判断命令行参数，然后在让输入判断
if [[ $line == 'update' ]];then
    echo "开始升级"
else
    read -p '是否需要升级go版本:yes(y) or no(n)'  anser
    if [[ $anser == 'y' ]];then
        echo "开始升级"
    else
        echo "结束升级进程退出"
        exit 0
    fi
fi


dnsfile
removego

cd /tmp/
test -f go1.17.1.linux-amd64.tar.gz || wget -t 1 --timeout=3s  https://golang.org/dl/go1.17.1.linux-amd64.tar.gz

if [[ $? == 0 ]]; then
    echo "开始解包安装"
    rm -rf /usr/local/go && tar -C /usr/local -xvf go1.17.1.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
else
    echo "无包"
fi

if grep '/usr/local/go/bin'  ~/.bashrc;then
    echo "已经有环境变量了"
else
    echo "加环境变量了"
    echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc
fi

source ~/.bashrc

go version

```

