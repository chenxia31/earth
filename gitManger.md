git init
git add. 添加到暂存区
git commmit 提交到工作区


commit id是区分不同地方
git追踪的是不同的修改

git log 或者git reflog可以获取不同时期的id
git reset --hard HEAD^ 或 git reset --hard commit_id可以随意到达任何一个版本
git reset 除了可以对文件夹进行操作，也可以对单个文件进行操作git reset HEAD [fileanme]
git checkout --[filename]可以丢弃修改；让文件返回到最近一次git commit之前的状态;同理也可以解决误删的情况


远程仓库的链接
关于GitHub的ssh public key和private key之间的生成回顾一下过程
ssh-keygen -t rsa -C 'your-email'
然后会在.ssh目录中生成id-rsa和id-rsa.pub文件
GitHub仓库中千万不能保存敏感信息

分支管理，不同的branch之间的划分
注意区分之间的概念，HEAD和commit-id；commit-id是最终的提交，HEAD指的是当前的分支，当前分支指向的是commit
git checkout -b 'md' 创建并转移到md分支

如何合并两个分支，可以通过将 【分支】和【分支】合并即可；合并之后可以删除没有用的分支
