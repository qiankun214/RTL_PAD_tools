# RTL_PAD_tools

RTL_PAD_tools即`RTL python aided design`工具包，其功能为使用python辅助进行**模块内**的逻辑（模块间辅助设计可以使用verilog_progen项目）。

个人理解的模块内设计应当是这样：
1. 明确功能
2. 确定每个寄存器和寄存器的功能
3. 确定每个寄存器的逻辑，并将复用或由明确含义的整理成wire
4. 验证

这个过程中，步骤1为理解需求文档，步骤2-4都在编写文档部分完成，编写RTL代码仅仅是对文档的翻译，合格的文档应当对设计中每个寄存器的功能、逻辑和时序进行描述。本工具目标为在编写文档的过程中，使用易于编写的python语言描述寄存器的功能，通过波形对比的方式粗略验证文档编写的正确性。