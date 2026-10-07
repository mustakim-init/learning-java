---
topic: variables
lessons: "M2_L1, M2_L2, M2_L3"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "40-60"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "2.4, 2.5, 2.6, 2.7, 2.8, 2.9:intro, 2.9.3, 2.10.1, 2.10.2, 2.16"
note: "2.9: Table 2.1 only. 2.9.3 and 2.10.1, 2.10.2 only (not all of 2.9 / 2.10)."
generated_by: tools/extract_refs.py
---
# Variables & Data Types - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.40 -->

## 2.4 Identifiers

*Identifiers are the names that identify the elements such as classes, methods, and vari-*

**Key**

**Point**

*ables in a program.*

As you see in Listing 2.3, `ComputeAverage`, `main`, `input`, `number1`, `number2`, `number3`, and so on are the names of things that appear in the program. In programming terminology, such names are called *identifiers*. All identifiers must obey the following rules:

- An identifier is a sequence of characters that consists of letters, digits, underscores (`_`), and dollar signs ($).
- An identifier must start with a letter, an underscore (`_`), or a dollar sign ($). It cannot start with a digit.
- An identifier cannot be a reserved word. See Appendix A for a list of reserved words. Reserved words have specific meaning in the Java language. Keywords are reserved words.
- An identifier can be of any length.

For example, `$2`, `ComputeArea`, `area`, `radius`, and `print` are legal identifiers, whereas `2A` and `d+4` are not because they do not follow the rules. The Java compiler detects illegal identifiers and reports syntax errors.

> **Note** Since Java is case sensitive, `area`, `Area`, and `AREA` are all different identifiers.

> **Tip** Identifiers are for naming variables, methods, classes, and other items in a program. Descriptive identifiers make programs easy to read. Avoid using abbreviations for identifiers. Using complete words is more descriptive. For example, `numberOfStudents` is better than `numStuds`, `numOfStuds`, or `numOfStudents`. We use descriptive names for complete programs in the text. However, we will occasionally use variable names such as `i`, `j`, `k`, `x`, and `y` in the code snippets for brevity. These names also provide a generic tone to the code snippets.

> **Tip** Do not name identifiers with the $ character. By convention, the $ character should be used only in mechanically generated source code.

**2.4.1** Which of the following identifiers are valid? Which are Java keywords?

**Check Point**

```java
miles, Test, a++, ––a, 4#R, $4, #44, apps
class, public, int, x, y, radius
```

## 2.5 Variables

*Variables are used to represent values that may be changed in the program.*

**Key**

As you see from the programs in the preceding sections, variables are used to store values

**Point**

to be used later in a program. They are called variables because their values can be changed. In the program in Listing 2.2, `radius` and `area` are variables of the `double` type. You can assign any numerical value to `radius` and `area`, and the values of `radius` and `area` can be reassigned. For example, in the following code, `radius` is initially `1.0` (line 2) then changed to `2.0` (line 7), and area is set to `3.14159` (line 3) then reset to `12.56636` (line 8).

<!-- LI p.41 -->

```java
// Compute the first area
radius = 1.0;
                                                      radius:  1.0
area = radius * radius * 3.14159;
                                                        area:  3.14159
System.out.println("The area is " + area + " for radius " + radius);

// Compute the second area
radius = 2.0;
                                                      radius:  2.0
area = radius * radius * 3.14159;
                                                        area:  12.56636
System.out.println("The area is " + area + " for radius " + radius);
```

Variables are for representing data of a certain type. To use a variable, you declare it by telling the compiler its name as well as what type of data it can store. The *variable declaration* tells the compiler to allocate appropriate memory space for the variable based on its data type. The syntax for declaring a variable is

```java
datatype variableName;
```

Here are some examples of variable declarations:

```java
int count;            // Declare count to be an integer variable
double radius;        // Declare radius to be a double variable
double interestRate;  // Declare interestRate to be a double variable
```

These examples use the data types `int` and `double`. Later you will be introduced to additional data types, such as `byte`, `short`, `long`, `float`, `char`, and `boolean`.

If variables are of the same type, they can be declared together, as follows:

```java
datatype variable1, variable2, . . . , variablen;
```

The variables are separated by commas. For example,

```java
int i, j, k; // Declare i, j, and k as int variables
```

Variables often have initial values. You can declare a variable and initialize it in one step. Consider, for instance, the following code:

```java
int count = 1;
```

This is equivalent to the next two statements:

```java
int count;
count = 1;
```

You can also use a shorthand form to declare and initialize variables of the same type together. For example,

```java
int i = 1, j = 2;
```

> **Tip** A variable must be declared before it can be assigned a value. A variable declared in a method must be assigned a value before it can be used.

> Whenever possible, declare a variable and assign its initial value in one step. This will make the program easy to read and avoid programming errors.

Every variable has a scope. The *scope of a variable* is the part of the program where the variable can be referenced. The rules that define the scope of a variable will be gradually introduced later in the book. For now, all you need to know is that a variable must be declared and initialized before it can be used.

<!-- LI p.42 -->

**2.5.1** Identify and fix the errors in the following code:

**Check Point**

```java
public class Test {
  public static void main(String[] args) {
    int i = k + 2;
    System.out.println(i);
  }
}
```

## 2.6 Assignment Statements and Assignment Expressions

> **Key Point** An assignment statement assigns a value to a variable. An assignment statement can also be used as an expression in Java.

After a variable is declared, you can assign a value to it by using an *assignment statement*. In Java, the equal sign (=) is used as the *assignment operator*. The syntax for assignment statements is as follows:

```java
variable = expression;
```

An *expression* represents a computation involving values, variables, and operators that, taking them together, evaluates to a value. In an assignment statement, the expression on the right-hand side of the assignment operator is evaluated, and then the value is assigned to the variable on the left-hand side of the assignment operator. For example, consider the following code:

```java
int y = 1;
                          // Assign 1 to variable y
double radius = 1.0;
                          // Assign 1.0 to variable radius
int x = 5 * (3 / 2);
                          // Assign the value of the expression to x
x = y + 1;
                          // Assign the addition of y and 1 to x
double area = radius * radius * 3.14159;
                                               // Compute area
```

You can use a variable in an expression. A variable can also be used in both sides of the = operator. For example,

```java
x = x + 1;
```

In this assignment statement, the result of `x + 1` is assigned to `x`. If `x` is `1` before the statement is executed, then it becomes `2` after the statement is executed.

To assign a value to a variable, you must place the variable name to the left of the assignment operator. Thus, the following statement is wrong:

```java
1 = x; // Wrong
```

> **Note** In mathematics, `x = 2 * x + 1` denotes an equation. However, in Java, `x = 2 * x + 1` is an assignment statement that evaluates the expression `2 * x + 1` and assigns the result to `x`.

In Java, an assignment statement is essentially an expression that evaluates to the value to be assigned to the variable on the left side of the assignment operator. For this reason, an assignment statement is also known as an *assignment expression.* For example, the following statement is correct:

```java
System.out.println(x = 1);
```

which is equivalent to

```java
x = 1;
System.out.println(x);
```

<!-- LI p.43 -->

If a value is assigned to multiple variables, you can use chained assignments like this:

```java
i = j = k = 1;
```

which is equivalent to

```java
k = 1;
j = k;
i = j;
```

> **Note** In an assignment statement, the data type of the variable on the left must be compatible with the data type of the value on the right. For example, `int x = 1.0` would be illegal, because the data type of `x` is `int`. You cannot assign a `double` value (`1.0`) to an `int` variable without using type casting. Type casting will be introduced in Section 2.15.

**2.6.1** Identify and fix the errors in the following code:

**Check**

**Point**

```java
1  public class Test {
```

```java
  public static void main(String[] args) {
    int i = j = k = 2;
    System.out.println(i + " " + j + " " + k);
  }
}
```

## 2.7 Named Constants

*A named constant is an identifier that represents a permanent value.*

The value of a variable may change during the execution of a program, but a *named constant,* or simply *constant*, represents permanent data that never changes. A constant is also known as a *final variable* in Java. In our `ComputeArea` program, π is a constant. If you use it fre-

**Key Point**

quently, you don’t want to keep typing `3.14159`; instead, you can declare a constant for π. Here is the syntax for declaring a constant:

```java
final datatype CONSTANTNAME = value;
```

A constant must be declared and initialized in the same statement. The word `final` is a Java keyword for declaring a constant. By convention, all letters in a constant are in uppercase. For example, you can declare π as a constant and rewrite Listing 2.2, as in Listing 2.4.

**Listing 2.4 ComputeAreaWithConstant.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner; // Scanner is in the java.util package

public class ComputeAreaWithConstant {
  public static void main(String[] args) {
    final double PI = 3.14159; // Declare a constant

    // Create a Scanner object
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter a radius
    System.out.print("Enter a number for radius: ");
    double radius = input.nextDouble();

    // Compute area
    double area = radius * radius * PI;

    // Display result
    System.out.println("The area for the circle of radius " +
      radius + " is " + area);
  }
}
```

<!-- LI p.44 -->

There are three benefits of using constants: (1) you don’t have to repeatedly type the same value if it is used multiple times; (2) if you have to change the constant value (e.g., from `3.14` to `3.14159` for `PI`), you need to change it only in a single location in the source code; and (3) a descriptive name for a constant makes the program easy to read. **2.7.1** What are the benefits of using constants? Declare an `int` constant `SIZE` with

**Check**

value `20`.

**Point**

**2.7.2** Translate the following algorithm into Java code:

Step 1: Declare a `double` variable named `miles` with an initial value `100`. Step 2: Declare a `double` constant named `KILOMETERS_PER_MILE` with value

`1.609`. Step 3: Declare a `double` variable named `kilometers`, multiply `miles` and

`KILOMETERS_PER_MILE`, and assign the result to `kilometers`. Step 4: Display `kilometers` to the console. What is `kilometers` after Step 4?

## 2.8 Naming Conventions

*Sticking with the Java naming conventions makes your programs easy to read and avoids errors.*

Make sure you choose descriptive names with straightforward meanings for the variables, constants, classes, and methods in your program. As mentioned earlier, names are case sensi-

**Key**

tive. Listed below are the conventions for naming variables, methods, and classes.

**Point**

- Use lowercase for variables and methods—for example, the variables `radius` and `area`, and the method `print`. If a name consists of several words, concatenate them into one, making the first word lowercase and capitalizing the first letter of each subsequent word—for example, the variable `numberOfStudents`. This naming style is known as the *camelCase* because the uppercase characters in the name resemble a camel’s humps.
- Capitalize the first letter of each word in a class name—for example, the class names `ComputeArea` and `System`.
- Capitalize every letter in a constant, and use underscores between words—for example, the constants `PI` and `MAX_VALUE`.

It is important to follow the naming conventions to make your programs easy to read.

> **Caution** Do not choose class names that are already used in the Java library. For example, since the `System` class is defined in Java, you should not name your class `System`.

**2.8.1** What are the naming conventions for class names, method names, constants, and

**Check**

variables? Which of the following items can be a constant, a method, a variable, or a

**Point**

class according to the Java naming conventions? `MAX_VALUE`, `Test`, `read`, `readDouble`

<!-- LI p.45 -->

## 2.9 Numeric Data Types and Operations

*Java has six numeric types for integers and floating-point numbers with operators +,* -*, *, /, and %.*

**Key**

Every data type has a range of values. The compiler allocates memory space for each variable

**Point**

or constant according to its data type. Java provides eight primitive data types for numeric values, characters, and Boolean values. This section introduces numeric data types and operators.

Table 2.1 lists the six numeric data types, their ranges, and their storage sizes.

**Table 2.1 Numeric Data Types**

| Name | Range | Storage Size |
|---|---|---|
| byte | -27 to 27 -1 (-128 to 127) | 8-bit signed |
| short | -215 to 215 -1 (-32768 to 32767) | 16-bit signed |
| int | -231 to 231 -1 (-2147483648 to 2147483647) | 32-bit signed |
| long | -263 to 263-1 | 64-bit signed |
|  | (i.e., -9223372036854775808 to 9223372036854775807) |  |
| float | Negative range: -3.4028235E + 38 to -1.4E -45 | 32-bit IEEE 754 |
|  | Positive range: 1.4E -45 to 3.4028235E+38 6–9 significant digits |  |
| double | Negative range: -1.7976931348623157E+308 to -4.9E -324 | 64-bit IEEE 754 |
|  | Positive range: 4.9E -324 to 1.7976931348623157E+308 15–17 significant digits |  |

> **Note** **IEEE 754** is a standard approved by the Institute of Electrical and Electronics Engineers for representing floating-point numbers on computers. The standard has been widely adopted. Java uses the 32-bit **IEEE 754** for the `float` type and the 64-bit **IEEE 754** for the `double` type. The **IEEE 754** standard also defines special floating-point values, which are listed in Appendix E.

Java uses four types for integers: `byte`, `short`, `int`, and `long`. Choose the type that is most appropriate for your variable. For example, if you know an integer stored in a variable is within a range of a byte, declare the variable as a `byte`. For simplicity and consistency, we will use `int` for integers most of the time in this book.

Java uses two types for floating-point numbers: `float` and `double`. The `double` type is twice as big as `float`, so the `double` is known as *double precision*, and `float` as *single precision.* Normally, you should use the `double` type, because it is more accurate than the `float` type.

<!-- LI p.48 -->

### 2.9.3 Exponent Operations

The `Math.pow(a, b)` method can be used to compute *ab*. The `pow` method is defined in the `Math` class in the Java API. You invoke the method using the syntax `Math.pow(a, b)` (e.g., `Math.pow(2, 3)`), which returns the result of *ab* (23). Here, `a` and `b` are parameters for the `pow` method and the numbers `2` and `3` are actual values used to invoke the method. For example,

```java
System.out.println(Math.pow(2, 3)); // Displays 8.0
System.out.println(Math.pow(4, 0.5)); // Displays 2.0
System.out.println(Math.pow(2.5, 2)); // Displays 6.25
System.out.println(Math.pow(2.5, –2)); // Displays 0.16
```

Chapter 6 introduces more details on methods. For now, all you need to know is how to invoke the `pow` method to perform the exponent operation. **2.9.1** Find the largest and smallest `byte`, `short`, `int`, `long`, `float`, and `double`. Which

**Check**

of these data types requires the least amount of memory?

**Point**

**2.9.2** Show the result of the following remainders:

```text
56  %   6
```

`78 %` -`4` -`34 % 5` -`34 %` -`5`

```text
5  %   1
1  %   5
```

**2.9.3** If today is Tuesday, what will be the day in 100 days? **2.9.4** What is the result of `25 / 4`? How would you rewrite the expression if you wished

the result to be a floating-point number? **2.9.5** Show the result of the following code:

```java
System.out.println(2 * (5 / 2 + 5 / 2));
System.out.println(2 * 5 / 2 + 2 * 5 / 2);
System.out.println(2 * (5 / 2));
System.out.println(2 * 5 / 2);
```

**2.9.6** Are the following statements correct? If so, show the output.

```java
System.out.println("25 / 4 is " + 25 / 4);
System.out.println("25 / 4.0 is " + 25 / 4.0);
System.out.println("3 * 2 / 4 is " + 3 * 2 / 4);
System.out.println("3.0 * 2 / 4 is " + 3.0 * 2 / 4);
```

**2.9.7** Write a statement to display the result of 23.5. **2.9.8** Suppose `m` and `r` are integers. Write a Java expression for mr2 to obtain a

floating-point result.

<!-- LI p.49 -->

### 2.10.1 Integer Literals

An integer literal can be assigned to an integer variable as long as it can fit into the variable. A compile error will occur if the literal is too large for the variable to hold. The statement `byte b = 128`, for example, will cause a compile error, because `128` cannot be stored in a variable of the `byte` type. (Note the range for a byte value is from `–128` to `127`.) An integer literal is assumed to be of the `int` type, whose value is between -231 (-2147483648) and 231 -1 (2147483647). To denote an integer literal of the `long` type, append the letter `L` or `l` to it. For example, to write integer `2147483648` in a Java program, you have to write it as `2147483648L` or `2147483648l`, because `2147483648` exceeds the range for the `int` value. `L` is preferred because `l` (lowercase `L`) can easily be confused with 1 (the digit one).

> **Note** By default, an integer literal is a decimal integer number. To denote a binary integer literal, use a leading `0b` or `0B` (zero B); to denote an octal integer literal, use a leading `0` (zero); and to denote a hexadecimal integer literal, use a leading `0x` or `0X` (zero X). For example,

```java
System.out.println(0B1111); // Displays 15
System.out.println(07777); // Displays 4095
System.out.println(0XFFFF); // Displays 65535
```

> Hexadecimal numbers, binary numbers, and octal numbers will be introduced in Appendix F.

### 2.10.2 Floating-Point Literals

Floating-point literals are written with a decimal point. By default, a floating-point literal is treated as a `double` type value. For example, `5.0` is considered a `double` value, not a `float` value. You can make a number a `float` by appending the letter `f` or `F`, and you can make a number a `double` by appending the letter `d` or `D`. For example, you can use `100.2f` or `100.2F` for a `float` number, and `100.2d` or `100.2D` for a `double` number.

> **Note** The `double` type values are more accurate than the `float` type values. For example,

```java
System.out.println("1.0 / 3.0 is " + 1.0 / 3.0);
displays 1.0 / 3.0 is 0.3333333333333333
```

```java
System.out.println("1.0F / 3.0F is " + 1.0F / 3.0F);
displays 1.0F / 3.0F is 0.33333334
```

A float value has `6–9` numbers of significant digits, and a double value has `15–17` numbers of significant digits.

> **Note** To improve readability, Java allows you to use underscores to separate two digits in a number literal. For example, the following literals are correct.

```java
long value = 232_45_4519;
double amount = 23.24_4545_4519_3415;
```

> However, `45_` or `_45` is incorrect. The underscore must be placed between two digits.

<!-- LI p.58 -->

## 2.16 Numeric Type Conversions

*Floating-point numbers can be converted into integers using explicit casting.*

Can you perform binary operations with two operands of different types? Yes. If an integer

**Key Point**

and a floating-point number are involved in a binary operation, Java automatically converts the integer to a floating-point value. Therefore, `3 * 4.5` is the same as `3.0 * 4.5`.

<!-- LI p.59 -->

You can always assign a value to a numeric variable whose type supports a larger range of values; thus, for instance, you can assign a `long` value to a `float` variable. You cannot, however, assign a value to a variable of a type with a smaller range unless you use *type casting. Casting* is an operation that converts a value of one data type into a value of another data type. Casting a type with a small range to a type with a larger range is known as *widening a type*. Casting a type with a large range to a type with a smaller range is known as *narrowing a type*. Java will automatically widen a type, but you must narrow a type explicitly. The syntax for casting a type is to specify the target type in parentheses, followed by the variable’s name or the value to be cast. For example, the following statement

```java
System.out.println((int)1.7);
```

displays `1`. When a `double` value is cast into an `int` value, the fractional part is truncated. The following statement

```java
System.out.println((double)1 / 2);
```

displays `0.5`, because `1` is cast to `1.0` first, then `1.0` is divided by `2`. However, the statement

```java
System.out.println(1 / 2);
```

displays `0`, because `1` and `2` are both integers and the resulting value should also be an integer.

> **Caution** Casting is necessary if you are assigning a value to a variable of a smaller type range, such as assigning a `double` value to an `int` variable. A compile error will occur if casting is not used in situations of this kind. However, be careful when using casting, as loss of information might lead to inaccurate results.

> **Note** Casting does not change the variable being cast. For example, `d` is not changed after casting in the following code:

```java
double d = 4.5;
int i = (int)d; // i becomes 4, but d is still 4.5
```

> **Note** In Java, an augmented expression of the form `x1 op= x2` is implemented as `x1 = (T)(x1 op x2)`, where `T` is the type for `x1`. Therefore, the following code is correct:

```java
int sum = 0;
sum += 4.5; // sum becomes 4 after this statement
```

> `sum += 4.5` is equivalent to `sum = (int)(sum + 4.5)`.

> **Note** To assign a variable of the `int` type to a variable of the `short` or `byte` type, explicit casting must be used. For example, the following statements have a compile error:

```java
int i = 1;
byte b = i; // Error because explicit casting is required
```

> However, so long as the integer literal is within the permissible range of the target variable, explicit casting is not needed to assign an integer literal to a variable of the `short` or `byte` type (see Section 2.10, Numeric Literals).

The program in Listing 2.8 displays the sales tax with two digits after the decimal point.

<!-- LI p.60 -->

**Listing 2.8 SalesTax.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class SalesTax {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter purchase amount: ");
    double purchaseAmount = input.nextDouble();

    double tax = purchaseAmount * 0.06;
    System.out.println("Sales tax is $" + (int)(tax * 100) / 100.0);
  }
}

 Enter purchase amount: 197.55
 Sales tax is $11.85
```

| line# | purchaseAmount | tax | Output |
|---|---|---|---|
| 8 | 197.55 |  |  |
| 10 |  | 11.853 |  |
| 11 |  |  | 11.85 |

Using the input in the sample run, the variable `purchaseAmount` is `197.55` (line 8). The sales tax is `6%` of the purchase, so the `tax` is evaluated as `11.853` (line 10). Note

`tax * 100` is `1185.3 (int)(tax * 100)` is `1185 (int)(tax * 100) / 100.0` is `11.85`

Thus, the statement in line 11 displays the tax `11.85` with two digits after the decimal point. Note the expression `(int)(tax * 100) / 100.0` rounds down `tax` to two decimal places. If `tax` is `3.456`, `(int)(tax * 100) / 100.0` would be `3.45`. Can it be rounded up to two decimal places? Note any double value `x` can be rounded up to an integer using `(int)(x + 0.5)`. Thus, `tax` can be rounded up to two decimal places using `(int)(tax * 100 + 0.5) / 100.0`. **2.16.1** Can different types of numeric values be used together in a computation?

**Check Point**

**2.16.2** What does an explicit casting from a `double` to an `int` do with the fractional part

of the `double` value? Does casting change the variable being cast? **2.16.3** Show the following output:

```java
float f = 12.5F;
int i = (int)f;
System.out.println("f is " + f);
System.out.println("i is " + i);
```

**2.16.4** If you change `(int)(tax * 100) / 100.0` to `(int)(tax * 100) / 100` in line

11 in Listing 2.8, what will be the output for the input purchase amount of `197.556`? **2.16.5** Show the output of the following code:

```java
double amount = 5;
System.out.println(amount / 2);
System.out.println(5 / 2);
```

**2.16.6** Write an expression that rounds up a `double` value in variable `d` to an integer.
