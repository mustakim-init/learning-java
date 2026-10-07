---
topic: string
lessons: "M8"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "126-146"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "4.3, 4.4, 4.5"
note: "4.5 Case Studies is optional in the mapping."
generated_by: tools/extract_refs.py
---
# Strings - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.126 -->

## 4.3 Character Data Type and Operations

*A character data type represents a single character.*

In addition to processing numeric values, you can process characters in Java. The character

**Key Point**

data type, `char`, is used to represent a single character. A character literal is enclosed in single quotation marks. Consider the following code:

```java
char letter = 'A';
char numChar = '4';
```

<!-- LI p.127 -->

The first statement assigns character `A` to the `char` variable `letter`. The second statement assigns digit character `4` to the `char` variable `numChar`.

> **Caution** A string literal must be enclosed in double quotation marks (" "). A character literal is a single character enclosed in single quotation marks (' '). Therefore, `"A"` is a string, but `'A'` is a character.

### 4.3.1 Unicode and ASCII Code

Computers use binary numbers internally. A character is stored in a computer as a sequence of 0s and 1s. Mapping a character to its binary representation is called *encoding*. There are different ways to encode a character. How characters are encoded is defined by an *encoding scheme*.

Java supports *Unicode*, an encoding scheme established by the Unicode Consortium to support the interchange, processing, and display of written texts in the world’s diverse lan-guages. Unicode was originally designed as a 16-bit character encoding. The primitive data type `char` was intended to take advantage of this design by providing a simple data type that could hold any character. However, it turned out that the 65,536 characters possible in a 16-bit encoding are not sufficient to represent all the characters in the world. The Unicode standard therefore has been extended to allow up to 1,112,064 characters. Those characters that go beyond the original 16-bit limit are called *supplementary characters*. Java supports the supplementary characters. The processing and representing of supplementary characters are beyond the scope of this book. For simplicity, this book considers only the original 16-bit Unicode characters. These characters can be stored in a `char` type variable.

A 16-bit Unicode takes two bytes, preceded by `\u`, expressed in four hexadecimal digits that run from `\u0000` to `\uFFFF`. Hexadecimal numbers are introduced in Appendix F, Number Systems. For example, the English word `welcome` is translated into Chinese using two characters,

. The Unicodes of these two characters are `\u6B22\u8FCE`. The Unicodes for the Greek letters a b g are `\u03b1 \u03b2 \u03b3` respectively.

Most computers use *ASCII* (*American Standard Code for Information Interchange*), an 8-bit encoding scheme, for representing all uppercase and lowercase letters, digits, punctuation marks, and control characters. Unicode includes ASCII code, with `\u0000` to `\u007F` corresponding to the 128 ASCII characters. Table 4.4 shows the ASCII code for some commonly used characters. Appendix B, “The ASCII Character Set,” gives a complete list of ASCII characters and their decimal and hexadecimal codes.

**Table 4.4 ASCII Code for Commonly Used Characters**

| Characters | Code Value in Decimal | Unicode Value |
|---|---|---|
| '0' to '9' | 48 to 57 | \u0030 to \u0039 |
| 'A' to 'Z' | 65 to 90 | \u0041 to \u005A |
| 'a' to 'z' | 97 to 122 | \u0061 to \u007A |

You can use ASCII characters such as `'X'`, `'1'`, and '$' in a Java program as well as Unicodes. Thus, for example, the following statements are equivalent:

```java
char letter = 'A';
char letter = '\u0041'; // Character A's Unicode is 0041
```

Both statements assign character `A` to the `char` variable `letter`.

> **Note** The increment and decrement operators can also be used on `char` variables to get the next or preceding Unicode character. For example, the following statements display character `b`:

```java
char ch = 'a';
System.out.println(++ch);
```

<!-- LI p.128 -->

### 4.3.2 Escape Sequences for Special Characters

Suppose you want to print a message with quotation marks in the output. Can you write a statement like this?

```java
System.out.println("He said "Java is fun"");
```

No, this statement has a compile error. The compiler thinks the second quotation character is the end of the string and does not know what to do with the rest of the characters.

To overcome this problem, Java uses a special notation to represent special characters, as listed in Table 4.5. This special notation, called an *escape sequence*, consists of a backslash (\) followed by a character or a combination of digits. For example, `\t` is an escape sequence for the Tab character, and an escape sequence such as `\u03b1` is used to represent a Unicode. The symbols in an escape sequence are interpreted as a whole rather than individually. An escape sequence is considered as a single character.

**Table 4.5 Escape Sequences**

| Escape Sequence | Name | Unicode Code | Decimal Value |
|---|---|---|---|
| \b | Backspace | \u0008 | 8 |
| \t | Tab | \u0009 | 9 |
| \n | Linefeed | \u000A | 10 |
| \f | Formfeed | \u000C | 12 |
| \r | Carriage Return | \u000D | 13 |
| \\ | Backslash | \u005C | 92 |
| \" | Double Quote | \u0022 | 34 |

So, now you can print the quoted message using the following statement:

```java
System.out.println("He said \"Java is fun\"");
```

The output is

```text
He said "Java is fun"
```

Note the symbols \ and " together represent one character.

The backslash \ is called an *escape character*. It is a special character. To display this character, you have to use an escape sequence \\. For example, the following code

```java
System.out.println("\\t is a tab character");
```

displays

```text
\t is a tab character
```

### 4.3.3 Casting between char and Numeric Types

A `char` can be cast into any numeric type, and vice versa. When an integer is cast into a `char`, only its lower 16 bits of data are used; the other part is ignored. For example:

```java
// Note a hex integer is written using prefix 0X
char ch = (char)0XAB0041; // The lower 16 bits hex code 0041 is
                          // assigned to ch
System.out.println(ch);   // ch is character A
```

When a floating-point value is cast into a `char`, the floating-point value is first cast into an `int`, which is then cast into a `char`.

<!-- LI p.129 -->

```java
char ch = (char)65.25;    // Decimal 65 is assigned to ch
System.out.println(ch);   // ch is character A
```

When a `char` is cast into a numeric type, the character’s Unicode is cast into the specified numeric type.

```java
int i = (int)'A'; // The Unicode of character A is assigned to i
System.out.println(i);  // i is 65
```

Implicit casting can be used if the result of a casting fits into the target variable. Otherwise, explicit casting must be used. For example, since the Unicode of `'a'` is `97`, which is within the range of a byte, these implicit castings are fine:

```java
byte b = 'a';
int i = 'a';
```

But the following statement is incorrect, because the Unicode `\uFFF4` cannot fit into a byte:

```java
byte b = '\uFFF4';
```

To force this assignment, use explicit casting, as follows:

```java
byte b = (byte)'\uFFF4';
```

Any positive integer between `0` and `FFFF` in hexadecimal can be cast into a character implicitly. Any number not in this range must be cast into a `char` explicitly. All numeric operators can be applied to `char` operands. A `char` operand is automatically cast into a number if the other operand is a number or a character. If a string is concatenated with a character, the character is converted into a string. For example, the following statements

```java
int i = '2' + '3'; // (int)'2' is 50 and (int)'3' is 51
System.out.println("i is " + i); // i is 101
int j = 2 + 'a'; // (int)'a' is 97
System.out.println("j is " + j); // j is 99
System.out.println(j + " is the Unicode for character ")
   + (char)j); // 99 is the Unicode for character c
System.out.println("Chapter " + '2');
```

display

```text
i is 101
j is 99
99 is the Unicode for character c
Chapter 2
```

### 4.3.4 Comparing and Testing Characters

Two characters can be compared using the relational operators just like comparing two numbers. This is done by comparing the Unicodes of the two characters. For example,

`'a' < 'b'` is true because the Unicode for `'a'` (`97`) is less than the Unicode for `'b'` (`98`). `'a' < 'A'` is false because the Unicode for `'a'` (`97`) is greater than the Unicode for `'A'` (`65`). `'1' < '8'` is true because the Unicode for `'1'` (`49`) is less than the Unicode for `'8'` (`56`).

Often in the program, you need to test whether a character is a number, a letter, an uppercase letter, or a lowercase letter. As given in Appendix B, the ASCII character set, that the Unicodes for lowercase letters are consecutive integers starting from the Unicode for `'a'`, then for `'b'`, `'c'`,. . . , and `'z'`. The same is true for the uppercase letters and for numeric characters. This property can be used to write the code to test characters. For example, the following code tests whether a character `ch` is an uppercase letter, a lowercase letter, or a digital character:

<!-- LI p.130 -->

```java
if (ch >= 'A' && ch <= 'Z')
  System.out.println(ch + " is an uppercase letter");
else if (ch >= 'a' && ch <= 'z')
  System.out.println(ch + " is a lowercase letter");
else if (ch >= '0' && ch <= '9')
  System.out.println(ch + " is a numeric character");
```

For convenience, Java provides the following methods in the `Character` class for testing characters as listed in Table 4.6. The `Character` class is defined in the `java.lang` package.

**Table 4.6 Methods in the Character Class**

| Method | Description |
|---|---|
| isDigit(ch) | Returns true if the specified character is a digit. |
| isLetter(ch) | Returns true if the specified character is a letter. |
| isLetterOrDigit(ch) | Returns true if the specified character is a letter or digit. |
| isLowerCase(ch) | Returns true if the specified character is a lowercase letter. |
| isUpperCase(ch) | Returns true if the specified character is an uppercase letter. |
| toLowerCase(ch) | Returns the lowercase of the specified character. |
| toUpperCase(ch) | Returns the uppercase of the specified character. |

For example,

```java
System.out.println("isDigit('a') is " + Character.isDigit('a'));
System.out.println("isLetter('a') is " + Character.isLetter('a'));
System.out.println("isLowerCase('a') is "
  + Character.isLowerCase('a'));
System.out.println("isUpperCase('a') is "
  + Character.isUpperCase('a'));
System.out.println("toLowerCase('T') is "
  + Character.toLowerCase('T'));
System.out.println("toUpperCase('q') is "
  + Character.toUpperCase('q'));
```

displays

```text
isDigit('a') is false
isLetter('a') is true
isLowerCase('a') is true
isUpperCase('a') is false
toLowerCase('T') is t
toUpperCase('q') is Q
```

**4.3.1** Which of the following are correct literals for characters?

**Check Point**

`'1'`, `'\u345dE'`, `'\u3fFa'`, `'\b'`, `'\t'` **4.3.2** How do you display the characters \ and "? **4.3.3** Use print statements to find out the ASCII code for `‘1’`, `‘A’`, `‘B’`, `‘a’`, and `‘b’`.

Use print statements to find out the character for the decimal codes `40`, `59`, `79`, `85`, and `90`. Use print statements to find out the character for the hexadecimal code `40`, `5A`, `71`, `72`, and `7A`. **4.3.4** Evaluate the following:

```java
int i = '1';
int j = '1' + '2' * ('4' − '3') + 'b' / 'a';
int k = 'a';
char c = 90;
```

<!-- LI p.131 -->

**4.3.5** Can the following conversions involving casting be allowed? If so, find the

converted result.

```java
char c = 'A';
int i = (int)c;

float f = 1000.34f;
int i = (int)f;

double d = 1000.34;
int i = (int)d;

int i = 97;
char c = (char)i;
```

**4.3.6** Show the output of the following program:

```java
public class Test {
  public static void main(String[] args) {
    char x = 'a';
    char y = 'c';
    System.out.println(++x);
    System.out.println(y++);
    System.out.println(x − y);
  }
}
```

**4.3.7** Write the code that generates a random lowercase letter. **4.3.8** Show the output of the following statements:

```java
System.out.println('a' < 'b');
System.out.println('a' <= 'A');
System.out.println('a' > 'b');
System.out.println('a' >= 'A');
System.out.println('a' == 'a');
System.out.println('a' != 'b');
```

## 4.4 The String Type

*A string is a sequence of characters.*

**Key**

The `char` type represents only one character. To represent a string of characters, use the data

**Point**

type called `String`. For example, the following code declares `message` to be a string with the value `“Welcome to Java"`.

```java
String message = "Welcome to Java";
```

`String` is a predefined class in the Java library, just like the classes `System` and `Scanner`.

**VideoNote**

The `String` type is not a primitive type. It is known as a *reference type*. Any Java class can

> Introduce strings and objects

be used as a reference type for a variable. The variable declared by a reference type is known as a reference variable that references an object. Here, `message` is a reference variable that references a string object with contents `Welcome to Java`.

Reference data types will be discussed in detail in Chapter 9, Objects and Classes. For the time being, you need to know only how to declare a `String` variable, how to assign a string to the variable, and how to use the methods in the `String` class. More details on using strings will be covered in Chapter 10.

Table 4.7 lists the `String` methods for obtaining string length, for accessing characters in the string, for concatenating string, for converting string to uppercases or lowercases, and for trimming a string.

<!-- LI p.132 -->

**Table 4.7 Simple Methods for** `String` **Objects**

| Method | Description |
|---|---|
| length() | Returns the number of characters in this string. |
| charAt(index) | Returns the character at the specified index from this string. |
| concat(s1) | Returns a new string that concatenates this string with string s1. |
| toUpperCase() | Returns a new string with all letters in uppercase. |
| toLowerCase() | Returns a new string with all letters in lowercase. |
| trim() | Returns a new string with whitespace characters trimmed on both sides. |

Strings are objects in Java. The methods listed in Table 4.7 can only be invoked from a specific string instance. For this reason, these methods are called *instance methods*. A non-instance method is called a *static method*. A static method can be invoked without using an object. All the methods defined in the `Math` class are static methods. They are not tied to a specific object instance. The syntax to invoke an instance method is `referenceVariable. methodName(arguments)`. A method may have many arguments or no arguments. For example, the `charAt(index)` method has one argument, but the `length()` method has no arguments. Recall that the syntax to invoke a static method is `ClassName.methodName(arguments)`. For example, the `pow` method in the `Math` class can be invoked using `Math. pow(2, 2.5)`.

### 4.4.1 Getting String Length

You can use the `length()` method to return the number of characters in a string. For example, the following code

```java
String message = "Welcome to Java";
System.out.println("The length of " + message + " is "
  + message.length());
```

displays

```text
The length of Welcome to Java is 15
```

> **Note** When you use a string, you often know its literal value. For convenience, Java allows you to use the *string literal* to refer directly to strings without creating new variables. Thus, `"Welcome to Java".length()` is correct and returns `15`. Note that "" denotes an *empty string* and `"".length()` is `0`.

### 4.4.2 Getting Characters from a String

The `s.charAt(index)` method can be used to retrieve a specific character in a string `s`, where the index is between `0` and `s.length()–1`. For example, `message.charAt(0)` returns the character `W`, as shown in Figure 4.1. Note that the index for the first character in the string is `0`.

```text
charAt(index)
```

```text
message.charAt(0)
                    message.length() is 15
                                             message.charAt(14)
```

**Figure 4.1** The characters in a `String` object can be accessed using its index.

<!-- LI p.133 -->

> **Caution** Attempting to access characters in a string `s` out of bounds is a common programming error. To avoid it, make sure that you do not use an index beyond `s.length()–1`. For example, `s.charAt(s.length())` would cause a `StringIndexOutOfBoundsException`.

### 4.4.3 Concatenating Strings

You can use the `concat` method to concatenate two strings. The statement given below, for example, concatenates strings `s1` and `s2` into `s3`:

```java
String s3 = s1.concat(s2);
                                                                         s1.concat(s2)
```

Because string concatenation is heavily used in programming, Java provides a convenient way to accomplish it. You can use the plus (+) operator to concatenate two strings, so the previous statement is equivalent to

```java
String s3 = s1 + s2;
                                                                         s1 + s2
```

The following code combines the strings `message`, `" and "`, and `"HTML"` into one string:

```java
String myString = message + " and " + "HTML";
```

Recall that the + operator can also concatenate a number or a character with a string. In this case, the number or character is converted into a string then concatenated. Note at least one of the operands must be a string in order for concatenation to take place. If one of the operands is a nonstring (e.g., a number), the nonstring value is converted into a string and concatenated with the other string. Here are some examples:

```java
// Three strings are concatenated
String message = "Welcome " + "to " + "Java";

// String Chapter is concatenated with number 2
String s = "Chapter" + 2; // s becomes Chapter2

// String Supplement is concatenated with character B
String s1 = "Supplement" + 'B'; // s1 becomes SupplementB
```

If neither of the operands is a string, the plus sign (+) is the addition operator that adds two numbers.

The augmented += operator can also be used for string concatenation. For example, the following code appends the string `" and Java is fun"` with the string `"Welcome to Java"` in `message`.

```java
message += " and Java is fun";
```

So the new `message` is `"Welcome to Java and Java is fun."` If `i = 1` and `j = 2`, what is the output of the following statement?

```java
System.out.println("i + j is " + i + j);
```

The output is `"i + j is 12"` because `"i + j is"` is concatenated with the value of `i` first. To force `i + j` to be executed first, enclose `i + j` in the parentheses, as follows:

```java
System.out.println("i + j is " + (i + j));
```

### 4.4.4 Converting Strings

The `toLowerCase()` method returns a new string with all lowercase letters, and the `toUpperCase()` method returns a new string with all uppercase letters. For example,

`"Welcome".toLowerCase()` returns a new string `welcome`.

```text
toLowerCase()
```

`"Welcome".toUpperCase()` returns a new string `WELCOME`.

```text
toUpperCase()
```

<!-- LI p.134 -->

The `trim()` method returns a new string by eliminating whitespace characters from both ends of the string. The characters ' ', `\t`, `\f`, `\r`, or `\n` are known as *whitespace characters*. For example,

`"\t Good Night \n".trim()` returns a new string `Good Night`.

### 4.4.5 Reading a String from the Console

To read a string from the console, invoke the `next()` method on a `Scanner` object. For example, the following code reads three strings from the keyboard:

```java
 Scanner input = new Scanner(System.in);
 System.out.print("Enter three words separated by spaces: ");
 String s1 = input.next();
 String s2 = input.next();
 String s3 = input.next();
 System.out.println("s1 is " + s1);
 System.out.println("s2 is " + s2);
 System.out.println("s3 is " + s3);

Enter three words separated by spaces: Welcome to Java
s1 is Welcome
s2 is to
s3 is Java
```

The `next()` method reads a string that ends with a whitespace character. You can use the `nextLine()` method to read an entire line of text. The `nextLine()` method reads a string that ends with the *Enter* key pressed. For example, the following statements read a line of text:

```java
 Scanner input = new Scanner(System.in);
 System.out.println("Enter a line: ");
 String s = input.nextLine();
 System.out.println("The line entered is " + s);

Enter a line: Welcome to Java
The line entered is Welcome to Java
```

For convenience, we call the input using the methods `next()`, `nextByte()`, `nextShort()`, `nextInt()`, `nextLong()`, `nextFloat()`, and `nextDouble()` the token-based input, because they read individual elements separated by whitespace characters rather than an entire line. The `nextLine()` method is called a line-based input.

**Important Caution**

> To *avoid input errors*, do not use a line-based input after a token-based input in the program. The reasons will be explained in Section 12.11.4, "How Does `Scanner` Work?"

### 4.4.6 Reading a Character from the Console

To read a character from the console, use the `nextLine()` method to read a string and then invoke the `charAt(0)` method on the string to return a character. For example, the following code reads a character from the keyboard:

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter a character: ");
String s = input.nextLine();
char ch = s.charAt(0);
System.out.println("The character entered is " + ch);
```

<!-- LI p.135 -->

### 4.4.7 Comparing Strings

The `String` class contains the methods, as listed in Table 4.8, for comparing two strings.

**Table 4.8 Comparison Methods for** `String` **Objects**

| Method | Description |
|---|---|
| equals(s1) | Returns true if this string is equal to string s1. |
| equalsIgnoreCase(s1) | Returns true if this string is equal to string s1; it is case insensitive. |
| compareTo(s1) | Returns an integer greater than 0, equal to 0, or less than 0 to indicate whether this string is greater than, equal to, or less than s1. |
| compareToIgnoreCase(s1) | Same as compareTo except that the comparison is case insensitive. |
| startsWith(prefix) | Returns true if this string starts with the specified prefix. |
| endsWith(suffix) | Returns true if this string ends with the specified suffix. |
| contains(s1) | Returns true if s1 is a substring in this string. |

How do you compare the contents of two strings? You might attempt to use the == operator, as follows:

```java
if (string1 == string2)
                                                                         ==
  System.out.println("string1 and string2 are the same object");
else
  System.out.println("string1 and string2 are different objects");
```

However, the == operator checks only whether `string1` and `string2` refer to the same object; it does not tell you whether they have the same contents. Therefore, you cannot use the == operator to find out whether two string variables have the same contents. Instead, you should use the `equals` method. The following code, for instance, can be used to compare two strings:

```java
if (string1.equals(string2))
                                                                         string1.
  System.out.println("string1 and string2 have the same contents");
                                                                         equals(string2)
else
  System.out.println("string1 and string2 are not equal");
```

For example, the following statements display `true` then `false:`

```java
String s1 = "Welcome to Java";
String s2 = "Welcome to Java";
String s3 = "Welcome to C++";
System.out.println(s1.equals(s2)); // true
System.out.println(s1.equals(s3)); // false
```

The `compareTo` method can also be used to compare two strings. For example, consider the following code:

```text
s1.compareTo(s2)
                                                                         s1.compareTo(s2)
```

The method returns the value `0` if `s1` is equal to `s2`, a value less than `0` if `s1` is lexicographically (i.e., in terms of Unicode ordering) less than `s2`, and a value greater than `0` if `s1` is lexicographically greater than `s2`.

The actual value returned from the `compareTo` method depends on the offset of the first two distinct characters in `s1` and `s2` from left to right. For example, suppose `s1` is `abc` and `s2` is `abg`, and `s1.compareTo(s2)` returns `−4`. The first two characters (`a` vs. `a`) from `s1` and `s2` are compared. Because they are equal, the second two characters (`b` vs. `b`) are compared. Because they are also equal, the third two characters (`c` vs. `g`) are compared. Since the character `c` is `4` less than `g`, the comparison returns `−4`.

<!-- LI p.136 -->

> **Caution** Syntax errors will occur if you compare strings by using relational operators >, >=, <, or <=. Instead, you have to use `s1.compareTo(s2)`.

> **Note** The `equals` method returns `true` if two strings are equal, and `false` if they are not. The `compareTo` method returns `0`, a positive integer, or a negative integer, depending on whether one string is equal to, greater than, or less than the other string.

The `String` class also provides the `equalsIgnoreCase` and `compareToIgnoreCase` methods for comparing strings. The `equalsIgnoreCase` and `compareToIgnoreCase` methods ignore the case of the letters when comparing two strings. You can also use `str. startsWith(prefix)` to check whether string `str` starts with a specified prefix, `str.end-sWith(suffix)` to check whether string `str` ends with a specified suffix, and `str.contains(s1)` to check whether string `str` contains string `s1`. For example,

`"Welcome to Java".startsWith("We")` returns `true`. `"Welcome to Java".startsWith("we")` returns `false`. `"Welcome to Java".endsWith("va")` returns `true`. `"Welcome to Java".endsWith("v")` returns `false`. `"Welcome to Java".contains("to")` returns `true`. `"Welcome to Java".contains("To")` returns `false`.

Listing 4.2 gives a program that prompts the user to enter two cities and displays them in alphabetical order.

**Listing 4.2 OrderTwoCities.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class OrderTwoCities {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    // Prompt the user to enter two cities
    System.out.print("Enter the first city: ");
    String city1 = input.nextLine();
    System.out.print("Enter the second city: ");
    String city2 = input.nextLine();

    if (city1.compareTo(city2) < 0)
      System.out.println("The cities in alphabetical order are " +
        city1 + " " + city2);
    else
      System.out.println("The cities in alphabetical order are " +
        city2 + " " + city1);
  }
}

 Enter the first city: New York
 Enter the second city: Boston
 The cities in alphabetical order are Boston New York
```

The program reads two strings for two cities (lines 9 and 11). If `input.nextLine()` is replaced by `input.next()` (line 9), you cannot enter a string with spaces for `city1`. Since a city name may contain multiple words separated by spaces, the program uses the `nextLine` method to read a string (lines 9 and 11). Invoking `city1.compareTo(city2)` compares two strings `city1` with `city2` (line 13). A negative return value indicates that `city1` is less than `city2`.

<!-- LI p.137 -->

### 4.4.8 Obtaining Substrings

You can obtain a single character from a string using the `charAt` method. You can also obtain a substring from a string using the `substring` method (see Figure 4.2) in the `String` class, as given in Table 4.9.

For example,

```java
String message = "Welcome to Java";
message = message.substring(0,11) + "HTML";
```

The string `message` now becomes `Welcome` to `HTML`.

**Table 4.9 The** `String` **Class Contains the Methods for Obtaining Substrings**

| Method | Description |
|---|---|
| substring(beginIndex) | Returns this string’s substring that begins with the character at the specified beginIndex and extends to the end of the string, as shown in Figure 4.2. |
| substring(beginIndex, endIndex) | Returns this string’s substring that begins at the specified beginIndex and extends to the character at index endIndex – 1, as shown in Figure 4.2. Note the character at endIndex is not part of the substring. |

```text
message.substring(0, 11)
                          message.substring(11)
```

**Figure 4.2** The `substring` method obtains a substring from a string.

> **Note** If `beginIndex` is `endIndex`, `substring(beginIndex, endIndex)` returns an empty string with length `0`. If `beginIndex` > `endIndex`, it would be a runtime error.

```text
beginIndex <= endIndex
```

### 4.4.9 Finding a Character or a Substring in a String

The `String` class provides several versions of `indexOf` and `lastIndexOf` methods to find a character or a substring in a string, as listed in Table 4.10.

**Table 4.10 The** `String` **Class Contains the Methods for Finding Substrings**

| Method | Description |
|---|---|
| indexOf(ch) | Returns the index of the first occurrence of ch in the string. Returns −1 if not matched. |
| indexOf(ch, fromIndex) | Returns the index of the first occurrence of ch after fromIndex in the string. Returns −1 if not matched. |
| indexOf(s) | Returns the index of the first occurrence of string s in this string. Returns −1 if not matched. |
| indexOf(s, fromIndex) | Returns the index of the first occurrence of string s in this string after fromIndex. Returns −1 if not matched. |
| lastIndexOf(ch) | Returns the index of the last occurrence of ch in the string. Returns −1 if not matched. |
| lastIndexOf(ch, fromIndex) | Returns the index of the last occurrence of ch before fromIndex in this string. Returns −1 if not matched. |
| lastIndexOf(s) | Returns the index of the last occurrence of string s. Returns −1 if not matched. |
| lastIndexOf(s, fromIndex) | Returns the index of the last occurrence of string s before fromIndex. Returns −1 if not matched. |

<!-- LI p.138 -->

For example,

`"Welcome to Java".indexOf('W')` returns `0`.

```text
IndexOf
```

`"Welcome to Java".indexOf('o')` returns `4`. `"Welcome to Java".indexOf('o', 5)` returns `9`. `"Welcome to Java".indexOf("come")` returns `3`. `"Welcome to Java".indexOf("Java", 5)` returns `11`. `"Welcome to Java".indexOf("java", 5)` returns `−1`.

`"Welcome to Java".lastIndexOf('W')` returns `0`.

```text
lastIndexOf
```

`"Welcome to Java".lastIndexOf('o')` returns `9`. `"Welcome to Java".lastIndexOf('o', 5)` returns `4`. `"Welcome to Java".lastIndexOf("come")` returns `3`. `"Welcome to Java".lastIndexOf("Java", 5)` returns `−1`. `"Welcome to Java".lastIndexOf("Java")` returns `11`.

Suppose that a string `s` contains the first name and last name separated by a space. You can use the following code to extract the first name and last name from the string:

```java
int k = s.indexOf(' ');
String firstName = s.substring(0, k);
String lastName = s.substring(k + 1);
```

For example, if `s` is `Kim Jones`, the following diagram illustrates how the first name and last name are extracted.

### 4.4.10 Conversion between Strings and Numbers

You can convert a numeric string into a number. To convert a string into an `int` value, use the `Integer.parseInt` method, as follows:

```java
int intValue = Integer.parseInt(intString);
```

where `intString` is a numeric string such as `"123"`.

To convert a string into a `double` value, use the `Double.parseDouble` method, as follows:

```text
Double.parseDouble
```

```java
double doubleValue = Double.parseDouble(doubleString);
```

where `doubleString` is a numeric string such as `"123.45"`. If the string is not a numeric string, the conversion would cause a runtime error. The `Integer` and `Double` classes are both included in the `java.lang` package, and thus they are automatically imported. You can convert a number into a string; simply use the string concatenating operator as follows:

```java
String s = number + "";
```

**4.4.1** Suppose `s1`, `s2`, and `s3` are three strings, given as follows:

**Check Point**

```java
String s1 = "Welcome to Java";
String s2 = "Programming is fun";
String s3 = "Welcome to Java";
```

<!-- LI p.139 -->

What are the results of the following expressions?

(l) `s1.lastIndexOf("o", 15)`

(a) `s1 == s2`

(b) `s2 == s3`

(m) `s1.length()`

(n) `s1.substring(5)`

(c) `s1.equals(s2)`

(o) `s1.substring(5, 11)`

(d) `s1.equals(s3)`

(p) `s1.startsWith("Wel")`

(e) `s1.compareTo(s2)`

(q) `s1.endsWith("Java")`

(f) `s2.compareTo(s3)`

(g) `s2.compareTo(s2)`

(r) `s1.toLowerCase()`

(h) `s1.charAt(0)`

(s) `s1.toUpperCase()`

(i) `s1.indexOf('j')`

(t) `s1.concat(s2)`

(j) `s1.indexOf("to")`

(u) `s1.contain(s2)`

(k) `s1.lastIndexOf('a')`

(v) `"\t Wel \t".trim()`

**4.4.2** Suppose `s1` and `s2` are two strings. Which of the following statements or expressions are incorrect?

```java
String s = "Welcome to Java";
String s3 = s1 + s2;
s3 = s1 − s2;
s1 == s2;
s1 >= s2;
s1.compareTo(s2);
int i = s1.length();
char c = s1(0);
char c = s1.charAt(s1.length());
```

**4.4.3** Show the output of the following statements (write a program to verify your results):

```java
System.out.println("1" + 1);
System.out.println('1' + 1);
System.out.println("1" + 1 + 1);
System.out.println("1" + (1 + 1));
System.out.println('1' + 1 + 1);
```

**4.4.4** Evaluate the following expressions (write a program to verify your results):

```text
1 + "Welcome " + 1 + 1
1 + "Welcome " + (1 + 1)
1 + "Welcome " + ('\u0001' + 1)
1 + "Welcome " + 'a' + 1
```

**4.4.5** Let `s1` be `" Welcome "` and `s2` be `" welcome "`. Write the code for the following statements:

(a) Check whether `s1` is equal to `s2` and assign the result to a Boolean variable

`isEqual`. (b) Check whether `s1` is equal to `s2`, ignoring case, and assign the result to a Bool-

ean variable `isEqual`. (c) Compare `s1` with `s2` and assign the result to an `int` variable `x`. (d) Compare `s1` with `s2`, ignoring case, and assign the result to an `int` variable `x`. (e) Check whether `s1` has the prefix `AAA` and assign the result to a Boolean

variable `b`. (f) Check whether `s1` has the suffix `AAA` and assign the result to a Boolean

variable `b`.

<!-- LI p.140 -->

(g) Assign the length of `s1` to an `int` variable `x`. (h) Assign the first character of `s1` to a `char` variable `x`. (i) Create a new string `s3` that combines `s1` with `s2`. (j) Create a substring of `s1` starting from index `1`. (k) Create a substring of `s1` from index `1` to index `4`. (l) Create a new string `s3` that converts `s1` to lowercase. (m) Create a new string `s3` that converts `s1` to uppercase. (n) Create a new string `s3` that trims whitespaces on both ends of `s1`. (o) Assign the index of the first occurrence of the character `e` in `s1` to an `int` variable `x`. (p) Assign the index of the last occurrence of the string `abc` in `s1` to an `int` variable `x`.

**4.4.6** Write one statement to return the number of digits in an integer `i`. **4.4.7** Write one statement to return the number of digits in a double value `d`.

## 4.5 Case Studies

*Strings are fundamental in programming. The ability to write programs using strings is essential in learning Java programming.*

You will frequently use strings to write useful programs. This section presents three examples

**Key Point**

of solving problems using strings.

### 4.5.1 Case Study: Guessing Birthdays

You can find out the date of the month when your friend was born by asking five questions. Each question asks whether the day is in one of the five sets of numbers.

1

The birthday is the sum of the first numbers in the sets where the day appears. For example, if the birthday is `19`, it appears in Set1, Set2, and Set5. The first numbers in these three sets are `1`, `2`, and `16`. Their sum is `19`.

Listing 4.3 gives a program that prompts the user to answer whether the day is in Set1 (lines 41–44), in Set2 (lines 50–53), in Set3 (lines 59–62), in Set4 (lines 68–71), and in Set5 (lines 77–80). If the number is in the set, the program adds the first number in the set to `day` (lines 47, 56, 65, 74, and 83).

**Listing 4.3 GuessBirthday.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class GuessBirthday {
  public static void main(String[] args) {
    String set1 =
      " 1 3 5 7\n" +
      " 9 11 13 15\n" +
      "17 19 21 23\n" +
      "25 27 29 31";

    String set2 =
      " 2 3 6 7\n" +
      "10 11 14 15\n" +
      "18 19 22 23\n" +
      "26 27 30 31";

    String set3 =
      " 4 5 6 7\n" +
      "12 13 14 15\n" +
      "20 21 22 23\n" +
      "28 29 30 31";

    String set4 =
      " 8 9 10 11\n" +
      "12 13 14 15\n" +
      "24 25 26 27\n" +
      "28 29 30 31";

    String set5 =
      "16 17 18 19\n" +
      "20 21 22 23\n" +
      "24 25 26 27\n" +
      "28 29 30 31";

    int day = 0;

    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Prompt the user to answer questions
    System.out.print("Is your birthday in Set1?\n");
    System.out.print(set1);
    System.out.print("\nEnter 0 for No and 1 for Yes: ");
    int answer = input.nextInt();

    if (answer == 1)
      day += 1;

    // Prompt the user to answer questions
    System.out.print("\nIs your birthday in Set2?\n");
    System.out.print(set2);
    System.out.print("\nEnter 0 for No and 1 for Yes: ");
    answer = input.nextInt();

    if (answer == 1)
      day += 2;

    // Prompt the user to answer questions
    System.out.print("\nIs your birthday in Set3?\n");
    System.out.print(set3);
    System.out.print("\nEnter 0 for No and 1 for Yes: ");
    answer = input.nextInt();

    if (answer == 1)
      day += 4;

    // Prompt the user to answer questions
    System.out.print("\nIs your birthday in Set4?\n");
    System.out.print(set4);
    System.out.print("\nEnter 0 for No and 1 for Yes: ");
    answer = input.nextInt();

    if (answer == 1)
      day += 8;

    // Prompt the user to answer questions
    System.out.print("\nIs your birthday in Set5?\n");
    System.out.print(set5);
    System.out.print("\nEnter 0 for No and 1 for Yes: ");
    answer = input.nextInt();

    if (answer == 1)
      day += 16;

    System.out.println("\nYour birthday is " + day + "!");
  }
}
```

<!-- LI p.142 -->

```text
Is your birthday in Set1?
  1  3   5  7
 9 11 13 15
17 19 21 23
25 27 29 31
Enter 0 for No and 1 for Yes: 1

Is your birthday in Set2?
 2  3  6  7
10 11 14 15
18 19 22 23
26 27 30 31
Enter 0 for No and 1 for Yes: 1

Is your birthday in Set3?
 4  5  6  7
12 13 14 15
20 21 22 23
28 29 30 31
Enter 0 for No and 1 for Yes: 0

Is your birthday in Set4?
 8  9 10 11
12 13 14 15
24 25 26 27
28 29 30 31
Enter 0 for No and 1 for Yes: 0

Is your birthday in Set5?
16 17 18 19
20 21 22 23
24 25 26 27
28 29 30 31
Enter 0 for No and 1 for Yes: 1
Your birthday is 19!
               day
                        answer
                                       output
35
               0
44
                        1
47
               1
53
                        1
56
               3
62
                        0
71
                        0
80
                        1
83
               19
85
                                       Your birthday is 19!
```

<!-- LI p.143 -->

**line#**

This game is easy to program. You may wonder how the game was created. The mathematics behind the game is actually quite simple. The numbers are not grouped together by accident— the way they are placed in the five sets is deliberate. The starting numbers in the five sets are `1`, `2`, `4`, `8`, and `16`, which correspond to `1`, `10`, `100`, `1000`, and `10000` in binary (binary numbers are introduced in Appendix F, Number Systems). A binary number for decimal integers between `1` and `31` has at most five digits, as shown in Figure 4.3a. Let it be *b*5*b*4*b*3*b*2*b*1. Thus, *b*5*b*4*b*3*b*2*b*1 = *b*5 0000 + *b*4 000 + *b*3 00 + *b*2 0 + *b*1, as shown in Figure 4.3b. If a day’s binary number has a digit `1` in *bk*, the number should appear in Set*k*. For example, number `19` is binary `10011`, so it appears in Set1, Set2, and Set5. It is binary `1 + 10 + 10000 = 10011` or decimal `1 + 2 + 16 = 19`. Number `31` is binary `11111`, so it appears in Set1, Set2, Set3, Set4, and Set5. It is binary `1 + 10 + 100 + 1000 + 10000 = 11111` or decimal `1 + 2 + 4 + 8 + 16 = 31`.

*b*5 *b*4 *b*3 *b*2 1 1 *b*1 1 *b*5 *b*4 *b*3 *b*2 *b*1

**Figure 4.3** (a) A number between `1` and `31` can be represented using a five-digit binary number. (b) A five-digit binary number can be obtained by adding binary numbers `1`, `10`, `100`, `1000`, or `10000`.

### 4.5.2 Case Study: Converting a Hexadecimal Digit to a Decimal Value

The hexadecimal number system has 16 digits: 0–9, A–F. The letters A, B, C, D, E, and F correspond to the decimal numbers 10, 11, 12, 13, 14, and 15. We now write a program that prompts the user to enter a hex digit and display its corresponding decimal value, as given in Listing 4.4.

**Listing 4.4 HexDigit2Dec.java**

```java
1  import java.util.Scanner;
```

**VideoNote**

> Convert hex to decimal

```text
2
```

```java
public class HexDigit2Dec {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter a hex digit: ");
    String hexString = input.nextLine();

    // Check if the hex string has exactly one character
    if (hexString.length() != 1) {
      System.out.println("You must enter exactly one character");
      System.exit(1);
    }

    // Display decimal value for the hex digit
    char ch = Character.toUpperCase(hexString.charAt(0));
    if ('A' <= ch && ch <= 'F') {
      int value = ch − 'A' + 10;
      System.out.println("The decimal value for hex digit "
        + ch + " is " + value);
    }
    else if (Character.isDigit(ch)) {
      System.out.println("The decimal value for hex digit "
        + ch + " is " + ch);
    }
    else {
      System.out.println(ch + " is an invalid input");
    }
  }
}
```

<!-- LI p.144 -->

```text
Enter a hex digit: AB7C
You must enter exactly one character
```

```text
Enter a hex digit: B
The decimal value for hex digit B is 11
```

```text
Enter a hex digit: 8
The decimal value for hex digit 8 is 8
```

```text
Enter a hex digit: T
T is an invalid input
```

The program reads a string from the console (line 7) and checks if the string contains a single character (line 10). If not, report an error and exit the program (line 12).

The program invokes the `Character.toUpperCase` method to obtain the character `ch` as an uppercase letter (line 16). If `ch` is between `'A'` and `'F'` (line 17), the corresponding decimal value is `ch – 'A' + 10` (line 18). Note `ch – 'A'` is `0` if `ch` is `'A'`, `ch – 'A'` is `1` if `ch` is `'B'`, and so on. When two characters perform a numerical operation, the characters' Unicodes are used in the computation.

The program invokes the `Character.isDigit(ch)` method to check if `ch` is between `'0'` and `'9'` (line 22). If so, the corresponding decimal digit is the same as `ch` (lines 23 and 24).

If `ch` is not between `'A'` and `'F'` nor a digit character, the program displays an error message (line 27).

<!-- LI p.145 -->

### 4.5.3 Case Study: Revising the Lottery Program Using Strings

The lottery program in Listing 3.8, Lottery.java, generates a random two-digit number, prompts the user to enter a two-digit number, and determines whether the user wins according to the following rule:

1. If the user input matches the lottery number in the exact order, the award is $10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.

The program in Listing 3.8 uses an integer to store the number. Listing 4.5 gives a new program that generates a random two-digit string instead of a number, and receives the user input as a string instead of a number.

**Listing 4.5 LotteryUsingStrings.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class LotteryUsingStrings {
  public static void main(String[] args) {
    // Generate a lottery as a two-digit string
    String lottery = "" + (int)(Math.random() * 10)
      + (int)(Math.random() * 10);

    // Prompt the user to enter a guess
    Scanner input = new Scanner(System.in);
    System.out.print("Enter your lottery pick (two digits): ");
    String guess = input.nextLine();

    // Get digits from lottery
    char lotteryDigit1 = lottery.charAt(0);
    char lotteryDigit2 = lottery.charAt(1);

    // Get digits from guess
    char guessDigit1 = guess.charAt(0);
    char guessDigit2 = guess.charAt(1);

    System.out.println("The lottery number is " + lottery);

    // Check the guess
    if (guess.equals(lottery))
      System.out.println("Exact match: you win $10,000");
    else if (guessDigit2 == lotteryDigit1
          && guessDigit1 == lotteryDigit2)
      System.out.println("Match all digits: you win $3,000");
    else if (guessDigit1 == lotteryDigit1
          || guessDigit1 == lotteryDigit2
          || guessDigit2 == lotteryDigit1
          || guessDigit2 == lotteryDigit2)
      System.out.println("Match one digit: you win $1,000");
    else
      System.out.println("Sorry, no match");
  }
}


 Enter your lottery pick (two digits): 00
 The lottery number is 00
 Exact match: you win $10,000
Enter your lottery pick (two digits): 45
The lottery number is 54
Match all digits: you win $3,000


Enter your lottery pick: 23
The lottery number is 34
Match one digit: you win $1,000


Enter your lottery pick: 23
The lottery number is 14
Sorry: no match
```

<!-- LI p.146 -->

The program generates two random digits and concatenates them into the string `lottery` (lines 6 and 7). After this, `lottery` contains two random digits.

The program prompts the user to enter a guess as a two-digit string (line 12) and checks the guess against the lottery number in this order:

- First, check whether the guess matches the lottery exactly (line 25).
- If not, check whether the reversal of the guess matches the lottery (line 27).
- If not, check whether one digit is in the lottery (lines 30–33).
- If not, nothing matches and display “Sorry, no match” (line 36).

**4.5.1** If you run Listing 4.3 GuessBirthday.java with input `1` for Set1, Set3, and Set4 and

**Check**

`0` for Set2 and Set5, what will be the birthday?

**Point**

**4.5.2** If you enter a lowercase letter such as `b`, the program in Listing 4.4 displays `B` is `11`.

Revise the code as to display `b` is `11`. **4.5.3** What would be wrong if lines 6 and 7 are in Listing 4.5 replaced by the following

code?

```java
String lottery = "" + (int)(Math.random() * 100);
```
