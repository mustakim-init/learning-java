---
topic: intro_java
lessons: "M1_L3"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "11-16"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "1.6, 1.7, 1.8"
generated_by: tools/extract_refs.py
---
# Introduction to Java - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.11 -->

## 1.6 The Java Language Specification, API, JDK, JRE, and IDE

*Java syntax is defined in the Java language specification, and the Java library is defined in the Java application program interface (API). The JDK is the software for compiling and running Java programs. An IDE is an integrated development environ-*

**Key**

*ment for rapidly developing programs.*

**Point**

Computer languages have strict rules of usage. If you do not follow the rules when writing a program, the computer will not be able to understand it. The Java language specification and the Java API define the Java standards.

The *Java language specification* is a technical definition of the Java programming language’s syntax and semantics. You can find the complete Java language specification at docs.oracle.com/javase/specs/.

The *application program interface (API)*, also known as *library*, contains predefined classes and interfaces for developing Java programs. The API is still expanding. You can view the latest Java API documentation at https://docs.oracle.com/en/java/javase/11/.

Java is a full-fledged and powerful language that can be used in many ways. It comes in three editions:

- *Java Standard Edition (Java SE)* to develop client-side applications. The applications can run on desktop.
- *Java Enterprise Edition (Java EE)* to develop server-side applications, such as Java servlets, JavaServer Pages (JSP), and JavaServer Faces (JSF).
- *Java Micro Edition (Java ME)* to develop applications for mobile devices, such as cell phones.

This book uses Java SE to introduce Java programming. Java SE is the foundation upon which all other Java technology is based. There are many versions of Java SE. The latest,

<!-- LI p.12 -->

Java SE 11 (or simply Java 11), is used in this book. Oracle releases each version with a *Java Development Toolkit (JDK)*. For Java 11, the Java Development Toolkit is called *JDK 11*.

The JDK consists of a set of separate programs, each invoked from a command line, for compiling, running, and testing Java programs. The program for running Java programs is known as *Java Runtime Environment (JRE)*. Instead of using the JDK, you can use a Java development tool (e.g., NetBeans, Eclipse, and TextPad)—software that provides an *integrated development environment (IDE)* for developing Java programs quickly. Editing, compiling, building, debugging, and online help are integrated in one graphical user interface. You simply enter source code in one window or open an existing file in a window, and then click a button or menu item or press a function key to compile and run the program.

**1.6.1** What is the Java language specification?

**Check**

**1.6.2** What does JDK stand for? What does JRE stand for?

**Point**

**1.6.3** What does IDE stand for? **1.6.4** Are tools like NetBeans and Eclipse different languages from Java, or are they dia-

lects or extensions of Java?

## 1.7 A Simple Java Program

> **Key Point** A Java program is executed from the* `main` *method in the class.

Let’s begin with a simple Java program that displays the message `Welcome to Java!` on the console. (The word *console* is an old computer term that refers to the text entry and display device of a computer. *Console input* means to receive input from the keyboard, and *console output* means to display output on the monitor.) The program is given in Listing 1.1.

**Listing 1.1 Welcome.java** *(line N of the listing = Nth line of the block)*

```java
public class Welcome {
  public static void main(String[] args) {
main method
    // Display message Welcome to Java! on the console
    System.out.println("Welcome to Java!");
  }
}
```

**VideoNote**

> Your first Java program

```text
Welcome to Java!
```

Note the *line numbers* are for reference purposes only; they are not part of the program.

```text
line numbers
```

So, don’t type line numbers in your program.

Line 1 defines a class. Every Java program must have at least one class. Each class has a name. By convention, *class names* start with an uppercase letter. In this example, the class

```java
class name
```

name is `Welcome`.

Line 2 defines the `main` method. The program is executed from the `main` method. A class may contain several methods. The `main` method is the entry point where the program begins execution.

A method is a construct that contains statements. The `main` method in this program contains the `System.out.println` statement. This statement displays the string `Welcome to Java!` on the console (line 4). *String* is a programming term meaning a sequence of characters. A string must be enclosed in double quotation marks. Every statement in Java ends with a semicolon (;), known as the *statement terminator*.

*Keywords* have a specific meaning to the compiler and cannot be used for other purposes in the program. For example, when the compiler sees the word `class`, it understands that the word after `class` is the name for the class. Other keywords in this program are `public`, `static`, and `void`.

<!-- LI p.13 -->

Line 3 is a *comment* that documents what the program is and how it is constructed. Comments help programmers to communicate and understand the program. They are not programming statements, and thus are ignored by the compiler. In Java, comments are preceded by two slashes (//) on a line, called a *line comment*, or enclosed between /* and */ on one or several lines, called a *block comment* or *paragraph comment*. When the compiler sees //, it ignores all text after // on the same line. When it sees /*, it scans for the next */ and ignores any text between /* and */. Here are examples of comments:

```text
// This application program displays Welcome to Java!
/* This application program displays Welcome to Java! */
/* This application program
   displays Welcome to Java! */
```

A pair of braces in a program forms a *block* that groups the program’s components. In Java, each block begins with an opening brace ({) and ends with a closing brace (}). Every class has a *class block* that groups the data and methods of the class. Similarly, every method has a *method block* that groups the statements in the method. Blocks can be *nested*, meaning that one block can be placed within another, as shown in the following code:

```java
public class Welcome {
  public static void main(String[] args) {
    System.out.println("Welcome to Java!");
  }
```

Method block

```java
}
```

Class block

> **Tip** An opening brace must be matched by a closing brace. Whenever you type an opening brace, immediately type a closing brace to prevent the missing-brace error. Most Java IDEs automatically insert the closing brace for each opening brace.

> **Caution** Java source programs are case sensitive. It would be wrong, for example, to replace `main` in the program with `Main`.

You have seen several special characters (e.g., { }, //, ;) in the program. They are used in almost every program. Table 1.2 summarizes their uses.

The most common errors you will make as you learn to program will be syntax errors. Like any programming language, Java has its own syntax, and you need to write code that conforms to the *syntax rules.* If your program violates a rule—for example, if the semicolon is missing, a brace is missing, a quotation mark is missing, or a word is misspelled—the Java

**Table 1.2 Special Characters**

| Character | Name | Description |
|---|---|---|
| {} | Opening and closing braces | Denote a block to enclose statements. |
| () | Opening and closing parentheses | Used with methods. |
| [] | Opening and closing brackets | Denote an array. |
| // | Double slashes | Precede a comment line. |
| "" | Opening and closing quotation marks | Enclose a string (i.e., sequence of characters). |
| ; | Semicolon | Mark the end of a statement. |

<!-- LI p.14 -->

compiler will report syntax errors. Try to compile the program with these errors and see what the compiler reports.

> **Note** You are probably wondering why the `main` method is defined this way and why `System.out.println(...)` is used to display a message on the console. *For the time being, simply accept that this is how things are done.* Your questions will be fully answered in subsequent chapters.

The program in Listing 1.1 displays one message. Once you understand the program, it is easy to extend it to display more messages. For example, you can rewrite the program to display three messages, as shown in Listing 1.2.

**Listing 1.2 WelcomeWithThreeMessages.java** *(line N of the listing = Nth line of the block)*

```java
public class WelcomeWithThreeMessages {
  public static void main(String[] args) {
main method
    System.out.println("Programming is fun!");
    System.out.println("Fundamentals First");
    System.out.println("Problem Driven");
  }
}

                        Programming is fun!
                        Fundamentals First
                        Problem Driven
```

Further, you can perform mathematical computations and display the result on the console. Listing 1.3 gives an example of evaluating 10.5 + 2 × 3

. 45 - 3.5

**Listing 1.3 ComputeExpression.java** *(line N of the listing = Nth line of the block)*

```java
public class ComputeExpression {
  public static void main(String[] args) {
main method
    System.out.print("(10.5 + 2 * 3) / (45 – 3.5) = ");
    System.out.println((10.5 + 2 * 3) / (45 – 3.5));
  }
}
```

```text
(10.5 + 2 * 3) / (45 – 3.5) = 0.39759036144578314
```

The `print` method in line 3

```text
print vs. println
```

```java
System.out.print("(10.5 + 2 * 3) / (45 – 3.5) = ");
```

is identical to the `println` method except that `println` moves to the beginning of the next line after displaying the string, but `print` does not advance to the next line when completed.

The multiplication operator in Java is *. As you can see, it is a straightforward process to translate an arithmetic expression to a Java expression. We will discuss Java expressions further in Chapter 2.

**1.7.1**

What is a keyword? List some Java keywords.

**Check**

**1.7.2**

**Point**

Is Java case sensitive? What is the case for Java keywords?

<!-- LI p.15 -->

**1.7.3**

What is a comment? Is the comment ignored by the compiler? How do you denote a comment line and a comment paragraph?

**1.7.4**

What is the statement to display a string on the console?

**1.7.5**

Show the output of the following code:

```java
public class Test {
  public static void main(String[] args) {
    System.out.println("3.5 * 4 / 2 – 2.5 is ");
    System.out.println(3.5 * 4 / 2 – 2.5);
  }
}
```

## 1.8 Creating, Compiling, and Executing a Java Program

*You save a Java program in a .java file and compile it into a .class file. The .class file is executed by the Java Virtual Machine (JVM).*

**Key**

You have to create your program and compile it before it can be executed. This process is

**Point**

repetitive, as shown in Figure 1.6. If your program has compile errors, you have to modify the program to fix them, then recompile it. If your program has runtime errors or does not produce the correct result, you have to modify the program, recompile it, and execute it again.

You can use any text editor or IDE to create and edit a Java source-code file. This section demonstrates how to create, compile, and run Java programs from a command window. Sections 1.11 and 1.12 will introduce developing Java programs using NetBeans and Eclipse. From the command window, you can use a text editor such as Notepad to create the Java source-code file, as shown in Figure 1.7.

**Source code (developed by the programmer)**

```java
public class Welcome {
  public static void main(String[] args) {
    System.out.println("Welcome to Java!");
  }
}
```

**Bytecode (generated by the compiler for JVM to read and interpret)**

```java
…
Method Welcome()
  0 aload_0
  …

Method void main(java.lang.String[])
  0 getstatic #2 …
  3 ldc #3 <String "Welcome to Java!">
  5 invokevirtual #4 …
  8 return
```

**“Welcome to Java” is displayed on the console**

```text
Welcome to Java!
```

**Figure 1.6** The Java program-development process consists of repeatedly creating/modifying source code, compiling, and executing programs.

<!-- LI p.16 -->

**Figure 1.7** You can create a Java source file using Windows Notepad.

> **Note** The source file must end with the extension `.java` and must have the same exact name as the public class name. For example, the file for the source code in Listing 1.1 should be named **Welcome.java**, since the public class name is `Welcome`.

A Java compiler translates a Java source file into a Java bytecode file. The following command compiles **Welcome.java**:

```text
javac Welcome.java
```

> **Note** You must first install and configure the JDK before you can compile and run programs. See Supplement I.A, Installing and Configuring JDK 11, for how to install the JDK and set up the environment to compile and run Java programs. If you have trouble compiling and running programs, see Supplement I.B, Compiling and Running Java from the Command Window. This supplement also explains how to use basic DOS commands and how to use Windows Notepad to create and edit files. All the supplements are accessible from the Companion Website.

If there aren’t any syntax errors, the *compiler* generates a bytecode file with a `.class` extension. Thus, the preceding command generates a file named **Welcome.class**, as shown in Figure 1.8a. The Java language is a high-level language, but Java bytecode is a low-level language. The *bytecode* is similar to machine instructions but is architecture neutral and can run on any platform that has a *Java Virtual Machine (JVM)*, as shown in Figure 1.8b. Rather than a physical machine, the virtual machine is a program that interprets Java bytecode. This is one of Java’s primary advantages: *Java bytecode can run on a variety of hardware platforms and operating systems.* Java source code is compiled into Java bytecode, and Java bytecode is interpreted by the JVM. Your Java code may use the code in the Java library. The JVM executes your code along with the code in the library.

**Figure 1.8** (a) Java source code is translated into bytecode. (b) Java bytecode can be executed on any computer with a Java Virtual Machine.
