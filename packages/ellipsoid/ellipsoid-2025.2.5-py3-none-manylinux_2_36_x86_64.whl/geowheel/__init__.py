"""
Python 定义了两种类型的包，常规包 和 命名空间包。 常规包是传统的包类型，它们在 Python 3.2 及之前就已存在。 常规包通常以一个包含 __init__.py 文件的目录形式实现。 当一个常规包被导入时，这个 __init__.py 文件会隐式地被执行，它所定义的对象会被绑定到该包命名空间中的名称。__init__.py 文件可以包含与任何其他模块中所包含的 Python 代码相似的代码，Python 将在模块被导入时为其添加额外的属性。

例如，以下文件系统布局定义了一个最高层级的 parent 包和三个子包:

parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
导入 parent.one 将隐式地执行 parent/__init__.py 和 parent/one/__init__.py。 后续导入 parent.two 或 parent.three 则将分别执行 parent/two/__init__.py 和 parent/three/__init__.py。
"""