# Hogwarts Browser Use

## 说明

[browser use](https://github.com/browser-use/browser-use) 是一个优秀的开源web自动化Agent，
因为这个工具内部默认使用了Google搜索，导致在中国区比较难以使用。
为了让霍格沃兹测试开发学社的学员更好的使用这个工具，进行了封装。

## 快速开始

必须使用Python 3.11及以上版本。

霍格沃兹测试开发学社学员定制版 Browser-Use

```bash
hogwarts-browser-use 打开ceshiren.com 进入搜索 点击高级搜索 搜索python

hogwarts-browser-use -m gpt-4o-mini 打开ceshiren.com 进入搜索 点击高级搜索 搜索python

hogwarts-browser-use -m mistral 打开ceshiren.com 进入搜索 点击高级搜索 搜索python

hogwarts-browser-use -m qwen2.5 打开ceshiren.com 进入搜索 点击高级搜索 搜索python

# 复用浏览器方式，需要提前在9222端口启动调试模式的浏览器，详见下一小节
hogwarts-browser-use --reuse-browser -m qwen2.5 打开ceshiren.com 进入搜索 点击高级搜索 搜索python
```

### 启动调试模式的浏览器

- 使用命令`hogwarts-browser-debug`，可以直接启动一个带有调试模式的chrome浏览器
- 可以手动启动调试模式的浏览器，需要先完全关闭chrome浏览器，然后过在启动浏览器时添加参数 `--remote-debugging-port=9222`

## 大模型

- 通过参数或者环境变量使用自己的大模型
- 使用霍格沃兹测试开发学社分配的gpt token
- 使用霍格沃兹测试开发学社提供的在线大模型服务

## 关于

- 霍格沃兹测试开发学社 https://testing-studio.com
- 测吧（北京）科技有限公司 https://ceba.ceshiren.com