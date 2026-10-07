---
topic: nested_loops_break
lessons: "M7"
book: "Java: The Complete Reference, 12th ed. (Schildt)"
printed_pages: "109-114"
pdf_offset: "pdf page = printed page + 35"
generated_by: tools/extract_refs.py
---
# Nested loops, break, continue - Java: The Complete Reference, 12th ed. (Schildt)

<!-- CR p.109 -->

### Nested Loops

Like all other programming languages, Java allows loops to be nested. That is, one loop may be inside another. For example, here is a program that nests `for` loops:

```java
// Loops may be nested.
class Nested {
  public static void main(String[] args) {
    int i, j;

    for(i=0; i<10; i++) {
      for(j=i; j<10; j++)
        System.out.print(".");
      System.out.println();
    }
  }
}
```

The output produced by this program is shown here:

```text
..........
.........
........
.......
......
.....
....
...
..
.
```

## Jump Statements

Java supports three jump statements: `break`, `continue`, and `return`. These statements transfer control to another part of your program. Each is examined here.

**NOTE** In addition to the jump statements discussed here, Java supports one other way that you can change

your program’s flow of execution: through exception handling. Exception handling provides a structured method by which run-time errors can be trapped and handled by your program. It is supported by the keywords `try`, `catch`, `throw`, `throws`, and `finally`. In essence, the exception handling mechanism allows your program to perform a nonlocal branch. Since exception handling is a large topic, it is discussed in its own chapter, Chapter 10.

### Using break

In Java, the `break` statement has three uses. First, as you have seen, it terminates a statement sequence in a `switch` statement. Second, it can be used to exit a loop. Third, it can be used as a “civilized” form of goto. The last two uses are explained here.

<!-- CR p.110 -->

##### Using break to Exit a Loop

By using `break`, you can force immediate termination of a loop, bypassing the conditional expression and any remaining code in the body of the loop. When a `break` statement is encountered inside a loop, the loop is terminated and program control resumes at the next statement following the loop. Here is a simple example:

```java
// Using break to exit a loop.
class BreakLoop {
  public static void main(String[] args) {
    for(int i=0; i<100; i++) {
      if(i == 10) break; // terminate loop if i is 10
      System.out.println("i: " + i);
    }
    System.out.println("Loop complete.");
  }
}
```

This program generates the following output:

```text
i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
i: 6
i: 7
i: 8
i: 9
Loop complete.
```

As you can see, although the `for` loop is designed to run from 0 to 99, the `break` statement causes it to terminate early, when `i` equals 10.

The `break` statement can be used with any of Java’s loops, including intentionally infinite loops. For example, here is the preceding program coded by use of a `while` loop. The output from this program is the same as just shown.

```java
// Using break to exit a while loop.
class BreakLoop2 {
  public static void main(String[] args) {
    int i = 0;

    while(i < 100) {
      if(i == 10) break; // terminate loop if i is 10
      System.out.println("i: " + i);
      i++;
    }
    System.out.println("Loop complete.");
  }
}
```

<!-- CR p.111 -->

When used inside a set of nested loops, the `break` statement will only break out of the innermost loop. For example:

```java
// Using break with nested loops.
class BreakLoop3 {
  public static void main(String[] args) {
    for(int i=0; i<3; i++) {
      System.out.print("Pass " + i + ": ");
      for(int j=0; j<100; j++) {
        if(j == 10) break; // terminate loop if j is 10
        System.out.print(j + " ");
      }
      System.out.println();
    }
    System.out.println("Loops complete.");
  }
}
```

This program generates the following output:

```text
Pass 0: 0 1 2 3 4 5 6 7 8 9
Pass 1: 0 1 2 3 4 5 6 7 8 9
Pass 2: 0 1 2 3 4 5 6 7 8 9
Loops complete.
```

As you can see, the `break` statement in the inner loop only causes termination of that loop. The outer loop is unaffected.

Here are two other points to remember about `break`. First, more than one `break` statement may appear in a loop. However, be careful. Too many `break` statements have the tendency to destructure your code. Second, the `break` that terminates a `switch` statement affects only that `switch` statement and not any enclosing loops.

**REMEMBER** `break` was not designed to provide the normal means by which a loop is terminated. The loop’s

conditional expression serves this purpose. The `break` statement should be used to cancel a loop only when some sort of special situation occurs.

##### Using break as a Form of Goto

In addition to its uses with the `switch` statement and loops, the `break` statement can also be employed by itself to provide a “civilized” form of the goto statement. Java does not have a goto statement because it provides a way to branch in an arbitrary and unstructured manner. This usually makes goto-ridden code hard to understand and hard to maintain. It also prohibits certain compiler optimizations. There are, however, a few places where the goto is a valuable and legitimate construct for flow control. For example, the goto can be useful when you are exiting from a deeply nested set of loops. To handle such situations, Java defines an expanded form of the `break` statement. By using this form of `break`, you can, for example, break out of one or more blocks of code. These blocks need not be part of a loop or a `switch`. They can be any block. Further, you can specify precisely where execution will resume, because this form of `break` works with a label. As you will see, `break` gives you the benefits of a goto without its problems.

<!-- CR p.113 -->

```java
      }
      System.out.println("This will not print");
    }
    System.out.println("Loops complete.");
  }
}
```

This program generates the following output:

```text
Pass 0: 0 1 2 3 4 5 6 7 8 9 Loops complete.
```

As you can see, when the inner loop breaks to the outer loop, both loops have been terminated. Notice that this example labels the `for` statement, which has a block of code as its target.

Keep in mind that you cannot break to any label which is not defined for an enclosing block. For example, the following program is invalid and will not compile:

```java
// This program contains an error.
class BreakErr {
  public static void main(String[] args) {

    one: for(int i=0; i<3; i++) {
      System.out.print("Pass " + i + ": ");
    }

    for(int j=0; j<100; j++) {
      if(j == 10) break one; // WRONG
      System.out.print(j + " ");
    }
  }
}
```

Since the loop labeled `one` does not enclose the `break` statement, it is not possible to transfer control out of that block.

### Using continue

Sometimes it is useful to force an early iteration of a loop. That is, you might want to continue running the loop but stop processing the remainder of the code in its body for this particular iteration. This is, in effect, a goto just past the body of the loop, to the loop’s end. The `continue` statement performs such an action. In `while` and `do-while` loops, a `continue` statement causes control to be transferred directly to the conditional expression that controls the loop. In a `for` loop, control goes first to the iteration portion of the `for` statement and then to the conditional expression. For all three loops, any intermediate code is bypassed.

Here is an example program that uses `continue` to cause two numbers to be printed on each line:

```java
// Demonstrate continue.
class Continue {
  public static void main(String[] args) {
    for(int i=0; i<10; i++) {
      System.out.print(i + " ");
      if (i%2 == 0) continue;
      System.out.println("");
    }
  }
}
```

<!-- CR p.114 -->

This code uses the % operator to check if `i` is even. If it is, the loop continues without printing a newline. Here is the output from this program:

```text
0 1
2 3
4 5
6 7
8 9
```

As with the `break` statement, `continue` may specify a label to describe which enclosing loop to continue. Here is an example program that uses `continue` to print a triangular multiplication table for 0 through 9:

```java
// Using continue with a label.
class ContinueLabel {
  public static void main(String[] args) {
outer: for (int i=0; i<10; i++) {
         for(int j=0; j<10; j++) {
           if(j > i) {
             System.out.println();
             continue outer;
           }
           System.out.print(" " + (i * j));
         }
       }
       System.out.println();
  }
}
```

The `continue` statement in this example terminates the loop counting `j` and continues with the next iteration of the loop counting `i`. Here is the output of this program:

```text
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
0 5 10 15 20 25
0 6 12 18 24 30 36
0 7 14 21 28 35 42 49
0 8 16 24 32 40 48 56 64
0 9 18 27 36 45 54 63 72 81
```

Good uses of `continue` are rare. One reason is that Java provides a rich set of loop statements which fit most applications. However, for those special circumstances in which early iteration is needed, the `continue` statement provides a structured way to accomplish it.
