---
topic: branching
lessons: "M5_L1, M5_L2"
book: "Java: The Complete Reference, 12th ed. (Schildt)"
printed_pages: "87-90"
pdf_offset: "pdf page = printed page + 35"
generated_by: tools/extract_refs.py
---
# Branching (if/else) and nested branching - Java: The Complete Reference, 12th ed. (Schildt)

<!-- CR p.87 -->

**CHAPTER**

5

**Control Statements**

A programming language uses *control* statements to cause the flow of execution to advance and branch based on changes to the state of a program. Java’s program control statements can be put into the following categories: selection, iteration, and jump. *Selection* statements allow your program to choose different paths of execution based upon the outcome of an expression or the state of a variable. *Iteration* statements enable program execution to repeat one or more statements (that is, iteration statements form loops). *Jump* statements allow your program to execute in a nonlinear fashion. All of Java’s control statements are examined here.

## Java’s Selection Statements

Java supports two selection statements: `if` and `switch`. These statements allow you to control the flow of your program’s execution based upon conditions known only during run time. You will be pleasantly surprised by the power and flexibility contained in these two statements.

### if

The `if` statement was introduced in Chapter 2. It is examined in detail here. The `if` statement is Java’s conditional branch statement. It can be used to route program execution through two different paths. Here is the general form of the `if` statement:

if (*condition*) *statement1*; else *statement2*; Here, each *statement* may be a single statement or a compound statement enclosed in curly braces (that is, a *block*). The *condition* is any expression that returns a `boolean` value. The `else` clause is optional.

The `if` works like this: If the *condition* is true, then *statement1* is executed. Otherwise, *statement2* (if it exists) is executed. In no case will both statements be executed. For example, consider the following:

```java
int a, b;
//...
if(a < b) a = 0;
else b = 0;
```

<!-- CR p.88 -->

Here, if `a` is less than `b`, then `a` is set to zero. Otherwise, `b` is set to zero. In no case are they both set to zero.

Most often, the expression used to control the `if` will involve the relational operators. However, this is not technically necessary. It is possible to control the `if` using a single `boolean` variable, as shown in this code fragment:

```java
boolean dataAvailable;
//...
if (dataAvailable)
  ProcessData();
else
  waitForMoreData();
```

Remember, only one statement can appear directly after the `if` or the `else`. If you want to include more statements, you’ll need to create a block, as in this fragment:

```java
int bytesAvailable;
// ...
if (bytesAvailable > 0) {
  ProcessData();
  bytesAvailable -= n;
} else
  waitForMoreData();
```

Here, both statements within the `if` block will execute if `bytesAvailable` is greater than zero.

Some programmers find it convenient to include the curly braces when using the `if`, even when there is only one statement in each clause. This makes it easy to add another statement at a later date, and you don’t have to worry about forgetting the braces. In fact, forgetting to define a block when one is needed is a common cause of errors. For example, consider the following code fragment:

```java
int bytesAvailable;
// ...
if (bytesAvailable > 0) {
  ProcessData();
  bytesAvailable -= n;
} else
  waitForMoreData();
  bytesAvailable = n;
```

It seems clear that the statement **bytesAvailable = n**; was intended to be executed inside the `else` clause, because of the indentation level. However, as you recall, whitespace is insignificant to Java, and there is no way for the compiler to know what was intended. This code will compile without complaint, but it will behave incorrectly when run. The preceding example is fixed in the code that follows:

```java
int bytesAvailable;
// ...
if (bytesAvailable > 0) {
  ProcessData();
  bytesAvailable -= n;
} else {
  waitForMoreData();
  bytesAvailable = n;
}
```

<!-- CR p.89 -->

##### Nested ifs

A *nested* `if` is an `if` statement that is the target of another `if` or `else`. Nested `if`s are very common in programming. When you nest `if`s, the main thing to remember is that an `else` statement always refers to the nearest `if` statement that is within the same block as the `else` and that is not already associated with an `else`. Here is an example:

```java
if(i == 10) {
  if(j < 20) a = b;
  if(k > 100) c = d; // this if is
  else a = c;        // associated with this else
}
else a = d;          // this else refers to if(i == 10)
```

As the comments indicate, the final `else` is not associated with `if(j<20)` because it is not in the same block (even though it is the nearest `if` without an `else`). Rather, the final `else` is associated with `if(i==10)`. The inner `else` refers to `if(k>100)` because it is the closest `if` within the same block.

##### The if-else-if Ladder

A common programming construct that is based upon a sequence of nested `if`s is the *if-else-if* ladder. It looks like this:

if(*condition*) *statement*; else if(*condition*) *statement*; else if(*condition*) *statement*; . . . else *statement*; The `if` statements are executed from the top down. As soon as one of the conditions controlling the `if` is `true`, the statement associated with that `if` is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final `else` statement will be executed. The final `else` acts as a default condition; that is, if all other conditional tests fail, then the last `else` statement is performed. If there is no final `else` and all other conditions are `false`, then no action will take place.

Here is a program that uses an `if-else-if` ladder to determine which season a particular month is in.

```java
// Demonstrate if-else-if statements.
class IfElse {
  public static void main(String[] args) {
    int month = 4; // April
    String season;

    if(month == 12 || month == 1 || month == 2)
      season = "Winter";
    else if(month == 3 || month == 4 || month == 5)
      season = "Spring";
    else if(month == 6 || month == 7 || month == 8)
      season = "Summer";
    else if(month == 9 || month == 10 || month == 11)
      season = "Autumn";
    else
      season = "Bogus Month";

    System.out.println("April is in the " + season + ".");
  }
}
```

<!-- CR p.90 -->

Here is the output produced by the program:

```text
April is in the Spring.
```

You might want to experiment with this program before moving on. As you will find, no matter what value you give `month`, one and only one assignment statement within the ladder will be executed.

### The Traditional switch

The `switch` statement is Java’s multiway branch statement. It provides an easy way to dispatch execution to different parts of your code based on the value of an expression. As such, it often provides a better alternative than a large series of `if-else-if` statements.

At the outset, it is necessary to state that beginning with JDK 14, the `switch` has been significantly enhanced and expanded with several new features that go far beyond its traditional form. The traditional form of `switch` has been part of Java from the beginning and is, therefore, in widespread use. Furthermore, it is the form that will work in all Java development environments and for all readers. Because of the substantial nature of the recent `switch` enhancements, they are described in Chapter 17, in the context of other recent additions to Java. Here, the traditional form of the `switch` is examined. Here is the general form of a traditional `switch` statement:

switch (*expression*) { case *value1*: // statement sequence break; case *value2*: // statement sequence break; . . .
