---
topic: nested_loops_break
lessons: "M7"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "178-189"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "5.9, 5.12"
generated_by: tools/extract_refs.py
---
# Nested loops, break, continue - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.178 -->

## 5.9 Nested Loops

*A loop can be nested inside another loop.*

*Nested loops* consist of an outer loop and one or more inner loops. Each time the outer loop is

**Key Point**

repeated, the inner loops are reentered, and started anew.

Listing 5.7 presents a program that uses nested `for` loops to display a multiplication table.

**Listing 5.7 MultiplicationTable.java** *(line N of the listing = Nth line of the block)*

```java
public class MultiplicationTable {
  /** Main method */
  public static void main(String[] args) {
    // Display the table heading
    System.out.println("         Multiplication Table");

    // Display the number title
    System.out.print("   ");
    for (int j = 1; j <= 9; j++)
      System.out.print("   " + j);

     System.out.println("\n — — — — — — — — — — —— — — — — — — — —");

    // Display table body
    for (int i = 1; i <= 9; i++) {
      System.out.print(i + " | ");
      for (int j = 1; j <= 9; j++) {
        // Display the product and align properly
        System.out.printf("%4d", i * j);
      }
      System.out.println();
    }
  }
}
```

<!-- LI p.179 -->

```text
Multiplication Table
      1
          2
              3
                  4
                     5
                         6
                             7
                                 8
                                    9

1 |
      1
          2
              3
                  4
                     5
                         6
                             7
                                 8
                                    9
2 |
      2
          4
              6
                  8
                    10
                        12
                            14
                                16
                                   18
3 |
      3
          6
              9
                 12
                    15
                        18
                            21
                                24
                                   27
4 |
      4
          8
             12
                 16
                    20
                        24
                            28
                                32
                                   36
5 |
      5
         10
             15
                 20
                    25
                        30
                            35
                                40
                                   45
6 |
      6
         12
             18
                 24
                    30
                        36
                            42
                                48
                                   54
7 |
     7
         14
             21
                 28
                    35
                        42
                            49
                                56
                                   63
8 |
     8
         16
             24
                 32
                    40
                        48
                            56
                                64
                                   72
9 |
     9
         18
             27
                 36
                    45
                        54
                            63
                                72
                                   81
```

The program displays a title (line 5) on the first line in the output. The first `for` loop (lines 9 and 10) displays the numbers `1–9` on the second line. A dashed (–) line is displayed on the third line (line 12).

The next loop (lines 15–22) is a nested `for` loop with the control variable `i` in the outer loop and `j` in the inner loop. For each `i`, the product `i * j` is displayed on a line in the inner loop, with `j` being `1`, `2`, `3`, …, `9`.

> **Note** Be aware that a nested loop may take a long time to run. Consider the following loop nested in three levels:

```java
for (int i = 0; i < 10000; i++)
  for (int j = 0; j < 10000; j++)
    for (int k = 0; k < 10000; k++)
      Perform an action
```

> The action is performed one trillion times. If it takes 1 microsecond to perform the action, the total time to run the loop would be more than 277 hours. Note 1 microsecond is one-millionth (10-6) of a second.

**5.9.1** How many times is the `println` statement executed?

**Check Point**

```java
for (int i = 0; i < 10; i++)
  for (int j = 0; j < i; j++)
    System.out.println(i * j)
```

<!-- LI p.180 -->

**5.9.2** Show the output of the following programs. (*Hint*: Draw a table and list the vari-

ables in the columns to trace these programs.)

```java
public class Test {
                                                public class Test {
  public static void main(String[] args) {
                                                  public static void main(String[] args) {
    for (int i = 1; i < 5; i++) {
                                                    int i = 0;
      int j = 0;
                                                    while (i < 5) {
      while (j < i) {
                                                      for (int j = i; j > 1; j––)
        System.out.print(j + " ");
                                                        System.out.print(j + " ");
        j++;
                                                      System.out.println("****");
      }
                                                      i++;
    }
                                                    }
  }
                                                  }
}
                                                }
```

```java
public class Test {
                                                public class Test {
  public static void main(String[] args) {
                                                  public static void main(String[] args) {
    int i = 5;
                                                    int i = 1;
    while (i >= 1) {
                                                    do {
      int num = 1;
                                                      int num = 1;
      for (int j = 1; j <= i; j++) {
                                                      for (int j = 1; j <= i; j++) {
        System.out.print(num + "xxx");
                                                        System.out.print(num + "G");
        num *= 2;
                                                        num += 2;
      }
                                                      }

      System.out.println();
                                                      System.out.println();
      i--;
                                                      i++;
    }
                                                    } while (i <= 5);
  }
                                                  }
}
                                                }
```

<!-- LI p.186 -->

## 5.12 Keywords break and continue

> **Key Point** The* `break` *and* `continue` *keywords provide additional controls in a loop.

> **Pedagogical Note** Two keywords, `break` and `continue`, can be used in loop statements to provide additional controls. Using `break` and `continue` can simplify programming in some cases. Overusing or improperly using them, however, can make programs difficult to read and debug. (*Note to instructors*: You may skip this section without affecting students’ understanding of the rest of the book.)

You have used the keyword `break` in a `switch` statement. You can also use `break` in a loop to immediately terminate the loop. Listing 5.12 presents a program to demonstrate the effect of using `break` in a loop.

**Listing 5.12 TestBreak.java** *(line N of the listing = Nth line of the block)*

```java
public class TestBreak {
  public static void main(String[] args) {
    int sum = 0;
    int number = 0;

    while (number < 20) {
      number++;
      sum += number;
      if (sum >= 100)
        break;
    }

    System.out.println("The number is " + number);
    System.out.println("The sum is " + sum);
  }
}
```

```text
The number is 14
The sum is 105
```

<!-- LI p.187 -->

The program in Listing 5.12 adds integers from `1` to `20` in this order to `sum` until `sum` is greater than or equal to `100`. Without the `if` statement (line 9), the program calculates the sum of the numbers from `1` to `20`. However, with the `if` statement, the loop terminates when `sum` becomes greater than or equal to `100`. Without the `if` statement, the output would be as follows:

```text
The number is 20
The sum is 210
```

You can also use the `continue` keyword in a loop. When it is encountered, it ends the current iteration and program control goes to the end of the loop body. In other words, `continue` breaks out of an iteration, while the `break` keyword breaks out of a loop. Listing 5.13 presents a program to demonstrate the effect of using `continue` in a loop.

**Listing 5.13 TestContinue.java** *(line N of the listing = Nth line of the block)*

```java
public class TestContinue {
  public static void main(String[] args) {
    int sum = 0;
    int number = 0;

    while (number < 20) {
      number++;
      if (number == 10 || number == 11)
        continue;
      sum += number;
    }

    System.out.println("The sum is " + sum);
  }
}


 The sum is 189
```

The program in Listing 5.13 adds integers from `1` to `20` except `10` and `11` to `sum`. With the `if` statement in the program (line 8), the `continue` statement is executed when `number` becomes `10` or `11`. The `continue` statement ends the current iteration so that the rest of the statement in the loop body is not executed; therefore, `number` is not added to `sum` when it is `10` or `11`. Without the `if` statement in the program, the output would be as follows:

```text
The sum is 210
```

In this case, all of the numbers are added to `sum`, even when `number` is `10` or `11`. Therefore, the result is `210`, which is `21` more than it was with the `if` statement.

> **Note** The `continue` statement is always inside a loop. In the `while` and `do-while` loops, the `loop-continuation-condition` is evaluated immediately after the `continue` statement. In the `for` loop, the `action-after-each-iteration` is performed, then the `loop-continuation-condition` is evaluated immediately after the `continue` statement.

<!-- LI p.188 -->

> **Note** Some programming languages have a `goto` statement. The `goto` statement indiscriminately transfers control to any statement in the program and executes it. This makes your program vulnerable to errors. The `break` and `continue` statements in Java are different from `goto` statements. They operate only in a loop or a `switch` statement. The `break` statement breaks out of the loop, and the `continue` statement breaks out of the current iteration in the loop.

You can always write a program without using `break` or `continue` in a loop (see CheckPoint Question 5.12.3). In general, though, using `break` and `continue` is appropriate if it simplifies coding and makes programs easier to read. Suppose you need to write a program to find the smallest factor other than `1` for an integer `n` (assume `n >= 2`). You can write a simple and intuitive code using the `break` statement as follows:

```java
int factor = 2;
while (factor <= n) {
  if (n % factor == 0)
    break;
  factor++;
}
System.out.println("The smallest factor other than 1 for "
  + n + " is " + factor);
```

You may rewrite the code without using `break` as follows:

```java
boolean found = false;
int factor = 2;
while (factor <= n && !found) {
  if (n % factor == 0)
    found = true;
  else
    factor++;
}
System.out.println("The smallest factor other than 1 for "
  + n + " is " + factor);
```

Obviously, the `break` statement makes this program simpler and easier to read in this case. However, you should use `break` and `continue` with caution. Too many `break` and `continue` statements will produce a loop with many exit points and make the program difficult to read.

> **Note** Programming is a creative endeavor. There are many different ways to write code. In fact, you can find a smallest factor using a rather simple code as follows:

```java
int factor = 2;
while (n % factor != 0)
  factor++;
or
for (int factor = 2; n % factor != 0; factor++);
```

> The code here finds the smallest factor for an integer `n`. Programming Exercise 5.16 writes a program that finds all smallest factors in `n`.

**5.12.1** What is the keyword `break` for? What is the keyword `continue` for? Will the fol-

**Check**

lowing programs terminate? If so, give the output.

**Point**

<!-- LI p.189 -->

```java
int balance = 10;
                                      int balance = 10;
while (true) {
                                      while (true) {
  if (balance < 9)
                                        if (balance < 9)
    break;
                                          continue;
  balance = balance – 9;
                                        balance = balance – 9;
}
                                      }

System.out.println("Balance is "
                                      System.out.println("Balance is "
  + balance);
                                        + balance);
```

**5.12.2** The `for` loop on the left is converted into the `while` loop on the right. What is

wrong? Correct it.

```java
int sum = 0;
                                              int i = 0, sum = 0;
for (int i = 0; i < 4; i++) {
                                              while (i < 4) {
  if (i % 3 == 0) continue;
                                                if (i % 3 == 0) continue;
  sum += i;
                                                sum += i;
}
                                                i++;
                                              }
```

**5.12.3** Rewrite the programs `TestBreak` and `TestContinue` in Listings 5.12 and 5.13

without using `break` and `continue`. **5.12.4** After the `break` statement in (a) is executed in the following loop, which statement

is executed? Show the output. After the `continue` statement in (b) is executed in the following loop, which statement is executed? Show the output.

```java
for (int i = 1; i < 4; i++) {
                                    for (int i = 1; i < 4; i++) {
  for (int j = 1; j < 4; j++) {
                                      for (int j = 1; j < 4; j++) {
    if (i * j > 2)
                                        if (i * j > 2)
      break;
                                          continue;

    System.out.println(i * j);
                                        System.out.println(i * j);
  }
                                      }

  System.out.println(i);
                                      System.out.println(i);
}
                                    }
```
