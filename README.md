# -
在渗透测试中，发现目标站点有时候会存在一些通过通用字典扫不出来的路径，而这些路径大多为与目标公司名称相关，或是与子域名与主域名相关，例如：
www.baidu.com/baidu/pic
www.baidu.com/baidupic/

talent.baidu.com/talnet/admin
talent.baidu.com/baidu/talnet

因此通用字典已经满足不了需求了，因此写了一个脚本，通过混合多个输入的路径+内置小字典进行混合，给出定制化的小字典。
通过定制化的小字典去目录扫描可能会有意想不到的收获，曾经扫到过一个列目录的路径，后续里面发现了大量信息泄露。

使用示例：
假设目标是建设银行，那么我可能会想到:ccb（建行的简称）,jianshe,jsyh等等，或者是目标的子域名为abc，那么我会将abc也加入进去。
![image](https://github.com/WhatHowie/-/assets/125801879/63d08040-3c45-45e2-870b-e86bc7e6045e)


得到结果：
![image](https://github.com/WhatHowie/-/assets/125801879/9cf3c961-29cd-49db-89ca-cf4bdf2270f5)
![image](https://github.com/WhatHowie/-/assets/125801879/d4ffaac8-50c7-41c1-8276-2ecb54b1f89b)


目前内置的小字典不多，如果想添加觉得常出现的，可以自己添加
![image](https://github.com/WhatHowie/-/assets/125801879/07f11ba2-32fa-4a17-b3fc-d3942acf543a)



