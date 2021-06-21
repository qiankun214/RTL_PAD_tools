# 输出波形描述方式

**时钟信号**
`..../````\..../````\....`

**单比特信号**

`.....|````````|....`

**多比特信号**

`20---|-10-----|-30-----`

# 时间片设计

1. 开始时间片
2. 计算reg类型变量
3. 更新reg类型变量
4. 计算wire类型变量
5. 更新wire类型变量
6. 结束时间片

# 访问方法

设置一个全局变量R和W分别为reg类型和wire类型的只读数据板，该数据板由signalboard生成，可以使用还能`R.name`和`W.name`访问变量
每次开始时间片是会产生两个这样的数据板

## 通过私有属性设置只读
Python里定义私有属性的方法见 http://blog.csdn.net/weixin_35653315/article/details/78073377.
用私有属性+@property定义只读属性, 需要预先定义好属性名, 然后实现对应的getter方法.
```python
class Vector2D(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

if __name__ == "__main__":
    v = Vector2D(3, 4)
    print(v.x, v.y)
    v.x = 8 # error will be raised.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
输出:

(3.0, 4.0)
Traceback (most recent call last):
  File ...., line 16, in <module>
    v.x = 8 # error will be raised.
AttributeError: can't set attribute
1
2
3
4
5
```
可以看出, 属性x是可读但不可写的.
————————————————
> 版权声明：本文为CSDN博主「Daniel2333」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。原文链接：https://blog.csdn.net/weixin_35653315/article/details/78077253