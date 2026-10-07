---
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
chapter: "ch06 6.1 Introduction"
printed_pages: "205-248"
pdf_offset: "pdf page = printed page + 23"
generated_by: tools/extract_refs.py --full
---
# ch06 6.1 Introduction

<!-- LI p.205 -->

CHAPTER

6

## Methods

Objectives

- To define methods with formal parameters (§6.2).
- To invoke methods with actual parameters (i.e., arguments) (§6.2).
- To define methods with a return value (§6.3).
- To define methods without a return value and distinguish the differences between void methods and value-returning methods (§6.4).
- To pass arguments by value (§6.5).
- To develop reusable code that is modular, easy to read, easy to debug, and easy to maintain (§6.6).
- To write a method that converts hexadecimals to decimals (§6.7).
- To use method overloading and understand ambiguous overloading (§6.8).
- To determine the scope of variables (§6.9).
- To apply the concept of method abstraction in software development (§6.10).
- To design and implement methods using stepwise refinement (§6.11).

<!-- LI p.206 -->

## 6.1 Introduction

*Methods can be used to define reusable code and organize and simplify coding, and make code easy to maintain.*

**Key**

Suppose you need to find the sum of integers from `1` to `10`, `20` to `37`, and `35` to `49`, respec-

**Point**

tively. You may write the code as follows:

```java
int sum = 0;
for (int i = 1; i <= 10; i++)
  sum += i;
System.out.println("Sum from 1 to 10 is " + sum);

sum = 0;
for (int i = 20; i <= 37; i++)
  sum += i;
System.out.println("Sum from 20 to 37 is " + sum);

sum = 0;
for (int i = 35; i <= 49; i++)
  sum += i;
System.out.println("Sum from 35 to 49 is " + sum);
```

You may have observed that computing these sums from `1` to `10`, `20` to `37`, and `35` to `49` are very similar, except that the starting and ending integers are different. Wouldn’t it be nice if we could write the common code once and reuse it? We can do so by defining a method and invoking it.

The preceding code can be simplified as follows:

**Listing** `MethodDemo.java`

```java
public static int sum(int i1, int i2) {
  int result = 0;
  for (int i = i1; i <= i2; i++)
    result += i;

  return result;
}

public static void main(String[] args) {
  System.out.println("Sum from 1 to 10 is " + sum(1, 10));
  System.out.println("Sum from 20 to 37 is " + sum(20, 37));
  System.out.println("Sum from 35 to 49 is " + sum(35, 49));
}
```

Lines 1–7 define the method named `sum` with two parameters `i1` and `i2`. The statements in the `main` method invoke `sum(1, 10)` to compute the sum from `1` to `10`, `sum(20, 37)` to compute the sum from `20` to `37`, and `sum(35, 49)` to compute the sum from `35` to `49`.

A *method* is a collection of statements grouped together to perform an operation. In earlier chap-ters you have used predefined methods such as `System.out.println`, `System.exit`, `Math. pow`, and `Math.random`. These methods are defined in the Java library. In this chapter, you will learn how to define your own methods and apply method abstraction to solve complex problems. **6.1.1** What are the benefits of using a method?

**Check Point**

## 6.2 Defining a Method

*A method definition consists of method name, parameters, return value type, and body.*

**Key**

The syntax for defining a method is as follows:

**Point**

```java
modifier returnValueType methodName(list of parameters) {
  // Method body;
}
```

<!-- LI p.207 -->

Let’s look at a method defined to find the larger between two integers. This method, named `max`, has two `int` parameters, `num1` and `num2`, the larger of which is returned by the method. Figure 6.1 illustrates the components of this method.

**Define a method Invoke a method**

```java
public static int max(int num1, int num2) {
                                                int z = max(x, y);

  int result;

  if (num1 > num2)
     result = num1;
  else
     result = num2;

  return result;
}
```

**Figure 6.1** A method definition consists of a method header and a method body.

The *method header* specifies the *modifiers*, *return value type*, *method name*, and *parameters* of the method. The `static` modifier is used for all the methods in this chapter. The reason for using it will be discussed in Chapter 9, Objects and Classes.

A method may return a value. The `returnValueType` is the data type of the value the method returns. Some methods perform desired operations without returning a value. In this case, the `returnValueType` is the keyword `void`. For example, the `returnValueType` is `void` in the `main` method, as well as in `System.exit`, and `System.out.println`. If a method returns a value, it is called a *value-returning method;* otherwise, it is called a *void method.*

The variables defined in the method header are known as *formal parameters* or simply *parameters*. A parameter is like a placeholder: when a method is invoked, you pass a value to the parameter. This value is referred to as an *actual parameter or argument*. The *parameter list* refers to the method’s type, order, and the number of parameters. The method name and the parameter list together constitute the *method signature*. Parameters are optional; that is, a method may contain no parameters. For example, the `Math.random()` method has no parameters.

The method body contains a collection of statements that implement the method. The method body of the `max` method uses an `if` statement to determine which number is larger and return the value of that number. In order for a value-returning method to return a result, a return statement using the keyword `return` is *required.* The method terminates when a return statement is executed.

> **Note** Some programming languages refer to methods as *procedures* and *functions.* In those languages, a value-returning method is called a *function* and a void method is called a *procedure.*

> **Caution** In the method header, you need to declare each parameter separately. For instance, `max(int num1, int num2)` is correct, but `max(int num1, num2)` is wrong.

> **Note** We say “*define* a method” and “*declare* a variable.” We are making a subtle distinction here. A definition defines what the defined item is, but a declaration usually involves allocating memory to store data for the declared item.

<!-- LI p.208 -->

**6.2.1** How do you simplify the `max` method in Listing 6.1 using the conditional operator?

**Check Point**

**6.2.2** Define the terms parameter, argument, and method signature.

## 6.3 Calling a Method

*Calling a method executes the code in the method.*

In a method definition, you define what the method is to do. To execute the method, you have

**Key Point**

to *call* or *invoke* it. The program that calls the function is called a *caller*. There are two ways to call a method, depending on whether the method returns a value or not.

If a method returns a value, a call to the method is usually treated as a value. For example,

```java
int larger = max(3, 4);
```

calls `max(3, 4)` and assigns the result of the method to the variable `larger`. Another example of a call that is treated as a value is

```java
System.out.println(max(3, 4));
```

which prints the return value of the method call `max(3`, `4)`.

If a method returns `void`, a call to the method must be a statement. For example, the method `println` returns `void`. The following call is a statement:

```java
System.out.println("Welcome to Java!");
```

> **Note** A value-returning method can also be invoked as a statement in Java. In this case, the caller simply ignores the return value. This is not often done, but it is permissible if the caller is not interested in the return value.

When a program calls a method, program control is transferred to the called method. A called method returns control to the caller when its return statement is executed or when its method-ending closing brace is reached.

Listing 6.1 presents a complete program that is used to test the `max` method.

**VideoNote**

**Listing 6.1 TestMax.java**

```text

```

> Define/invoke `max` method

```java
public class TestMax {
  /** Main method */
  public static void main(String[] args) {
    int i = 5;
    int j = 2;
    int k = max(i, j);
    System.out.println("The maximum of " + i +
      " and " + j + " is " + k);
  }

  /** Return the max of two numbers */
  public static int max(int num1, int num2) {
    int result;

    if (num1 > num2)
      result = num1;
    else
      result = num2;

    return result;
  }
}
The maximum of 5 and 2 is 5
```

<!-- LI p.209 -->

**line# i j k num1 num2 result**

**4 5**

**5 2**

**12 5 2**

**13 undefined**

Invoking max c

**16 5**

**6 5**

This program contains the `main` method and the `max` method. The `main` method is just like any other method, except that it is invoked by the JVM to start the program.

The `main` method’s header is always the same. Like the one in this example, it includes the modifiers `public` and `static`, return value type `void`, method name `main`, and a parameter of the `String[]` type. `String[]` indicates the parameter is an array of `String`, a subject addressed in Chapter 7.

The statements in `main` may invoke other methods that are defined in the class that contains the `main` method or in other classes. In this example, the `main` method invokes `max(i, j)`, which is defined in the same class with the `main` method.

When the `max` method is invoked (line 6), variable `i`’s value `5` is passed to `num1` and variable `j`’s value `2` is passed to `num2` in the `max` method. The flow of control transfers to the `max` method and the `max` method is executed. When the `return` statement in the `max` method is executed, the `max` method returns the control to its caller (in this case, the caller is the `main` method). This process is illustrated in Figure 6.2.

```java
public static
                                             public static int max
    void main(String[] args) {
                                                 (int num1, int num2) {
  int i = 5;
                                               int result;
  int j = 2;
  int k = max(i, j);
                                               if (num1 > num2)
  System.out.println("The " +
                                                 result = num1;
    "maximum between " + i +
                                               else
    " and " + j + " is " + k);
                                                 result = num2;
}
                                               return result;
                                             }
```

**Figure 6.2** When the `max` method is invoked, the flow of control transfers to it. Once the `max` method is finished, it returns control back to the caller.

> **Caution** A `return` statement is required for a value-returning method. The method given in (a) is logically correct, but it has a compile error because the Java compiler thinks this method might not return a value.

<!-- LI p.210 -->

```java
public static int sign(int n) {
                                              public static int sign(int n) {
                                                if (n > 0)
  if (n > 0)
                                                  return 1;
    return 1;
                                                else if (n == 0)
  else if (n == 0)
                                                  return 0;
    return 0;
                                                else
  else if (n < 0)
```

`return` 2`1; return` 2`1;`

```java
                                           }
}
```

> To fix this problem, delete `if (n < 0)` in (a), so the compiler will see a `return` statement to be reached regardless of how the `if` statement is evaluated, as shown in (b).

> **Note** Methods enable code sharing and reuse. The `max` method can be invoked from any class, not just `TestMax`. If you create a new class, you can invoke the `max` method using `ClassName.methodName` (i.e., `TestMax.max`).

Each time a method is invoked, the system creates an *activation record* that stores parameters and variables for the method and places the activation record in an area of memory known as a *call stack.* A call stack is also known as an *execution stack*, *runtime stack*, or *machine stack* and it is often shortened to just “the stack.” When a method calls another method, the caller’s activation record is kept intact and a new activation record is created for the new method called. When a method finishes its work and returns to its caller, its activation record is removed from the call stack.

A call stack stores the activation records in a last-in, first-out fashion: The activation record for the method that is invoked last is removed first from the stack. For example, suppose method `m1` calls method `m2`, and `m2` calls method `m3`. The runtime system pushes `m1`’s activation record into the stack, then `m2`’s, and then `m3`’s. After `m3` is finished, its activation record is removed from the stack. After `m2` is finished, its activation record is removed from the stack. After `m1` is finished, its activation record is removed from the stack.

Understanding call stacks helps you to comprehend how methods are invoked. The variables defined in the `main` method in Listing 6.1 are `i`, `j`, and `k`. The variables defined in the `max` method are `num1`, `num2`, and `result`. The variables `num1` and `num2` are defined in the method signature and are parameters of the `max` method. Their values are passed through method invocation. Figure 6.3 illustrates the activation records for method calls in the stack.

```text
                 Activation record
                                          Activation record
                 for the max method
                                          for the max method
                       result:
                                                result: 5
                         num2: 2
                                                  num2: 2
                         num1: 5
                                                  num1: 5
Activation record
                 Activation record
                                          Activation record
                                                               Activation record
for the main method
                 for the main method
                                          for the main method
                                                               for the main method
           k:
                            k:
                                                     k:
                                                                          k: 5
                                                                                     Stack is empty
           j: 2
                            j: 2
                                                     j: 2
                                                                          j: 2
           i: 5
                            i: 5
                                                     i: 5
                                                                          i: 5
```

**Figure 6.3** When the `max` method is invoked, the flow of control transfers to the `max` method. Once the `max` method is finished, it returns control back to the caller. **6.3.1** How do you define a method? How do you invoke a method?

**Check Point**

**6.3.2** Reformat the following program according to the programming style and documen-

tation guidelines proposed in Section 1.9, Programming Style and Documentation. Use the end-of-line brace style.

<!-- LI p.211 -->

```java
public class Test {
  public static double method(double i, double j)
  {
    while (i < j) {
      j−−;
    }
    return j;
  }
}
```

## 6.4 void vs. Value-Returning Methods

*A* `void` *method does not return a value.*

The preceding section gives an example of a value-returning method. This section shows

**Key Point**

how to define and invoke a `void` method. Listing 6.2 gives a program that defines a method named `printGrade` and invokes it to print the grade for a given score.

**Listing 6.2**

**VideoNote**

```text
TestVoidMethod.java
```

> Use `void` method

```java
public class TestVoidMethod {
  public static void main(String[] args) {
    System.out.print("The grade is ");
    printGrade(78.5);

    System.out.print("The grade is ");
    printGrade(59.5);
  }

  public static void printGrade(double score) {
    if (score >= 90.0) {
      System.out.println('A');
    }
    else if (score >= 80.0) {
      System.out.println('B');
    }
    else if (score >= 70.0) {
      System.out.println('C');
    }
    else if (score >= 60.0) {
      System.out.println('D');
    }
    else {
      System.out.println('F');
    }
  }
}
```

```text
The grade is C
The grade is F
```

The `printGrade` method is a `void` method because it does not return any value. A call to a `void` method must be a statement. Therefore, it is invoked as a statement in line 4 in the `main` method. Like any Java statement, it is terminated with a semicolon.

To see the differences between a void and value-returning method, let’s redesign the `printGrade` method to return a value. The new method, which we call `getGrade`, returns the grade as given in Listing 6.3.

<!-- LI p.212 -->

**Listing 6.3 TestReturnGradeMethod.java** *(line N of the listing = Nth line of the block)*

```java
public class TestReturnGradeMethod {
  public static void main(String[] args) {
    System.out.print("The grade is " + getGrade(78.5));
    System.out.print("\nThe grade is " + getGrade(59.5));
  }

  public static char getGrade(double score) {
    if (score >= 90.0)
      return 'A';
    else if (score >= 80.0)
      return 'B';
    else if (score >= 70.0)
      return 'C';
    else if (score >= 60.0)
      return 'D';
    else
      return 'F';
  }
}

 The grade is C
 The grade is F
```

The `getGrade` method defined in lines 7–18 returns a character grade based on the numeric score value. The caller invokes this method in lines 3 and 4. The `getGrade` method can be invoked by a caller wherever a character may appear. The `printGrade` method does not return any value, so it must be invoked as a statement.

> **Note** A `return` statement is not needed for a `void` method, but it can be used for terminating the method and returning to the method’s caller. The syntax is simply

```java
return;
```

> This is not often done, but sometimes it is useful for circumventing the normal flow of control in a `void` method. For example, the following code has a return statement to terminate the method when the score is invalid:

```java
public static void printGrade(double score) {
  if (score < 0 || score > 100) {
    System.out.println("Invalid score");
    return;
  }

  if (score >= 90.0) {
    System.out.println('A');
  }
  else if (score >= 80.0) {
    System.out.println('B');
  }
  else if (score >= 70.0) {
    System.out.println('C');
  }
  else if (score >= 60.0) {
    System.out.println('D');
  }
  else {
    System.out.println('F');
  }
}
```

<!-- LI p.213 -->

**6.4.1** True or false? A call to a method with a `void` return type is always a statement it-

self, but a call to a value-returning method cannot be a statement by itself. **6.4.2** What is the `return` type of a `main` method? **6.4.3** What would be wrong with not writing a `return` statement in a value-returning

method? Can you have a `return` statement in a `void` method? Does the `return` statement in the following method cause syntax errors?

```java
public static void xMethod(double x, double y) {
  System.out.println(x + y);
  return x + y;
}
```

**6.4.4** Write method headers (not the bodies) for the following methods:

a. Return a sales commission, given the sales amount and the commission rate.

b. Display the calendar for a month, given the month and year.

c. Return a square root of a number.

d. Test whether a number is even, and returning `true` if it is.

e. Display a message a specified number of times.

f. Return the monthly payment, given the loan amount, number of years, and annual interest rate.

g. Return the corresponding uppercase letter, given a lowercase letter.

**6.4.5** Identify and correct the errors in the following program:

```java
public class Test {
  public static method1(int n, m) {
    n += m;
    method2(3.4);
  }

  public static int method2(int n) {
    if (n > 0) return 1;
    else if (n == 0) return 0;
    else if (n < 0) return −1;
  }
}
```

## 6.5 Passing Arguments by Values

*The arguments are passed by value to parameters when invoking a method.*

The power of a method is its ability to work with parameters. You can use `println` to print any string, and `max` to find the maximum of any two `int` values. When calling a method, you

**Key Point**

need to provide arguments, which must be given in the same order as their respective parameters in the method signature. This is known as *parameter order association.* For example, the following method prints a message `n` times:

```java
public static void nPrintln(String message, int n) {
  for (int i = 0; i < n; i++)
    System.out.println(message);
}
```

You can use `nPrintln("Hello", 3)` to print `Hello` three times. The `nPrintln("Hello",`

`3)` statement passes the actual string parameter `Hello` to the parameter `message`, passes `3` to `n`, and prints `Hello` three times. However, the statement `nPrintln(3, "Hello")` would be wrong. The data type of `3` does not match the data type for the first parameter, `message`, nor does the second argument, `Hello`, match the second parameter, `n`.

<!-- LI p.214 -->

> **Caution** The arguments must match the parameters in *order, number,* and *compatible type,* as defined in the method signature. Compatible type means you can pass an argument to a parameter without explicit casting, such as passing an `int` value argument to a `double` value parameter.

When you invoke a method with an argument, the value of the argument is passed to the parameter. This is referred to as *pass-by-value*. If the argument is a variable rather than a literal value, the value of the variable is passed to the parameter. The variable is not affected, regardless of the changes made to the parameter inside the method. As given in Listing 6.4, the value of `x` (`1`) is passed to the parameter `n` to invoke the `increment` method (line 5). The parameter `n` is incremented by `1` in the method (line 10), but `x` is not changed no matter what the method does.

**Listing 6.4 Increment.java** *(line N of the listing = Nth line of the block)*

```java
public class Increment {
  public static void main(String[] args) {
    int x = 1;
    System.out.println("Before the call, x is " + x);
    increment(x);
    System.out.println("After the call, x is " + x);
  }

  public static void increment(int n) {
    n++;
    System.out.println("n inside the method is " + n);
  }
}
```

```text
Before the call, x is 1
n inside the method is 2
After the call, x is 1
```

Listing 6.5 gives another program that demonstrates the effect of passing by value. The program creates a method for swapping two variables. The `swap` method is invoked by passing two arguments. Interestingly, the values of the arguments are not changed after the method is invoked.

**Listing 6.5 TestPassByValue.java** *(line N of the listing = Nth line of the block)*

```java
public class TestPassByValue {
  /** Main method */
  public static void main(String[] args) {
    // Declare and initialize variables
    int num1 = 1;
    int num2 = 2;

    System.out.println("Before invoking the swap method, num1 is " +
      num1 + " and num2 is " + num2);

    // Invoke the swap method to attempt to swap two variables
    swap(num1, num2);

    System.out.println("After invoking the swap method, num1 is " +
      num1 + " and num2 is " + num2);
  }

  /** Swap two variables */
  public static void swap(int n1, int n2) {
    System.out.println("\tInside the swap method");
    System.out.println("\t\tBefore swapping, n1 is " + n1
      + " and n2 is " + n2);

    // Swap n1 with n2
    int temp = n1;
    n1 = n2;
    n2 = temp;

    System.out.println("\t\tAfter swapping, n1 is " + n1
      + " and n2 is " + n2);
  }
}
```

<!-- LI p.215 -->

```text
Before invoking the swap method, num1 is 1 and num2 is 2
  Inside the swap method
    Before swapping, n1 is 1 and n2 is 2
    After swapping, n1 is 2 and n2 is 1
After invoking the swap method, num1 is 1 and num2 is 2
```

Before the `swap` method is invoked (line 12), `num1` is `1` and `num2` is `2`. After the `swap` method is invoked, `num1` is still `1` and `num2` is still `2`. Their values have not been swapped. As shown in Figure 6.4, the values of the arguments `num1` and `num2` are passed to `n1` and `n2`, but `n1` and `n2` have their own memory locations independent of `num1` and `num2`. Therefore, changes in `n1` and `n2` do not affect the contents of `num1` and `num2`.

```text
n2: 2
                         n2: 1
n1: 1
                         n1: 2
```

```text
num2: 2
                     num2: 2
                                             num2: 2
                                                                  num2: 2
num1: 1
                     num1: 1
                                             num1: 1
                                                                  num1: 1
```

**Figure 6.4** The values of the variables are passed to the method’s parameters.

<!-- LI p.216 -->

Another twist is to change the parameter name `n1` in `swap` to `num1`. What effect does this have? No change occurs, because it makes no difference whether the parameter and the argument have the same name. The parameter is a variable in the method with its own memory space. The variable is allocated when the method is invoked, and it disappears when the method is returned to its caller.

> **Note** For simplicity, Java programmers often say *passing* `x` to `y`, which actually means *passing the value of argument* `x` *to parameter* `y`.

**6.5.1** How is an argument passed to a method? Can the argument have the same name as

**Check**

its parameter?

**Point**

**6.5.2** Identify and correct the errors in the following program:

```java
public class Test {
  public static void main(String[] args) {
    nPrintln(5, "Welcome to Java!");
  }

  public static void nPrintln(String message, int n) {
    int n = 1;
    for (int i = 0; i < n; i++)
      System.out.println(message);
  }
}
```

**6.5.3** What is pass-by-value? Show the result of the following programs.

**6.5.4** For (a) in the preceding question, show the contents of the activation records in the

call stack just before the method `max` is invoked, just as `max` is entered, just before `max` is returned, and right after `max` is returned.

```java
public class Test {
                                                    public class Test {
  public static void main(String[] args) {
                                                      public static void main(String[] args) {
    int max = 0;
                                                        int i = 1;
    max(1, 2, max);
                                                        while (i <= 6) {
    System.out.println(max);
                                                          method1(i, 2);
  }
                                                          i++;
                                                        }
  public static void max(
                                                      }
      int value1, int value2, int max) {
    if (value1 > value2)
                                                      public static void method1(
      max = value1;
                                                          int i, int num) {
    else
                                                        for (int j = 1; j <= i; j++) {
      max = value2;
                                                          System.out.print(num + " ");
  }
                                                          num *= 2;
}
                                                        }

                                                        System.out.println();
                                                      }
                                                    }
public class Test {
                                                    public class Test {
  public static void main(String[] args) {
                                                      public static void main(String[] args) {
    // Initialize times
                                                        int i = 0;
    int times = 3;
                                                        while (i <= 4) {
    System.out.println("Before the call,"
                                                          method1(i);
      + " variable times is " + times);
                                                          i++;
                                                        }
    // Invoke nPrintln and display times
    nPrintln("Welcome to Java!", times);
                                                        System.out.println("i is " + i);
    System.out.println("After the call,"
                                                      }
      + " variable times is " + times);
  }
                                                      public static void method1(int i) {
                                                        do {
  // Print the message n times
                                                          if (i % 3 != 0)
  public static void nPrintln(
                                                            System.out.print(i + " ");
      String message, int n) {
                                                          i––;
    while (n > 0) {
                                                        }
      System.out.println("n = " + n);
                                                        while (i >= 1);
      System.out.println(message);
      n––;
                                                        System.out.println();
    }
                                                      }
  }
                                                    }
}
```

<!-- LI p.217 -->

## 6.6 Modularizing Code

> **Key Point** Modularizing makes the code easy to maintain and debug and enables the code to be reused.

Methods can be used to reduce redundant code and enable code reuse. Methods can also be used to modularize code and improve the quality of the program.

Listing 5.9 gives a program that prompts the user to enter two integers and displays their greatest common divisor. You can rewrite the program using a method, as given in

**VideoNote**

Listing 6.6.

> Modularize code

**Listing 6.6 GreatestCommonDivisorMethod.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class GreatestCommonDivisorMethod {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter two integers
    System.out.print("Enter first integer: ");
    int n1 = input.nextInt();
    System.out.print("Enter second integer: ");
    int n2 = input.nextInt();

    System.out.println("The greatest common divisor for " + n1 +
      " and " + n2 + " is " + gcd(n1, n2));
  }

  /** Return the gcd of two integers */
  public static int gcd(int n1,int n2) {
    int gcd = 1; // Initial gcd is 1
    int k = 2; // Possible gcd

    while (k <= n1 && k <= n2) {
      if (n1 % k == 0 && n2 % k == 0)
        gcd = k; // Update gcd
      k++;
    }

    return gcd; // Return gcd
  }
}
```

<!-- LI p.218 -->

```text
Enter first integer: 45
Enter second integer: 75
The greatest common divisor for 45 and 75 is 15
```

By encapsulating the code for obtaining the gcd in a method, this program has several advantages:

1. It isolates the problem for computing the gcd from the rest of the code in the main method. Thus, the logic becomes clear, and the program is easier to read.
2. The errors on computing the gcd are confined in the `gcd` method, which narrows the scope of debugging.
3. The `gcd` method now can be reused by other programs.

Listing 6.7 applies the concept of code modularization to improve Listing 5.15, PrimeNumber.java.

**Listing 6.7 PrimeNumberMethod.java** *(line N of the listing = Nth line of the block)*

```java
public class PrimeNumberMethod {
  public static void main(String[] args) {
    System.out.println("The first 50 prime numbers are \n");
    printPrimeNumbers(50);
  }

printPrimeNumbers
  public static void printPrimeNumbers(int numberOfPrimes) {
    final int NUMBER_OF_PRIMES_PER_LINE = 10; // Display 10 per line
    int count = 0; // Count the number of prime numbers
    int number = 2; // A number to be tested for primeness

    // Repeatedly find prime numbers
    while (count < numberOfPrimes) {
      // Print the prime number and increase the count
      if (isPrime(number)) {
        count++; // Increase the count

        if (count % NUMBER_OF_PRIMES_PER_LINE == 0) {
          // Print the number and advance to the new line
          System.out.printf("%−5d\n", number);
        }
        else
          System.out.printf("%−5d", number);
      }

      // Check whether the next number is prime
      number++;
    }
  }

  /** Check whether number is prime */
  public static boolean isPrime(int number) {
    for (int divisor = 2; divisor <= number / 2; divisor++) {
      if (number % divisor == 0) { // If true, number is not prime
        return false; // Number is not a prime
      }
    }

    return true; // Number is prime
  }
}
```

<!-- LI p.219 -->

```text
The first 50 prime numbers are

2    3    5    7    11   13   17   19   23   29
31   37   41   43   47   53   59   61   67   71
73   79   83   89   97   101  103  107  109  113
127  131  137  139  149  151  157  163  167  173
179  181  191  193  197  199  211  223  227  229
```

We divided a large problem into two subproblems: determining whether a number is a prime, and printing the prime numbers. As a result, the new program is easier to read and easier to debug. Moreover, the methods `printPrimeNumbers` and `isPrime` can be reused by other programs. **6.6.1** Trace the `gcd` method to find the return value for `gcd(4, 6)`.

**Check**

**6.6.2** Trace the `isPrime` method to find the return value for `isPrime(25)`.

**Point**

## 6.7 Case Study: Converting Hexadecimals to Decimals

> **Key Point** This section presents a program that converts a hexadecimal number into a decimal number.

Listing 5.11, Dec2Hex.java, gives a program that converts a decimal to a hexadecimal. How would you convert a hex number into a decimal?

Given a hexadecimal number *hnhn*-1*hn*-2 c *h*2*h*1*h*0, the equivalent decimal value is *hn* × 16*n* + *hn*-1 × 16*n*-1 + *hn*-2 × 16*n*-2 + c + *h*2 × 162 + *h*1 × 161 + *h*0 × 160

For example, the hex number `AB8C` is

10 × 163 + 11 × 162 + 8 × 161 + 12 × 160 = 43916

Our program will prompt the user to enter a hex number as a string and convert it into a decimal using the following method:

```java
public static int hexToDecimal(String hex)
```

<!-- LI p.220 -->

A brute-force approach is to convert each hex character into a decimal number, multiply it by 16*i* for a hex digit at the `i`’s position, and then add all the items together to obtain the equivalent decimal value for the hex number.

Note that *hn* × 16*n* + *hn*-1 × 16*n*-1 + *hn*-2 × 16*n*-2 + g + *h*1 × 161 + *h*0 × 160

= ( c ((*hn* × 16 + *hn*-1) × 16 + *hn*-2) × 16 + g + *h*1) × 16 + *h*0

This observation, known as the Horner’s algorithm, leads to the following efficient code for converting a hex string to a decimal number:

```java
int decimalValue = 0;
for (int i = 0; i < hex.length(); i++) {
  char hexChar = hex.charAt(i);
  decimalValue = decimalValue * 16 + hexCharToDecimal(hexChar);
}
```

Here is a trace of the algorithm for hex number `AB8C`:

```text
             hexCharToDecimal
i
    hexChar
             (hexChar)
                              decimalValue
```

Before the loop

```text
0
```

After the 1st iteration

```text
0
    A
            10
                            10
```

After the 2nd iteration

```text
1
    B
             11
                              10 * 16 + 11
```

After the 3rd iteration

```text
2
    8
             8
                              (10 * 16 + 11) * 16 + 8
```

After the 4th iteration

```text
                              ((10 * 16 + 11)
3
    C
             12
                              * 16 + 8) * 16 + 12
```

Listing 6.8 gives the complete program.

**Listing 6.8 Hex2Dec.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class Hex2Dec {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter a string
    System.out.print("Enter a hex number: ");
    String hex = input.nextLine();

    System.out.println("The decimal value for hex number "
      + hex + " is " + hexToDecimal(hex.toUpperCase()));
  }

  public static int hexToDecimal(String hex) {
    int decimalValue = 0;
    for (int i = 0; i < hex.length(); i++) {
      char hexChar = hex.charAt(i);
      decimalValue = decimalValue * 16 + hexCharToDecimal(hexChar);
    }

    return decimalValue;
  }

  public static int hexCharToDecimal(char ch) {
    if (ch >= 'A' && ch <= 'F')
      return 10 + ch – 'A';
    else // ch is '0', '1', ..., or '9'
      return ch − '0';
  }
}
```

<!-- LI p.221 -->

```text
Enter a hex number: AB8C
The decimal value for hex number AB8C is 43916
```

```text
Enter a hex number: af71
The decimal value for hex number af71 is 44913
```

The program reads a string from the console (line 11) and invokes the `hexToDecimal` method to convert a hex string to decimal number (line 14). The characters can be in either lowercase or uppercase. They are converted to uppercase before invoking the `hexToDecimal` method.

The `hexToDecimal` method is defined in lines 17–25 to return an integer. The length of the string is determined by invoking `hex.length()` in line 19.

The `hexCharToDecimal` method is defined in lines 27–32 to return a decimal value for a hex character. The character can be in either lowercase or uppercase. Recall that to subtract two characters is to subtract their Unicodes. For example, `'5' – '0'` is `5`.

**6.7.1**

What is `hexCharToDecimal('B'))`?

**Check**

What is `hexCharToDecimal('7'))`?

**Point**

What is `hexToDecimal("A9"))`?

## 6.8 Overloading Methods

*Overloading methods enable you to define the methods with the same name as long as*

**Key**

*their parameter lists are different.*

**Point**

The `max` method used earlier works only with the `int` data type. But what if you need to determine which of the two floating-point numbers has the maximum value? The solution is to create another method with the same name but different parameters, as shown in the following code:

```java
public static double max(double num1, double num2) {
  if (num1 > num2)
    return num1;
  else
    return num2;
}
```

If you call `max` with `int` parameters, the `max` method that expects `int` parameters will be invoked; and if you call `max` with `double` parameters, the `max` method that expects `double` parameters will be invoked. This is referred to as *method overloading*; that is, two methods have the same name but different parameter lists within one class. The Java compiler deter-mines which method to use based on the method signature.

<!-- LI p.222 -->

Listing 6.9 is a program that creates three methods. The first finds the maximum integer, the second finds the maximum double, and the third finds the maximum among three double values. All three methods are named `max`.

**Listing 6.9 TestMethodOverloading.java** *(line N of the listing = Nth line of the block)*

```java
public class TestMethodOverloading {
  /** Main method */
  public static void main(String[] args) {
    // Invoke the max method with int parameters
    System.out.println("The maximum of 3 and 4 is "
      + max(3, 4));

    // Invoke the max method with the double parameters
    System.out.println("The maximum of 3.0 and 5.4 is "
      + max(3.0, 5.4));

    // Invoke the max method with three double parameters
    System.out.println("The maximum of 3.0, 5.4, and 10.14 is "
      + max(3.0, 5.4, 10.14));
  }

  /** Return the max of two int values */
  public static int max(int num1, int num2) {
    if (num1 > num2)
      return num1;
    else
      return num2;
  }

  /** Find the max of two double values */
  public static double max(double num1, double num2) {
    if (num1 > num2)
      return num1;
    else
      return num2;
  }

  /** Return the max of three double values */
  public static double max(double num1, double num2, double num3) {
    return max(max(num1, num2), num3);
  }
}


 The maximum of 3 and 4 is 4
 The maximum of 3.0 and 5.4 is 5.4
 The maximum of 3.0, 5.4, and 10.14 is 10.14
```

When calling `max(3, 4)` (line 6), the `max` method for finding the maximum of two integers is invoked. When calling `max(3.0, 5.4)` (line 10), the `max` method for finding the maximum of two doubles is invoked. When calling `max(3.0, 5.4, 10.14)` (line 14), the `max` method for finding the maximum of three double values is invoked.

Can you invoke the `max` method with an `int` value and a `double` value, such as `max(2, 2.5)`? If so, which of the `max` methods is invoked? The answer to the first question is yes. The answer to the second question is that the `max` method for finding the maximum of two `double` values is invoked. The argument value `2` is automatically converted into a `double` value and passed to this method.

<!-- LI p.223 -->

You may be wondering why the method `max(double, double)` is not invoked for the call `max(3, 4)`. Both `max(double, double)` and `max(int, int)` are possible matches for `max(3, 4)`. The Java compiler finds the method that best matches a method invocation. Since the method `max(int, int)` is a better match for `max(3, 4)` than `max(double, double)`, `max(int, int)` is used to invoke `max(3, 4)`.

> **Tip** Overloading methods can make programs clearer and more readable. Methods that perform the same function with different types of parameters should be given the same name.

> **Note** Overloaded methods must have different parameter lists. You cannot overload methods based on different modifiers or return types.

> **Note** Sometimes there are two or more possible matches for the invocation of a method, but the compiler cannot determine the most specific match. This is referred to as *ambiguous invocation*. Ambiguous invocation causes a compile error. Consider the following code:

```java
public class AmbiguousOverloading {
  public static void main(String[] args) {
    System.out.println(max(1, 2));
  }

  public static double max(int num1, double num2) {
    if (num1 > num2)
      return num1;
    else
      return num2;
  }

  public static double max(double num1, int num2) {
    if (num1 > num2)
      return num1;
    else
      return num2;
  }
}
```

> Both `max(int, double)` and `max(double, int)` are possible candidates to match `max(1, 2)`. Because neither is more specific than the other, the invocation is ambiguous, resulting in a compile error.

**6.8.1** What is method overloading? Is it permissible to define two methods that have the

**Check**

same name but different parameter types? Is it permissible to define two methods

**Point**

in a class that have identical method names and parameter lists, but different return value types or different modifiers? **6.8.2** What is wrong in the following program?

```java
public class Test {
  public static void method(int x) {
  }

  public static int method(int y) {
    return y;
  }
}
```

<!-- LI p.224 -->

**6.8.3** Given two method definitions,

```java
public static double m(double x, double y)

public static double m(int x, double y)
```

tell which of the two methods is invoked for:

a. `double z = m(4, 5);`

b. `double z = m(4, 5.4);`

c. `double z = m(4.5, 5.4);`

## 6.9 The Scope of Variables

**Key Point**

*The scope of a variable is the part of the program where the variable can be referenced.*

Section 2.5 introduced the scope of a variable. This section discusses the scope of variables in detail. A variable defined inside a method is referred to as a *local variable*. The scope of a local variable starts from its declaration and continues to the end of the block that contains the variable. A local variable must be declared and assigned a value before it can be used.

A parameter is actually a local variable. The scope of a method parameter covers the entire method. A variable declared in the initial-action part of a `for`-loop header has its scope in the entire loop. However, a variable declared inside a `for`-loop body has its scope limited in the loop body from its declaration to the end of the block that contains the variable, as shown in Figure 6.5.

```java
public static void method() {
   .
   .
  for (int i = 1; i < 10; i++) {
     .
     .
     int j;
     .
     .
     .
  }
}
```

**Figure 6.5** A variable declared in the initial-action part of a `for`-loop header has its scope in the entire loop.

You can declare a local variable with the same name in different blocks in a method, but you cannot declare a local variable twice in the same block or in nested blocks, as shown in Figure 6.6.

> **Caution** A common mistake is to declare a variable in a `for` loop and then attempt to use it outside the loop. As shown in the following code, `i` is declared in the `for` loop, but it is accessed from the outside of the `for` loop, which causes a syntax error.

```java
for (int i = 0; i < 10; i++) {
}
System.out.println(i); // Causes a syntax error on i
```

> The last statement would cause a syntax error, because variable `i` is not defined outside of the `for` loop.

<!-- LI p.225 -->

```java
public static void method1() {
  int x = 1;
  int y = 1;

  for (int i = 1; i < 10; i++) {
    x += i;
  }

  for (int i = 1; i < 10; i++) {
    y += i;
  }
}
```

```java
public static void method2() {
  int i = 1;
  int sum = 0;

  for (int i = 1; i < 10; i++) {
    sum += i;

  }
}
```

**Figure 6.6** A variable can be declared multiple times in nonnested blocks, but only once in nested blocks.

**6.9.1** What is a local variable?

**Check**

**6.9.2** What is the scope of a local variable?

**Point**

## 6.10 Case Study: Generating Random Characters

> **Key Point** A character is coded using an integer. Generating a random character is to generate

*an integer.*

Computer programs process numerical data and characters. You have seen many examples that involve numerical data. It is also important to understand characters and how to process them. This section presents an example of generating random characters.

As introduced in Section 4.3, every character has a unique Unicode between `0` and `FFFF` in hexadecimal (`65535` in decimal). To generate a random character is to generate a random integer between `0` and `65535` using the following expression (note since `0 <= Math.random() < 1.0`, you have to add `1` to `65535`):

```java
(int)(Math.random() * (65535 + 1))
```

Now let’s consider how to generate a random lowercase letter. The Unicodes for lowercase letters are consecutive integers starting from the Unicode for `a,` then for `b, c,` . . ., and `z`. The Unicode for `a` is

```java
(int)'a'
```

Thus, a random integer between `(int)'a'` and `(int)'z'` is

```java
(int)((int)'a' + Math.random() * ((int)'z' – (int)'a' + 1))
```

<!-- LI p.226 -->

As discussed in Section 4.3.3, all numeric operators can be applied to the `char` operands. The `char` operand is cast into a number if the other operand is a number or a character. Therefore, the preceding expression can be simplified as follows:

```text
'a' + Math.random() * ('z' – 'a' + 1)
```

and a random lowercase letter is

```text
(char)('a' + Math.random() * ('z' – 'a' + 1))
```

Hence, a random character between any two characters `ch1` and `ch2` with `ch1 < ch2` can be generated as follows:

```text
(char)(ch1 + Math.random() * (ch2 – ch1 + 1))
```

This is a simple but useful discovery. Listing 6.10 defines a class named `RandomCharacter` with overloaded methods to get a certain type of random character. You can use these methods in your future projects.

**Listing 6.10 RandomCharacter.java** *(line N of the listing = Nth line of the block)*

```java
public class RandomCharacter {
  /** Generate a random character between ch1 and ch2 */
  public static char getRandomCharacter(char ch1, char ch2) {
getRandomCharacter
    return (char)(ch1 + Math.random() * (ch2 – ch1 + 1));
  }

  /** Generate a random lowercase letter */
getRandomLower
  public static char getRandomLowerCaseLetter() {
  CaseLetter()
    return getRandomCharacter('a', 'z');
  }

  /** Generate a random uppercase letter */
getRandomUpper
  public static char getRandomUpperCaseLetter() {
  CaseLetter()
    return getRandomCharacter('A', 'Z');
  }

  /** Generate a random digit character */
getRandomDigit
  public static char getRandomDigitCharacter() {
  Character()
    return getRandomCharacter('0', '9');
  }

  /** Generate a random character */
getRandomCharacter()
  public static char getRandomCharacter() {
    return getRandomCharacter('\u0000', '\uFFFF');
  }
}
```

Listing 6.11 gives a test program that displays 175 random lowercase letters.

**Listing 6.11 TestRandomCharacter.java** *(line N of the listing = Nth line of the block)*

```java
public class TestRandomCharacter {
  /** Main method */
  public static void main(String[] args) {
    final int NUMBER_OF_CHARS = 175;
    final int CHARS_PER_LINE = 25;

    // Print random characters between 'a' and 'z', 25 chars per line
    for (int i = 0; i < NUMBER_OF_CHARS; i++) {
      char ch = RandomCharacter.getRandomLowerCaseLetter();
      if ((i + 1) % CHARS_PER_LINE == 0)
        System.out.println(ch);
      else
        System.out.print(ch);
    }
  }
}


 gmjsohezfkgtazqgmswfclrao
 pnrunulnwmaztlfjedmpchcif
 lalqdgivxkxpbzulrmqmbhikr
 lbnrjlsopfxahssqhwuuljvbe
 xbhdotzhpehbqmuwsfktwsoli
 cbuwkzgxpmtzihgatdslvbwbz
 bfesoklwbhnooygiigzdxuqni
```

<!-- LI p.227 -->

Line 9 invokes `getRandomLowerCaseLetter()` defined in the `RandomCharacter` class. Note `getRandomLowerCaseLetter()` does not have any parameters, but you still have to use the parentheses when defining and invoking the method.

## 6.11 Method Abstraction and Stepwise Refinement

> **Key Point** The key to developing software is to apply the concept of abstraction.

You will learn many levels of abstraction from this book. *Method abstraction* is achieved by separating the use of a method from its implementation. The client can use a method without knowing how it is implemented. The details of the implementation are encapsulated in the

**VideoNote**

method and hidden from the client who invokes the method. This is also known as *informa-*

> Stepwise refinement

*tion hiding* or *encapsulation.* If you decide to change the implementation, the client program will not be affected, provided that you do not change the method signature. The implementation of the method is hidden from the client in a “black box,” as shown in Figure 6.7.

**Figure 6.7** The method body can be thought of as a black box that contains the detailed implementation for the method.

You have already used the `System.out.print` method to display a string and the `max` method to find the maximum number. You know how to write the code to invoke these methods in your program, but as a user of these methods, you are not required to know how they are implemented.

The concept of method abstraction can be applied to the process of developing programs. When writing a large program, you can use the *divide-and-conquer* strategy, also known as *stepwise refinement*, to decompose it into subproblems. The subproblems can be further decomposed into smaller, more manageable problems.

Suppose that you write a program that displays the calendar for a given month of the year. The program prompts the user to enter the year and the month, and then displays the entire calendar for the month, as presented in the following sample run:

<!-- LI p.228 -->

```text
Enter full year (e.g., 2012):  2012
Enter month as number between 1 and 12:  3

        March 2012
-----------------------------
 Sun Mon Tue Wed Thu Fri Sat
                   1   2   3
   4   5   6   7   8   9  10
  11  12  13  14  15  16  17
  18  19  20  21  22  23  24
  25  26  27  28  29  30
```

Let us use this example to demonstrate the divide-and-conquer approach.

### 6.11.1 Top-Down Design

How would you get started on such a program? Would you immediately start coding? Beginning programmers often start by trying to work out the solution to every detail. Although details are important in the final program, concern for detail in the early stages may block the problem-solving process. To make problem solving flow as smoothly as possible, this example begins by using method abstraction to isolate details from design and only later implements the details.

For this example, the problem is first broken into two subproblems: get input from the user, and print the calendar for the month. At this stage, you should be concerned with what the subproblems will achieve, not with how to get input and print the calendar for the month. You can draw a structure chart to help visualize the decomposition of the problem (see Figure 6.8a).

```text
printCalendar
   (main)
                                            printMonth
```

```text
readInput
                       printMonth
                                        printMonthTitle
                                                                printMonthBody
```

**Figure 6.8** The structure chart shows the `printCalendar` problem is divided into two subproblems, `readInput` and `printMonth` in (a), and `printMonth` is divided into two smaller subproblems, `printMonthTitle` and `printMonthBody` in (b).

You can use `Scanner` to read input for the year and the month. The problem of printing the calendar for a given month can be broken into two subproblems: print the month title, and print the month body, as shown in Figure 6.8b. The month title consists of three lines: month and year, a dashed line, and the names of the seven days of the week. You need to get the month name (e.g., January) from the numeric month (e.g., 1). This is accomplished in `getMonthName` (see Figure 6.9a).

In order to print the month body, you need to know which day of the week is the first day of the month (`getStartDay`) and how many days the month has (`getNumberOfDaysInMonth`),

<!-- LI p.229 -->

```text
printMonthTitle
                               printMonthBody
```

```text
getMonthName
                   getStartDay
                                     getNumberOfDaysInMonth
```

**Figure 6.9** (a) To `printMonthTitle`, you need `getMonthName`. (b) The `printMonthBody` problem is refined into several smaller problems.

as shown in Figure 6.9b. For example, December 2013 has 31 days, and December 1, 2013 is a Sunday.

How would you get the start day for the first date in a month? There are several ways to do so. Assume you know that the start day for January 1, 1800 was a Wednesday (`START_DAY_ FOR_JAN_1_1800 = 3`). You could compute the total number of days (`totalNumberOfDays`) between January 1, 1800 and the first date of the calendar month. The start day for the calendar month is `(totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7`, since every week has seven days. Thus, the `getStartDay` problem can be further refined as `getTotalNumberOfDays`, as shown in Figure 6.10a.

```text
     getStartDay
                        getTotalNumberOfDays


                                           getNumberOfDaysInMonth


getTotalNumberOfDays
                             isLeapYear
```

**Figure 6.10** (a) To `getStartDay`, you need `getTotalNumberOfDays`. (b) The `getTotalNumberOfDays` problem is refined into two smaller problems.

To get the total number of days, you need to know whether the year is a leap year and the number of days in each month. Thus, `getTotalNumberOfDays` can be further refined into two subproblems: `isLeapYear` and `getNumberOfDaysInMonth`, as shown in Figure 6.10b. The complete structure chart is shown in Figure 6.11.

### 6.11.2 Top-Down and/or Bottom-Up Implementation

Now we turn our attention to implementation. In general, a subproblem corresponds to a method in the implementation, although some are so simple that this is unnecessary. You would need to decide which modules to implement as methods and which to combine with other methods. Decisions of this kind should be based on whether the overall program will be easier to read as a result of your choice. In this example, the subproblem `readInput` can be simply implemented in the `main` method.

You can use either a “top-down” or a “bottom-up” approach. The top-down approach implements one method in the structure chart at a time from the top to the bottom. *Stubs*—a simple but incomplete version of a method—can be used for the methods waiting to be implemented. The use of stubs enables you to quickly build the framework of the program. Implement the `main` method first then use a stub for the `printMonth` method. For example,

<!-- LI p.230 -->

```text
printCalendar
    (main)
```

```text
readInput
                       printMonth
```

```text
printMonthTitle
                   printMonthBody


 getMonthName
                    getStartDay


               getTotalNumberOfDays
```

```text
getNumberOfDaysInMonth
```

```text
isLeapYear
```

**Figure 6.11** The structure chart shows the hierarchical relationship of the subproblems in the program.

let `printMonth` display the year and the month in the stub. Thus, your program may begin as follows:

```java
public class PrintCalendar {
  /** Main method */
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter year
    System.out.print("Enter full year (e.g., 2012): ");
    int year = input.nextInt();

    // Prompt the user to enter month
    System.out.print("Enter month as a number between 1 and 12: ");
    int month = input.nextInt();

    // Print calendar for the month of the year
    printMonth(year, month);
  }

  /** A stub for printMonth may look like this */
  public static void printMonth(int year, int month) {
    System.out.print(month + " " + year);
  }

  /** A stub for printMonthTitle may look like this */
  public static void printMonthTitle(int year, int month) {
  }

  /** A stub for printMonthBody may look like this */
  public static void printMonthBody(int year, int month) {
  }
  /** A stub for getMonthName may look like this */
  public static String getMonthName(int month) {
    return "January"; // A dummy value
  }

  /** A stub for getStartDay may look like this */
  public static int getStartDay(int year, int month) {
    return 1; // A dummy value
  }

  /** A stub for getTotalNumberOfDays may look like this */
  public static int getTotalNumberOfDays(int year, int month) {
    return 10000; // A dummy value
  }

  /** A stub for getNumberOfDaysInMonth may look like this */
  public static int getNumberOfDaysInMonth(int year, int month) {
    return 31; // A dummy value
  }

  /** A stub for isLeapYear may look like this */
  public static boolean isLeapYear(int year) {
    return true; // A dummy value
  }
}
```

<!-- LI p.231 -->

Compile and test the program, and fix any errors. You can now implement the `printMonth` method. For methods invoked from the `printMonth` method, you can again use stubs.

The bottom-up approach implements one method in the structure chart at a time from the bottom to the top. For each method implemented, write a test program, known as the *driver*, to test it. The top-down and bottom-up approaches are equally good: Both approaches implement methods incrementally, help to isolate programming errors, and make debugging easy. They can be used together.

### 6.11.3 Implementation Details

The `isLeapYear(int year)` method can be implemented using the following code from Section 3.11:

```java
return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
```

Use the following facts to implement `getTotalNumberOfDaysInMonth(int year, int month)`:

- January, March, May, July, August, October, and December have 31 days.
- April, June, September, and November have 30 days.
- February has 28 days during a regular year, and 29 days during a leap year. A regular year, therefore, has 365 days, and a leap year has 366 days.

To implement `getTotalNumberOfDays(int year, int month)`, you need to compute the total number of days (`totalNumberOfDays`) between January 1, 1800 and the first day of the calendar month. You could find the total number of days between the year 1800 and the calendar year then figure out the total number of days prior to the calendar month in the calendar year. The sum of these two totals is `totalNumberOfDays`.

To print a body, first pad some space before the start day then print the lines for every week.

The complete program is given in Listing 6.12.

<!-- LI p.232 -->

**Listing 6.12 PrintCalendar.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class PrintCalendar {
  /** Main method */
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter year
    System.out.print("Enter full year (e.g., 2012): ");
    int year = input.nextInt();

    // Prompt the user to enter month
    System.out.print("Enter month as a number between 1 and 12: ");
    int month = input.nextInt();

    // Print calendar for the month of the year
    printMonth(year, month);
  }

  /** Print the calendar for a month in a year */
printMonth
  public static void printMonth(int year, int month) {
    // Print the headings of the calendar
    printMonthTitle(year, month);

    // Print the body of the calendar
    printMonthBody(year, month);
  }

  /** Print the month title, e.g., March 2012 */
printMonthTitle
  public static void printMonthTitle(int year, int month) {
    System.out.println("         " + getMonthName(month)
      + " " + year);
    System.out.println("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−");
    System.out.println(" Sun Mon Tue Wed Thu Fri Sat");
  }

  /** Get the English name for the month */
getMonthName
  public static String getMonthName(int month) {
    String monthName = "";
    switch (month) {
      case 1: monthName = "January"; break;
      case 2: monthName = "February"; break;
      case 3: monthName = "March"; break;
      case 4: monthName = "April"; break;
      case 5: monthName = "May"; break;
      case 6: monthName = "June"; break;
      case 7: monthName = "July"; break;
      case 8: monthName = "August"; break;
      case 9: monthName = "September"; break;
      case 10: monthName = "October"; break;
      case 11: monthName = "November"; break;
      case 12: monthName = "December";
    }

    return monthName;
  }

  /** Print month body */
  public static void printMonthBody(int year, int month) {
                                                                           printMonthBody
    // Get start day of the week for the first date in the month
    int startDay = getStartDay(year, month);

    // Get number of days in the month
    int numberOfDaysInMonth = getNumberOfDaysInMonth(year, month);

    // Pad space before the first day of the month
    int i = 0;
    for (i = 0; i < startDay; i++)
      System.out.print("    ");

    for (i = 1; i <= numberOfDaysInMonth; i++) {
      System.out.printf("%4d", i);

      if ((i + startDay) % 7 == 0)
        System.out.println();
    }

    System.out.println();
  }

  /** Get the start day of month/1/year */
  public static int getStartDay(int year, int month) {
                                                                           getStartDay
    final int START_DAY_FOR_JAN_1_1800 = 3;
    // Get total number of days from 1/1/1800 to month/1/year
    int totalNumberOfDays = getTotalNumberOfDays(year, month);

    // Return the start day for month/1/year
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7;
  }

  /** Get the total number of days since January 1, 1800 */
  public static int getTotalNumberOfDays(int year, int month) {
                                                                           getTotalNumberOfDays
    int total = 0;

    // Get the total days from 1800 to 1/1/year
    for (int i = 1800; i < year; i++)
      if (isLeapYear(i))
        total = total + 366;
      else
        total = total + 365;

    // Add days from Jan to the month prior to the calendar month
    for (int i = 1; i < month; i++)
      total = total + getNumberOfDaysInMonth(year, i);

    return total;
  }

  /** Get the number of days in a month */
  public static int getNumberOfDaysInMonth(int year, int month) {
                                                                           getNumberOfDaysInMonth
    if (month == 1 || month == 3 || month == 5 || month == 7 ||
      month == 8 || month == 10 || month == 12)
      return 31;

    if (month == 4 || month == 6 || month == 9 || month == 11)
      return 30;

    if (month == 2) return isLeapYear(year)? 29: 28;

    return 0; // If month is incorrect
  }

  /** Determine if it is a leap year */
isLeapYear
  public static boolean isLeapYear(int year) {
    return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
  }
}
```

<!-- LI p.234 -->

The program does not validate user input. For instance, if the user enters either a month not in the range between `1` and `12` or a year before `1800`, the program displays an erroneous calendar. To avoid this error, add an `if` statement to check the input before printing the calendar.

This program prints calendars for a month, but could easily be modified to print calendars for a whole year. Although it can print months only after January `1800`, it could be modified to print months before `1800`.

### 6.11.4 Benefits of Stepwise Refinement

Stepwise refinement breaks a large problem into smaller manageable subproblems. Each subproblem can be implemented using a method. This approach makes the program easier to write, reuse, debug, test, modify, and maintain.

#### Simpler Program

The print calendar program is long. Rather than writing a long sequence of statements in one method, stepwise refinement breaks it into smaller methods. This simplifies the program and makes the whole program easier to read and understand.

#### Reusing Methods

Stepwise refinement promotes code reuse within a program. The `isLeapYear` method is defined once and invoked from the `getTotalNumberOfDays` and `getNumberOfDaysInMonth` methods. This reduces redundant code.

#### Easier Developing, Debugging, and Testing

Since each subproblem is solved in a method, a method can be developed, debugged, and tested individually. This isolates the errors and makes developing, debugging, and testing easier.

When implementing a large program, use the top-down and/or bottom-up approach. Do not write the entire program at once. Using these approaches seems to take more development time (because you repeatedly compile and run the program), but it actually saves time and makes debugging easier.

#### Better Facilitating Teamwork

When a large problem is divided into subprograms, subproblems can be assigned to different programmers. This makes it easier for programmers to work in teams.

**Key Terms**

actual parameter 207

method overloading 221 ambiguous invocation 223

method signature 207 argument 207

modifier 207 divide and conquer 227

parameter 207 formal parameter (i.e., parameter) 207

pass-by-value 214 information hiding 227

scope of a variable 224 method 206

stepwise refinement 227 method abstraction 227

stub 229

<!-- LI p.235 -->

**Chapter Summary**

**1.** Making programs modular and reusable is one of the central goals in software engineering. Java provides many powerful constructs that help to achieve this goal. *Methods* are one such construct.

**2.** The method header specifies the *modifiers*, *return value type*, *method name*, and *parameters* of the method. The `static` modifier is used for all the methods in this chapter.

**3.** A method may return a value. The `returnValueType` is the data type of the value the method returns. If the method does not return a value, the `returnValueType` is the keyword `void`.

**4.** The *parameter list* refers to the type, order, and number of a method’s parameters. The method name and the parameter list together constitute the *method signature.* Parameters are optional; that is, a method doesn’t need to contain any parameters.

**5.** A return statement can also be used in a `void` method for terminating the method and returning to the method’s caller. This is useful occasionally for circumventing the normal flow of control in a method.

**6.** The arguments that are passed to a method should have the same number, type, and order as the parameters in the method signature.

**7.** When a program calls a method, program control is transferred to the called method. A called method returns control to the caller when its return statement is executed, or when its method-ending closing brace is reached.

**8.** A value-returning method can also be invoked as a statement in Java. In this case, the caller simply ignores the return value.

**9.** A method can be overloaded. This means that two methods can have the same name, as long as their method parameter lists differ.

**10.** A variable declared in a method is called a local variable. The *scope of a local variable* starts from its declaration and continues to the end of the block that contains the variable. A local variable must be declared and initialized before it is used.

**11.** *Method abstraction* is achieved by separating the use of a method from its implementation. The client can use a method without knowing how it is implemented. The details of the implementation are encapsulated in the method and hidden from the client who invokes the method. This is known as *information hiding* or *encapsulation.*

**12.** Method abstraction modularizes programs in a neat, hierarchical manner. Programs written as collections of concise methods are easier to write, debug, maintain, and modify than would otherwise be the case. This writing style also promotes method reusability.

**13.** When implementing a large program, use the top-down and/or bottom-up coding approach. Do not write the entire program at once. This approach may seem to take more time for coding (because you are repeatedly compiling and running the program), but it actually saves time and makes debugging easier.

<!-- LI p.236 -->

**Quiz**

Answer the quiz for this chapter online at the Companion Website.

**Programming Exercises**

> **Note** A common error for the exercises in this chapter is that students don’t implement the methods to meet the requirements even though the output from the main program is correct. For an example of this type of error, see liveexample.pearsoncmg.com/etc/ CommonMethodErrorJava.pdf.

**Sections 6.2–6.9**

**6.1**

(*Math: pentagonal numbers*) A pentagonal number is defined as *n*(3*n*-1)/2 for *n* = 1, 2, . . ., and so on. Therefore, the first few numbers are 1, 5, 12, 22, ... . Write a method with the following header that returns a pentagonal number:

```java
public static int getPentagonalNumber(int n)
```

For example, `getPentagonalNumber(1)` returns `1` and `getPentagonalNumber(2)` returns `5`. Write a test program that uses this method to display the first 100 pentagonal numbers with 10 numbers on each line. Use the `%7d` format to display each number.

***6.2**

(*Sum the digits in an integer*) Write a method that computes the sum of the digits in an integer. Use the following method header:

```java
public static int sumDigits(long n)
```

For example, `sumDigits(234)` returns `9` (= 2 + 3 + 4). (*Hint*: Use the % operator to extract digits and the / operator to remove the extracted digit. For instance, to extract 4 from 234, use `234 % 10` (= 4). To remove 4 from 234, use `234 / 10` (= 23). Use a loop to repeatedly extract and remove the digit until all the digits are extracted. Write a test program that prompts the user to enter an integer then displays the sum of all its digits.

****6.3**

(*Palindrome integer*) Write the methods with the following headers:

```java
// Return the reversal of an integer, e.g., reverse(456) re-
turns 654
public static int reverse(int number)

// Return true if number is a palindrome
public static boolean isPalindrome(int number)
```

Use the `reverse` method to implement `isPalindrome`. A number is a palindrome if its reversal is the same as itself. Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.

***6.4**

(*Display an integer reversed*) Write a method with the following header to display an integer in reverse order:

**VideoNote**

> Reverse an integer

```java
public static void reverse(int number)
```

For example, `reverse(3456)` displays `6543`. Write a test program that prompts the user to enter an integer then displays its reversal.

<!-- LI p.237 -->

***6.5**

(*Sort three numbers*) Write a method with the following header to display three numbers in increasing order:

```java
public static void displaySortedNumbers(
  double num1, double num2, double num3)
```

Write a test program that prompts the user to enter three numbers and invokes the method to display them in increasing order.

***6.6**

(*Display patterns*) Write a method to display a pattern as follows:

```text
              1
            2 1
          3 2 1
...
n n–1 ... 3 2 1
```

The method header is

```java
public static void displayPattern(int n)
```

Write a test program that prompts the user to enter a number n and invokes `displayPattern(n)` to display the pattern.

***6.7**

(*Financial application: compute the future investment value*) Write a method that computes future investment value at a given interest rate for a specified number of years. The future investment is determined using the formula in Programming Exercise 2.21. Use the following method header:

```java
public static double futureInvestmentValue(
  double investmentAmount, double monthlyInterestRate,int years)
```

For example, `futureInvestmentValue(10000, 0.05/12, 5)` returns `12833.59`. Write a test program that prompts the user to enter the investment amount (e.g., 1,000) and the interest rate (e.g., 9%) and prints a table that displays future value for the years from 1 to 30, as shown below:

```text
The amount invested: 1000
Annual interest rate: 9
Years     Future Value
1             1093.80
2             1196.41
...
29           13467.25
30           14730.57
```

**6.8**

(*Conversions between Celsius and Fahrenheit*) Write a class that contains the following two methods:

```java
/** Convert from Celsius to Fahrenheit */
public static double celsiusToFahrenheit(double celsius)

/** Convert from Fahrenheit to Celsius */
public static double fahrenheitToCelsius(double fahrenheit)
```

<!-- LI p.238 -->

The formula for the conversion is as follows:

```text
fahrenheit = (9.0 / 5) * celsius + 32
celsius = (5.0 / 9) * (fahrenheit – 32)
```

Write a test program that invokes these methods to display the following table:

```text
Celsius
          Fahrenheit
                      |
                            Fahrenheit
                                          Celsius
40.0
          104.0
                      |
                            120.0
                                          48.89
39.0
          102.2
                      |
                            110.0
                                          43.33
38.0
          100.4
                      |
                            100.0
                                          37.78
37.0
          98.6
                      |
                            90.0
                                          32.22
36.0
          96.8
                      |
                            80.0
                                          26.67
35.0
          95.0
                      |
                            70.0
                                          21.11
34.0
          93.2
                      |
                            60.0
                                          21.11
33.0
          91.4
                      |
                            50.0
                                          10.00
32.0
          89.6
                      |
                            40.0
                                          4.44
31.0
          87.8
                      |
                            30.0
                                          –1.11
```

**6.9**

(*Conversions between feet and meters*) Write a class that contains the following two methods:

```java
/** Convert from feet to meters */
public static double footToMeter(double foot)

/** Convert from meters to feet */
public static double meterToFoot(double meter)
```

The formula for the conversion is:

```text
meter = 0.305 * foot
foot = 3.279 * meter
```

Write a test program that invokes these methods to display the following tables:

```text
Feet
          Meters
                      |
                            Meters
                                          Feet
1.0
          0.305
                      |
                            20.0
                                          65.574
2.0
          0.610
                      |
                            25.0
                                          81.967
3.0
          0.915
                      |
                            30.0
                                          98.361
4.0
          1.220
                      |
                            35.0
                                          114.754
5.0
          1.525
                      |
                            40.0
                                          131.148
6.0
          1.830
                      |
                            45.0
                                          147.541
7.0
          2.135
                      |
                            50.0
                                          163.934
8.0
          2.440
                      |
                            55.0
                                          180.328
9.0
          2.745
                      |
                            60.0
                                          196.721
10.0
          3.050
                      |
                            65.0
                                          213.115
```

**6.10**

(*Use the* `isPrime` *Method*) Listing 6.7, PrimeNumberMethod.java, provides the `isPrime(int number)` method for testing whether a number is prime. Use this method to find the number of prime numbers less than `10000`.

<!-- LI p.239 -->

**6.11**

(*Financial application: compute commissions*) Write a method that computes the commission, using the scheme in Programming Exercise 5.39. The header of the method is as follows:

```java
public static double computeCommission(double salesAmount)
```

Write a test program that displays the following table:

```text
Sales Amount
                   Commission
10000
                   900.0
15000
                   1500.0
20000
                   2100.0
25000
                   2700.0
30000
                   3300.0
35000
                   3900.0
40000
                   4500.0
45000
                   5100.0
50000
                   5700.0
55000
                   6300.0
60000
                   6900.0
65000
                   7500.0
70000
                   8100.0
75000
                   8700.0
80000
                   9300.0
85000
                   9900.0
90000
                   10500.0
95000
                   11100.0
100000
                   11700.0
```

**6.12**

(*Display characters*) Write a method that prints characters using the following header:

```java
public static void printChars(char ch1, char ch2, int
  numberPerLine)
```

This method prints the characters between `ch1` and `ch2` with the specified numbers per line. Write a test program that prints 10 characters per line from `1` to `Z`. Characters are separated by exactly one space.

***6.13**

(*Sum series*) Write a method to compute the following summation:

*m*(*i*) = 1 2 + 2 *i* 3 + g + *i* + 1

Write a test program that displays the following table:

```text
i
                    m(i)
1
                    0.5000
2
                    1.1667
3
                    1.9167
i
                    m(i)
4
                    2.7167
5
                    3.5500
6
                    4.4071
7
                    5.2821
8
                    6.1710
9
                    7.0710
10
                    7.9801
11
                    8.8968
12
                    9.8199
13
                    10.7484
14
                    11.6818
15
                    12.6193
16
                    13.5604
17
                    14.5049
18
                    15.4523
19
                    16.4023
20
                    17.3546
```

<!-- LI p.240 -->

***6.14**

(*Estimate* π) π can be computed using the following summation:

*m*(*i*) = 4a1 - 1 2*i* - 1 b 11 + g + (-1)*i*+1 3 + 1 5 - 1 7 + 1 9 - 1

**VideoNote**

> Estimate π

Write a method that returns `m(i)` for a given `i` and write a test program that displays the following table:

```text
i
                    m(i)
1
                    4.0000
101
                    3.1515
201
                    3.1466
301
                    3.1449
401
                    3.1441
501
                    3.1436
601
                    3.1433
701
                    3.1430
801
                    3.1428
901
                    3.1427
```

***6.15**

(*Financial application: print a tax table*) Listing 3.5 gives a program to compute tax. Write a method for computing tax using the following header:

```java
public static double computeTax(int status, double
  taxableIncome)
```

Use this method to write a program that prints a tax table for taxable income from $50,000 to $60,000 with intervals of $50 for all the following statuses:

<!-- LI p.241 -->

```text
Taxable
         Single
                  Married Joint
                                 Married
                                            Head of
Income
                  or Qualifying
                                 Separate
                                            House hold
                  Widow(er)
50000
         8688
                  6665
                                 8688
                                            7353
50050
         8700
                  6673
                                 8700
                                            7365
50100
         8712
                  6680
                                 8712
                                            7378
50150
         8725
                  6688
                                 8725
                                            7390
. . .
59850
         11150
                  8142
                                 11150
                                            9815
59900
         11162
                  8150
                                 11162
                                            9828
59950
         11175
                  8158
                                 11175
                                            9840
60000
         11188
                  8165
                                 11188
                                            9853
```

*Hint:* round the tax into integers using `Math.round` (i.e., `Math .round(computeTax(status, taxableIncome))`).

***6.16**

(*Number of days in a year*) Write a method that returns the number of days in a year using the following header:

```java
public static int numberOfDaysInAYear(int year)
```

Write a test program that displays the number of days in year from 2000 to 2020.

**Sections 6.10 and 6.11**

***6.17**

(*Display matrix of 0s and 1s*) Write a method that displays an *n*-by-*n* matrix using the following header: Here is a sample run:

```java
public static int printMatrix(int year)
```

that prompts the user to enter `n` and displays an *n*-by-*n* matrix. Here is a sample run:

```text
Enter n: 3
0 1 0
0 0 0
1 1 1
```

```java
public static void printMatrix(int n)
```

Each element is 0 or 1, which is generated randomly. Write a test program that prompts the user to enter `n` and displays an *n*-by-*n* matrix.

****6.18**

(*Check password*) Some Websites impose certain rules for passwords. Write a method that checks whether a string is a valid password. Suppose the password rules are as follows:

- A password must have at least eight characters.
- A password must contain only letters and digits.
- A password must contain at least two digits.

Write a program that prompts the user to enter a password and displays `Valid Password` if the rules are followed, or `Invalid Password` otherwise.

<!-- LI p.242 -->

***6.19**

(*Triangles*) Implement the following two methods:

```java
/** Return true if the sum of every two sides is
 * greater than the third side. */
public static boolean isValid(
  double side1, double side2, double side3)
/** Return the area of the triangle. */
public static double area(
  double side1, double side2, double side3)
```

Write a test program that reads three sides for a triangle and uses the `isValid` method to test if the input is valid and uses the `area` method to obtain the area. The program displays the area if the input is valid. Otherwise, it displays that the input is invalid. The formula for computing the area of a triangle is given in Programming Exercise 2.19.

***6.20**

(*Count the letters in a string*) Write a method that counts the number of letters in a string using the following header:

```java
public static int countLetters(String s)
```

Write a test program that prompts the user to enter a string and displays the number of letters in the string.

***6.21**

(*Phone keypads*) The international standard letter/number mapping for tele-phones is given in Programming Exercise 4.15. Write a method that returns a number, given an uppercase letter, as follows:

```java
public static int getNumber(char uppercaseLetter)
```

Write a test program that prompts the user to enter a phone number as a string. The input number may contain letters. The program translates a letter (uppercase or lowercase) to a digit and leaves all other characters intact. Here are sample runs of the program:

```text
Enter a string: 1-800-Flowers
1-800-3569377
```

```text
Enter a string: 1800flowers
18003569377
```

****6.22**

(*Math: approximate the square root*) There are several techniques for implementing the `sqrt` method in the `Math` class. One such technique is known as the *Babylonian method.* It approximates the square root of a number, `n`, by repeatedly performing the calculation using the following formula:

```text
nextGuess = (lastGuess + n / lastGuess) / 2
```

When `nextGuess` and `lastGuess` are almost identical, `nextGuess` is the approximated square root. The initial guess can be any positive value (e.g., `1`). This value will be the starting value for `lastGuess`. If the difference between `nextGuess` and `lastGuess` is less than a very small number, such as `0.0001`, you can claim that `nextGuess` is the approximated square root of `n`. If not, `nextGuess` becomes `lastGuess` and the approximation process continues. Implement the following method that returns the square root of `n`:

```java
public static double sqrt(long n)
```

<!-- LI p.243 -->

Write a test program that prompts the user to enter a positive double value and displays its square root.

***6.23**

(*Occurrences of a specified character*) Write a method that finds the number of occurrences of a specified character in a string using the following header:

```java
public static int count(String str, char a)
```

For example, `count("Welcome", 'e')` returns `2`. Write a test program that prompts the user to enter a string followed by a character then displays the number of occurrences of the character in the string.

**Sections 6.10–6.12**

****6.24**

(*Display current date and time*) Listing 2.7, ShowCurrentTime.java, displays the current time. Revise this example to display the current date and time. The calendar example in Listing 6.12, PrintCalendar.java, should give you some ideas on how to find the year, month, and day.

****6.25**

(*Convert milliseconds to hours, minutes, and seconds*) Write a method that converts milliseconds to hours, minutes, and seconds using the following header:

```java
public static String convertMillis(long millis)
```

The method returns a string as *hours:minutes:seconds*. For example, `convertMillis(5500)` returns a string `0:0:5`, `convertMillis(100000)` returns a string `0:1:40`, and `convertMillis(555550000)` returns a string `154:19:10`. Write a test program that prompts the user to enter a long integer for milliseconds and displays a string in the format of hours:minutes:seconds.

**Comprehensive**

****6.26**

(*Palindromic prime*) A *palindromic prime* is a prime number and also palindromic. For example, 131 is a prime and also a palindromic prime, as are 313 and 757. Write a program that displays the first 100 palindromic prime numbers. Display 10 numbers per line, separated by exactly one space, as follows:

```text
2 3 5 7 11 101 131 151 181 191
313 353 373 383 727 757 787 797 919 929
...
```

****6.27**

(*Emirp*) An *emirp* (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime. For example, 17 is a prime and 71 is a prime, so 17 and 71 are emirps. Write a program that displays the first 100 emirps. Display 10 numbers per line, separated by exactly one space, as follows:

```text
13 17 31 37 71 73 79 97 107 113
149 157 167 179 199 311 337 347 359 389
...
```

****6.28**

(*Mersenne prime*) A prime number is called a *Mersenne prime* if it can be written in the form 2*p* - 1 for some positive integer *p*. Write a program that finds all Mersenne primes with *p* … 31 and displays the output as follows:

**p**

**2^p – 1**

```text
2
             3
3
             7
5
             31
...
```

<!-- LI p.244 -->

****6.29**

(*Twin primes*) Twin primes are a pair of prime numbers that differ by 2. For example, 3 and 5 are twin primes, 5 and 7 are twin primes, and 11 and 13 are twin primes. Write a program to find all twin primes less than 1,000. Display the output as follows:

```text
(3, 5)
(5, 7)
...
```

****6.30**

(*Game: craps*) Craps is a popular dice game played in casinos. Write a program to play a variation of the game, as follows: Roll two dice. Each die has six faces representing values 1, 2, . . ., and 6, respectively. Check the sum of the two dice. If the sum is 2, 3, or 12 (called *craps*), you lose; if the sum is 7 or 11 (called *natural*), you win; if the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established. Continue to roll the dice until either a 7 or the same point value is rolled. If 7 is rolled, you lose. Otherwise, you win. Your program acts as a single player. Here are some sample runs.

```text
You rolled 5 + 6 = 11
You win
```

```text
You rolled 1 + 2 = 3
You lose
```

```text
You rolled 4 + 4 = 8
point is 8
You rolled 6 + 2 = 8
You win
```

```text
You rolled 3 + 2 = 5
point is 5
You rolled 2 + 5 = 7
You lose
```

****6.31**

(*Financial: credit card number validation*) Credit card numbers follow certain patterns. A credit card number must have between 13 and 16 digits. It must start with

- 4 for Visa cards
- 5 for Master cards
- 37 for American Express cards
- 6 for Discover cards

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to determine whether a card number is entered correctly, or whether a credit card is scanned correctly by a scanner. Credit card numbers are generated following this validity check, commonly known as the

<!-- LI p.245 -->

*Luhn check* or the *Mod 10 check,* which can be described as follows (for illustration, consider the card number 4388576018402626):

1. Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number.
2. Now add all single-digit numbers from Step 1.

4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

3. Add all digits in the odd places from right to left in the card number.

6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

4. Sum the results from Step 2 and Step 3.

37 + 38 = 75

5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. For example, the number 4388576018402626 is invalid, but the number 4388576018410707 is valid.

Write a program that prompts the user to enter a credit card number as a `long` integer. Display whether the number is valid or invalid. Design your program to use the following methods:

```java
/** Return true if the card number is valid */
public static boolean isValid(long number)

/** Get the result from Step 2 */
public static int sumOfDoubleEvenPlace(long number)

/** Return this number if it is a single digit, otherwise,
 * return the sum of the two digits */
public static int getDigit(int number)

/** Return sum of odd-place digits in number */
public static int sumOfOddPlace(long number)

/** Return true if the number d is a prefix for number */
public static boolean prefixMatched(long number, int d)

/** Return the number of digits in d */
public static int getSize(long d)

/** Return the first k number of digits from number. If the
 * number of digits in number is less than k, return number. */
public static long getPrefix(long number, int k)
```

<!-- LI p.246 -->

(You may also implement this program by reading the input as a string and pro-cessing the string to validate the credit card.)

```text
Enter a credit card number as a long integer:
  4388576018410707
4388576018410707 is valid
```

```text
Enter a credit card number as a long integer:
  4388576018402626
4388576018402626 is invalid
```

****6.32**

(*Game: chance of winning at craps*) Revise Programming Exercise 6.30 to run it 10,000 times and display the number of winning games.

****6.33**

(*Current date and time*) Invoking `System.currentTimeMillis()` returns the elapsed time in milliseconds since midnight of January 1, 1970. Write a program that displays the date and time. Here is a sample run:

```text
Current date and time is May 16, 2012 10:34:23
```

****6.34**

(*Print calendar*) Programming Exercise 3.21 uses Zeller’s congruence to calculate the day of the week. Simplify Listing 6.12, PrintCalendar.java, using Zeller’s algorithm to get the start day of the month.

**6.35**

(*Geometry: area of a pentagon*) The area of a pentagon can be computed using the following formula:

5 × *s*2 4 × tan aπ 5 b *Area* =

Write a method that returns the area of a pentagon using the following header:

```java
public static double area(double side)
```

Write a main method that prompts the user to enter the side of a pentagon and displays its area. Here is a sample run:

```text
Enter the side: 5.5
The area of the pentagon is 52.04444136781625
```

***6.36**

(*Geometry: area of a regular polygon*) A regular polygon is an *n*-sided polygon in which all sides are of the same length and all angles have the same degree (i.e., the polygon is both equilateral and equiangular). The formula for computing the area of a regular polygon is

<!-- LI p.247 -->

*n* × *s*2 4 × tan aπ *n* b *Area* =

Write a method that returns the area of a regular polygon using the following header:

```java
public static double area(int n, double side)
```

Write a main method that prompts the user to enter the number of sides and the side of a regular polygon and displays its area. Here is a sample run:

```text
Enter the number of sides: 5
Enter the side: 6.5
The area of the polygon is 72.69017017488385
```

**6.37**

(*Format an integer*) Write a method with the following header to format the integer with the specified width.

```java
public static String format(int number, int width)
```

The method returns a string for the number with one or more prefix `0`s. The size of the string is the width. For example, `format(34, 4)` returns `0034` and `format(34, 5)` returns `00034`. If the number is longer than the width, the method returns the string representation for the number. For example, `format(34, 1)` returns `34`. Write a test program that prompts the user to enter a number and its width, and displays a string returned by invoking `format(number, width)`.

***6.38**

(*Generate random characters*) Use the methods in `RandomCharacter` in Listing 6.10 to print 100 uppercase letters then 100 single digits, printing 50 per line.

**6.39**

(*Geometry: point position*) Programming Exercise 3.32 shows how to test whether a point is on the left side of a directed line, on the right, or on the same line. Write the methods with the following headers:

```java
/** Return true if point (x2, y2) is on the left side of the
 * directed line from (x0, y0) to (x1, y1) */
public static boolean leftOfTheLine(double x0, double y0,
  double x1, double y1, double x2, double y2)

/** Return true if point (x2, y2) is on the same
 * line from (x0, y0) to (x1, y1) */
public static boolean onTheSameLine(double x0, double y0,
  double x1, double y1, double x2, double y2)

/** Return true if point (x2, y2) is on the
 * line segment from (x0, y0) to (x1, y1) */
public static boolean onTheLineSegment(double x0, double y0,
  double x1, double y1, double x2, double y2)
```

<!-- LI p.248 -->

Write a program that prompts the user to enter the three points for `p0`, `p1`, and `p2` and displays whether `p2` is on the left side of the line from `p0` to `p1`, right side, the same line, or on the line segment. Here are some sample runs:

```text
Enter three points for p0, p1, and p2: 1 1 2 2 1.5 1.5
(1.5, 1.5) is on the line segment from (1.0, 1.0) to (2.0, 2.0)
```

```text
Enter three points for p0, p1, and p2: 1 1 2 2 3 3
(3.0, 3.0) is on the same line from (1.0, 1.0) to (2.0, 2.0)
```

```text
Enter three points for p0, p1, and p2: 1 1 2 2 1 1.5
(1.0, 1.5) is on the left side of the line
  from (1.0, 1.0) to (2.0, 2.0)
```

```text
Enter three points for p0, p1, and p2: 1 1 2 2 1 –1
(1.0, −1.0) is on the right side of the line
  from (1.0, 1.0) to (2.0, 2.0)
```
