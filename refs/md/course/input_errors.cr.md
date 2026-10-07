---
topic: input_errors
lessons: "M4_L1, M4_L2"
book: "Java: The Complete Reference, 12th ed. (Schildt)"
printed_pages: "13-695"
pdf_offset: "pdf page = printed page + 35"
generated_by: tools/extract_refs.py
---
# User input (Scanner) and understanding errors - Java: The Complete Reference, 12th ed. (Schildt)

<!-- CR p.13 -->

## The Java Buzzwords

No discussion of Java’s history is complete without a look at the Java buzzwords. Although the fundamental forces that necessitated the invention of Java are portability and security, other factors also played an important role in molding the final form of the language. The key considerations were summed up by the Java team in the following list of buzzwords:

- Simple
- Secure
- Portable
- Object-oriented
- Robust
- Multithreaded
- Architecture-neutral
- Interpreted
- High performance
- Distributed
- Dynamic

Two of these buzzwords have already been discussed: secure and portable. Let’s examine what each of the others implies.

### Simple

Java was designed to be easy for the professional programmer to learn and use effectively. Assuming that you have some programming experience, you will not find Java hard to master. If you already understand the basic concepts of object-oriented programming, learning Java will be even easier. Best of all, if you are an experienced C++ programmer, moving to Java will require very little effort. Because Java inherits the C/C++ syntax and many of the object-oriented features of C++, most programmers have little trouble learning Java.

### Object-Oriented

Although influenced by its predecessors, Java was not designed to be source-code compatible with any other language. This allowed the Java team the freedom to design with a blank slate. One outcome of this was a clean, usable, pragmatic approach to objects. Borrowing liberally from many seminal object-software environments of the last few decades, Java managed to strike a balance between the purist’s “everything is an object” paradigm and the pragmatist’s “stay out of my way” model. The object model in Java is simple and easy to extend, while primitive types, such as integers, were kept as high-performance nonobjects.

### Robust

The multiplatformed environment of the Web places extraordinary demands on a program, because the program must execute reliably in a variety of systems. Thus, the ability to create robust programs was given a high priority in the design of Java. To gain reliability, Java restricts you in a few key areas to force you to find your mistakes early in program development. At the same time, Java frees you from having to worry about many of the most common causes of programming errors. Because Java is a strictly typed language, it checks your code at compile time. However, it also checks your code at run time. Many hard-to-track-down bugs that often turn up in hard-to-reproduce run-time situations are simply impossible to create in Java. Knowing that what you have written will behave in a predictable way under diverse conditions is a key feature of Java.

<!-- CR p.14 -->

To better understand how Java is robust, consider two of the main reasons for program failure: memory management mistakes and mishandled exceptional conditions (that is, run-time errors). Memory management can be a difficult, tedious task in traditional programming environments. For example, in C/C++, the programmer will often manually allocate and free dynamic memory. This sometimes leads to problems, because programmers will either forget to free memory that has been previously allocated or, worse, try to free some memory that another part of their code is still using. Java virtually eliminates these problems by managing memory allocation and deallocation for you. (In fact, deallocation is completely automatic, because Java provides garbage collection for unused objects.) Exceptional conditions in traditional environments often arise in situations such as division by zero or “file not found,” and they must be managed with clumsy and hard-to-read constructs. Java helps in this area by providing object-oriented exception handling. In a well-written Java program, all run-time errors can—and should—be managed by your program.

### Multithreaded

Java was designed to meet the real-world requirement of creating interactive, networked programs. To accomplish this, Java supports multithreaded programming, which allows you to write programs that do many things simultaneously. The Java run-time system comes with an elegant yet sophisticated solution for multiprocess synchronization that enables you to construct smoothly running interactive systems. Java’s easy-to-use approach to multithreading allows you to think about the specific behavior of your program, not the multitasking subsystem.

### Architecture-Neutral

A central issue for the Java designers was that of code longevity and portability. At the time of Java’s creation, one of the main problems facing programmers was that no guarantee existed that if you wrote a program today, it would run tomorrow—even on the same machine. Operating system upgrades, processor upgrades, and changes in core system resources can all combine to make a program malfunction. The Java designers made several hard decisions in the Java language and the Java Virtual Machine in an attempt to alter this situation. Their goal was “write once; run anywhere, any time, forever.” To a great extent, this goal was accomplished.

### Interpreted and High Performance

As described earlier, Java enables the creation of cross-platform programs by compiling into an intermediate representation called Java bytecode. This code can be executed on any system that implements the Java Virtual Machine. Most previous attempts at cross-platform

<!-- CR p.691 -->

The output is the same as before.

### The Java printf( ) Connection

Although there is nothing technically wrong with using **Formatter** directly (as the preceding examples have done) when creating output that will be displayed on the console, there is a more convenient alternative: the **printf( )** method. The **printf( )** method automatically uses **Formatter** to create a formatted string. It then displays that string on `System.out`, which is the console by default. The **printf( )** method is defined by both **PrintStream** and `PrintWriter`. The **printf( )** method is described in Chapter 22.

## Scanner

`Scanner` is the complement of **Formatter**. It reads formatted input and converts it into its binary form. `Scanner` can be used to read input from the console, a file, a string, or any source that implements the **Readable** interface or **ReadableByteChannel**. For example, you can use `Scanner` to read a number from the keyboard and assign its value to a variable. As you will see, given its power, `Scanner` is surprisingly easy to use.

### The Scanner Constructors

`Scanner` defines many constructors. A sampling is shown in Table 21-14. In general, a `Scanner` can be created for a `String`, an **InputStream**, a `File`, a **Path**, or any object that implements the **Readable** or **ReadableByteChannel** interfaces. Here are some examples.

The following sequence creates a `Scanner` that reads the file `Test.txt`:

```java
FileReader fin = new FileReader("Test.txt");
Scanner src = new Scanner(fin);
```

This works because **FileReader** implements the **Readable** interface. Thus, the call to the constructor resolves to `Scanner(Readable)`.

This next line creates a `Scanner` that reads from standard input, which is the keyboard by default:

```java
Scanner conin = new Scanner(System.in);
```

This works because `System.in` is an object of type **InputStream**. Thus, the call to the constructor maps to `Scanner(InputStream)`.

The next sequence creates a `Scanner` that reads from a string.

```java
String instr = "10 99.88 scanning is easy.";
Scanner conin = new Scanner(instr);
```

### Scanning Basics

Once you have created a `Scanner`, it is a simple matter to use it to read formatted input. In general, a `Scanner` reads *tokens* from the underlying source that you specified when the `Scanner` was created. As it relates to `Scanner`, a token is a portion of input that is delineated by a set of delimiters, which is whitespace by default. A token is read by matching it with a particular *regular expression*, which defines the format of the data. Although `Scanner` allows

<!-- CR p.692 -->

| Method | Description |
|---|---|
| Scanner(File from) throws FileNotFoundException | Creates a Scanner that uses the file specified by from as a source for input. |
| Scanner(File from, String charset) throws FileNotFoundException | Creates a Scanner that uses the file specified by from with the encoding specified by charset as a source for input. |
| Scanner(InputStream from) | Creates a Scanner that uses the stream specified by from as a source for input. |
| Scanner(InputStream from, String charset) | Creates a Scanner that uses the stream specified by from with the encoding specified by charset as a source for input. |
| Scanner(Path from) throws IOException | Creates a Scanner that uses the file specified by from as a source for input. |
| Scanner(Path from, String charset) throws IOException | Creates a Scanner that uses the file specified by from with the encoding specified by charset as a source for input. |
| Scanner(Readable from) | Creates a Scanner that uses the Readable object specified by from as a source for input. |
| Scanner (ReadableByteChannel from) | Creates a Scanner that uses the ReadableByteChannel specified by from as a source for input. |
| Scanner(ReadableByteChannel from, String charset) | Creates a Scanner that uses the ReadableByteChannel specified by from with the encoding specified by charset as a source for input. |
| Scanner(String from) | Creates a Scanner that uses the string specified by from as a source for input. |

**Table 21-14**

A Sampling of `Scanner` Constructors

you to define the specific type of expression that its next input operation will match, it includes many predefined patterns, which match the primitive types, such as `int` and `double`, and strings. Thus, often you won’t need to specify a pattern to match.

In general, to use `Scanner`, follow this procedure:

1. Determine if a specific type of input is available by calling one of `Scanner`’s `hasNext`*X* methods, where *X* is the type of data desired.
2. If input is available, read it by calling one of `Scanner`’s `next`*X* methods.
3. Repeat the process until input is exhausted.
4. Close the `Scanner` by calling **close( )**.

As the preceding indicates, `Scanner` defines two sets of methods that enable you to read input. The first are the `hasNext`*X* methods, which are shown in Table 21-15. These methods determine if the specified type of input is available. For example, calling **hasNextInt( )** returns `true` only if the next token to be read is an integer. If the desired data is available, then you read it by calling one of `Scanner`’s `next`*X* methods, which are shown in Table 21-16. For

<!-- CR p.693 -->

| Method | Description |
|---|---|
| boolean hasNext( ) | Returns true if another token of any type is available to be read. Returns false otherwise. |
| boolean hasNext(Pattern pattern) | Returns true if a token that matches the pattern passed in pattern is available to be read. Returns false otherwise. |
| boolean hasNext(String pattern) | Returns true if a token that matches the pattern passed in pattern is available to be read. Returns false otherwise. |
| boolean hasNextBigDecimal( ) | Returns true if a value that can be stored in a BigDecimal object is available to be read. Returns false otherwise. |
| boolean hasNextBigInteger( ) | Returns true if a value that can be stored in a BigInteger object is available to be read. Returns false otherwise. The default radix is used. (Unless changed, the default radix is 10.) |
| boolean hasNextBigInteger(int radix) | Returns true if a value in the specified radix that can be stored in a BigInteger object is available to be read. Returns false otherwise. |
| boolean hasNextBoolean( ) | Returns true if a boolean value is available to be read. Returns false otherwise. |
| boolean hasNextByte( ) | Returns true if a byte value is available to be read. Returns false otherwise. The default radix is used. (Unless changed, the default radix is 10.) |
| boolean hasNextByte(int radix) | Returns true if a byte value in the specified radix is available to be read. Returns false otherwise. |
| boolean hasNextDouble( ) | Returns true if a double value is available to be read. Returns false otherwise. |
| boolean hasNextFloat( ) | Returns true if a float value is available to be read. Returns false otherwise. |
| boolean hasNextInt( ) | Returns true if an int value is available to be read. Returns false otherwise. The default radix is used. (Unless changed, the default radix is 10.) |
| boolean hasNextInt(int radix) | Returns true if an int value in the specified radix is available to be read. Returns false otherwise. |
| boolean hasNextLine( ) | Returns true if a line of input is available. |
| boolean hasNextLong( ) | Returns true if a long value is available to be read. Returns false otherwise. The default radix is used. (Unless changed, the default radix is 10.) |
| boolean hasNextLong(int radix) | Returns true if a long value in the specified radix is available to be read. Returns false otherwise. |
| boolean hasNextShort( ) | Returns true if a short value is available to be read. Returns false otherwise. The default radix is used. (Unless changed, the default radix is 10.) |
| boolean hasNextShort(int radix) | Returns true if a short value in the specified radix is available to be read. Returns false otherwise. |

**Table 21-15**

The **Scanner hasNext** Methods

<!-- CR p.694 -->

| Method | Description |
|---|---|
| String next( ) | Returns the next token of any type from the input source. |
| String next(Pattern pattern) | Returns the next token that matches the pattern passed in pattern from the input source. |
| String next(String pattern) | Returns the next token that matches the pattern passed in pattern from the input source. |
| BigDecimal nextBigDecimal( ) | Returns the next token as a BigDecimal object. |
| BigInteger nextBigInteger( ) | Returns the next token as a BigInteger object. The default radix is used. (Unless changed, the default radix is 10.) |
| BigInteger nextBigInteger(int radix) | Returns the next token (using the specified radix) as a BigInteger object. |
| boolean nextBoolean( ) | Returns the next token as a boolean value. |
| byte nextByte( ) | Returns the next token as a byte value. The default radix is used. (Unless changed, the default radix is 10.) |
| byte nextByte(int radix) | Returns the next token (using the specified radix) as a byte value. |
| double nextDouble( ) | Returns the next token as a double value. |
| float nextFloat( ) | Returns the next token as a float value. |
| int nextInt( ) | Returns the next token as an int value. The default radix is used. (Unless changed, the default radix is 10.) |
| int nextInt(int radix) | Returns the next token (using the specified radix) as an int value. |
| String nextLine( ) | Returns the next line of input as a string. |
| long nextLong( ) | Returns the next token as a long value. The default radix is used. (Unless changed, the default radix is 10.) |
| long nextLong(int radix) | Returns the next token (using the specified radix) as a long value. |
| short nextShort( ) | Returns the next token as a short value. The default radix is used. (Unless changed, the default radix is 10.) |
| short nextShort(int radix) | Returns the next token (using the specified radix) as a short value. |

**Table 21-16**

The **Scanner next** Methods

example, to read the next integer, call **nextInt( )**. The following sequence shows how to read a list of integers from the keyboard.

```java
Scanner conin = new Scanner(System.in);
int i;

// Read a list of integers.
while(conin.hasNextInt()) {
  i = conin.nextInt();
  // ...
}
```

<!-- CR p.695 -->

The `while` loop stops as soon as the next token is not an integer. Thus, the loop stops reading integers as soon as a non-integer is encountered in the input stream.

If a `next` method cannot find the type of data it is looking for, it throws an **InputMismatchException**. A **NoSuchElementException** is thrown if no more input is available. For this reason, it is best to first confirm that the desired type of data is available by calling a `hasNext` method before calling its corresponding `next` method.

### Some Scanner Examples

`Scanner` makes what could be a tedious task into an easy one. To understand why, let’s look at some examples. The following program averages a list of numbers entered at the keyboard:

```java
// Use Scanner to compute an average of the values.
import java.util.*;

class AvgNums {
  public static void main(String[] args) {
    Scanner conin = new Scanner(System.in);

    int count = 0;
    double sum = 0.0;

    System.out.println("Enter numbers to average.");

    // Read and sum numbers.
    while(conin.hasNext()) {
      if(conin.hasNextDouble()) {
        sum += conin.nextDouble();
        count++;
      }
      else {
        String str = conin.next();
        if(str.equals("done")) break;
        else {
          System.out.println("Data format error.");
          return;
        }
      }
    }

    conin.close();
    System.out.println("Average is " + sum / count);
  }
}
```
