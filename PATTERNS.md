# Patterns Introduction（设计模式介绍）

## Strategy Pattern（策略模式）
策略模式定义了算法族，分别封装起来，让他们之间可以互相替换，此模式让算法的变化独立于使用算法的客户。

### 应用场景
1. 多个类只区别在表现行为不同，可以使用Strategy模式，在运行时动态选择具体要执行的行为。
2. 需要在不同情况下使用不同的策略(算法)，或者策略还可能在未来用其它方式来实现。
3. 对客户隐藏具体策略(算法)的实现细节，彼此完全独立。