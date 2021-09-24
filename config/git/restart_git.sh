#!/bin/bash

#这个脚本用于删掉旧的历史记录，删掉git分支
#然后重新从现在这个状态开始
##useful:
## 比如 一不小心把密码或者一些不想放的东西给传上去了。 然后 执行他
## 把所有东西 历史记录全部重置  很好用把。


basepath=$(dirname "$(readlink -f "$0")")
#切换到git目录下
gitconfig=
myurl=
function  findsomething()
    ###找到git的全路径
    {
        basepath=$1
        if  find $basepath | grep -q '\.git'
            then
                gitconfig=$basepath
                echo "do "
                echo $gitconfig
            else
                echo "not do"
                basepath=$(dirname $basepath)
                findsomething $basepath
        fi

    }

function deleteGit()
    {
        cd $basepath
        myurl=$(cat $basepath/.git/config | grep url | awk -F= '{print $2}')
        rm -rf .git
        git init
        git add .
        git commit -m "`date` Initial commit"
        git remote add origin $myurl
        git push -u --force origin master
    }

findsomething "$basepath"
deleteGit
