---
topic: loops
lessons: "M6_L1, M6_L2"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "160-176"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "5.1, 5.2, 5.4, 5.6, 5.7"
generated_by: tools/extract_refs.py
---
# Loops (while, for) - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.160 -->

## 5.1 Introduction

*A loop can be used to tell a program to execute statements repeatedly.*

Suppose you need to display a string (e.g., `Welcome to Java!`) a hundred times. It would

**Key Point**

be tedious to have to write the following statement a hundred times:

```java
System.out.println("Programming is fun");
System.out.println("Programming is fun");
...
System.out.println("Programming is fun");
```

So, how do you solve this problem?

Java provides a powerful construct called a *loop* that controls how many times an operation or a sequence of operations is performed in succession. Using a loop statement, you can simply tell the computer to display a string a hundred times without having to code the print statement a hundred times, as follows:

```java
int count = 0;
while (count < 100) {
  System.out.println("Welcome to Java!");
  count++;
}
```

The variable `count` is initially `0`. The loop checks whether `count < 100` is `true`. If so, it executes the loop body to display the message `Welcome to Java!` and increments `count` by `1`. It repeatedly executes the loop body until `count < 100` becomes `false`. When `count < 100` is `false` (i.e., when `count` reaches `100`), the loop terminates, and the next statement after the loop statement is executed.

*Loops* are constructs that control repeated executions of a block of statements. The concept of looping is fundamental to programming. Java provides three types of loop statements: `while` loops, `do-while` loops, and `for` loops.

## 5.2 The while Loop

*A* `while` *loop executes statements repeatedly while the condition is true.*

The syntax for the `while` loop is as follows:

**Key Point**

```java
while (loop-continuation-condition) {
  // Loop body
  Statement(s);
}
```

**VideoNote**

Figure 5.1a shows the `while` loop flowchart. The part of the loop that contains the statements

> Use while loop loop body

to be repeated is called the *loop body*. A one-time execution of a loop body is referred to as an

*iteration* (or *repetition) of the loop.* Each loop contains a `loop-continuation-condition`,

> iteration

a Boolean expression that controls the execution of the body. It is evaluated each time to determine if the loop body is executed. If its evaluation is `true`, the loop body is executed; if its evaluation is `false`, the entire loop terminates and the program control turns to the statement that follows the `while` loop.

> loop-continuation-condition

The loop for displaying `Welcome to Java!` a hundred times introduced in the preceding section is an example of a `while` loop. Its flowchart is shown in Figure 5.1b.

<!-- LI p.161 -->

```java
int count = 0;
```

```text
    loop-
continuation-
                                         (count < 100)?
 condition?
```

```java
System.out.println("Welcome to Java!");
count++;
```

**Figure 5.1** The `while` loop repeatedly executes the statements in the loop body when the `loop-continuation-condition` evaluates to `true`.

The `loop-continuation-condition` is `count < 100` and the loop body contains two statements in the following code:

```java
int count = 0;
while (count < 100) {
  System.out.printIn("Welcome to Java!");
  count++;
}
```

In this example, you know exactly how many times the loop body needs to be executed because the control variable `count` is used to count the number of iterations. This type of loop is known as a *counter-controlled loop.*

> **Note** The `loop-continuation-condition` must always appear inside the parentheses. The braces enclosing the loop body can be omitted only if the loop body contains one or no statement.

Here is another example to help understand how a loop works.

```java
int sum = 0, i = 1;
while (i < 10) {
  sum = sum + i;
  i++;
}
System.out.println("sum is " + sum); // sum is 45
```

If `i < 10` is `true`, the program adds `i` to `sum`. Variable `i` is initially set to `1`, then is incremented to `2`, `3`, and up to `10`. When `i` is `10`, `i < 10` is `false`, so the loop exits. Therefore, the sum is `1 + 2 + 3 + ... + 9 = 45`.

<!-- LI p.162 -->

What happens if the loop is mistakenly written as follows?

```java
int sum = 0, i = 1;
while (i < 10) {
  sum = sum + i;
}
```

This loop is infinite, because `i` is always `1` and `i < 10` will always be `true`.

> **Note** Make sure that the `loop-continuation-condition` eventually becomes `false` so that the loop will terminate. A common programming error involves *infinite loops* (i.e., the loop runs forever). If your program takes an unusually long time to run and does not stop, it may have an infinite loop. If you are running the program from the command window, press *CTRL*+*C* to stop it.

> **Caution** Programmers often make the mistake of executing a loop one more or less time. This is commonly known as the *off-by-one error*. For example, the following loop displays `Welcome to Java` 101 times rather than 100 times. The error lies in the condition, which should be `count < 100` rather than `count <= 100`.

```java
int count = 0;
while (count <= 100) {
  System.out.println("Welcome to Java!");
  count++;
}
```

Recall that Listing 3.1, AdditionQuiz.java, gives a program that prompts the user to enter an answer for a question on addition of two single digits. Using a loop, you can now rewrite the program to let the user repeatedly enter a new answer until it is correct, as given in Listing 5.1.

**Listing 5.1 RepeatAdditionQuiz.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class RepeatAdditionQuiz {
  public static void main(String[] args) {
    int number1 = (int)(Math.random() * 10);
    int number2 = (int)(Math.random() * 10);

    // Create a Scanner
    Scanner input = new Scanner(System.in);

    System.out.print(
      "What is " + number1 + " + " + number2 + "? ");
    int answer = input.nextInt();

    while (number1 + number2 != answer)  {
      System.out.print("Wrong answer. Try again. What is "
        + number1 + " + " + number2 + "? ");
      answer = input.nextInt();
    }

    System.out.println("You got it!");
  }
}

 What is 5 + 9? 12
 Wrong answer. Try again. What is 5 + 9? 34
 Wrong answer. Try again. What is 5 + 9? 14
 You got it!
```

<!-- LI p.163 -->

The loop in lines 15–19 repeatedly prompts the user to enter an `answer` when `number1 + number2 != answer` is `true`. Once `number1 + number2 != answer` is `false`, the loop exits.

**5.2.1** Analyze the following code. Is `count < 100` always `true`, always `false`, or

**Check**

sometimes `true` or sometimes `false` at Point A, Point B, and Point C?

**Point**

```java
int count = 0;
while (count < 100) {
  // Point A
  System.out.println("Welcome to Java!");
  count++;
  // Point B
}
// Point C
```

**5.2.2** How many times are the following loop bodies repeated? What is the output of each

loop?

```java
int i = 1;
                                  int i = 1;
                                                                     int i = 1;
while (i < 10)
                                  while (i < 10)
                                                                     while (i < 10)
  if (i % 2 == 0)
                                    if (i % 2 == 0)
                                                                       if ((i++) % 2 == 0)
    System.out.println(i);
                                      System.out.println(i++);
                                                                         System.out.println(i);
```

**5.2.3** What is the output of the following code? Explain the reason.

```java
int x = 80000000;

while (x > 0)
  x++;

System.out.println("x is " + x);
```

<!-- LI p.166 -->

## 5.4 Loop Design Strategies

> **Key Point** The key to designing a loop is to identify the code that needs to be repeated and write a condition for terminating the loop.

Writing a correct loop is not an easy task for novice programmers. Consider three steps when writing a loop.

Step 1: Identify the statements that need to be repeated.

Step 2: Wrap these statements in a loop as follows:

```java
while (true) {
  Statements;
}
```

Step 3: Code the `loop-continuation-condition` and add appropriate statements for controlling the loop.

```java
while (loop-continuation-condition) {
  Statements;
  Additional statements for controlling the loop;
}
```

The Math subtraction learning tool program in Listing 3.3, SubtractionQuiz.java, generates just one question for each run. You can use a loop to generate questions repeatedly. How

**VideoNote**

do you write the code to generate five questions? Follow the loop design strategy. First,

> Multiple subtraction quiz

identify the statements that need to be repeated. These are the statements for obtaining two random numbers, prompting the user with a subtraction question, and grading the question. Second, wrap the statements in a loop. Third, add a loop control variable and the `loop- continuation-condition` to execute the loop five times.

Listing 5.4 gives a program that generates five questions and, after a student answers all five, reports the number of correct answers. The program also displays the time spent on the test and lists all the questions.

**Listing 5.4 SubtractionQuizLoop.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class SubtractionQuizLoop {
  public static void main(String[] args) {
    final int NUMBER_OF_QUESTIONS = 5; // Number of questions
    int correctCount = 0; // Count the number of correct answers
    int count = 0; // Count the number of questions
    long startTime = System.currentTimeMillis();
    String output = " "; // output string is initially empty
    Scanner input = new Scanner(System.in);

    while (count < NUMBER_OF_QUESTIONS) {
      // 1. Generate two random single-digit integers
      int number1 = (int)(Math.random() * 10);
      int number2 = (int)(Math.random() * 10);

      // 2. If number1 < number2, swap number1 with number2
      if (number1 < number2) {
        int temp = number1;
        number1 = number2;
        number2 = temp;
      }

      // 3. Prompt the student to answer "What is number1 – number2?"
      System.out.print(
        "What is " + number1 + " – " + number2 + "? ");
      int answer = input.nextInt();

      // 4. Grade the answer and display the result
      if (number1 – number2 == answer) {
        System.out.println("You are correct!");
        correctCount++; // Increase the correct answer count
      }
      else
        System.out.println("Your answer is wrong.\n" + number1
          + " – " + number2 + " should be " + (number1 — number2));

      // Increase the question count
      count++;

      output += "\n" + number1 + "–" + number2 + "=" + answer +
        ((number1 – number2 == answer) ? " correct": " wrong");
    }

    long endTime = System.currentTimeMillis();
    long testTime = endTime – startTime;

    System.out.println("Correct count is " + correctCount +
      "\nTest time is " + testTime / 1000 + " seconds\n" + output);
  }
}

 What is 9 – 2?  7
 You are correct!

 What is 3 – 0?  3
 You are correct!

 What is 3 – 2?  1
 You are correct!

 What is 7 – 4?  4
 Your answer is wrong.
 7 – 4 should be 3

 What is 7 – 5?  4
 Your answer is wrong.
 7 – 5 should be 2

 Correct count is 3
 Test time is 1021 seconds

 9–2=7 correct
 3–0=3 correct
 3–2=1 correct
 7–4=4 wrong
 7–5=4 wrong
```

<!-- LI p.168 -->

The program uses the control variable `count` to control the execution of the loop. `count` is initially `0` (line 7) and is increased by `1` in each iteration (line 39). A subtraction question is displayed and processed in each iteration. The program obtains the time before the test starts in line 8 and the time after the test ends in line 45, then computes the test time in line 46. The test time is in milliseconds and is converted to seconds in line 49.

**5.4.1** Revise the code using the `System.nanoTime()` to measure the time in nano seconds.

**Check Point**

<!-- LI p.171 -->

## 5.6 The do-while Loop

*A* `do-while` *loop is the same as a* `while` *loop except that it executes the loop body first then checks the loop continuation condition.*

**Key**

The `do-while` *loop* is a variation of the `while` loop. Its syntax is as follows:

**Point**

```java
do {
  // Loop body;
```

**VideoNote**

```java
  Statement(s);
} while (loop-continuation-condition);
```

> Use do-while loop do-while loop

Its execution flowchart is shown in Figure 5.2a. The loop body is executed first, then the `loop-continuation-condition` is evaluated. If the evaluation is `true`, the loop body is executed again; if it is `false`, the `do-while` loop terminates. For example, the following `while` loop statement

```java
int count = 0;
while (count < 100) {
  System.out.println("Welcome to Java!");
  count++;
}
```

can be written using a `do-while` loop as follows:

```java
int count = 0;
do {
  System.out.println("Welcome to Java!");
  count++;
} while (count < 100);
```

The flowchart of this `do-while` loop is shown in Figure 5.2b.

The difference between a `while` loop and a `do-while` loop is the order in which the `loop-continuation-condition` is evaluated and the loop body is executed. In the case of a `do-while` loop, the loop body is executed at least once. You can write a loop using either the `while` loop or the `do-while` loop. Sometimes one is a more convenient choice than the other. For example, you can rewrite the `while` loop in Listing 5.5 using a `do-while` loop, as given in Listing 5.6.

```java
int count = 0;
```

```java
System.out.println("Welcome to Java!");
count++;
```

```text
(count < 100)?
```

**Figure 5.2** The `do-while` loop executes the loop body first then checks the `loop- continuation-condition` to determine whether to continue or terminate the loop.

<!-- LI p.172 -->

**Listing 5.6 TestDoWhile.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class TestDoWhile {
  /** Main method */
  public static void main(String[] args) {
    int data;
    int sum = 0;

    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Keep reading data until the input is 0
    do {
      // Read the next data
      System.out.print(
        "Enter an integer (the input ends if it is 0): ");
      data = input.nextInt();

      sum += data;
    } while (data != 0);

    System.out.println("The sum is " + sum);
  }
}
```

```text
Enter an integer (the input ends if it is 0): 3
Enter an integer (the input ends if it is 0): 5
Enter an integer (the input ends if it is 0): 6
Enter an integer (the input ends if it is 0): 0
The sum is 14
```

> **Tip** Use a `do-while` loop if you have statements inside the loop that must be executed *at least once,* as in the case of the `do-while` loop in the preceding `TestDoWhile` program. These statements must appear before the loop as well as inside it if you use a `while` loop.

**5.6.1** Suppose the input is `2 3 4 5 0`. What is the output of the following code?

**Check Point**

```java
import java.util.Scanner;

public class Test {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int number, max;
    number = input.nextInt();
    max = number;

    do {
      number = input.nextInt();
      if (number > max)
        max = number;
    } while (number != 0);
    System.out.println("max is " + max);
    System.out.println("number " + number);
  }
}
```

<!-- LI p.173 -->

**5.6.2** What are the differences between a `while` loop and a `do-while` loop? Convert the

following `while` loop into a `do-while` loop:

```java
Scanner input = new Scanner(System.in);
int sum = 0;
System.out.println("Enter an integer " +
   "(the input ends if it is 0)");
int number = input.nextInt();
while (number != 0) {
  sum += number;
  System.out.println("Enter an integer " +
     "(the input ends if it is 0)");
  number = input.nextInt();
}
```

## 5.7 The for Loop

*A* `for` *loop has a concise syntax for writing loops.*

Often you write a loop in the following common form:

**Key Point**

```java
i = initialValue; // Initialize loop control variable
while (i < endValue) {
  // Loop body
  ...
  i++; // Adjust loop control variable
}
```

This loop is intuitive and easy for beginners to grasp. However, programmers often forget to adjust the control variable, which leads to an infinite loop. A `for` loop can be used to avoid the potential error and simplify the preceding loop as shown in (a) below. In general, the syntax for a for loop is as shown in (a), which is equivalent to (b).

```java
for (i = initialValue; i < endValue; i++) {
                                             i = initialValue;
  // Loop body
                                             while (i < endValue) {
  ...
}
                                               // Loop body
                                               ...
                                               i++;
                                             }
```

In general, the syntax of a `for` *loop* is as follows:

```java
for (initial-action; loop-continuation-condition;
     action-after-each-iteration) {
  // Loop body;
  Statement(s);
}
```

The flowchart of the `for` loop is shown in Figure 5.3a. The `for` loop statement starts with the keyword `for`, followed by a pair of parentheses enclosing the control structure of the loop. This structure consists of `initial-action`, `loop-continuation-condition`, and `action-after-each-iteration`. The control structure is

<!-- LI p.174 -->

```java
i = 0;
```

```text
(i < 100)?
```

```java
System.out.println(
  "Welcome to Java!");
```

```java
i++;
```

**Figure 5.3** A `for` loop performs an initial action once, then repeatedly executes the statements in the loop body, and performs an action after an iteration when the `loop- continuation-condition` evaluates to `true`.

followed by the loop body enclosed inside braces. The `initial-action`, `loop-continuation-condition`, and `action-after-each-iteration` are separated by semicolons.

A `for` loop generally uses a variable to control how many times the loop body is executed and when the loop terminates. This variable is referred to as a *control variable.* The `initial-action` often initializes a control variable, the `action-after-each-iteration` usually increments or decrements the control variable, and the `loop-continuation-condition` tests whether the control variable has reached a termination value. For example, the following `for` loop prints `Welcome to Java!` a hundred times:

```java
int i;
for (i = 0; i < 100; i++) {
  System.out.println("Welcome to Java!");
}
```

The flowchart of the statement is shown in Figure 5.3b. The `for` loop initializes `i` to `0`, then repeatedly executes the `println` statement and evaluates `i++` while `i` is less than `100`.

The `initial-action`, `i 0`, initializes the control variable, `i`. The `loop-`

```text
=
```

`continuation-condition`, `i < 100`, is a Boolean expression. The expression is evaluated right after the initialization and at the beginning of each iteration. If this condition is `true`, the loop body is executed. If it is `false`, the loop terminates and the program control turns to the line following the loop.

The `action-after-each-iteration`, `i++`, is a statement that adjusts the control variable. This statement is executed after each iteration and increments the control variable. Eventually, the value of the control variable should force the `loop-continuation-condition` to become `false`; otherwise, the loop is infinite.

The loop control variable can be declared and initialized in the `for` loop. Here is an example:

```java
for (int i = 0; i < 100; i++) {
  System.out.println("Welcome to Java!");
}
```

<!-- LI p.175 -->

If there is only one statement in the loop body, as in this example, the braces can be omitted.

> **Tip** The control variable must be declared inside the control structure of the loop or before the loop. If the loop control variable is used only in the loop, and not elsewhere, it is a good programming practice to declare it in the `initial-action` of the `for` loop. If the variable is declared inside the loop control structure, it cannot be referenced outside the loop. In the preceding code, for example, you cannot reference `i` outside the `for` loop, because it is declared inside the `for` loop.

> **Note** The `initial-action` in a `for` loop can be a list of zero or more comma-separated variable declaration statements or assignment expressions. For example:

```java
for (int i = 0, j = 0; i + j < 10; i++, j++) {
  // Do something
}
```

> The `action-after-each-iteration` in a `for` loop can be a list of zero or more comma-separated statements. For example:

```java
for (int i = 1; i < 100; System.out.println(i), i++) ;
```

> This example is correct, but it is a bad example, because it makes the code difficult to read. Normally, you declare and initialize a control variable as an initial action, and increment or decrement the control variable as an action after each iteration.

> **Note** If the `loop-continuation-condition` in a `for` loop is omitted, it is implicitly `true`. Thus, the statement given below in (a), which is an infinite loop, is the same as in (b). To avoid confusion, though, it is better to use the equivalent loop in (c).

```java
for ( ; ; ) {
                                                                while (true) {
  // Do something
                                  // Do something
                                                                  // Do something
}
                                }
                                                                }
```

**5.7.1**

Do the following two loops result in the same value in `sum`?

**Check Point**

```java
for (int i = 0; i < 10; ++i) {
                                     for (int i = 0; i < 10; i++) {
  sum += i;
                                        sum += i;
}
                                      }
```

> (a) (b)

**5.7.2** What are the three parts of a `for` loop control? Write a `for` loop that prints the numbers from `1` to `100`. **5.7.3** Suppose the input is `2 3 4 5 0`. What is the output of the following code?

```java
import java.util.Scanner;

public class Test {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int number, sum = 0, count;
    for (count = 0; count < 5; count++) {
      number = input.nextInt();
      sum += number;
    }
    System.out.println("sum is " + sum);
    System.out.println("count is " + count);
  }
}
```

<!-- LI p.176 -->

**5.7.4** What does the following statement do?

```java
for ( ; ; ) {
      // Do something
}
```

**5.7.5** If a variable is declared in a `for` loop control, can it be used after the loop exits? **5.7.6** Convert the following `for` loop statement to a `while` loop and to a `do-while` loop:

```java
long sum = 0;
for (int i = 0; i <= 1000; i++)
  sum = sum + i;
```

**5.7.7** Count the number of iterations in the following loops.

```java
int count = 0;
                               for (int count = 0;
while (count < n) {
                                 count <= n; count++) {
  count++;
                               }
}
```

```java
int count = 5;
                               int count = 5;
while (count < n) {
                               while (count < n) {
  count++;
                                 count = count + 3;
}
                               }
```
