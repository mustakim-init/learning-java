---
topic: input_errors
lessons: "M4_L1, M4_L2"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "19-23"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "1.10.1, 1.10.2, 1.10.3, 1.10.4, 1.10.5, 1.10.6"
generated_by: tools/extract_refs.py
---
# User input (Scanner) and understanding errors - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.19 -->

### 1.10.1 Syntax Errors

Errors that are detected by the compiler are called *syntax errors* or *compile errors*. Syntax errors result from errors in code construction, such as mistyping a keyword, omitting some necessary punctuation, or using an opening brace without a corresponding closing brace.

<!-- LI p.20 -->

These errors are usually easy to detect because the compiler tells you where they are and what caused them. For example, the program in Listing 1.4 has a syntax error, as shown in Figure 1.10.

**Listing 1.4 ShowSyntaxErrors.java** *(line N of the listing = Nth line of the block)*

```java
public class ShowSyntaxErrors {
  public static main(String[] args) {
    System.out.println("Welcome to Java);
  }
}
```

Four errors are reported, but the program actually has two errors:

- The keyword `void` is missing before `main` in line 2.
- The string `Welcome to Java` should be closed with a closing quotation mark in line 3.

Since a single error will often display many lines of compile errors, it is a good practice to fix errors from the top line and work downward. Fixing errors that occur earlier in the program may also fix additional errors that occur later.

**Figure 1.10** The compiler reports syntax errors.

> **Tip** If you don’t know how to correct an error, compare your program closely, character by character, with similar examples in the text. In the first few weeks of this course, you will probably spend a lot of time fixing syntax errors. Soon you will be familiar with Java syntax, and can quickly fix syntax errors.

### 1.10.2 Runtime Errors

*Runtime errors* are errors that cause a program to terminate abnormally. They occur while a program is running if the environment detects an operation that is impossible to carry out. Input mistakes typically cause runtime errors. An *input error* occurs when the program is waiting for the user to enter a value, but the user enters a value that the program cannot handle. For instance, if the program expects to read in a number, but instead the user enters a string, this causes data-type errors to occur in the program.

<!-- LI p.21 -->

Another example of runtime errors is division by zero. This happens when the divisor is zero for integer divisions. For instance, the program in Listing 1.5 would cause a runtime error, as shown in Figure 1.11.

**Listing 1.5 ShowRuntimeErrors.java** *(line N of the listing = Nth line of the block)*

```java
public class ShowRuntimeErrors {
  public static void main(String[] args) {
    System.out.println(1 / 0);
  }
}
```

**Figure 1.11** The runtime error causes the program to terminate abnormally.

### 1.10.3 Logic Errors

*Logic errors* occur when a program does not perform the way it was intended to. Errors of this kind occur for many different reasons. For example, suppose you wrote the program in Listing 1.6 to convert Celsius `35` degrees to a Fahrenheit degree:

**Listing 1.6 ShowLogicErrors.java** *(line N of the listing = Nth line of the block)*

```java
public class ShowLogicErrors {
  public static void main(String[] args) {
    System.out.print("Celsius 35 is Fahrenheit degree ");
    System.out.println((9 / 5) * 35 + 32);
  }
}
```

```text
Celsius 35 is Fahrenheit degree 67
```

You will get Fahrenheit `67` degrees, which is wrong. It should be `95.0`. In Java, the division for integers is the quotient—the fractional part is truncated—so in Java `9 / 5` is `1`. To get the correct result, you need to use `9.0 / 5`, which results in `1.8`.

In general, syntax errors are easy to find and easy to correct because the compiler gives indications as to where the errors came from and why they are wrong. Runtime errors are not difficult to find, either, since the reasons and locations for the errors are displayed on the console when the program aborts. Finding logic errors, on the other hand, can be very challenging. In the upcoming chapters, you will learn the techniques of tracing programs and finding logic errors.

### 1.10.4 Common Errors

Missing a closing brace, missing a semicolon, missing quotation marks for strings, and misspelling names are common errors for new programmers.

<!-- LI p.22 -->

**Common Error 1: Missing Braces**

The braces are used to denote a block in the program. Each opening brace must be matched by a closing brace. A common error is missing the closing brace. To avoid this error, type a closing brace whenever an opening brace is typed, as shown in the following example:

```java
public class Welcome {

}
```

If you use an IDE such as NetBeans and Eclipse, the IDE automatically inserts a closing brace for each opening brace typed.

**Common Error 2: Missing Semicolons**

Each statement ends with a statement terminator (;). Often, a new programmer forgets to place a statement terminator for the last statement in a block, as shown in the following example:

```java
public static void main(String[] args) {
  System.out.println("Programming is fun!");
  System.out.println("Fundamentals First");
  System.out.println("Problem Driven")
}
```

**Common Error 3: Missing Quotation Marks**

A string must be placed inside the quotation marks. Often, a new programmer forgets to place a quotation mark at the end of a string, as shown in the following example:

```java
System.out.println("Problem Driven );
```

If you use an IDE such as NetBeans and Eclipse, the IDE automatically inserts a closing quotation mark for each opening quotation mark typed.

**Common Error 4: Misspelling Names**

Java is case sensitive. Misspelling names is a common error for new programmers. For example, the word `main` is misspelled as `Main` and `String` is misspelled as `string` in the following code:

```java
public class Test {
  public static void Main(string[] args) {
    System.out.println((10.5 + 2 * 3) / (45 - 3.5));
  }
}
```

**1.10.1**

What are syntax errors (compile errors), runtime errors, and logic errors?

**Check**

**1.10.2** Give examples of syntax errors, runtime errors, and logic errors.

**Point**

**1.10.3** If you forget to put a closing quotation mark on a string, what kind of error will be

raised? **1.10.4** If your program needs to read integers, but the user entered strings, an error would

occur when running this program. What kind of error is this?

**1.10.5**

Suppose you write a program for computing the perimeter of a rectangle and you mistakenly write your program so it computes the area of a rectangle. What kind of error is this?

<!-- LI p.23 -->

**1.10.6** Identify and fix the errors in the following code:

```java
public class Welcome {
  public void Main(String[] args) {
    System.out.println('Welcome to Java!);
  }
)
```
