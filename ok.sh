#!/bin/bash
basepath=$(dirname "$(readlink -f "$0")") #绝对路径
cd $basepath
git add .
echo "文件添加"
git commit -m "`date` ok" 
echo "文件更新"
git push 
echo "文件完成"
