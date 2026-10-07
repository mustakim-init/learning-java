---
topic: loops
lessons: "M6_L1, M6_L2"
book: "Head First Java, 3rd ed. (Sierra, Bates, Gee)"
printed_pages: "13-14"
pdf_offset: "pdf page = printed page + 38"
generated_by: tools/extract_refs.py
---
# Loops (while, for) - Head First Java, 3rd ed. (Sierra, Bates, Gee)

<!-- HF p.13 -->

### Looping and looping and...

Java has a lot of looping constructs: while, do-while, and *for*, being the oldest. You’ll get the full loop scoop later in the book, but not right now. Let’s start with while.

The syntax (not to mention logic) is so simple you’re probably asleep already. As long as some condition is true, you do everything inside the loop *block*. The loop block is bounded by a pair of curly braces, so whatever you want to repeat needs to be inside that block.

The key to a loop is the *conditional test*. In Java, a conditional test is an expression that results in a *boolean* value—in other words, something that is either ***true*** or ***false***.

If you say something like, “While *iceCreamInTheTub is true*, keep scooping,” you have a clear boolean test. There either *is* ice cream in the tub or there *isn’t*. But if you were to say, “While *Bob* keep scooping,” you don’t have a real test. To make that work, you’d have to change it to something like, “While Bob is snoring...” or “While Bob is *not* wearing plaid...”

You can do a simple boolean test by checking the value of a variable, using a comparison operator like:

< (less than)

> (greater than)

== (equality) (yes, that’s *two* equals signs)

Notice the difference between the *assignment* operator (a *single* equals sign) and the *equals* operator (*two* equals signs). Lots of programmers accidentally type = when they *want* ==. (But not you.)

```java
int x = 4; // assign 4 to x
while (x > 3) {
  // loop code will run because
  // x is greater than 3
  x = x - 1; // or we'd loop forever
}
int z = 27; //
while (z == 17) {
  // loop code will not run because
  // z is not equal to 17
}
```

![figure](figures/hf_p13_1.png)

> *Figure/sidebar text on this page:* while (moreBalls == true) { / keepJuggling( ) ; / } / Simple boolean tests

<!-- HF p.14 -->

there are no

Dumb Questions

Q: **Why does everything have**

```java
public class Loopy {
  public static void main(String[] args) {
```

**to be in a class?**

```java
int x = 1;
System.out.println("Before the Loop");
```

A: Java is an object-oriented

```java
while (x < 4) {
  System.out.println("In the loop");
```

(OO) language. It’s not like the old days when you had steam-

```java
System.out.println("Value of x is " + x);
```

driven compilers and wrote one

```java
x = x + 1;
```

monolithic source file with a pile

```java
}
```

of procedures. In Chapter 2, *A Trip*

```java
System.out.println("This is after the loop");
```

*to Objectville*, you’ll learn that a class is a blueprint for an object,

```java
}
```

and that nearly everything in Java

```java
}
```

is an object.

```text
% java Loopy
```

Q: **Do I have to put a main in**

```text
Before the Loop
In the loop
```

**every class I write?**

```text
Value of x is 1
```

A: Nope. A Java program

```text
In the loop
Value of x is 2
```

might use dozens of classes (even

```text
In the loop
```

hundreds), but you might only

```text
Value of x is 3
```

have *one* with a main method— the one that starts the program

```text
This is after the loop
```

running.

Q: **In my other language I can**

**do a boolean test on an integer. In Java, can I say something like:**

�

```java
int x = 1;
```

�

```java
while (x){ }
```

�

A: No. A *boolean* and an

�

*integer* are not compatible types in

�

Java. Since the result of a condi

�

tional test *must* be a boolean, the only variable you can directly test (without using a comparison op

�

erator) is a ***boolean.*** For example, you can say:

```java
boolean isHot = true;
while(isHot) { }
```

�

```java
while (x == 4) { }
```

> *Figure/sidebar text on this page:* Example of a while loop / This is the output / BULLET POINTS / Statements end in a semicolon ; / Code blocks are defined by a pair of curly braces { } / Declare an int variable with a name and a type: int x; / The assignment operator is one equals sign = / The equals operator uses two equals signs == / A while loop runs everything within its block (defined by curly / braces) as long as the conditional test is true. / If the conditional test is false, the while loop code block won’t / run, and execution will move down to the code immediately / after the loop block. / Put a boolean test inside parentheses:
