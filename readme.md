# q6p3ui

## 加载插件

加载插件的机制是通过一个 C++ 预先写好的 PySidePlugin.dll 插件来加载 Python 的插件。
这个 DLL 放在 Python 环境的 Lib\site-packages\PySide6\plugins\designer 和其他插件一起在目录下。
通过环境变量 PYSIDE_DESIGNER_PLUGINS 指定 Python 插件的目录。
不过目前好像有 bug ，无法找到目录，指定了官方的示例也是找不到模块。
官方示例文档目录下 Lib\site-packages\PySide6\examples\designer\taskmenuextension 。
