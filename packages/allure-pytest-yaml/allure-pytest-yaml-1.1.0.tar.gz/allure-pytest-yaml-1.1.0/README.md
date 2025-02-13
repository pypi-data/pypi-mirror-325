# pytest-yaml-fei

#### 介绍
本项目是基于上海悠悠的pytest-yaml-yoyo的二次开发，旨在提供一个基于YAML文件的自动化测试框架。
该项目作为一个Python的pytest插件，通过读取和解析YAML文件来生成和管理测试用例，
从而实现快速、灵活且可维护性。


#### 软件架构
python + yaml + pytest + allure + requests + logging


#### 安装教程

最低版本要求 Python 3.8 版本或以上版本. 目前兼容 python3.8, python3.9, python3.10版本 (低于 python3.8 版本无法安装此插件，低版本python不做适配) Pytest 7.2.0+ 最新版可以有最佳体验

pip 安装插件即可使用，不需要下载源码

```
pip install allure-pytest-yaml
```


#### 使用说明

使用 --start-project 命令， 帮助初学者快速创建项目 demo 结构, 并自动创建几个简单的用例。

执行以下命令

```
pytest --start-project
```

#### 参与贡献
非常感谢上海悠悠的框架支持，感谢悠悠的开源精神。
1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
