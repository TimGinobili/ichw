# ichw2

# Q1:用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么.

## A1:

### 为何要证明：

1900年，数学家希尔伯特提出了23个具有挑战性的数学课题，

其中提到了算数公理的无矛盾性，即在一个体系中所有的命题都可以被证明或证伪。而这个命题被后来的哥德尔不完备性定理推翻。

图灵为了解决这个问题，希望设计模型来证明“图灵停机问题”，即“是否存在一个程序P，对于任意输入的程序w，能够判断w会在有限时间内结束或者死循环”，
并通过这种方式解决希尔伯特的问题。

### 证明方法：

假设存在一个万能程序H，其可以判断一个程序能否停机。再构造一个程序K，其可以调用H但与H的输出相反：

若K的输入经H判断为可以停机，则K不停机；若K的输入经H判断为不可停机，则K停机。

现在把K输入K，让H来判断，结果将是：如果K能够停机则K陷入循环，如果K不能停机则K停机。

结果矛盾，故结论是：不存在这样的万能程序H。

### 数学原理：

是康托尔对角线原理。

 
# Q2:你在向中学生做科普，请向他们解释二进制补码的原理.

## A2:

补码是计算机中用来表示负数，使得负数能够使用加法器参与加法运算的一种码，

也就是说补码可以把加减法统一起来，让减法也可以按照加法的规则运算，即减去一个数等于加上它的相反数（补码）。

那么如何求一个数的补码？

简单地说就是规定的模减去这个数。

举个例子，假如一个时钟现在显示的是7点，如何将它调到4点？有两种方法：向前拨9个小时，或者向后拨3个小时。

此时9+3=12，12是模，9和3就互为补码。7-3和7+（12-3）的结果是一样的。

可是7+（12-3）不应该等于16吗？是的，但是你的钟并没有地方存储这多余的12个小时，

换句话说，你把这溢出的12个小时自动舍弃了。当第二个人来查看时钟时间的时候，他看到的时间就是准的。

在二进制中，正数的补码仍然是它本身。

负数补码的求法是：将该二进制数的各位（不考虑符号位）逐一求反，再加1，即得到该数的补码。如101101的补码求法即为:求反，得110010，加1，得110011，即为其补码。

为什么可以这么求呢？观察上面的例子，不考虑符号位，10011+01101=100000，就等于5位二进制的模。

所以在计算减法的时候，可以直接用加上补码的操作代替减去某个值。如15-10 要想让减法变加法，必须转换算式为 15+（-10）

15为正数，符号位为0，二进制表示为01111

-10为负数，符号位为1，负数源码为11010 ，补码符号位不变，其余逐位求反再 +1，即10110

所以 15+（-11）=01111+10110 = 100100，舍弃最高位（由于存储只限5位）溢出位，即00100，即+4

# Q3: IEEE 754浮点数格式的 16 bit 浮点数表示, 有 8 个小数位, 请给出 ±0, ±1.0, 最大非规范化数, 最小非规范化数, 最小规范化浮点数, 最大规范化浮点数,±∞, NaN 的二进制表示.

## A3:

*      Sign  	  Exp  	      Frac  	       Value

*      *        0000000     00000000      ±0

*      0        0111111     00000000      1.0

*      1        0111111     00000000      -1.0

*      *        0000000     11111111      ±(1-2^(-8))* 2^(-62)

*      *        0000000     00000001      ±2^(-8)* 2^(-62)

*      *        0000001     00000000      ±2^(-62)

*      *        1111110     11111111      ±(2-2^(-8))* 2(63)

*      *        1111111     00000000      ±∞

*      *        1111111     non zero      NaN
