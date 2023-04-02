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
git checkout [branchname] 或者 git switch branchname
git merge [brachname] // in other branch environment
git branch -d [branchname]
当一个file在branchA中修改，在branchB中修改，此时git merge就会导致conflict得产生，这个时候需要手动修改代码
在实际开发中的策略应该包括：
- main 非常稳定的，仅仅用于发布新的版本
- dev 用于开发的版本，等到成熟之后才把dev版本合并到main中
- 每个人可以在dev的分支上干活，每个人都有自己的分支，可以往dev上merge
![16777475726656](https://chenxia31blog.oss-cn-hangzhou.aliyuncs.com/2023/03/16777475726656.jpg?chenxia31blog/sample.jpg?x-oss-process=style/stylename)

