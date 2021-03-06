# TouhouChain_whitebook
[Toc]

## 一个基于区块链的去中心化皮肤交易系统

### 摘要

    本文提出了一个点对点的皮肤交易系统，不需要中心机构

### 皮肤

     我们将一串有足够信息量的随机字符作为皮肤，用这些字符中的变量生成相应的图像，能够保证这些每个皮肤都不相同

### 交易

    每个交易记录中包含发出者和接受者，发出者的数字签名和皮肤字符，并在交易时回溯，检查发出者是否拥有这个皮肤

### 账号

    每个人的账号为一对公钥私钥，其中公钥作为账户名，私钥在数字签名时使用

### 工作量证明

    本质上采用 SHA-256 碰撞，但也会加入其他机制，并会限制计算速度以降低硬件性能的影响

### 记账奖励

    最先完成工作量证明的用户将取得记账资格，记账人会将监听到的所有交易记录写入账本并发布到全网，这时，会奖励记账者一定量的皮肤,并通过工作量证明表明该块的合法性

### 区块

    一个区块应当含有两个部分，区块头与交易记录，区块头包括上一区块的哈希值，时间戳，块名称，一个随机数。
    
    交易记录为一个列表，里面存储着记账者的所记录的交易信息
    
    若篡改整个块中的任何内容，都会导致工作量证明失效和链接失效

### 安全性

    该系统没有任何中心机构存储记录用户的账户与密码，账户在全网公开，密码在用户自己手中记录，没有任何中心机构可供攻击者攻击以获取密码，存在全网链中的只有账号间的交易记录，无法查出账号的真实身份，所有交易记录在全网计算机内存储，基本没有篡改的可能性
