---
topic: branching
lessons: "M5_L1, M5_L2"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "80-85"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "3.3, 3.4, 3.5"
generated_by: tools/extract_refs.py
---
# Branching (if/else) and nested branching - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.80 -->

## 3.3 if Statements

*An* `if` *statement is a construct that enables a program to specify alternative paths of execution.*

**Key**

The preceding program displays a message such as “6 + 2 = 7 is false.” If you wish the

**Point**

message to be “6 + 2 = 7 is incorrect,” you have to use a selection statement to make this minor change.

Java has several types of selection statements: one-way `if` statements, two-way `if-else` statements, nested `if` statements, multi-way `if-else` statements, `switch` statements, and conditional operators.

A one-way `if` statement executes an action if and only if the condition is `true`. The syntax for a one-way `if` statement is as follows:

```java
if (boolean-expression) {
  statement(s);
}
```

The flowchart in Figure 3.1a illustrates how Java executes the syntax of an `if` statement. A *flowchart* is a diagram that describes an algorithm or process, showing the steps as boxes of various kinds, and their order by connecting these with arrows. Process operations are represented in these boxes, and the arrows connecting them represent the flow of control. A diamond box denotes a Boolean condition, and a rectangle box represents statements.

```java
 boolean-
              false
                                                           false
                                            (radius >= 0)
expression


                                              true
true

                          area = radius * radius * PI;
                          System.out.println("The area for the circle of"
                            + " radius " + radius + " is " + area);
```

**Figure 3.1** An `if` statement executes statements if the `boolean-expression` evaluates to `true`.

<!-- LI p.81 -->

If the `boolean-expression` evaluates to `true`, the statements in the block are executed. As an example, see the following code:

```java
if (radius >= 0) {
  area = radius * radius * PI;
  System.out.println("The area for the circle of radius " +
    radius + " is " + area);
}
```

The flowchart of the preceding statement is shown in Figure 3.1b. If the value of `radius` is greater than or equal to `0`, then the `area` is computed and the result is displayed; otherwise, the two statements in the block will not be executed.

The `boolean-expression` is enclosed in parentheses. For example, the code in (a) is wrong. It should be corrected, as shown in (b).

```java
if  i > 0  {
                                          if (i > 0) {
  System.out.println("i is positive");
                                            System.out.println("i is positive");
}
                                          }
```

The block braces can be omitted if they enclose a single statement. For example, the following statements are equivalent:

```java
if (i > 0) {
                                                         if (i > 0)
  System.out.println("i is positive");
                                                           System.out.println("i is positive");
}
```

> **Caution** Omitting braces makes the code shorter, but it is prone to errors. It is a common mistake to forget the braces when you go back to modify the code that omits the braces.

Listing 3.2 gives a program that prompts the user to enter an integer. If the number is a multiple of `5`, the program displays `HiFive`. If the number is divisible by `2`, it displays `HiEven`.

**Listing 3.2 SimpleIfDemo.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class SimpleIfDemo {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter an integer: ");
    int number = input.nextInt();

    if (number % 5 == 0)
      System.out.println("HiFive");

    if (number % 2 == 0)
      System.out.println("HiEven");
  }
}
Enter an integer: 4
HiEven
```

<!-- LI p.82 -->

```text
Enter an integer: 30
HiFive
HiEven
```

The program prompts the user to enter an integer (lines 6–7) and displays `HiFive` if it is divisible by `5` (lines 9–10) and `HiEven` if it is divisible by `2` (lines 12–13). **3.3.1** Write an `if` statement that assigns `1` to `x` if `y` is greater than `0`.

**Check**

**3.3.2** Write an `if` statement that increases pay by 3% if `score` is greater than `90`.

**Point**

**3.3.3** What is wrong in the following code?

```java
if radius >= 0
{
  area = radius * radius * PI;
  System.out.println("The area for the circle of " +
    " radius " + radius + " is " + area);
}
```

## 3.4 Two-Way if-else Statements

> **Key Point** An* `if-else` *statement decides the execution path based on whether the condition is

*true or false.*

A one-way `if` statement performs an action if the specified condition is `true`. If the condition is `false`, nothing is done. But what if you want to take alternative actions when the condition is `false`? You can use a two-way `if-else` statement. The actions that a two-way `if-else` statement specifies differ based on whether the condition is `true` or `false`.

Here is the syntax for a two-way `if-else` statement:

```java
if (boolean-expression) {
  statement(s)-for-the-true-case;
}
else {
  statement(s)-for-the-false-case;
}
```

The flowchart of the statement is shown in Figure 3.2.

```text
true
                            false
            boolean-
           expression
```

**Figure 3.2** An `if-else` statement executes statements for the true case if the `boolean-expression` evaluates to `true`; otherwise, statements for the `false` case are executed.

<!-- LI p.83 -->

If the `boolean-expression` evaluates to `true`, the statement(s) for the true case are executed; otherwise, the statement(s) for the `false` case are executed. For example, consider the following code:

```java
if (radius >= 0) {
  area = radius * radius * PI;
  System.out.println("The area for the circle of radius " +
    radius + " is " + area);
}
else {
  System.out.println("Negative input");
}
```

If `radius >= 0` is `true`, `area` is computed and displayed; if it is `false`, the message `"Negative input"` is displayed.

As usual, the braces can be omitted if there is only one statement within them. The braces enclosing the `System.out.println("Negative input")` statement can therefore be omitted in the preceding example.

Here is another example of using the `if-else` statement. The example checks whether a number is even or odd, as follows:

```java
if (number % 2 == 0)
  System.out.println(number + " is even.");
else
  System.out.println(number + " is odd.");
```

**3.4.1**

Write an `if` statement that increases `pay` by 3% if `score` is greater than `90`, oth-

**Check**

erwise increases `pay` by 1%.

**Point**

**3.4.2** What is the output of the code in (a) and (b) if `number` is `30`? What if `number` is `35`?

```java
if
   (number % 2 == 0)
                                if
                                   (number % 2 == 0)
  System.out.println(number
                                  System.out.println(number
    + "is even.");
                                    + "is even.");
                                else
System.out.println(number
                                System.out.println(number
    + "is odd");
                                    + "is odd");
```

## 3.5 Nested if and Multi-Way if-else Statements

> **Key Point** An* `if` *statement can be inside another* `if` *statement to form a nested* `if` *statement.

The statement in an `if` or `if-else` statement can be any legal Java statement, including another `if` or `if-else` statement. The inner `if` statement is said to be *nested* inside the outer `if` statement. The inner `if` statement can contain another `if` statement; in fact, there is no limit to the depth of the nesting. For example, the following is a nested `if` statement:

```java
if (i > k) {
  if (j > k)
    System.out.println("i and j are greater than k");
}
else
  System.out.println("i is less than or equal to k");
```

The `if (j > k)` statement is nested inside the `if (i > k)` statement.

The nested `if` statement can be used to implement multiple alternatives. The statement given in Figure 3.3a, for instance, prints a letter grade according to the score, with multiple alternatives.

<!-- LI p.84 -->

```java
if (score >= 90)
                                                if (score >= 90)
  System.out.print("A");
                                                  System.out.print("A");
else
                                                else if (score >= 80)
  if (score >= 80)
                                                  System.out.print("B");
    System.out.print("B");
                                                else if (score >= 70)
  else
                                                  System.out.print("C");
    if (score >= 70)
                                                else if (score >= 60)
      System.out.print("C");
                                                  System.out.print("D");
    else
                                                else
      if (score >= 60)
                                                  System.out.print("F");
        System.out.print("D");
      else
        System.out.print("F");
```

**Figure 3.3** A preferred format for multiple alternatives is shown in (b) using a multi-way `if-else` statement.

The execution of this `if` statement proceeds as shown in Figure 3.4. The first condition `(score >= 90)` is tested. If it is `true`, the grade is `A`. If it is `false`, the second condition `(score >= 80)` is tested. If the second condition is `true`, the grade is `B`. If that condition is `false`, the third condition and the rest of the conditions (if necessary) are tested until a condition is met or all of the conditions prove to be `false`. If all of the conditions are `false`, the grade is `F`. Note a condition is tested only when all of the conditions that come before it are `false`.

```text
(score >= 90)


               (score >= 80)

 grade is A
                             (score >= 70)

                grade is B
                                            (score >= 60)

                               grade is C


                                             grade is D

                                                            grade is F
```

**Figure 3.4** You can use a multi-way `if-else` statement to assign a grade.

<!-- LI p.85 -->

The `if` statement in Figure 3.3a is equivalent to the `if` statement in Figure 3.3b. In fact, Figure 3.3b is the preferred coding style for multiple alternative `if` statements. This style, called *multi-way* `if-else` *statements*, avoids deep indentation and makes the program easy to read.

**3.5.1**

Suppose `x = 3` and `y = 2`; show the output, if any, of the following code. What

**Check**

is the output if `x = 3` and `y = 4`? What is the output if `x = 2` and `y = 2`? Draw

**Point**

a flowchart of the code.

```java
if (x > 2) {
  if (y > 2) {
    z = x + y;
    System.out.println("z is " + z);
  }
}
else
  System.out.println("x is " + x);
```

**3.5.2** Suppose `x = 2` and `y = 3`. Show the output, if any, of the following code. What is

the output if `x = 3` and `y = 2`? What is the output if `x = 3` and `y = 3`?

```java
if (x > 2)
  if (y > 2) {
    int z = x + y;
      System.out.println("z is " + z);
  }
else
  System.out.println("x is " + x);
```

**3.5.3** What is wrong in the following code?

```java
if (score >= 60)
  System.out.println("D");
else if (score >= 70)
  System.out.println("C");
else if (score >= 80)
  System.out.println("B");
else if (score >= 90)
  System.out.println("A");
else
  System.out.println("F");
```
