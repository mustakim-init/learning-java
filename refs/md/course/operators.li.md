---
topic: operators
lessons: "M3_L1, M3_L2"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "46-107"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "2.9.2, 2.12, 2.14, 2.15, 3.2, 3.10, 3.14, 3.15"
note: "2.9.2: Table 2.3 only. 3.2: Table 3.1 only."
generated_by: tools/extract_refs.py
---
# Operators - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.46 -->

### 2.9.2 Numeric Operators

The operators for numeric data types include the standard arithmetic operators: addition (+), subtraction (–), multiplication (*), division (/), and remainder (%), as listed in Table 2.3. The *operands* are the values operated by an operator.

**Table 2.3 Numeric Operators**

| Name | Meaning | Example | Result |
|---|---|---|---|
| + | Addition | 34 + 1 | 35 |
| - | Subtraction | 34.0 - 0.1 | 33.9 |
| * | Multiplication | 300*30 | 9000 |
| / | Division | 1.0 / 2.0 | 0.5 |
| % | Remainder | 20 % 3 | 2 |

When both operands of a division are integers, the result of the division is the quotient and the fractional part is truncated. For example, `5 / 2` yields `2`, not `2.5`, and `–5 / 2` yields `–2`, not `–2.5`. To perform a floating-point division, one of the operands must be a floating-point number. For example, `5.0 / 2` yields `2.5`.

The % operator, known as *remainder*, yields the remainder after division. The operand on the left is the dividend, and the operand on the right is the divisor. Therefore, `7 % 3` yields `1`, `3 % 7` yields `3`, `12 % 4` yields `0`, `26 % 8` yields `2`, and `20 % 13` yields `7`.

<!-- LI p.47 -->

The % operator is often used for positive integers, but it can also be used with negative integers and floating-point values. The remainder is negative only if the dividend is negative. For example, -`7 % 3` yields -`1`, -`12 % 4` yields `0`, -`26 %` -`8` yields -`2`, and `20 %` -`13` yields `7`.

Remainder is very useful in programming. For example, an even number `% 2` is always `0` and a positive odd number `% 2` is always `1`. Thus, you can use this property to determine whether a number is even or odd. If today is Saturday, it will be Saturday again in 7 days. Suppose you and your friends are going to meet in 10 days. What will be the day in 10 days? You can find that the day is Tuesday using the following expression:

The program in Listing 2.5 obtains minutes and remaining seconds from an amount of time in seconds. For example, `500` seconds contains `8` minutes and `20` seconds.

**Listing 2.5 DisplayTime.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class DisplayTime {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    // Prompt the user for input
    System.out.print("Enter an integer for seconds: ");
    int seconds = input.nextInt();

    int minutes = seconds / 60; // Find minutes in seconds
    int remainingSeconds = seconds % 60; // Seconds remaining
    System.out.println(seconds + " seconds is " + minutes +
      " minutes and " + remainingSeconds + " seconds");
  }
}
```

```text
Enter an integer for seconds: 500
500 seconds is 8 minutes and 20 seconds
```

**line#**

```text
seconds
             minutes
                          remainingSeconds
```

**8**

```text
500
```

**10**

```text
8
```

**11**

```text
20
```

The `nextInt()` method (line 8) reads an integer for `seconds`. Line 10 obtains the minutes using `seconds / 60`. Line 11 (`seconds % 60`) obtains the remaining seconds after taking away the minutes.

<!-- LI p.48 -->

The + and - operators can be both unary and binary. A *unary operator* has only one operand; a *binary operator* has two. For example, the – operator in `–5` is a unary operator to negate number `5`, whereas the – operator in `4 – 5` is a binary operator for subtracting `5` from `4`.

<!-- LI p.52 -->

## 2.12 Evaluating Expressions and Operator Precedence

*Java expressions are evaluated in the same way as arithmetic expressions.*

Writing a numeric expression in Java involves a straightforward translation of an arithmetic

**Key**

expression using Java operators. For example, the arithmetic expression

**Point**

+ 9a4 b 3 + 4*x*

- 10(*y* - 5)(*a* + *b* + *c*) *x* + 9 + *x* 5 *x y* can be translated into a Java expression as follows:

`(3 + 4 * x) / 5 – 10 * (y` - `5) * (a + b + c) / x +`

```text
9 * (4 / x + (9 + x) / y)
```

Although Java has its own way to evaluate an expression behind the scene, the result of a Java expression and its corresponding arithmetic expression is the same. Therefore, you can safely apply the arithmetic rule for evaluating a Java expression. Operators contained within pairs of parentheses are evaluated first. Parentheses can be nested, in which case the expression in the inner parentheses is evaluated first. When more than one operator is used in an expression, the following operator precedence rule is used to determine the order of evaluation:

<!-- LI p.53 -->

- Multiplication, division, and remainder operators are applied first. If an expression contains several multiplication, division, and remainder operators, they are applied from left to right.
- Addition and subtraction operators are applied last. If an expression contains several addition and subtraction operators, they are applied from left to right.

Here is an example of how an expression is evaluated:

```text
3 + 4 * 4 + 5 * (4 + 3) – 1

3 + 4 * 4 + 5 * 7 – 1

3 + 16 + 5 * 7 – 1

3 + 16 + 35 – 1

19 + 35 – 1

54 – 1

53
```

Celsius = 15

92(Fahrenheit - 32). Listing 2.6 gives a program that converts a Fahrenheit degree to Celsius using the formula

**Listing 2.6 FahrenheitToCelsius.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class FahrenheitToCelsius {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter a degree in Fahrenheit: ");
    double fahrenheit = input.nextDouble();

    // Convert Fahrenheit to Celsius
```

`11 double celsius = (5.0 / 9) * (fahrenheit` - `32);`

```java
    System.out.println("Fahrenheit " + fahrenheit + " is " +
      celsius + " in Celsius");
  }
}
```

```text
Enter a degree in Fahrenheit: 100
Fahrenheit 100.0 is 37.77777777777778 in Celsius
```

| line# | fahrenheit | celsius |
|---|---|---|
| 8 | 100 |  |
| 11 |  | 37.77777777777778 |

<!-- LI p.54 -->

Be careful when applying division. Division of two integers yields an integer in Java. 5 9 is coded `5.0 / 9` instead of `5 / 9` in line 11, because `5 / 9` yields `0` in Java.

**2.12.1** How would you write the following arithmetic expressions in Java?

**Check Point**

3(*r* + 34) - 9(*a* + *bc*) + 3 + *d*(2 + *a*) 4 a. *a* + *bd*

b. 5.5 × (*r* + 2.5)2.5+*t*

<!-- LI p.56 -->

## 2.14 Augmented Assignment Operators

> **Key Point** The operators* +, -, *, /*, and* % *can be combined with the assignment operator to form augmented operators.

Very often, the current value of a variable is used, modified, then reassigned back to the same variable. For example, the following statement increases the variable `count` by `1`:

```java
count = count + 1;
```

Java allows you to combine assignment and addition operators using an augmented (or compound) assignment operator. For example, the preceding statement can be written as

```java
count += 1;
```

The += is called the *addition assignment operator.* Table 2.4 shows other augmented assignment operators.

**Table 2.4 Augmented Assignment Operators**

| Operator | Name | Example | Equivalent |
|---|---|---|---|
| += | Addition assignment | i += 8 | i = i + 8 |
| -= | Subtraction assignment | i -= 8 | i = i - 8 |
| *= | Multiplication assignment | i *= 8 | i = i * 8 |
| /= | Division assignment | i /= 8 | i = i / 8 |
| %= | Remainder assignment | i %= 8 | i = i % 8 |

The augmented assignment operator is performed last after all the other operators in the expression are evaluated. For example,

```java
x /= 4 + 5.5 * 1.5;
```

is same as

```java
x = x / (4 + 5.5 * 1.5);
```

> **Caution** There are no spaces in the augmented assignment operators. For example, + = should be +=.

> **Note** Like the assignment operator (=), the operators (+=, -=, *=, /=, and %=) can be used to form an assignment statement as well as an expression. For example, in the following code, `x += 2` is a statement in the first line, and an expression in the second line:

<!-- LI p.57 -->

**2.14.1** Show the output of the following code:

**Check Point**

```java
double a = 6.5;
a += a + 1;
System.out.println(a);
a = 6;
a /= 2;
System.out.println(a);
```

## 2.15 Increment and Decrement Operators

*The increment operator (*+ +*) and decrement operator (*— —*) are for incrementing and decrementing a variable by 1.*

**Key**

The ++ and — — are two shorthand operators for incrementing and decrementing a variable by

**Point**

`1`. These are handy because that’s often how much the value needs to be changed in many programming tasks. For example, the following code increments `i` by `1` and decrements `j` by `1`.

```java
int i = 3, j = 3;
i++; // i becomes 4
j— —; // j becomes 2
```

`i++` is pronounced as "i plus plus" and `i— —` as "`i` minus minus." These operators are known as *postfix increment* (or *postincrement*) and *postfix decrement* (or *postdecrement*), because the operators ++ and — — are placed after the variable. These operators can also be placed before the variable. For example,

```java
int i = 3, j = 3;
++i; // i becomes 4
— —j; // j becomes 2
```

`++i` increments `i` by `1` and `— —j` decrements `j` by `1`. These operators are known as *prefix increment* (or *preincrement*) and *prefix decrement* (or predecrement).

As you see, the effect of `i++` and `++i` or `i— —` and `— —i` are the same in the preceding examples. However, their effects are different when they are used in statements that do more than just increment and decrement. Table 2.5 describes their differences and gives examples.

**Table 2.5 Increment and Decrement Operators**

| Operator | Name | Description | Example (assume i = 1) |
|---|---|---|---|
| ++var | preincrement | Increment var by 1, and use the new var value in the statement | int j = ++i; // j is 2, i is 2 |
| var++ | postincrement | Increment var by 1, but use the original var value in the statement | int j = i++; // j is 1, i is 2 |
| ——var | predecrement | Decrement var by 1, and use the new var value in the statement | int j = — —i; // j is 0, i is 0 |
| var—— | postdecrement | Decrement var by 1, and use the original var value in the statement | int j = i— —; // j is 1, i is 0 |

Here are additional examples to illustrate the differences between the prefix form of ++ (or

- —) and the postfix form of ++ (or — —). Consider the following code:

```java
int i = 10;
                                        int newNum = 10 * i;
int newNum = 10 * i++;
                                        i = i + 1;
System.out.print("i is " + i
    + ", newNum is " + newNum);
```

<!-- LI p.58 -->

In this case, `i` is incremented by `1`, then the *old* value of `i` is used in the multiplication. Thus, `newNum` becomes `100`. If `i++` is replaced by `++i`, then it becomes as follows:

```java
int i = 10;
                                         i = i + 1;
int newNum = 10 * (++i);
                                         int newNum = 10 * i;
System.out.print("i is " + i
    + ", newNum is " + newNum);
```

`i` is incremented by `1`, and the new value of `i` is used in the multiplication. Thus, `newNum` becomes `110`.

Here is another example:

```java
double x = 1.0;
double y = 5.0;
double z = x–– + (++y);
```

After all three lines are executed, `y` becomes `6.0`, `z` becomes `7.0`, and `x` becomes `0.0`.

Operands are evaluated from left to right in Java. The left-hand operand of a binary operator is evaluated before any part of the right-hand operand is evaluated. This rule takes precedence over any other rules that govern expressions. Here is an example:

```java
int i = 1;
int k = ++i + i * 3;
```

`++i` is evaluated and returns `2`. When evaluating `i * 3`, `i` is now `2`. Therefore, `k` becomes `8`.

> **Tip** Using increment and decrement operators makes expressions short, but it also makes them complex and difficult to read. Avoid using these operators in expressions that modify multiple variables or the same variable multiple times, such as this one: `int k = ++i + i * 3`.

**2.15.1** Which of these statements are true?

**Check Point**

a. Any expression can be used as a statement.

b. The expression `x++` can be used as a statement.

c. The statement `x = x + 5` is also an expression.

d. The statement `x = y = x = 0` is illegal.

**2.15.2**  Show the output of the following code:

```java
int a = 6;
int b = a++;
System.out.println(a);
System.out.println(b);
a = 6;
b = ++a;
System.out.println(a);
System.out.println(b);
```

<!-- LI p.78 -->

## 3.2 boolean Data Type, Values, and Expressions

*The* `boolean` *data type declares a variable with the value either* `true` *or* `false`.

How do you compare two values, such as whether a radius is greater than `0`, equal to `0`,

**Key Point**

or less than `0`? Java provides six *relational operators* (also known as *comparison operators*), shown in Table 3.1, which can be used to compare two values (assume radius is `5` in the table).

**Table 3.1 Relational Operators**

*Java Operator*

*Mathematics Symbol Name Example (radius is 5) Result*

Less than

```text
<
             <
                                                    radius < 0
                                                                       false
```

Less than or equal to

```text
<=
             ≤
                                                    radius <= 0
                                                                       false
```

Greater than

```text
>
             >
                                                    radius > 0
                                                                       true
```

Greater than or equal to

```text
>=
             ≥
                                                    radius >= 0
                                                                       true
```

Equal to

```text
==
             =
                                                    radius == 0
                                                                       false
!=
             ≠
```

Not equal to

```text
radius != 0
                   true
```

> **Caution** The equality testing operator is two equal signs (==), not a single equal sign (=). The latter symbol is for assignment.

```text
== vs. =
```

The result of the comparison is a Boolean value: `true` or `false`. For example, the following statement displays `true`:

```java
double radius = 1;
System.out.println(radius > 0);
```

A variable that holds a Boolean value is known as a *Boolean variable*. The `boolean` data type is used to declare Boolean variables. A `boolean` variable can hold one of the two values: `true` or `false`. For example, the following statement assigns `true` to the variable `lightsOn`:

<!-- LI p.79 -->

```java
boolean lightsOn = true;
```

`true` and `false` are literals, just like a number such as `10`. They are not keywords, but are reserved words and cannot be used as identifiers in the program.

Suppose you want to develop a program to let a first-grader practice addition. The program randomly generates two single-digit integers, `number1` and `number2`, and displays to the

**VideoNote**

student a question such as “What is 1 + 7?, ” as shown in the sample run in Listing 3.1. After the student types the answer, the program displays a message to indicate whether it is true or false.

There are several ways to generate random numbers. For now, generate the first integer using `System.currentTimeMillis() % 10` (i.e., the last digit in the current time) and the second using `System.currentTimeMillis() / 10 % 10` (i.e., the second last digit in the current time). Listing 3.1 gives the program. Lines 5–6 generate two numbers, `number1` and `number2`. Line 14 obtains an answer from the user. The answer is graded in line 18 using a Boolean expression `number1 + number2 == answer`.

**Listing 3.1 AdditionQuiz.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class AdditionQuiz {
  public static void main(String[] args) {
    int number1 = (int)(System.currentTimeMillis() % 10);
    int number2 = (int)(System.currentTimeMillis() / 10 % 10);

    // Create a Scanner
    Scanner input = new Scanner(System.in);

    System.out.print(
      "What is " + number1 + " + " + number2 + "? ");

    int answer = input.nextInt();

    System.out.println(
      number1 + " + " + number2 + " = " + answer + " is " +
      (number1 + number2 == answer));
  }
}


 What is 1 + 7? 8
 1 + 7 = 8 is true


 What is 4 + 8? 9
 4 + 8 = 9 is false
```

**line#**

```text
            number1
                         number2
                                     answer
                                                  output

 5
            4
 6
                         8
14
                                     9
16
                                                  4 + 8 = 9 is false
```

<!-- LI p.80 -->

**3.2.1**

List six relational operators.

**Check Point**

**3.2.2**

Assuming `x` is `1`, show the result of the following Boolean expressions:

```text
(x > 0)
(x < 0)
(x != 0)
(x >= 0)
(x != 1)
```

**3.2.3**

Can the following conversions involving casting be allowed? Write a test program to verify it.

```java
boolean b = true;
i = (int)b;

int i = 1;
boolean b = (boolean)i;
```

<!-- LI p.95 -->

## 3.10 Logical Operators

> **Key Point** The logical operators* !, &&, ||*, and* ^ *can be used to create a compound Boolean expression.

Sometimes, whether a statement is executed is determined by a combination of several conditions. You can use logical operators to combine these conditions to form a compound Boolean expression. *Logical operators*, also known as *Boolean operators*, operate on Boolean values to create a new Boolean value. Table 3.3 lists the Boolean operators. Table 3.4 defines the not (!) operator, which negates `true` to `false` and `false` to `true`. Table 3.5 defines the and (&&) operator. The and (&&) of two Boolean operands is `true` if and only if both the operands are `true`. Table 3.6 defines the or (||) operator. The or (||) of two Boolean operands is `true` if at least one of the operands is `true`. Table 3.7 defines the exclusive or (^) operator. The exclusive or (^) of two Boolean operands is `true` if and only if the two operands have different Boolean values. Note `p1 ^ p2` is the same as `p1 != p2`.

**Table 3.3 Boolean Operators**

| Operator | Name | Description |
|---|---|---|
| ! | not | Logical negation |
| && | and | Logical conjunction |
| \|\| | or | Logical disjunction |
| ^ | exclusive or | Logical exclusion |

**Table 3.4 Truth Table for Operator** !

```text
p
           !p
```

*Example (assume* `age = 24, weight = 140`)

`!(age > 18)` is `false`, because `(age > 18)` is `true`. `!(weight == 150)` is `true`, because `(weight == 150)`

```text
true
            false
```

```text
false
            true
```

is `false`.

<!-- LI p.96 -->

**Table 3.5 Truth Table for Operator** &&

```text
p1
       p2
             p1 && p2
```

*Example (assume* `age = 24, weight = 140`)

```text
false
       false
              false
```

`(age > 28) && (weight <= 140)` is `false`, because `(age >`

```text
false
       true
              false
```

`28)` is `false`.

```text
true
       false
              false
```

`(age > 18) && (weight >= 140)` is `true`, because `(age > 18)`

```text
true
       true
              true
```

and `(weight >= 140)` are both `true`.

**Table 3.6 Truth Table for Operator** ||

```text
p1
      p2
             p1 || p2
```

*Example (assume* `age = 24, weight = 140`)

`(age > 34) || (weight >= 150)` is `false`, because `(age >`

```text
false
       false
              false
```

`34)` and `(weight >= 150)` are both `false`.

```text
false
       true
              true
```

`(age > 18) || (weight < 140)` is `true`, because `(age > 18)`

```text
true
       false
              true
```

is `true`.

```text
true
       true
              true
```

**Table 3.7 Truth Table for Operator** ^

```text
p1
       p2
```

*Example (assume* `age = 24, weight = 140`)

```text
p1 ^ p2
```

`(age > 34) ^ (weight > 140)` is `false`, because `(age > 34)`

```text
false
       false
              false
```

and `(weight > 140)` are both `false`. `(age > 34) ^ (weight >= 140)` is `true`, because `(age > 34)`

```text
false
       true
              true
```

is `false` but `(weight >= 140)` is `true`.

```text
true
       false
              true
true
       true
              false
```

Listing 3.6 gives a program that checks whether a number is divisible by `2` and `3`, by `2` or `3`, and by `2` or `3` but not both.

**Listing 3.6 TestBooleanOperators.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class TestBooleanOperators {
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Receive an input
    System.out.print("Enter an integer: ");
    int number = input.nextInt();

    if (number % 2 == 0 && number % 3 == 0)
      System.out.println(number + " is divisible by 2 and 3.");

    if (number % 2 == 0 || number % 3 == 0)
      System.out.println(number + " is divisible by 2 or 3.");

    if (number % 2 == 0 ^ number % 3 == 0)
      System.out.println(number +
        " is divisible by 2 or 3, but not both.");
  }
}


 Enter an integer: 4
 4 is divisible by 2 or 3.
 4 is divisible by 2 or 3, but not both.
```

<!-- LI p.97 -->

```text
Enter an integer: 18
18 is divisible by 2 and 3.
18 is divisible by 2 or 3.
```

`(number % 2 == 0 && number % 3 == 0)` (line 12) checks whether the number is divisible by both `2` and `3`. `(number % 2 == 0 || number % 3 == 0)` (line 15) checks whether the number is divisible by `2` or by `3`. `(number % 2 == 0 ^ number % 3 == 0)` (line 18) checks whether the number is divisible by `2` or `3`, but not both.

> **Caution** In mathematics, the expression

```text
28 <= numberOfDaysInAMonth <= 31
```

> is correct. However, it is incorrect in Java, because `28 <= numberOfDaysInAMonth` is evaluated to a `boolean` value, which cannot be compared with `31`. Here, two operands (a `boolean` value and a numeric value) are *incompatible*. The correct expression in Java is

```text
28 <= numberOfDaysInAMonth && numberOfDaysInAMonth <= 31
```

> **Note** De Morgan’s law, named after Indian-born British mathematician and logician Augustus De Morgan (1806–1871), can be used to simplify Boolean expressions. The law states the following:

```text
!condition1 || !condition2

!condition1 && !condition2
```

> For example,

```text
!(number % 2 == 0 && number % 3 == 0)
```

> can be simplified using an equivalent expression:

```text
number % 2 != 0 || number % 3 != 0
```

> As another example,

```text
!(number == 2 || number == 3)
```

> is better written as

```text
number != 2 && number != 3
```

<!-- LI p.98 -->

If one of the operands of an && operator is `false`, the expression is `false`; if one of the operands of an || operator is `true`, the expression is `true`. Java uses these properties to improve the performance of these operators. When evaluating `p1 && p2`, Java first evaluates `p1` then, if `p1` is `true`, evaluates `p2`; if `p1` is `false`, it does not evaluate `p2`. When evaluating `p1 || p2`, Java first evaluates `p1` then, if `p1` is `false`, evaluates `p2`; if `p1` is `true`, it does not evaluate `p2`. In programming language terminology, && and || are known as the *short-circuit* or *lazy operators*. Java also provides the & and | operators, which are covered in Supplement III.C for advanced readers.

**3.10.1**

Assuming that `x` is `1`, show the result of the following Boolean expressions:

**Check Point**

```text
(true) && (3 > 4)
!(x > 0) && (x > 0)
(x > 0) || (x < 0)
(x != 0) || (x == 0)
(x >= 0) || (x < 0)
(x != 1) == !(x == 1)
```

**3.10.2** (a) Write a Boolean expression that evaluates to `true` if a number stored in vari-

able `num` is between `1` and `100`. (b) Write a Boolean expression that evaluates to `true` if a number stored in variable `num` is between `1` and `100` or the number is negative. **3.10.3** (a) Write a Boolean expression for �*x* - 5�6 4.5. (b) Write a Boolean expres-

sion for �*x* - 5�7 4.5. **3.10.4** Assume `x` and `y` are `int` type. Which of the following are legal Java expressions?

```text
x > y > 0
x = y && y
x /= y
x or y
x and y
(x != 0) || (x = 0)
```

**3.10.5** Are the following two expressions the same?

```text
x % 2 == 0 && x % 3 == 0

x % 6 == 0
```

**3.10.6**

What is the value of the expression `x >= 50 && x <= 100` if `x` is `45`, `67`, or `101`? **3.10.7** Suppose, when you run the following program, you enter the input `2 3 6` from

the console. What is the output?

```java
public class Test {
  public static void main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    double x = input.nextDouble();
    double y = input.nextDouble();
    double z = input.nextDouble();

    System.out.println("(x < y && y < z) is " + (x < y && y < z));
    System.out.println("(x < y || y < z) is " + (x < y || y < z));
    System.out.println("!(x < y) is " + !(x < y));
    System.out.println("(x + y < z) is " + (x + y < z));
    System.out.println("(x + y > z) is " + (x + y > z));
  }
}
```

**3.10.8** Write a Boolean expression that evaluates to `true` if `age` is greater than `13` and

less than `18`.

<!-- LI p.99 -->

**3.10.9** Write a Boolean expression that evaluates to `true` if `weight` is greater than `50`

pounds or height is greater than `60` inches. **3.10.10** Write a Boolean expression that evaluates to `true` if `weight` is greater than `50`

pounds and height is greater than `60` inches. **3.10.11** Write a Boolean expression that evaluates to `true` if either `weight` is greater than

`50` pounds or height is greater than `60` inches, but not both.

<!-- LI p.105 -->

## 3.14 Conditional Operators

*A conditional operator evaluates an expression based on a condition.*

**Key**

You might want to assign a value to a variable that is restricted by certain conditions. For

**Point**

example, the following statement assigns `1` to `y` if `x` is greater than `0` and `−1` to `y` if `x` is less than or equal to `0`:

```java
if (x > 0)
  y = 1;
else
  y = −1;
```

Alternatively, as in the following example, you can use a *conditional operator* to achieve the same result.

```java
y = (x > 0)? 1: −1;
```

The symbols? and: appearing together is called a conditional operator (also known as a *ternary operator* because it uses three operands. It is the only ternary operator in Java. The conditional operator is in a completely different style, with no explicit `if` in the statement. The syntax to use the operator is as follows:

```text
boolean-expression? expression1: expression2
```

The result of this expression is `expression1` if `boolean-expression` is true; otherwise the result is `expression2`.

Suppose you want to assign the larger number of variable `num1` and `num2` to `max`. You can simply write a statement using the conditional operator:

```java
max = (num1 > num2)? num1: num2;
```

<!-- LI p.106 -->

For another example, the following statement displays the message “num is even” if `num` is even, and otherwise displays “num is odd.”

```java
System.out.println((num % 2 == 0)? "num is even": "num is odd");
```

As you can see from these examples, the conditional operator enables you to write short and concise code.

Conditional expressions can be embedded. For example, the following code assigns `1`, `0`, or `−1` to status if `n1 > n1, n1 == n2`, or `n1 < n2`:

```java
status = n1 > n2? 1: (n1 == n2? 0: −1);
```

**3.14.1**

Suppose when you run the following program, you enter the input `2 3 6` from the

**Check**

console. What is the output?

**Point**

```java
public class Test {
  public static void main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    double x = input.nextDouble();
    double y = input.nextDouble();
    double z = input.nextDouble();

    System.out.println((x < y && y < z)? "sorted": "not sorted");
  }
}
```

**3.14.2** Rewrite the following `if` statements using the conditional operator.

```java
if (ages >= 16)
  ticketPrice = 20;
else
  ticketPrice = 10;
```

**3.14.3** Rewrite the following codes using `if-else` statements.

**3.14.4** Write an expression using a conditional operator that returns randomly `−1` or `1`.

## 3.15 Operator Precedence and Associativity

> **Key Point** Operator precedence and associativity determine the order in which operators are evaluated.

Section 2.11 introduced operator precedence involving arithmetic operators. This section dis-cusses operator precedence in more detail. Suppose you have this expression:

```text
3 + 4 * 4 > 5 * (4 + 3) – 1 && (4 – 3 > 5)
```

What is its value? What is the execution order of the operators? The expression within parentheses is evaluated first. (Parentheses can be nested, in which case the expression within the inner parentheses is executed first.) When evaluating an expression without parentheses, the operators are applied according to the precedence rule and the associativity rule.

The precedence rule defines precedence for operators, as shown in Table 3.8, which contains the operators you have learned so far. Operators are listed in decreasing order of precedence from top to bottom. The logical operators have lower precedence than the relational operators, and the relational operators have lower precedence than the arithmetic operators. Operators with the same precedence appear in the same group. (See Appendix C, *Operator Precedence Chart*, for a complete list of Java operators and their precedence.)

<!-- LI p.107 -->

**Table 3.8 Operator Precedence Chart**

| Precedence | Operator |
|---|---|
|  | var++ and var−− (Postfix) |
|  | +, − (Unary plus and minus), ++var and −−var (Prefix) |
|  | (type) (Casting) |
|  | !(Not) |
|  | *, /, % (Multiplication, division, and remainder) |
|  | +, − (Binary addition and subtraction) |
|  | <, <=, >, >= (Relational) |
|  | ==, != (Equality) |
|  | ^ (Exclusive OR) |
|  | && (AND) |
|  | \|\| (OR) |
|  | ?: (Ternary operator) |
|  | =, +=, −=, *=, /=, %= (Assignment operators) |

If operators with the same precedence are next to each other, their *associativity* determines the order of evaluation. All binary operators except assignment operators are *left associative*. For example, since + and − are of the same precedence and are left associative, the expression

```text
a - b + c - d
                          ((a - b) + c) - d
```

Assignment operators are *right associative*. Therefore, the expression

```text
                           a = (b += (c = 5))
a = b += c = 5
```

Suppose `a`, `b`, and `c` are `1` before the assignment; after the whole expression is evaluated, `a` becomes `6`, `b` becomes `6`, and `c` becomes `5`. Note that left associativity for the assignment operator would not make sense.

> **Note** Java has its own way to evaluate an expression internally. The result of a Java evaluation is the same as that of its corresponding arithmetic evaluation. Advanced readers may refer to Supplement III.B for more discussions on how an expression is evaluated in Java *behind the scenes*.

**3.15.1**

List the precedence order of the Boolean operators. Evaluate the following expressions:

**Check Point**

```text
true || true && false
true && true || false
```

**3.15.2** True or false? All the binary operators except = are left associative. **3.15.3** Evaluate the following expressions:

```text
2 * 2 – 3 > 2 && 4 – 2 > 5
2 * 2 – 3 > 2 || 4 – 2 > 5
```

**3.15.4** Is `(x > 0 && x < 10)` the same as `((x > 0) && (x < 10))`?

Is `(x > 0 || x < 10)` the same as `((x > 0) || (x < 10))`? Is `(x > 0 || x < 10 && y < 0)` the same as `(x > 0 || (x < 10 && y < 0))`?
