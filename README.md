# ASRT_SDK_Python3

[![GPL-3.0 Licensed](https://img.shields.io/badge/License-GPL3.0-blue.svg?style=flat)](https://opensource.org/licenses/GPL-3.0) 
[![Stars](https://img.shields.io/github/stars/nl8590687/ASRT_SDK_Python3)](https://github.com/nl8590687/ASRT_SDK_Python3) 
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/) 
<!--
[![Python package](https://github.com/nl8590687/ASRT_SDK_Python3/actions/workflows/python-package.yml/badge.svg)](https://github.com/nl8590687/ASRT_SDK_Python3/actions/workflows/python-package.yml)
[![Pylint](https://github.com/nl8590687/ASRT_SDK_Python3/actions/workflows/pylint.yml/badge.svg)](https://github.com/nl8590687/ASRT_SDK_Python3/actions/workflows/pylint.yml)
-->

An Python3 SDK and Demo example for ASRT speech recognition system. 

一个可用于ASRT语音识别系统的Python3 SDK和Demo样例

本软件是用来配套ASRT语音识别系统API调用的客户端SDK，并实现了一个演示用的Demo客户端，可以基于此进一步开发语音识别应用软件

如果您觉得喜欢，请点一个 **"Star"** 吧~

[**ASRT项目主页**](https://asrt.ailemon.net/) | 
[**ASRT语音识别系统服务端仓库**](https://github.com/nl8590687/ASRT_SpeechRecognition) |
[**发布版下载**](https://asrt.ailemon.net/download) | 
[**本项目的Wiki文档**](https://wiki.ailemon.net/docs/asrt-doc) | 
[**实用效果体验Demo**](https://asrt.ailemon.net/demo) | 
[**打赏作者**](https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1deo9u61unti9)

如果程序运行期间或使用中有什么问题，可以及时在issue中提出来，我将尽快做出答复。本项目作者交流QQ群：**894112051**

提问前请仔细查看[项目文档](https://wiki.ailemon.net/docs/asrt-doc/)、 
[FAQ常见问题](https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1deoeud494h4f)
以及[Issues](https://github.com/nl8590687/ASRT_SDK_Python3/issues) 避免重复提问

## 简介
本项目是用于ASRT语音识别系统的Python3 SDK包。

文件 `client_example.py` 为一个调用本SDK包实现的ASRT语音识别系统调用样例。运行前请先部署并启动ASRT语音识别系统服务端。

注意：本项目不能够单独实现语音识别功能，只是一个Python实现的对调用`ASRT语音识别系统`API接口过程高度封装的软件包，可以降低您的应用接入语音识别功能时的学习和开发成本。

## 安装
以下两种方式二选一即可：

直接从pypi源安装：
```shell
$ pip install asrt-sdk
```

或者，通过源码构建安装：

```shell
$ python setup.py build
$ python setup.py install
```

## 软件环境要求
* 操作系统: 支持Windows 和 Linux、MacOS
* 开发环境： Python 3.6 +

## License 开源许可协议

[GPL v3.0](LICENSE) © [nl8590687](https://github.com/nl8590687) 作者：[AI柠檬](https://www.ailemon.net/)
