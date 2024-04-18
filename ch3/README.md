
比原生的 `sys.argv` 較優的 CLI 套件為:

- argparse : 如果 CLI 功能會非常複雜, 使用 argparse
- click    : 大多數情況下開發 CLI, 使用 click
- fire     : 如果 CLI 需要快速開發, 使用 fire (具備 introspection, 非常省 Code, 並且自帶 指令 及 說明文件)
