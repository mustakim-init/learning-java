---
book: "Java: The Complete Reference, 12th ed. (Schildt)"
chapter: "ch21 java.util Part 2: More Utility Classes"
printed_pages: "706-712"
pdf_offset: "pdf page = printed page + 35"
generated_by: tools/extract_refs.py --full
---
# ch21 java.util Part 2: More Utility Classes

<!-- CR p.706 -->

## Miscellaneous Utility Classes and Interfaces

In addition to the classes already discussed, `java.util` includes the following classes:

| Base64 | Supports Base64 encoding. Encoder and Decoder nested classes are also defined. |
|---|---|
| DoubleSummaryStatistics | Supports the compilation of double values. The following statistics are available: average, minimum, maximum, count, and sum. |
| EventListenerProxy | Extends the EventListener class to allow additional parameters. See Chapter 25 for a discussion of event listeners. |
| EventObject | The superclass for all event classes. Events are discussed in Chapter 25. |
| FormattableFlags | Defines formatting flags that are used with the Formattable interface. |
| HexFormat | Provides various conversions to and from hexadecimal strings and digits. It is a value-based class. |
| IntSummaryStatistics | Supports the compilation of int values. The following statistics are available: average, minimum, maximum, count, and sum. |
| Objects | Various methods that operate on objects. |
| PropertyPermission | Manages property permissions. |
| ServiceLoader | Provides a means of finding service providers. |
| StringJoiner | Supports the concatenation of CharSequences, which may include a separator, a prefix, and a suffix. |
| UUID | Encapsulates and manages Universally Unique Identifiers (UUIDs). |

The following interfaces are also packaged in `java.util`:

| EventListener | Indicates that a class is an event listener. Events are discussed in Chapter 25. |
|---|---|
| Formattable | Enables a class to provide custom formatting. |

<!-- CR p.707 -->

## The java.util Subpackages

Java defines the following subpackages of `java.util`:

- java.util.concurrent
- java.util.concurrent.atomic
- java.util.concurrent.locks
- java.util.function
- java.util.jar
- java.util.logging
- java.util.prefs
- java.util.random
- java.util.regex
- java.util.spi
- java.util.stream
- java.util.zip

Except as otherwise noted, all are part of the `java.base` module. Each is briefly examined here.

### java.util.concurrent, java.util.concurrent.atomic, and java.util.concurrent.locks

The `java.util.concurrent` package along with its two subpackages, `java.util.concurrent .atomic` and `java.util.concurrent.locks`, support concurrent programming. These packages provide a high-performance alternative to using Java’s built-in synchronization features when thread-safe operation is required. The `java.util.concurrent` package also provides the Fork/ Join Framework. These packages are examined in detail in Chapter 29.

### java.util.function

The `java.util.function` package defines several predefined functional interfaces that you can use when creating lambda expressions or method references. They are also widely used throughout the Java API. The functional interfaces defined by `java.util.function` are shown in Table 21-18 along with a synopsis of their abstract methods. Be aware that some of these interfaces also define default or static methods that supply additional functionality. You will want to explore them fully on your own. (For a discussion of the use of functional interfaces, see Chapter 15.)

### java.util.jar

The `java.util.jar` package provides the ability to read and write Java Archive (JAR) files.

<!-- CR p.708 -->

| Interface | Abstract Method |
|---|---|
| BiConsumer<T, U> | void accept(T tVal, U uVal) Description: Acts on tVal and uVal. |
| BiFunction<T, U, R> | R apply(T tVal, U uVal) Description: Acts on tVal and uVal and returns the result. |
| BinaryOperator<T> | T apply(T val1, T val2) Description: Acts on two objects of the same type and returns the result, which is also of the same type. |
| BiPredicate<T, U> | boolean test(T tVal, U uVal) Description: Returns true if tVal and uVal satisfy the condition defined by test( ) and false otherwise. |
| BooleanSupplier | boolean getAsBoolean( ) Description: Returns a boolean value. |
| Consumer<T> | void accept(T val) Description: Acts on val. |
| DoubleBinaryOperator | double applyAsDouble(double val1, double val2) Description: Acts on two double values and returns a double result. |
| DoubleConsumer | void accept(double val) Description: Acts on val. |
| DoubleFunction<R> | R apply(double val) Description: Acts on a double value and returns the result. |
| DoublePredicate | boolean test(double val) Description: Returns true if val satisfies the condition defined by test( ) and false otherwise. |
| DoubleSupplier | double getAsDouble( ) Description: Returns a double result. |
| DoubleToIntFunction | int applyAsInt(double val) Description: Acts on a double value and returns the result as an int. |
| DoubleToLongFunction | long applyAsLong(double val) Description: Acts on a double value and returns the result as a long. |
| DoubleUnaryOperator | double applyAsDouble(double val) Description: Acts on a double and returns a double result. |
| Function<T, R> | R apply(T val) Description: Acts on val and returns the result. |
| IntBinaryOperator | int applyAsInt(int val1, int val2) Description: Acts on two int values and returns an int result. |

**Table 21-18**

Functional Interfaces Defined by `java.util.function` and Their Abstract Methods *(continued)*

<!-- CR p.709 -->

| Interface | Abstract Method |
|---|---|
| IntConsumer | int accept(int val) Description: Acts on val. |
| IntFunction<R> | R apply(int val) Description: Acts on an int value and returns the result. |
| IntPredicate | boolean test(int val) Description: Returns true if val satisfies the condition defined by test( ) and false otherwise. |
| IntSupplier | int getAsInt( ) Description: Returns an int result. |
| IntToDoubleFunction | double applyAsDouble(int val) Description: Acts on an int value and returns the result as a double. |
| IntToLongFunction | long applyAsLong(int val) Description: Acts on an int value and returns the result as a long. |
| IntUnaryOperator | int applyAsInt(int val) Description: Acts on an int and returns an int result. |
| LongBinaryOperator | long applyAsLong(long val1, long val2) Description: Acts on two long values and returns a long result. |
| LongConsumer | void accept(long val) Description: Acts on val. |
| LongFunction<R> | R apply(long val) Description: Acts on a long value and returns the result. |
| LongPredicate | boolean test(long val) Description: Returns true if val satisfies the condition defined by test( ) and false otherwise. |
| LongSupplier | long getAsLong( ) Description: Returns a long result. |
| LongToDoubleFunction | double applyAsDouble(long val) Description: Acts on a long value and returns the result as a double. |
| LongToIntFunction | int applyAsInt(long val) Description: Acts on a long value and returns the result as an int. |
| LongUnaryOperator | long applyAsLong(long val) Description: Acts on a long and returns a long result. |
| ObjDoubleConsumer<T> | void accept(T val1, double val2) Description: Acts on val1 and the double value val2. |

**Table 21-18**

Functional Interfaces Defined by `java.util.function` and Their Abstract Methods *(continued)*

<!-- CR p.710 -->

| Interface | Abstract Method |
|---|---|
| ObjIntConsumer<T> | void accept(T val1, int val2) Description: Acts on val1 and the int value val2. |
| ObjLongConsumer<T> | void accept(T val1, long val2) Description: Acts on val1 and the long value val2. |
| Predicate<T> | boolean test(T val) Description: Returns true if val satisfies the condition defined by test( ) and false otherwise. |
| Supplier<T> | T get( ) Description: Returns an object of type T. |
| ToDoubleBiFunction<T, U> | double applyAsDouble(T tVal, U uVal) Description: Acts on tVal and uVal and returns the result as a double. |
| ToDoubleFunction<T> | double applyAsDouble(T val) Description: Acts on val and returns the result as a double. |
| ToIntBiFunction<T, U> | int applyAsInt(T tVal, U uVal) Description: Acts on tVal and uVal and returns the result as an int. |
| ToIntFunction<T> | int applyAsInt(T val) Description: Acts on val and returns the result as an int. |
| ToLongBiFunction<T, U> | long applyAsLong(T tVal, U uVal) Description: Acts on tVal and uVal and returns the result as a long. |
| ToLongFunction<T> | long applyAsLong(T val) Description: Acts on val and returns the result as a long. |
| UnaryOperator<T> | T apply(T val) Description: Acts on val and returns the result |

**Table 21-18**

Functional Interfaces Defined by `java.util.function` and Their Abstract Methods

### java.util.logging

The `java.util.logging` package provides support for program activity logs, which can be used to record program actions, and to help find and debug problems. This package is in the `java.logging` module.

### java.util.prefs

The `java.util.prefs` package provides support for user preferences. It is typically used to support program configuration. This package is in the `java.prefs` module.

<!-- CR p.711 -->

### java.util.random

The `java.util.random` package provides extensive support for random number generators. (Added by JDK 17.)

### java.util.regex

The `java.util.regex` package provides support for regular expression handling. It is described in detail in Chapter 31.

### java.util.spi

The `java.util.spi` package provides support for service providers.

### java.util.stream

The `java.util.stream` package contains Java’s stream API. A discussion of the stream API is found in Chapter 30.

### java.util.zip

The `java.util.zip` package provides the ability to read and write files in the popular ZIP and GZIP formats. Both ZIP and GZIP input and output streams are available.

<!-- CR p.712 -->

*This page intentionally left blank*
