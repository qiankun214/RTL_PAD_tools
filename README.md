# RTL_PAD_tools

RTL_PAD_tools即`RTL python aided design`工具包，其功能为使用python辅助进行**模块内**的逻辑（模块间辅助设计可以使用verilog_progen项目）。

个人理解的模块内设计应当是这样：
1. 明确功能
2. 确定每个寄存器和寄存器的功能
3. 确定每个寄存器的逻辑，并将复用或由明确含义的整理成wire
4. 验证

这个过程中，步骤1为理解需求文档，步骤2-4都在编写文档部分完成，编写RTL代码仅仅是对文档的翻译，合格的文档应当对设计中每个寄存器的功能、逻辑和时序进行描述。本工具目标为在编写文档的过程中，使用易于编写的python语言描述寄存器的功能，通过波形对比的方式粗略验证文档编写的正确性。

# 模块的建立

引用module类和装饰器reg和drive：

```python
from sim.module import module,reg,drive
```

通过继承的方式建立module

```python
class test(module):

    def __init__(self) -> None:
        super(test,self).__init__()
        self.din_valid()
        self.din_busy()
        self.din_valid_reg()

    @reg(initial_value=0)
    def din_valid(self):
        print("valid is",self.value.din_valid)
        return self.value.din_valid_reg

    @reg(initial_value=1)
    def din_busy(self):
        print("busy is",self.value.din_busy)
        return self.value.din_valid % 2 

    @drive(initial_value=1)
    def din_valid_reg(self):
        print("valid reg is ",self.value.din_valid_reg)
        yield 1
        print("valid reg is ",self.value.din_valid_reg)
        yield 2
        print("valid reg is ",self.value.din_valid_reg)
        yield 3
        print("valid reg is ",self.value.din_valid_reg)
        yield 4
```

使用装饰器`reg`定义一个方法，这个方法被定义为寄存器型变量，方法名即为寄存器名，可以使用`self.value.<name>`访问，该方法每个cycle会被调用，需要将值返回：

```python
@reg(initial_value=0)
def din_valid(self):
    print("valid is",self.value.din_valid)
    return self.value.din_valid_reg
```

同理，使用装饰器`drive`定义激励，使用生成器的方法定义激励，每个cycle