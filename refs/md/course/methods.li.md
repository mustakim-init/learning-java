---
topic: methods
lessons: "M10"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "206-225"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "6.1-6.7, 6.9"
generated_by: tools/extract_refs.py
---
# Methods - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

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

<!-- LI p.224 -->

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
