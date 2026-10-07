---
topic: fileio
lessons: "M12"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "477-486"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "12.10, 12.11"
generated_by: tools/extract_refs.py
---
# File I/O - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.477 -->

## 12.10 The File Class

*The* `File` *class contains the methods for obtaining the properties of a file/directory, and for renaming and deleting a file/directory.*

**Key**

Having learned exception handling, you are ready to step into file processing. Data stored in

**Point**

the program are temporary; they are lost when the program terminates. To permanently store the data created in a program, you need to save them in a file on a disk or other permanent storage device. The file can then be transported and read later by other programs. Since data are stored in files, this section introduces how to use the `File` class to obtain file/directory properties, to delete and rename files/directories, and to create directories. The next section introduces how to read/write data from/to text files.

Every file is placed in a directory in the file system. An *absolute file name* (or *full name*) contains a file name with its complete path and drive letter. For example, **c:\book\ Welcome.java** is the absolute file name for the file **Welcome.java** on the Windows operating system. Here, **c:\book** is referred to as the *directory path* for the file. Absolute file names are machine dependent. On the UNIX platform, the absolute file name may be **/home/liang/book/Welcome.java**, where **/home/liang/book** is the directory path for the file **Welcome.java**.

A *relative file name* is in relation to the current working directory. The complete directory path for a relative file name is omitted. For example, **Welcome.java** is a relative file name. If the current working directory is **c:\book**, the absolute file name would be **c:\book\Welcome.java**.

The `File` class is intended to provide an abstraction that deals with most of the machine-dependent complexities of files and path names in a machine-independent fashion. The `File` class contains the methods for obtaining file and directory properties, and for renaming and deleting files and directories, as shown in Figure 12.6. However, *the* `File` *class does not contain the methods for reading and writing file contents*.

The file name is a string. The `File` class is a wrapper class for the file name and its directory path. For example, `new File("c:\\book")` creates a `File` object for the directory **c:\book** and `new File("c:\\book\\test.dat")` creates a `File` object for the file **c:\book\test.dat**, both on Windows. You can use the `File` class’s `isDirectory()` method to check whether the object represents a directory, and the `isFile()` method to check whether the object represents a file.

<!-- LI p.478 -->

```text
            java.io.File

+File(pathname: String)

+File(parent: String, child: String)

+File(parent: File, child: String)

+exists(): boolean
+canRead(): boolean
+canWrite(): boolean
+isDirectory(): boolean
+isFile(): boolean
+isAbsolute(): boolean
+isHidden(): boolean
```

```text
+getAbsolutePath(): String

+getCanonicalPath(): String


+getName(): String

+getPath(): String

+getParent(): String


+lastModified(): long
+length(): long
+listFile(): File[]
+delete(): boolean

+renameTo(dest: File): boolean

+mkdir(): boolean

+mkdirs(): boolean
```

**Figure 12.6** The `File` class can be used to obtain file and directory properties, to delete and rename files and directories, and to create directories.

> **Caution** The directory separator for Windows is a backslash (\). The backslash is a special character in Java and should be written as \\ in a string literal (see Table 4.5).

> **Note** *Constructing a* `File` *instance does not create a file on the machine*. You can create a `File` instance for any file name regardless of whether it exists or not. You can invoke the `exists()` method on a `File` instance to check whether the file exists.

Do not use absolute file names in your program. If you use a file name such as `c:\\book\\ Welcome.java`, it will work on Windows but not on other platforms. You should use a file name relative to the current directory. For example, you may create a `File` object using `new File("Welcome.java")` for the file **Welcome.java** in the current directory. You may create a `File` object using `new File("image/us.gif")` for the file **us.gif** under the **image** directory in the current directory. The forward slash (/) is the Java directory separator, which is the same as on UNIX. The statement `new File("image/us.gif")` works on Windows, UNIX, and any other platform.

<!-- LI p.479 -->

Listing 12.12 demonstrates how to create a `File` object and use the methods in the `File` class to obtain its properties. The program creates a `File` object for the file **us.gif**. This file is stored under the **image** directory in the current directory.

**Listing 12.12 TestFileClass.java** *(line N of the listing = Nth line of the block)*

```java
public class TestFileClass {
  public static void main(String[] args) {
    java.io.File file = new java.io.File("image/us.gif");
    System.out.println("Does it exist? " + file.exists());
                                                                           exists()
    System.out.println("The file has " + file.length() + " bytes");
                                                                           length()
    System.out.println("Can it be read? " + file.canRead());
                                                                           canRead()
    System.out.println("Can it be written? " + file.canWrite());
                                                                           canWrite()
    System.out.println("Is it a directory? " + file.isDirectory());
                                                                           isDirectory()
    System.out.println("Is it a file? " + file.isFile());
                                                                           isFile()
    System.out.println("Is it absolute? " + file.isAbsolute());
                                                                           isAbsolute()
    System.out.println("Is it hidden? " + file.isHidden());
                                                                           isHidden()
    System.out.println("Absolute path is " +
      file.getAbsolutePath());
                                                                           getAbsolutePath()
    System.out.println("Last modified on " +
      new java.util.Date(file.lastModified()));
                                                                           lastModified()
  }
}
```

The `lastModified()` method returns the date and time when the file was last modified, measured in milliseconds since the beginning of UNIX time (00:00:00 GMT, January 1, 1970). The `Date` class is used to display it in a readable format in lines 14 and 15.

Figure 12.7a shows a sample run of the program on Windows and Figure 12.7b, a sample run on UNIX. As shown in the figures, the path-naming conventions on Windows are different from those on UNIX.

**Figure 12.7** The program creates a `File` object and displays file properties.

**12.10.1** What is wrong about creating a `File` object using the following statement?

**Check**

```java
new File("c:\book\test.dat");
```

**Point**

**12.10.2** How do you check whether a file already exists? How do you delete a file? How

do you rename a file? Can you find the file size (the number of bytes) using the `File` class? How do you create a directory? **12.10.3** Can you use the `File` class for I/O? Does creating a `File` object create a file on

the disk?

<!-- LI p.480 -->

## 12.11 File Input and Output

> **Key Point** Use the* `Scanner` *class for reading text data from a file, and the* `PrintWriter` *class for writing text data to a file.

A `File` object encapsulates the properties of a file or a path, but it does not contain the methods for writing/reading data to/from a file (referred to as data *input* and *output*, or *I/O* for short). In order to perform I/O, you need to create objects using appropriate Java I/O classes. The objects contain the methods for reading/writing data from/to a file. There are two types of files:

**VideoNote**

text and binary. Text files are essentially characters on disk. This section introduces how to read/write strings and numeric values from/to a text file using the `Scanner` and `PrintWriter` classes. Binary files will be introduced in Chapter 17.

> Write and read data

### 12.11.1 Writing Data Using PrintWriter

The `java.io.PrintWriter` class can be used to create a file and write data to a text file. First, you have to create a `PrintWriter` object for a text file as follows:

```java
PrintWriter output = new PrintWriter(filename);
```

Then, you can invoke the `print`, `println`, and `printf` methods on the `PrintWriter` object to write data to a file. Figure 12.8 summarizes frequently used methods in `PrintWriter`.

```java
     java.io.PrintWriter

+PrintWriter(file: File)
+PrintWriter(filename: String)
+print(s: String): void
+print(c: char): void
+print(cArray: char[]): void
+print(i: int): void
+print(l: long): void
+print(f: f loat): void
+print(d: double): void
+print(b: boolean): void
```

**Figure 12.8** The `PrintWriter` class contains the methods for writing data to a text file.

Listing 12.13 gives an example that creates an instance of `PrintWriter` and writes two lines to the file **scores.txt**. Each line consists of a first name (a string), a middle-name initial (a character), a last name (a string), and a score (an integer).

**Listing 12.13**

```java
                  WriteData.java
 1 public class WriteData {
 public static void main(String[] args) throws java.io.IOException {
   java.io.File file = new java.io.File("scores.txt");
   if (file.exists()) {
     System.out.println("File already exists");
     System.exit(1);
   }

   // Create a file
   java.io.PrintWriter output = new java.io.PrintWriter(file);

   // Write formatted output to the file
   output.print("John T Smith ");
   output.println(90);
                                               John T Smith 90
                                                              scores.txt
   output.print("Eric K Jones ");
                                               Eric K Jones 85
   output.println(85);

   // Close the file
   output.close();
 }
21 }
```

<!-- LI p.481 -->

Lines 4–7 check whether the file **scores.txt** exists. If so, exit the program (line 6).

Invoking the constructor of `PrintWriter` will create a new file if the file does not exist. If the file already exists, the current content in the file will be discarded without verifying with the user.

Invoking the constructor of `PrintWriter` may throw an I/O exception. Java forces you to write the code to deal with this type of exception. For simplicity, we declare `throws`

```text
throws IOException
```

`IOException` in the main method header (line 2).

You have used the `System.out.print`, `System.out.println`, and `System.out .printf` methods to write text to the console output. `System.out` is a standard Java object for the console. You can create `PrintWriter` objects for writing text to any file using `print`, `println`, and `printf` (lines 13–16).

The `close()` method must be used to close the file (line 19). If this method is not invoked, the data may not be saved properly in the file.

> **Note** You can append data to an existing file using new PrintWriter(new FileOutputStream(file, true)) to create a PrintWriter object. FileOutputStream will be introduced in Chapter 17.

> **Tip** When the program writes data to a file, it first stores the data temporarily in a buffer in the memory. When the buffer is full, the data are automatically saved to the file on the disk. Once you close the file, all the data left in the buffer are saved to the file on the disk. Therefore, you must close the file to ensure that all data are saved to the file.

### 12.11.2 Closing Resources Automatically Using try-with-resources

Programmers often forget to close the file. JDK 7 provides the following try-with-resources syntax that automatically closes the files.

```java
try (declare and create resources) {
  Use the resource to process the file;
}
```

Using the try-with-resources syntax, we rewrite the code in Listing 12.13 as shown in Listing 12.14.

**Listing 12.14 WriteDataWithAutoClose.java** *(line N of the listing = Nth line of the block)*

```java
public class WriteDataWithAutoClose {
  public static void main(String[] args) throws Exception {
    java.io.File file = new java.io.File("scores.txt");
    if (file.exists()) {
      System.out.println("File already exists");
      System.exit(0);
    }

    try (
      // Create a file
      java.io.PrintWriter output = new java.io.PrintWriter(file);
    ) {
      // Write formatted output to the file
      output.print("John T Smith ");
      output.println(90);
      output.print("Eric K Jones ");
      output.println(85);
    }
  }
}
```

<!-- LI p.482 -->

A resource is declared and created in the parentheses following the keyword `try`. The resources must be a subtype of `AutoCloseable` such as a `PrinterWriter` that has the `close()` method. A resource must be declared and created in the same statement, and multiple resources can be declared and created inside the parentheses. The statements in the block (lines 12–18) immediately following the resource declaration use the resource. After the block is finished, the resource’s `close()` method is automatically invoked to close the resource. Using try-with-resources can not only avoid errors, but also make the code simpler. Note the catch clause may be omitted in a try-with-resources statement.

Note that (1) you have to declare the resource reference variable and create the resource altogether in the `try(...)` clause; (2) the semicolon (;) in last statement in the `try(...)` clause may be omitted; (3) You may create multiple `AutoCloseable` resources in the the `try(...)` clause; (4) The `try(...)` clause can contain only the statements for creating resources. Here is an example.

```java
try (
  Scanner input = new Scanner(System.in);
  PrintWriter output =
    new PrintWriter("c:\\temp\\temp.txt");
) {
  System.out.println(input.nextLine());
}
```

### 12.11.3 Reading Data Using Scanner

The `java.util.Scanner` class was used to read strings and primitive values from the console in Section 2.3, Reading Input from the Console. A `Scanner` breaks its input into tokens delimited by whitespace characters. To read from the keyboard, you create a `Scanner` for `System.in`, as follows:

```java
Scanner input = new Scanner(System.in);
```

To read from a file, create a `Scanner` for a file, as follows:

```java
Scanner input = new Scanner(new File(filename));
```

Figure 12.9 summarizes frequently used methods in `Scanner`.

<!-- LI p.483 -->

```java
       java.util.Scanner

+Scanner(source: File)
+Scanner(source: String)
+close()
+hasNext(): boolean
+next(): String
+nextLine(): String
+nextByte(): byte
+nextShort(): short
+nextInt(): int
+nextLong(): long
+nextFloat(): float
+nextDouble(): double
+useDelimiter(pattern: String):
 Scanner
```

**Figure 12.9** The `Scanner` class contains the methods for scanning data.

Listing 12.15 gives an example that creates an instance of `Scanner` and reads data from the file **scores.txt**.

**Listing 12.15**

```java
                  ReadData.java
 1 import java.util.Scanner;
 2
 3 public class ReadData {
 4   public static void main(String[] args) throws Exception {
 5     // Create a File instance
 6     java.io.File file = new java.io.File("scores.txt");
 7
 8     // Create a Scanner for the file
 9     Scanner input = new Scanner(file);
10
11     // Read data from a file
                                                             scores.txt
12     while (input.hasNext()) {
                                                        John T Smith 90
13       String firstName = input.next();
                                                        Eric K Jones 85
14       String mi = input.next();
15       String lastName = input.next();
16       int score = input.nextInt();
17       System.out.println(
18         firstName + " " + mi + " " + lastName + " " + score);
19    }
20
21     // Close the file
22     input.close();
23   }
24 }
```

Note `new Scanner(String)` creates a `Scanner` for a given string. To create a `Scanner` to read data from a file, you have to use the `java.io.File` class to create an instance of the `File` using the constructor `new File(filename)` (line 6) and use `new Scanner(File)` to create a `Scanner` for the file (line 9).

Invoking the constructor `new Scanner(File)` may throw an I/O exception, so the `main`

```text
throws Exception
```

method declares `throws Exception` in line 4.

Each iteration in the `while` loop reads the first name, middle initial, last name, and score from the text file (lines 12–19). The file is closed in line 22.

<!-- LI p.484 -->

It is not necessary to close the input file (line 22), but it is a good practice to do so to release the resources occupied by the file. You can rewrite this program using the try-with-resources

syntax. See liveexample.pearsoncmg.com/html/ReadDataWithAutoClose.html.

**Check Point 12.11.4** How Does Scanner Work?

Section 4.5.5 introduced token-based and line-based input. The token-based input methods `nextByte()`, `nextShort()`, `nextInt()`, `nextLong()`, `nextFloat()`, `nextDouble()`, and `next()` read input separated by delimiters. By default, the delimiters are whitespace characters. You can use the `useDelimiter(String regex)` method to set a new pattern for delimiters.

How does an input method work? A token-based input first skips any delimiters (whitespace characters by default) then reads a token ending at a delimiter. The token is then automatically converted into a value of the `byte`, `short`, `int`, `long`, `float`, or `double` type for `nextByte()`, `nextShort()`, `nextInt()`, `nextLong()`, `nextFloat()`, and `nextDouble()`, respectively. For the `next()` method, no conversion is performed. If the token does not match the expected type, a runtime exception `java.util.InputMismatchException` will be thrown.

```text
InputMismatchException
```

Both methods `next()` and `nextLine()` read a string. The `next()` method reads a string separated by delimiters and `nextLine()` reads a line ending with a line separator.

> **Note** The line-separator string is defined by the system. It is `\r\n` on Windows and `\n` on UNIX. To get the line separator on a particular platform, use

```java
String lineSeparator = System.getProperty("line.separator");
```

> If you enter input from a keyboard, a line ends with the *Enter* key, which corresponds to the `\n` character.

The token-based input method does not read the delimiter after the token. If the `nextLine()` method is invoked after a token-based input method, this method reads characters that start from this delimiter and end with the line separator. The line separator is read, but it is not part of the string returned by `nextLine()`.

Suppose a text file named **test.txt** contains a line

```text
34 567
```

After the following code is executed,

```java
Scanner input = new Scanner(new File("test.txt"));
int intValue = input.nextInt();
String line = input.nextLine();
```

`intValue` contains `34` and `line` contains the characters ' ', `5`, `6`, and `7`.

What happens if the input is *entered from the keyboard*? Suppose you enter `34`, press the *Enter* key, then enter `567` and press the *Enter* key for the following code:

```java
Scanner input = new Scanner(System.in);
int intValue = input.nextInt();
String line = input.nextLine();
```

You will get `34` in `intValue` and an empty string in `line`. Why? Here is the reason. The token-based input method `nextInt()` reads in `34` and stops at the delimiter, which in this case is a line separator (the *Enter* key). The `nextLine()` method ends after reading the line separator and returns the string read before the line separator. Since there are no characters before the line separator, `line` is empty. For this reason, *you should not use a line-based input after a token-based input.*

You can read data from a file or from the keyboard using the `Scanner` class. You can also scan data from a string using the `Scanner` class. For example, the following code:

<!-- LI p.485 -->

```java
Scanner input = new Scanner("13 14");
int sum = input.nextInt() + input.nextInt();
System.out.println("Sum is " + sum);
```

displays

```text
Sum is 27
```

### 12.11.5 Case Study: Replacing Text

Suppose you are to write a program named `ReplaceText` that replaces all occurrences of a string in a text file with a new string. The file name and strings are passed as command-line arguments as follows:

```text
java ReplaceText sourceFile targetFile oldString newString
```

For example, invoking

```text
java ReplaceText FormatString.java t.txt StringBuilder StringBuffer
```

replaces all the occurrences of `StringBuilder` by `StringBuffer` in the file **FormatString.java** and saves the new file in **t.txt**.

Listing 12.16 gives the program. The program checks the number of arguments passed to the `main` method (lines 7–11), checks whether the source and target files exist (lines 14–25), creates a `Scanner` for the source file (line 29), creates a `PrintWriter` for the target file (line 30), and repeatedly reads a line from the source file (line 33), replaces the text (line 34), and writes a new line to the target file (line 35).

**Listing 12.16**

```java
                  ReplaceText.java
import java.io.*;
import java.util.*;

public class ReplaceText {
  public static void main(String[] args) throws Exception {
    // Check command line parameter usage
    if (args.length != 4) {
      System.out.println(
          "Usage: java ReplaceText sourceFile targetFile oldStr newStr");
      System.exit(1);
    }

    // Check if source file exists
    File sourceFile = new File(args[0]);
    if (!sourceFile.exists()) {
      System.out.println("Source file " + args[0] + " does not exist");
      System.exit(2);
    }

    // Check if target file exists
    File targetFile = new File(args[1]);
    if (targetFile.exists()) {
      System.out.println("Target file " + args[1] + " already exists");
      System.exit(3);
    }

    try (
      // Create input and output files
      Scanner input = new Scanner(sourceFile);
      PrintWriter output = new PrintWriter(targetFile);
    ) {
      while (input.hasNext()) {
        String s1 = input.nextLine();
        String s2 = s1.replaceAll(args[2], args[3]);
        output.println(s2);
      }
    }
  }
}
```

<!-- LI p.486 -->

In a normal situation, the program is terminated after a file is copied. The program is terminated abnormally if the command-line arguments are not used properly (lines 7–11), if the source file does not exist (lines 14–18), or if the target file already exists (lines 22–25). The exit status codes 1, 2, and 3 are used to indicate these abnormal terminations (lines 10, 17, and 24).

**12.11.1** How do you create a `PrintWriter` to write data to a file? What is the

**Check**

reason to declare `throws Exception` in the main method in Listing 12.13,

**Point**

WriteData.java? What would happen if the `close()` method were not invoked in Listing 12.13? **12.11.2** Show the contents of the file **temp.txt** after the following program is executed:

```java
public class Test {
  public static void main(String[] args) throws Exception {
    java.io.PrintWriter output = new
      java.io.PrintWriter("temp.txt");
    output.printf("amount is %f %e\r\n", 32.32, 32.32);
    output.printf("amount is %5.4f %5.4e\r\n", 32.32, 32.32);
    output.printf("%6b\r\n", (1 > 2));
    output.printf("%6s\r\n", "Java");
    output.close();
  }
}
```

**12.11.3** Rewrite the code in the preceding question using a try-with-resources syntax. **12.11.4** How do you create a `Scanner` to read data from a file? What is the reason to define

`throws Exception` in the main method in Listing 12.15, ReadData.java? What would happen if the `close()` method were not invoked in Listing 12.15? **12.11.5** What will happen if you attempt to create a `Scanner` for a nonexistent file?

What will happen if you attempt to create a `PrintWriter` for an existing file? **12.11.6** Is the line separator the same on all platforms? What is the line separator on

Windows? **12.11.7** Suppose you enter `45 57.8 789`, then press the *Enter* key. Show the contents of

the variables after the following code is executed:

```java
Scanner input = new Scanner(System.in);
int intValue = input.nextInt();
double doubleValue = input.nextDouble();
String line = input.nextLine();
```

**12.11.8** Suppose you enter `45`, press the *Enter* key, enter `57.8`, press the *Enter* key,

and enter `789`, press the *Enter* key. Show the contents of the variables after the following code is executed:

```java
Scanner input = new Scanner(System.in);
int intValue = input.nextInt();
double doubleValue = input.nextDouble();
String line = input.nextLine();
```
