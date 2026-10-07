---
book: "Java: The Complete Reference, 12th ed. (Schildt)"
chapter: "ch21 java.util Part 2: More Utility Classes"
printed_pages: "653-706"
pdf_offset: "pdf page = printed page + 35"
generated_by: tools/extract_refs.py --full
---
# ch21 java.util Part 2: More Utility Classes

<!-- CR p.653 -->

**CHAPTER**

21

**java.util Part 2: More Utility Classes**

This chapter continues our discussion of `java.util` by examining those classes and interfaces that are not part of the Collections Framework. These include classes that support timers, work with dates, compute random numbers, and bundle resources. Also covered are the **Formatter** and `Scanner` classes which make it easy to write and read formatted data, and the **Optional** class, which simplifies handling situations in which a value may be absent. Finally, the subpackages of `java.util` are summarized at the end of this chapter. Of particular interest is `java.util.function`, which defines several standard functional interfaces. One last point: the **Observer** interface and the **Observable** class packaged in `java.util`. have been deprecated since JDK 9. For this reason they are not discussed here.

## StringTokenizer

The processing of text often consists of parsing a formatted input string. *Parsing* is the division of text into a set of discrete parts, or *tokens*, which in a certain sequence can convey a semantic meaning. The **StringTokenizer** class provides the first step in this parsing process, often called the *lexer* (lexical analyzer) or *scanner*. **StringTokenizer** implements the **Enumeration** interface. Therefore, given an input string, you can enumerate the individual tokens contained in it using **StringTokenizer**. Before we begin, it is important to point out that **StringTokenizer** is described here primarily for the benefit of those programmers working with legacy code. For new code, regular expressions, discussed in Chapter 31, offer a more modern alternative.

To use **StringTokenizer**, you specify an input string and a string that contains delimiters. *Delimiters* are characters that separate tokens. Each character in the delimiters string is considered a valid delimiter—for example, ",;:" sets the delimiters to a comma, semicolon, and colon. The default set of delimiters consists of the whitespace characters: space, tab, form feed, newline, and carriage return.

The **StringTokenizer** constructors are shown here:

StringTokenizer(String *str*) StringTokenizer(String *str*, String *delimiters*) StringTokenizer(String *str*, String *delimiters*, boolean *delimAsToken*)

<!-- CR p.654 -->

In all versions, *str* is the string that will be tokenized. In the first version, the default delimiters are used. In the second and third versions, *delimiters* is a string that specifies the delimiters. In the third version, if *delimAsToken* is `true`, then the delimiters are also returned as tokens when the string is parsed. Otherwise, the delimiters are not returned. Delimiters are not returned as tokens by the first two forms.

Once you have created a **StringTokenizer** object, the **nextToken( )** method is used to extract consecutive tokens. The **hasMoreTokens( )** method returns `true` while there are more tokens to be extracted. Since **StringTokenizer** implements **Enumeration**, the **hasMoreElements( )** and **nextElement( )** methods are also implemented, and they act the same as **hasMoreTokens( )** and **nextToken( )**, respectively. The **StringTokenizer** methods are shown in Table 21-1.

Here is an example that creates a **StringTokenizer** to parse "key=value" pairs. Consecutive sets of "key=value" pairs are separated by a semicolon.

```java
// Demonstrate StringTokenizer.
import java.util.StringTokenizer;

class STDemo {
  static String in = "title=Java: The Complete Reference;" +
    "author=Schildt;" +
    "publisher=McGraw Hill;" +
    "copyright=2022";

  public static void main(String[] args) {
    StringTokenizer st = new StringTokenizer(in, "=;");

    while(st.hasMoreTokens()) {
      String key = st.nextToken();
      String val = st.nextToken();
      System.out.println(key + "\t" + val);
    }
  }
}
```

| Method | Description |
|---|---|
| int countTokens( ) | Using the current set of delimiters, the method determines the number of tokens left to be parsed and returns the result. |
| boolean hasMoreElements( ) | Returns true if one or more tokens remain in the string and returns false if there are none. |
| boolean hasMoreTokens( ) | Returns true if one or more tokens remain in the string and returns false if there are none. |
| Object nextElement( ) | Returns the next token as an Object. |
| String nextToken( ) | Returns the next token as a String. |
| String nextToken(String delimiters) | Returns the next token as a String and sets the delimiters string to that specified by delimiters. |

**Table 21-1**

The Methods Defined by **StringTokenizer**

<!-- CR p.655 -->

The output from this program is shown here:

```text
title  Java: The Complete Reference
author  Schildt
publisher  McGraw Hill
copyright  2022
```

## BitSet

A **BitSet** class creates a special type of array that holds bit values in the form of `boolean` values. This array can increase in size as needed. This makes it similar to a vector of bits. The **BitSet** constructors are shown here:

BitSet( ) BitSet(int *size*)

The first version creates a default object. The second version allows you to specify its initial size (that is, the number of bits that it can hold). All bits are initialized to `false`.

**BitSet** defines the methods listed in Table 21-2.

| Method | Description |
|---|---|
| void and(BitSet bitSet) | ANDs the contents of the invoking BitSet object with those specified by bitSet. The result is placed into the invoking object. |
| void andNot(BitSet bitSet) | For each set bit in bitSet, the corresponding bit in the invoking BitSet is cleared. |
| int cardinality( ) | Returns the number of set bits in the invoking object. |
| void clear( ) | Zeros all bits. |
| void clear(int index) | Zeros the bit specified by index. |
| void clear(int startIndex, int endIndex) | Zeros the bits from startIndex to endIndex –1. |
| Object clone( ) | Duplicates the invoking BitSet object. |
| boolean equals(Object bitSet) | Returns true if the invoking bit set is equivalent to the one passed in bitSet. Otherwise, the method returns false. |
| void flip(int index) | Reverses the bit specified by index. |
| void flip(int startIndex, int endIndex) | Reverses the bits from startIndex to endIndex –1. |
| boolean get(int index) | Returns the current state of the bit at the specified index. |
| BitSet get(int startIndex, int endIndex) | Returns a BitSet that consists of the bits from startIndex to endIndex –1. The invoking object is not changed. |
| int hashCode( ) | Returns the hash code for the invoking object. |
| boolean intersects(BitSet bitSet) | Returns true if at least one pair of corresponding bits within the invoking object and bitSet are set. |

**Table 21-2**

The Methods Defined by **BitSet** *(continued)*

<!-- CR p.656 -->

| Method | Description |
|---|---|
| boolean isEmpty( ) | Returns true if all bits in the invoking object are cleared. |
| int length( ) | Returns the number of bits required to hold the contents of the invoking BitSet. This value is determined by the location of the last set bit. |
| int nextClearBit(int startIndex) | Returns the index of the next cleared bit (that is, the next false bit), starting from the index specified by startIndex. |
| int nextSetBit(int startIndex) | Returns the index of the next set bit (that is, the next true bit), starting from the index specified by startIndex. If no bit is set, –1 is returned. |
| void or(BitSet bitSet) | ORs the contents of the invoking BitSet object with that specified by bitSet. The result is placed into the invoking object. |
| int previousClearBit(int startIndex) | Returns the index of the next cleared bit (that is, the next false bit) at or prior to the index specified by startIndex. If no cleared bit is found, –1 is returned. |
| int previousSetBit(int startIndex) | Returns the index of the next set bit (that is, the next true bit) at or prior to the index specified by startIndex. If no set bit is found, –1 is returned. |
| void set(int index) | Sets the bit specified by index. |
| void set(int index, boolean v) | Sets the bit specified by index to the value passed in v. true sets the bit; false clears the bit. |
| void set(int startIndex, int endIndex) | Sets the bits from startIndex to endIndex –1. |
| void set(int startIndex, int endIndex, boolean v) | Sets the bits from startIndex to endIndex –1 to the value passed in v. true sets the bits; false clears the bits. |
| int size( ) | Returns the number of bits in the invoking BitSet object. |
| IntStream stream( ) | Returns a stream that contains the bit positions, from low to high, that have set bits. |
| byte[ ] toByteArray( ) | Returns a byte array that contains the invoking BitSet object. |
| long[ ] toLongArray( ) | Returns a long array that contains the invoking BitSet object. |
| String toString( ) | Returns the string equivalent of the invoking BitSet object. |
| static BitSet valueOf(byte[ ] v) | Returns a BitSet that contains the bits in v. |
| static BitSet valueOf(ByteBuffer v) | Returns a BitSet that contains the bits in v. |
| static BitSet valueOf(long[ ] v) | Returns a BitSet that contains the bits in v. |
| static BitSet valueOf(LongBuffer v) | Returns a BitSet that contains the bits in v. |
| void xor(BitSet bitSet) | XORs the contents of the invoking BitSet object with that specified by bitSet. The result is placed into the invoking object. |

**Table 21-2**

The Methods Defined by **BitSet**

<!-- CR p.657 -->

Here is an example that demonstrates **BitSet**:

```java
// BitSet Demonstration.
import java.util.BitSet;

class BitSetDemo {
  public static void main(String[] args) {
    BitSet bits1 = new BitSet(16);
    BitSet bits2 = new BitSet(16);

    // set some bits
    for(int i=0; i<16; i++) {
      if((i%2) == 0) bits1.set(i);
      if((i%5) != 0) bits2.set(i);
    }

    System.out.println("Initial pattern in bits1: ");
    System.out.println(bits1);
    System.out.println("\nInitial pattern in bits2: ");
    System.out.println(bits2);

    // AND bits
    bits2.and(bits1);
    System.out.println("\nbits2 AND bits1: ");
    System.out.println(bits2);

    // OR bits
    bits2.or(bits1);
    System.out.println("\nbits2 OR bits1: ");
    System.out.println(bits2);

    // XOR bits
    bits2.xor(bits1);
    System.out.println("\nbits2 XOR bits1: ");
    System.out.println(bits2);
  }
}
```

The output from this program is shown here. When **toString( )** converts a **BitSet** object to its string equivalent, each set bit is represented by its bit position. Cleared bits are not shown.

```java
Initial pattern in bits1:
{0, 2, 4, 6, 8, 10, 12, 14}

Initial pattern in bits2:
{1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14}

bits2 AND bits1:
{2, 4, 6, 8, 12, 14}

bits2 OR bits1:
{0, 2, 4, 6, 8, 10, 12, 14}

bits2 XOR bits1:
{}
```

<!-- CR p.658 -->

## Optional, OptionalDouble, OptionalInt, and OptionalLong

Beginning with JDK 8, the classes called **Optional**, **OptionalDouble**, **OptionalInt**, and **OptionalLong** offer a way to handle situations in which a value may or may not be present. In the past, you would normally use the value `null` to indicate that no value is present. However, this can lead to null pointer exceptions if an attempt is made to dereference a null reference. As a result, frequent checks for a `null` value were necessary to avoid generating an exception. These classes provide a better way to handle such situations. One other point: These classes are value-based. (See Chapter 13 for a description of value-based classes.)

The first and most general of these classes is **Optional**. For this reason, it is the primary focus of this discussion. It is shown here:

class Optional<T>

Here, **T** specifies the type of value stored. It is important to understand that an **Optional** instance can either contain a value of type **T** or be empty. In other words, an **Optional** object does not necessarily contain a value. **Optional** does not define any constructors, but it does define several methods that let you work with **Optional** objects. For example, you can determine if a value is present, obtain the value if it is present, obtain a default value when no value is present, and construct an **Optional** value. The **Optional** methods are shown in Table 21-3.

| Method | Description |
|---|---|
| static <T> Optional<T> empty( ) | Returns an object for which isPresent( ) returns false. |
| boolean equals(Object optional) | Returns true if the invoking object equals optional. Otherwise, returns false. |
| Optional<T> filter( Predicate<? super T> condition) | Returns an Optional instance that contains the same value as the invoking object if that value satisfies condition. Otherwise, an empty object is returned. |
| U Optional<U> flatMap( Function<? super T, Optional<U>> mapFunc) | Applies the mapping function specified by mapFunc to the invoking object if that object contains a value and returns the result. Returns an empty object otherwise. |
| T get( ) | Returns the value in the invoking object. However, if no value is present, NoSuchElementException is thrown. |
| int hashCode( ) | Returns a hash code for the value in invoking object. Returns 0 if there is no value. |
| void ifPresent( Consumer<? super T> func) | Calls func if a value is present in the invoking object, passing the object to func. If no value is present, no action occurs. |
| void ifPresentOrElse( Consumer<? super T> func, Runnable onEmpty) | Calls func if a value is present in the invoking object, passing the object to func. If no value is present, onEmpty will be executed. |

**Table 21-3**

The Methods Defined by **Optional** *(continued)*

<!-- CR p.659 -->

| Method | Description |
|---|---|
| boolean isEmpty( ) | Returns true if the invoking object does not contain a value. Returns false if a value is present. |
| boolean isPresent( ) | Returns true if the invoking object contains a value. Returns false if no value is present. |
| U Optional<U> map( Function<? super T, ? extends U>> mapFunc) | Applies the mapping function specified by mapFunc to the invoking object if that object contains a value and returns the result. Returns an empty object otherwise. |
| static <T> Optional<T> of(T val) | Creates an Optional instance that contains val and returns the result. The value of val must not be null. |
| static <T> Optional<T> ofNullable(T val) | Creates an Optional instance that contains val and returns the result. However, if val is null, then an empty Optional instance is returned. |
| Optional<T> or(Supplier<? extends Optional<? extends T>> func) | If no value is present in the invoking object, calls func to construct and return an Optional instance that contains a value. Otherwise, returns an Optional instance that contains the invoking object’s value. |
| T orElse(T defVal) | If the invoking object contains a value, the value is returned. Otherwise, the value specified by defVal is returned. |
| T orElseGet( Supplier<? extends T> getFunc) | If the invoking object contains a value, the value is returned. Otherwise, the value obtained from getFunc is returned. |
| T orElseThrow( ) | Returns the value in the invoking object. However, if no value is present, NoSuchElementException is thrown. |
| <X extends Throwable> T orElseThrow( Supplier<? extends X> excFunc) throws X extends Throwable | Returns the value in the invoking object. However, if no value is present, the exception generated by excFunc is thrown. |
| Stream<T> stream( ) | Returns a stream that contains the invoking object’s value. If no value is present, the stream will contain no values. |
| String toString( ) | Returns a string corresponding to the invoking object. |

**Table 21-3**

The Methods Defined by **Optional**

The best way to understand **Optional** is to work through an example that uses its core methods. At the foundation of **Optional** are **isPresent( )** and **get( )**. You can determine if a value is present by calling **isPresent( )**. If a value is available, it will return `true`. Otherwise, `false` is returned. If a value is present in an **Optional** instance, you can obtain it by calling **get( )**. However, if you call **get( )** on an object that does not contain a value, **NoSuchElementException** is thrown. For this reason, you should always first confirm that a value is present before calling **get( )** on an **Optional** object. Beginning with JDK 10, the parameterless version of **orElseThrow( )** can be used instead of **get( )**, and its name adds clarity to the operation. However, the examples in this book will use **get( )** so that the code will compile for readers using earlier versions of Java.

Of course, having to call two methods to retrieve a value adds overhead to each access. Fortunately, **Optional** defines methods that combine the check for a value with the retrieval of the value. One such method is **orElse( )**. If the object on which it is called contains a value, the value is returned. Otherwise, a default value is returned.

<!-- CR p.660 -->

**Optional** does not define any constructors. Instead, you will use one of its methods to create an instance. For example, you can create an **Optional** instance with a specified value by using **of( )**. You can create an instance of **Optional** that does not contain a value by using **empty( )**.

The following program demonstrates these methods:

```java
// Demonstrate several Optional<T> methods

import java.util.*;

class OptionalDemo {
  public static void main(String[] args) {

    Optional<String> noVal = Optional.empty();

    Optional<String> hasVal = Optional.of("ABCDEFG");

    if(noVal.isPresent()) System.out.println("This won't be displayed");
    else System.out.println("noVal has no value");

    if(hasVal.isPresent()) System.out.println("The string in hasVal is: " +
                                               hasVal.get());

    String defStr = noVal.orElse("Default String");
    System.out.println(defStr);
  }
}
```

The output is shown here:

```text
noVal has no value
The string in hasVal is: ABCDEFG
Default String
```

As the output shows, a value can be obtained from an **Optional** object only if one is present. This basic mechanism enables **Optional** to prevent null pointer exceptions.

The **OptionalDouble**, **OptionalInt**, and **OptionalLong** classes work much like **Optional**, except that they are designed expressly for use on `double`, `int`, and `long` values, respectively. As such, they specify the methods **getAsDouble( )**, **getAsInt( )**, and **getAsLong( )**, respectively, rather than **get( )**. Also, they do not support the **filter( )**, **ofNullable( )**, **map( )**, **flatMap( ),** and **or( )** methods.

## Date

The **Date** class encapsulates the current date and time. Before beginning our examination of **Date**, it is important to point out that it has changed substantially from its original version defined by Java 1.0. When Java 1.1 was released, many of the functions carried out by the original **Date** class were moved into the **Calendar** and **DateFormat** classes, and as a result, many of the original 1.0 **Date** methods were deprecated. Since the deprecated 1.0 methods should not be used for new code, they are not described here.

<!-- CR p.661 -->

| Method | Description |
|---|---|
| boolean after(Date date) | Returns true if the invoking Date object contains a date that is later than the one specified by date. Otherwise, it returns false. |
| boolean before(Date date) | Returns true if the invoking Date object contains a date that is earlier than the one specified by date. Otherwise, it returns false. |
| Object clone( ) | Duplicates the invoking Date object. |
| int compareTo(Date date) | Compares the value of the invoking object with that of date. Returns 0 if the values are equal. Returns a negative value if the invoking object is earlier than date. Returns a positive value if the invoking object is later than date. |
| boolean equals(Object date) | Returns true if the invoking Date object contains the same time and date as the one specified by date. Otherwise, it returns false. |
| static Date from(Instant t) | Returns a Date object corresponding to the Instant object passed in t. |
| long getTime( ) | Returns the number of milliseconds that have elapsed since January 1, 1970. |
| int hashCode( ) | Returns a hash code for the invoking object. |
| void setTime(long time) | Sets the time and date as specified by time, which represents an elapsed time in milliseconds from midnight, January 1, 1970. |
| Instant toInstant( ) | Returns an Instant object corresponding to the invoking Date object. |
| String toString( ) | Converts the invoking Date object into a string and returns the result. |

**Table 21-4**

The Nondeprecated Methods Defined by **Date**

**Date** supports the following non-deprecated constructors:

Date( ) Date(long *millisec*)

The first constructor initializes the object with the current date and time. The second constructor accepts one argument that equals the number of milliseconds that have elapsed since midnight, January 1, 1970. The non-deprecated methods defined by **Date** are shown in Table 21-4. **Date** also implements the **Comparable** interface.

As you can see by examining Table 21-4, the non-deprecated **Date** features do not allow you to obtain the individual components of the date or time. As the following program demonstrates, you can only obtain the date and time in terms of milliseconds, in its default string representation as returned by **toString( )**, or as an **Instant** object. To obtain more-detailed information about the date and time, you will use the **Calendar** class.

```java
// Show date and time using only Date methods.
import java.util.Date;

class DateDemo {
  public static void main(String[] args) {
    // Instantiate a Date object
    Date date = new Date();
    // display time and date using toString()
    System.out.println(date);

    // Display number of milliseconds since midnight, January 1, 1970 GMT
    long msec = date.getTime();
    System.out.println("Milliseconds since Jan. 1, 1970 GMT = " + msec);
  }
}
```

<!-- CR p.662 -->

Sample output is shown here:

```text
Sat Jan 01 10:52:44 CST 2022
Milliseconds since Jan. 1, 1970 GMT = 1641056951341
```

## Calendar

The abstract **Calendar** class provides a set of methods that allows you to convert a time in milliseconds to a number of useful components. Some examples of the type of information that can be provided are year, month, day, hour, minute, and second. It is intended that subclasses of **Calendar** will provide the specific functionality to interpret time information according to their own rules. This is one aspect of the Java class library that enables you to write programs that can operate in international environments. An example of such a subclass is **GregorianCalendar**.

**NOTE** Another date and time API is found in `java.time`. See Chapter 31.

**Calendar** provides no public constructors. **Calendar** defines several protected instance variables. `areFieldsSet` is a `boolean` that indicates if the time components have been set. `fields` is an array of `int`s that holds the components of the time. `isSet` is a `boolean` array that indicates if a specific time component has been set. `time` is a `long` that holds the current time for this object. `isTimeSet` is a `boolean` that indicates if the current time has been set.

A sampling of methods defined by **Calendar** are shown in Table 21-5.

| Method | Description |
|---|---|
| abstract void add(int which, int val) | Adds val to the time or date component specified by which. To subtract, add a negative value. which must be one of the fields defined by Calendar, such as Calendar.HOUR. |
| boolean after(Object calendarObj) | Returns true if the invoking Calendar object contains a date that is later than the one specified by calendarObj. Otherwise, it returns false. |
| boolean before(Object calendarObj) | Returns true if the invoking Calendar object contains a date that is earlier than the one specified by calendarObj. Otherwise, it returns false. |

**Table 21-5**

A Sampling of the Methods Defined by **Calendar** *(continued)*

<!-- CR p.663 -->

| Method | Description |
|---|---|
| final void clear( ) | Zeros all time components in the invoking object. |
| final void clear(int which) | Zeros the time component specified by which in the invoking object. |
| Object clone( ) | Returns a duplicate of the invoking object. |
| boolean equals(Object calendarObj) | Returns true if the invoking Calendar object contains a date that is equal to the one specified by calendarObj. Otherwise, it returns false. |
| int get(int calendarField) | Returns the value of one component of the invoking object. The component is indicated by calendarField. Examples of the components that can be requested are Calendar.YEAR, Calendar.MONTH, Calendar.MINUTE, and so forth. |
| static Locale[ ] getAvailableLocales( ) | Returns an array of Locale objects that contains the locales for which calendars are available. |
| static Calendar getInstance( ) | Returns a Calendar object for the default locale and time zone. |
| static Calendar getInstance(TimeZone tz) | Returns a Calendar object for the time zone specified by tz. The default locale is used. |
| static Calendar getInstance(Locale locale) | Returns a Calendar object for the locale specified by locale. The default time zone is used. |
| static Calendar getInstance(TimeZone tz, Locale locale) | Returns a Calendar object for the time zone specified by tz and the locale specified by locale. |
| final Date getTime( ) | Returns a Date object equivalent to the time of the invoking object. |
| TimeZone getTimeZone( ) | Returns the time zone for the invoking object. |
| final boolean isSet(int which) | Returns true if the specified time component is set. Otherwise, it returns false. |
| void set(int which, int val) | Sets the date or time component specified by which to the value specified by val in the invoking object. which must be one of the fields defined by Calendar, such as Calendar.HOUR. |
| final void set(int year, int month, int dayOfMonth) | Sets various date and time components of the invoking object. |
| final void set(int year, int month, int dayOfMonth, int hours, int minutes) | Sets various date and time components of the invoking object. |
| final void set(int year, int month, int dayOfMonth, int hours, int minutes, int seconds) | Sets various date and time components of the invoking object. |

**Table 21-5**

A Sampling of the Methods Defined by **Calendar** *(continued)*

<!-- CR p.664 -->

| Method | Description |
|---|---|
| final void setTime(Date d) | Sets various date and time components of the invoking object. This information is obtained from the Date object d. |
| void setTimeZone(TimeZone tz) | Sets the time zone for the invoking object to that specified by tz. |
| final Instant toInstant( ) | Returns an Instant object corresponding to the invoking Calendar instance. |

**Table 21-5**

A Sampling of the Methods Defined by **Calendar**

**Calendar** defines the following `int` constants, which are used when you get or set components of the calendar.

| ALL_STYLES | HOUR_OF_DAY | PM |
|---|---|---|
| AM | JANUARY | SATURDAY |
| AM_PM | JULY | SECOND |
| APRIL | JUNE | SEPTEMBER |
| AUGUST | LONG | SHORT |
| DATE | LONG_FORMAT | SHORT_FORMAT |
| DAY_OF_MONTH | LONG_STANDALONE | SHORT_STANDALONE |
| DAY_OF_WEEK | MARCH | SUNDAY |
| DAY_OF_WEEK_IN_MONTH | MAY | THURSDAY |
| DAY_OF_YEAR | MILLISECOND | TUESDAY |
| DECEMBER | MINUTE | UNDECIMBER |
| DST_OFFSET | MONDAY | WEDNESDAY |
| ERA | MONTH | WEEK_OF_MONTH |
| FEBRUARY | NARROW_FORMAT | WEEK_OF_YEAR |
| FIELD_COUNT | NARROW_STANDALONE | YEAR |
| FRIDAY | NOVEMBER | ZONE_OFFSET |
| HOUR | OCTOBER |  |

The following program demonstrates several **Calendar** methods:

```java
// Demonstrate Calendar
import java.util.Calendar;

class CalendarDemo {
  public static void main(String[] args) {
    String[] months = {
             "Jan", "Feb", "Mar", "Apr",
             "May", "Jun", "Jul", "Aug",
             "Sep", "Oct", "Nov", "Dec"};
    // Create a calendar initialized with the
    // current date and time in the default
    // locale and timezone.
    Calendar calendar = Calendar.getInstance();

    // Display current time and date information.
    System.out.print("Date: ");
    System.out.print(months[calendar.get(Calendar.MONTH)]);
    System.out.print(" " + calendar.get(Calendar.DATE) + " ");
    System.out.println(calendar.get(Calendar.YEAR));

    System.out.print("Time: ");
    System.out.print(calendar.get(Calendar.HOUR) + ":");
    System.out.print(calendar.get(Calendar.MINUTE) + ":");
    System.out.println(calendar.get(Calendar.SECOND));

    // Set the time and date information and display it.
    calendar.set(Calendar.HOUR, 10);
    calendar.set(Calendar.MINUTE, 29);
    calendar.set(Calendar.SECOND, 22);
    System.out.print("Updated time: ");
    System.out.print(calendar.get(Calendar.HOUR) + ":");
    System.out.print(calendar.get(Calendar.MINUTE) + ":");
    System.out.println(calendar.get(Calendar.SECOND));
  }
}
```

<!-- CR p.665 -->

Sample output is shown here:

```text
Date: Jan 1 2022
Time: 11:29:39
Updated time: 10:29:22
```

## GregorianCalendar

**GregorianCalendar** is a concrete implementation of a **Calendar** that implements the normal Gregorian calendar with which you are familiar. The **getInstance( )** method of **Calendar** will typically return a **GregorianCalendar** initialized with the current date and time in the default locale and time zone.

**GregorianCalendar** defines two fields: **AD** and **BC**. These represent the two eras defined by the Gregorian calendar.

There are also several constructors for **GregorianCalendar** objects. The default, **GregorianCalendar( )**, initializes the object with the current date and time in the default locale and time zone. Three more constructors offer increasing levels of specificity:

GregorianCalendar(int *year*, int *month*, int *dayOfMonth*) GregorianCalendar(int *year*, int *month*, int *dayOfMonth*, int *hours*, int *minutes*) GregorianCalendar(int *year*, int *month*, int *dayOfMonth*, int *hours*, int *minutes*, int *seconds*)

<!-- CR p.666 -->

All three versions set the day, month, and year. Here, *year* specifies the year. The month is specified by *month*, with zero indicating January. The day of the month is specified by *dayOfMonth*. The first version sets the time to midnight. The second version also sets the hours and the minutes. The third version adds seconds.

You can also construct a **GregorianCalendar** object by specifying the locale and/or time zone. The following constructors create objects initialized with the current date and time using the specified time zone and/or locale:

GregorianCalendar(Locale *locale*) GregorianCalendar(TimeZone *timeZone*) GregorianCalendar(TimeZone *timeZone*, Locale *locale*) **GregorianCalendar** provides an implementation of all the abstract methods in **Calendar**. It also provides some additional methods. Perhaps the most interesting is **isLeapYear( )**, which tests if the year is a leap year. Its form is

boolean isLeapYear(int *year*) This method returns `true` if *year* is a leap year and `false` otherwise. Two other methods of interest are **from( )** and **toZonedDateTime( )**, which support the date and time API added by JDK 8 and packaged in `java.time`.

The following program demonstrates **GregorianCalendar**:

```java
// Demonstrate GregorianCalendar
import java.util.*;

class GregorianCalendarDemo {
  public static void main(String[] args) {
    String[] months = {
             "Jan", "Feb", "Mar", "Apr",
             "May", "Jun", "Jul", "Aug",
             "Sep", "Oct", "Nov", "Dec"};
    int year;

    // Create a Gregorian calendar initialized
    // with the current date and time in the
    // default locale and timezone.
    GregorianCalendar gcalendar = new GregorianCalendar();

    // Display current time and date information.
    System.out.print("Date: ");
    System.out.print(months[gcalendar.get(Calendar.MONTH)]);
    System.out.print(" " + gcalendar.get(Calendar.DATE) + " ");
    System.out.println(year = gcalendar.get(Calendar.YEAR));

    System.out.print("Time: ");
    System.out.print(gcalendar.get(Calendar.HOUR) + ":");
    System.out.print(gcalendar.get(Calendar.MINUTE) + ":");
    System.out.println(gcalendar.get(Calendar.SECOND));

    // Test if the current year is a leap year
    if(gcalendar.isLeapYear(year)) {
      System.out.println("The current year is a leap year");
    }
    else {
      System.out.println("The current year is not a leap year");
    }
  }
}
```

<!-- CR p.667 -->

Sample output is shown here:

```text
Date: Jan 1 2022
Time: 1:45:5
The current year is not a leap year
```

## TimeZone

Another time-related class is **TimeZone**. The abstract **TimeZone** class allows you to work with time zone offsets from Greenwich mean time (GMT), also referred to as Coordinated Universal Time (UTC). It also computes daylight saving time. **TimeZone** only supplies the default constructor.

A sampling of methods defined by **TimeZone** is given in Table 21-6.

| Method | Description |
|---|---|
| Object clone( ) | Returns a TimeZone-specific version of clone( ). |
| static String[ ] getAvailableIDs( ) | Returns an array of String objects representing the names of all time zones. |
| static String[ ] getAvailableIDs(int timeDelta) | Returns an array of String objects representing the names of all time zones that are timeDelta offset from GMT. |
| static TimeZone getDefault( ) | Returns a TimeZone object that represents the default time zone used on the host computer. |
| String getID( ) | Returns the name of the invoking TimeZone object. |
| abstract int getOffset(int era, int year, int month, int dayOfMonth, int dayOfWeek, int millisec) | Returns the offset that should be added to GMT to compute local time. This value is adjusted for daylight saving time. The parameters to the method represent date and time components. |
| abstract int getRawOffset( ) | Returns the raw offset (in milliseconds) that should be added to GMT to compute local time. This value is not adjusted for daylight saving time. |
| static TimeZone getTimeZone(String tzName) | Returns the TimeZone object for the time zone named tzName. |
| abstract boolean inDaylightTime(Date d) | Returns true if the date represented by d is in daylight saving time in the invoking object. Otherwise, it returns false. |

**Table 21-6**

A Sampling of the Methods Defined by **TimeZone** *(continued)*

<!-- CR p.668 -->

| Method | Description |
|---|---|
| static void setDefault(TimeZone tz) | Sets the default time zone to be used on this host. tz is a reference to the TimeZone object to be used. |
| void setID(String tzName) | Sets the name of the time zone (that is, its ID) to that specified by tzName. |
| abstract void setRawOffset(int millis) | Sets the offset in milliseconds from GMT. |
| ZoneId toZoneId( ) | Converts the invoking object into a ZoneId and returns the result. ZoneId is packaged in java.time. |
| abstract boolean useDaylightTime( ) | Returns true if the invoking object uses daylight saving time. Otherwise, it returns false. |

**Table 21-6**

A Sampling of the Methods Defined by **TimeZone**

## SimpleTimeZone

The **SimpleTimeZone** class is a convenient subclass of **TimeZone**. It implements **TimeZone**'s abstract methods and allows you to work with time zones for a Gregorian calendar. It also computes daylight saving time. **SimpleTimeZone** defines four constructors. One is

SimpleTimeZone(int *timeDelta*, String *tzName*)

This constructor creates a **SimpleTimeZone** object. The offset relative to Greenwich mean time (GMT) is *timeDelta*. The time zone is named *tzName*. The second **SimpleTimeZone** constructor is

SimpleTimeZone(int *timeDelta*, String *tzId*, int *dstMonth0*, int *dstDayInMonth0*, int *dstDay0*, int *time0*, int *dstMonth1*, int *dstDayInMonth1*, int *dstDay1*, int *time1*)

Here, the offset relative to GMT is specified in *timeDelta*. The time zone name is passed in *tzId*. The start of daylight saving time is indicated by the parameters *dstMonth0*, *dstDayInMonth0*, *dstDay0*, and *time0*. The end of daylight saving time is indicated by the parameters *dstMonth1*, *dstDayInMonth1*, *dstDay1*, and *time1*. The third **SimpleTimeZone** constructor is

SimpleTimeZone(int *timeDelta*, String *tzId*, int *dstMonth0*, int *dstDayInMonth0*, int *dstDay0*, int *time0*, int *dstMonth1*, int *dstDayInMonth1*, int *dstDay1*, int *time1*, int *dstDelta*)

Here, *dstDelta* is the number of milliseconds saved during daylight saving time. The fourth **SimpleTimeZone** constructor is:

SimpleTimeZone(int *timeDelta*, String *tzId*, int *dstMonth0*, int *dstDayInMonth0*, int *dstDay0*, int *time0*, int *time0mode*, int *dstMonth1*, int *dstDayInMonth1*, int *dstDay1*, int *time1*, int *time1mode*, int *dstDelta*)

<!-- CR p.669 -->

Here, *time0mode* specifies the mode of the starting time, and *time1mode* specifies the mode of the ending time. Valid mode values include:

STANDARD_TIME WALL_TIME UTC_TIME

The time mode indicates how the time values are interpreted. The default mode used by the other constructors is `WALL_TIME`.

## Locale

The **Locale** class is instantiated to produce objects that describe a geographical or cultural region. It is one of several classes that provide you with the ability to write programs that can execute in different international environments. For example, the formats used to display dates, times, and numbers are different in various regions.

Internationalization is a large topic that is beyond the scope of this book. However, many programs will only need to deal with its basics, which include setting the current locale.

The **Locale** class defines the following constants that are useful for dealing with several common locales:

| CANADA | GERMAN | KOREAN |
|---|---|---|
| CANADA_FRENCH | GERMANY | PRC |
| CHINA | ITALIAN | SIMPLIFIED_CHINESE |
| CHINESE | ITALY | TAIWAN |
| ENGLISH | JAPAN | TRADITIONAL_CHINESE |
| FRANCE | JAPANESE | UK |
| FRENCH | KOREA | US |

For example, the expression **Locale**.**CANADA** represents the **Locale** object for Canada.

The constructors for **Locale** are

Locale(String *language*) Locale(String *language*, String *country*) Locale(String *language*, String *country*, String *variant*)

These constructors build a **Locale** object to represent a specific *language* and in the case of the last two, *country*. These values must contain standard language and country codes. Auxiliary variant information can be provided in *variant*.

**Locale** defines several methods. One of the most important is **setDefault( )**, shown here:

static void setDefault(Locale *localeObj*)

This sets the default locale used by the JVM to that specified by *localeObj*.

Some other interesting methods are the following:

final String getDisplayCountry( ) final String getDisplayLanguage( ) final String getDisplayName( )

<!-- CR p.670 -->

These return human-readable strings that can be used to display the name of the country, the name of the language, and the complete description of the locale.

The default locale can be obtained using **getDefault( )**, shown here:

static Locale getDefault( ) JDK 7 added significant upgrades to the **Locale** class that support Internet Engineering Task Force (IETF) BCP 47, which defines tags for identifying languages, and Unicode Technical Standard (UTS) 35, which defines the Locale Data Markup Language (LDML). Support for BCP 47 and UTS 35 caused several features to be added to **Locale**, including several new methods and the `Locale.Builder` class. Among others, new methods include **getScript( )**, which obtains the locale’s script, and **toLanguageTag( )**, which obtains a string that contains the locale’s language tag. The `Locale.Builder` class constructs **Locale** instances. It ensures that a locale specification is well-formed as defined by BCP 47. (The **Locale** constructors do not provide such a check.) Several new methods were also added to **Locale** by JDK 8. Among these are methods that support filtering, extensions, and lookups. JDK 9 added a method called **getISOCountries( )**, which returns a collection of country codes for a given `Locale.IsoCountryCode` enumeration value.

**Calendar** and **GregorianCalendar** are examples of classes that operate in a locale-sensitive manner. **DateFormat** and **SimpleDateFormat** also depend on the locale.

## Random

The **Random** class is a generator of pseudorandom numbers. These are called *pseudorandom* numbers because they are simply uniformly distributed sequences. Beginning with JDK 17, **Random** implements the new **RandomGenerator** interface, which provides a standardized interface for random value generators.

**Random** defines the following constructors:

Random( ) Random(long *seed*) The first version creates a number generator that uses a reasonably unique seed. The second form allows you to specify a seed value manually.

If you initialize a **Random** object with a seed, you define the starting point for the random sequence. If you use the same seed to initialize another **Random** object, you will extract the same random sequence. If you want to generate different sequences, specify different seed values. One way to do this is to use the current time to seed a **Random** object. This approach reduces the possibility of getting repeated sequences.

The core public methods provided by **Random** are shown in Table 21-7. These are the methods that have been available in **Random** for several years (many since Java 1.0) and are widely used.

As you can see, there are seven types of random numbers that you can extract from a **Random** object. Random Boolean values are available from **nextBoolean( )**. Random bytes can be obtained by calling **nextBytes( )**. Integers can be extracted via the **nextInt( )** method. Long integers can be obtained with **nextLong( )**. The **nextFloat( )** and **nextDouble( )** methods return `float` and `double` values, respectively, between 0.0 and 1.0. Finally, **nextGaussian( )** returns a `double` value centered at 0.0 with a standard deviation of 1.0. This is what is known as a *bell curve*.

<!-- CR p.671 -->

| Method | Description |
|---|---|
| boolean nextBoolean( ) | Returns the next boolean random number. |
| void nextBytes(byte[ ] vals) | Fills vals with randomly generated values. |
| double nextDouble( ) | Returns the next double random number. |
| float nextFloat( ) | Returns the next float random number. |
| double nextGaussian( ) | Returns the next Gaussian random number. |
| int nextInt( ) | Returns the next int random number. |
| int nextInt(int n) | Returns the next int random number within the range zero to n. |
| long nextLong( ) | Returns the next long random number. |
| void setSeed(long newSeed) | Sets the seed value (that is, the starting point for the random number generator) to that specified by newSeed. |

**Table 21-7**

The Core Methods Defined by **Random**

Here is an example that demonstrates the sequence produced by **nextGaussian( )**. It obtains 100 random Gaussian values and averages these values. The program also counts the number of values that fall within two standard deviations, plus or minus, using increments of 0.5 for each category. The result is graphically displayed sideways on the screen.

```java
// Demonstrate random Gaussian values.
import java.util.Random;
class RandDemo {
  public static void main(String[] args) {
    Random r = new Random();
    double val;
    double sum = 0;
    int[] bell = new int[10];

    for(int i=0; i<100; i++) {
      val = r.nextGaussian();
      sum += val;
      double t = -2;

      for(int x=0; x<10; x++, t += 0.5)
        if(val < t) {
          bell[x]++;
          break;
        }
    }
    System.out.println("Average of values: " +
                        (sum/100));

    // display bell curve, sideways
    for(int i=0; i<10; i++) {
      for(int x=bell[i]; x>0; x--)
        System.out.print("*");
      System.out.println();
    }
  }
}
```

<!-- CR p.672 -->

Here is a sample program run. As you can see, a bell-like distribution of numbers is obtained.

```text
Average of values: 0.0702235271133344
**
*******
******
***************
******************
*****************
*************
**********
********
***
```

It is useful to point out that JDK 8 added three methods to **Random** that support the stream API (see Chapter 30). They are called **doubles( )**, **ints( )**, and **longs( )**, and each returns a reference to a stream that contains a sequence of pseudorandom values of the specified type. Each method defines several overloads. Here are their simplest forms:

DoubleStream doubles( )

IntStream ints( )

LongStream longs( )

The **doubles( )** method returns a stream that contains pseudorandom `double` values. (The range of these values will be less than 1.0 but greater than or equal to 0.0.) The **ints( )** method returns a stream that contains pseudorandom `int` values. The **longs( )** method returns a stream that contains pseudorandom `long` values. For these three methods, the stream returned is effectively infinite. Several overloads of each method are provided that let you specify the size of the stream, an origin, and an upper bound.

## Timer and TimerTask

An interesting and useful feature offered by `java.util` is the ability to schedule a task for execution at some future time. The classes that support this are **Timer** and **TimerTask**. Using these classes, you can create a thread that runs in the background, waiting for a specific time. When the time arrives, the task linked to that thread is executed. Various options allow you to schedule a task for repeated execution, and to schedule a task to run on a specific date. Although it was always possible to manually create a task that would be executed at a specific time using the **Thread** class, **Timer** and **TimerTask** greatly simplify this process.

**Timer** and **TimerTask** work together. **Timer** is the class that you will use to schedule a task for execution. The task being scheduled must be an instance of **TimerTask**. Thus, to schedule a task, you will first create a **TimerTask** object and then schedule it for execution using an instance of **Timer**.

**TimerTask** implements the **Runnable** interface; thus, it can be used to create a thread of execution. Its constructor is shown here:

protected TimerTask( )

<!-- CR p.673 -->

| Method | Description |
|---|---|
| boolean cancel( ) | Terminates the task. Returns true if an execution of the task is prevented. Otherwise, returns false. |
| abstract void run( ) | Contains the code for the timer task. |
| long scheduledExecutionTime( ) | Returns the time at which the last execution of the task was scheduled to have occurred. |

**Table 21-8**

The Methods Defined by **TimerTask**

**TimerTask** defines the methods shown in Table 21-8. Notice that **run( )** is abstract, which means that it must be overridden. The **run( )** method, defined by the **Runnable** interface, contains the code that will be executed. Thus, the easiest way to create a timer task is to extend **TimerTask** and override **run( )**.

Once a task has been created, it is scheduled for execution by an object of type **Timer**. The constructors for **Timer** are shown here:

Timer( ) Timer(boolean *DThread*) Timer(String *tName*) Timer(String *tName*, boolean *DThread*)

The first version creates a **Timer** object that runs as a normal thread. The second uses a daemon thread if *DThread* is `true`. A daemon thread will execute only as long as the rest of the program continues to execute. The third and fourth constructors allow you to specify a name for the **Timer** thread. The methods defined by **Timer** are shown in Table 21-9.

Once a **Timer** has been created, you will schedule a task by calling **schedule( )** on the **Timer** that you created. As Table 21-9 shows, there are several forms of **schedule( )** which allow you to schedule tasks in a variety of ways.

If you create a non-daemon task, then you will want to call **cancel( )** to end the task when your program ends. If you don’t do this, then your program may "hang" for a period of time.

The following program demonstrates **Timer** and **TimerTask**. It defines a timer task whose **run( )** method displays the message "Timer task executed." This task is scheduled to run once every half second after an initial delay of one second.

```java
// Demonstrate Timer and TimerTask.

import java.util.*;

class MyTimerTask extends TimerTask {
  public void run() {
    System.out.println("Timer task executed.");
  }
}

class TTest {
  public static void main(String[] args) {
    MyTimerTask myTask = new MyTimerTask();
    Timer myTimer = new Timer();
```

<!-- CR p.674 -->

| Method | Description |
|---|---|
| void cancel( ) | Cancels the timer thread. |
| int purge( ) | Deletes canceled tasks from the timer’s queue. |
| void schedule(TimerTask TTask, long wait) | TTask is scheduled for execution after the period passed in wait has elapsed. The wait parameter is specified in milliseconds. |
| void schedule(TimerTask TTask, long wait, long repeat) | TTask is scheduled for execution after the period passed in wait has elapsed. The task is then executed repeatedly at the interval specified by repeat. Both wait and repeat are specified in milliseconds. |
| void schedule(TimerTask TTask, Date targetTime) | TTask is scheduled for execution at the time specified by targetTime. |
| void schedule(TimerTask TTask, Date targetTime, long repeat) | TTask is scheduled for execution at the time specified by targetTime. The task is then executed repeatedly at the interval passed in repeat. The repeat parameter is specified in milliseconds. |
| void scheduleAtFixedRate( TimerTask TTask, long wait, long repeat) | TTask is scheduled for execution after the period passed in wait has elapsed. The task is then executed repeatedly at the interval specified by repeat. Both wait and repeat are specified in milliseconds. The time of each repetition is relative to the first execution, not the preceding execution. Thus, the overall rate of execution is fixed. |
| void scheduleAtFixedRate( TimerTask TTask, Date targetTime, long repeat) | TTask is scheduled for execution at the time specified by targetTime. The task is then executed repeatedly at the interval passed in repeat. The repeat parameter is specified in milliseconds. The time of each repetition is relative to the first execution, not the preceding execution. Thus, the overall rate of execution is fixed. |

**Table 21-9**

The Methods Defined by **Timer**

```java
    /* Set an initial delay of 1 second,
       then repeat every half second.
    */
    myTimer.schedule(myTask, 1000, 500);

    try {
      Thread.sleep(5000);
    } catch (InterruptedException exc) {}

    myTimer.cancel();
  }
}
```

<!-- CR p.675 -->

| Method | Description |
|---|---|
| static Set<Currency> getAvailableCurrencies( ) | Returns a set of the supported currencies. |
| String getCurrencyCode( ) | Returns the code (as defined by ISO 4217) that describes the invoking currency. |
| int getDefaultFractionDigits( ) | Returns the number of digits after the decimal point that are normally used by the invoking currency. For example, there are two fractional digits normally used for dollars. |
| String getDisplayName( ) | Returns the name of the invoking currency for the default locale. |
| String getDisplayName(Locale loc) | Returns the name of the invoking currency for the specified locale. |
| static Currency getInstance(Locale localeObj) | Returns a Currency object for the locale specified by localeObj. |
| static Currency getInstance(String code) | Returns a Currency object associated with the currency code passed in code. |
| int getNumericCode( ) | Returns the numeric code (as defined by ISO 4217) for the invoking currency. |
| String getNumericCodeAsString( ) | Returns in string form the numeric code (as defined by ISO 4217) for the invoking currency. |
| String getSymbol( ) | Returns the currency symbol (such as $) for the invoking object. |
| String getSymbol(Locale localeObj) | Returns the currency symbol (such as $) for the locale passed in localeObj. |
| String toString( ) | Returns the currency code for the invoking object. |

**Table 21-10**

The Methods Defined by **Currency**

## Currency

The **Currency** class encapsulates information about a currency. It defines no constructors. The methods supported by **Currency** are shown in Table 21-10. The following program demonstrates **Currency**:

```java
// Demonstrate Currency.
import java.util.*;

class CurDemo {
  public static void main(String[] args) {
    Currency c;

    c = Currency.getInstance(Locale.US);

    System.out.println("Symbol: " + c.getSymbol());
    System.out.println("Default fractional digits: " +
                       c.getDefaultFractionDigits());
  }
}
```

<!-- CR p.676 -->

The output is shown here:

```text
Symbol: $
Default fractional digits: 2
```

## Formatter

At the core of Java’s support for creating formatted output is the **Formatter** class. It provides *format conversions* that let you display numbers, strings, and time and date in virtually any format you like. It operates in a manner similar to the C/C++ **printf( )** function, which means that if you are familiar with C/C++, then learning to use **Formatter** will be very easy. It also further streamlines the conversion of C/C++ code to Java. If you are not familiar with C/C++, it is still quite easy to format data.

**NOTE** Although Java’s **Formatter** class operates in a manner very similar to the C/C++ **printf( )** function, there

are some differences, and some new features. Therefore, if you have a C/C++ background, a careful reading is advised.

### The Formatter Constructors

Before you can use **Formatter** to format output, you must create a **Formatter** object. In general, **Formatter** works by converting the binary form of data used by a program into formatted text. It stores the formatted text in a buffer, the contents of which can be obtained by your program whenever they are needed. It is possible to let **Formatter** supply this buffer automatically, or you can specify the buffer explicitly when a **Formatter** object is created. It is also possible to have **Formatter** output its buffer to a file.

The **Formatter** class defines many constructors, which enable you to construct a **Formatter** in a variety of ways. Here is a sampling:

Formatter( ) Formatter(Appendable *buf*) Formatter(Appendable *buf*, Locale *loc*) Formatter(String *filename*) throws FileNotFoundException Formatter(String *filename*, String *charset*) throws FileNotFoundException, UnsupportedEncodingException Formatter(File *outF*) throws FileNotFoundException Formatter(OutputStream *outStrm*)

Here, *buf* specifies a buffer for the formatted output. If *buf* is null, then **Formatter** automatically allocates a **StringBuilder** to hold the formatted output. The *loc* parameter specifies a locale. If no locale is specified, the default locale is used. The *filename* parameter specifies the name of a file that will receive the formatted output. The *charset* parameter specifies the character set. If no character set is specified, then the

<!-- CR p.677 -->

| Method | Description |
|---|---|
| void close( ) | Closes the invoking Formatter. This causes any resources used by the object to be released. After a Formatter has been closed, it cannot be reused. An attempt to use a closed Formatter results in a FormatterClosedException. |
| void flush( ) | Flushes the format buffer. This causes any output currently in the buffer to be written to the destination. This applies mostly to a Formatter tied to a file. |
| Formatter format(String fmtString, Object ... args) | Formats the arguments passed via args according to the format specifiers contained in fmtString. Returns the invoking object. |
| Formatter format(Locale loc, String fmtString, Object ... args) | Formats the arguments passed via args according to the format specifiers contained in fmtString. The locale specified by loc is used for this format. Returns the invoking object. |
| IOException ioException( ) | If the underlying object that is the destination for output throws an IOException, then this exception is returned. Otherwise, null is returned. |
| Locale locale( ) | Returns the invoking object’s locale. |
| Appendable out( ) | Returns a reference to the underlying object that is the destination for output. |
| String toString( ) | Returns a String containing the formatted output. |

**Table 21-11**

The Methods Defined by **Formatter**

default character set is used. The *outF* parameter specifies a reference to an open file that will receive output. The *outStrm* parameter specifies a reference to an output stream that will receive output. When using a file, output is also written to the file.

Perhaps the most widely used constructor is the first, which has no parameters. It automatically uses the default locale and allocates a **StringBuilder** to hold the formatted output.

### The Formatter Methods

**Formatter** defines the methods shown in Table 21-11.

### Formatting Basics

After you have created a **Formatter**, you can use it to create a formatted string. To do so, use the **format( )** method. The version we will use is shown here:

Formatter format(String *fmtString*, Object ... *arg*s) The *fmtSring* consists of two types of items. The first type is composed of characters that are simply copied to the output buffer. The second type contains *format specifiers* that define the way the subsequent arguments are displayed.

In its simplest form, a format specifier begins with a percent sign followed by the format *conversion specifier*. All format conversion specifiers consist of a single character. For example, the format specifier for floating-point data is **%f**. In general, there must be the same number of arguments as there are format specifiers, and the format specifiers and the arguments are matched in order from left to right. For example, consider this fragment:

<!-- CR p.678 -->

```java
Formatter fmt = new Formatter();
fmt.format("Formatting %s is easy %d %f", "with Java", 10, 98.6);
```

This sequence creates a **Formatter** that contains the following string:

```text
Formatting with Java is easy 10 98.600000
```

In this example, the format specifiers, **%s**, **%d**, and **%f**, are replaced with the arguments that follow the format string. Thus, **%s** is replaced by “with Java”, **%d** is replaced by 10, and **%f** is replaced by 98.6. All other characters are simply used as-is. As you might guess, the format specifier **%s** specifies a string, and **%d** specifies an integer value. As mentioned earlier, the **%f** specifies a floating-point value.

The **format( )** method accepts a wide variety of format specifiers, which are shown in Table 21-12. Notice that many specifiers have both upper- and lowercase forms. When an

| Format Specifier | Conversion Applied |
|---|---|
| %a %A | Floating-point hexadecimal |
| %b %B | Boolean |
| %c %C | Character |
| %d | Decimal integer |
| %h %H | Hash code of the argument |
| %e %E | Scientific notation |
| %f | Decimal floating-point |
| %g %G | Uses %e or %f, based on the value being formatted and the precision |
| %o | Octal integer |
| %n | Inserts a newline character |
| %s %S | String |
| %t %T | Time and date |
| %x %X | Integer hexadecimal |
| %% | Inserts a % sign |

**Table 21-12**

The Format Specifiers uppercase specifier is used, then letters are shown in uppercase. Otherwise, the upper- and lowercase specifiers perform the same conversion. It is important to understand that Java type-checks each format specifier against its corresponding argument. If the argument doesn’t match, an **IllegalFormatException** is thrown.

<!-- CR p.679 -->

Once you have formatted a string, you can obtain it by calling **toString( )**. For example, continuing with the preceding example, the following statement obtains the formatted string contained in `fmt`:

```java
String str = fmt.toString();
```

Of course, if you simply want to display the formatted string, there is no reason to first assign it to a `String` object. When a **Formatter** object is passed to **println( )**, for example, its **toString( )** method is automatically called.

Here is a short program that puts together all of the pieces, showing how to create and display a formatted string:

```java
// A very simple example that uses Formatter.
import java.util.*;

class FormatDemo {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    fmt.format("Formatting %s is easy %d %f", "with Java", 10, 98.6);

    System.out.println(fmt);
    fmt.close();
  }
}
```

One other point: You can obtain a reference to the underlying output buffer by calling **out( )**. It returns a reference to an **Appendable** object.

Now that you know the general mechanism used to create a formatted string, the remainder of this section discusses in detail each conversion. It also describes various options, such as justification, minimum field width, and precision.

### Formatting Strings and Characters

To format an individual character, use **%c**. This causes the matching character argument to be output, unmodified. To format a string, use **%s**.

### Formatting Numbers

To format an integer in decimal format, use **%d**. To format a floating-point value in decimal format, use **%f**. To format a floating-point value in scientific notation, use **%e**. Numbers represented in scientific notation take this general form:

*x.dddddd*e+/–yy

<!-- CR p.680 -->

The **%g** format specifier causes **Formatter** to use either **%f** or **%e**, based on the value being formatted and the precision, which is 6 by default. The following program demonstrates the effect of the **%f** and **%e** format specifiers:

```java
// Demonstrate the %f and %e format specifiers.
import java.util.*;

class FormatDemo2 {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    for(double i=1.23; i < 1.0e+6; i *= 100) {
      fmt.format("%f %e ", i, i);
      System.out.println(fmt);
    }
    fmt.close();

  }
}
```

It produces the following output:

```text
1.230000 1.230000e+00
1.230000 1.230000e+00 123.000000 1.230000e+02
1.230000 1.230000e+00 123.000000 1.230000e+02 12300.000000 1.230000e+04
```

You can display integers in octal or hexadecimal format by using **%o** and **%x**, respectively. For example, this fragment:

```java
fmt.format("Hex: %x, Octal: %o", 196, 196);
```

produces this output:

```text
Hex: c4, Octal: 304
```

You can display floating-point values in hexadecimal format by using **%a**. The format produced by **%a** appears a bit strange at first glance. This is because its representation uses a form similar to scientific notation that consists of a hexadecimal significand and a decimal exponent of powers of 2. Here is the general format:

0x1.*sig*p*exp*

Here, *sig* contains the fractional portion of the significand and *exp* contains the exponent. The `p` indicates the start of the exponent. For example, this call:

```java
fmt.format("%a", 512.0);
```

produces this output:

```text
0x1.0p9
```

<!-- CR p.681 -->

### Formatting Time and Date

One of the more powerful conversion specifiers is **%t**. It lets you format time and date information. The **%t** specifier works a bit differently than the others because it requires the use of a suffix to describe the portion and precise format of the time or date desired. The suffixes are shown in Table 21-13. For example, to display minutes, you would use **%tM**, where **M** indicates minutes in a two-character field. The argument corresponding to the **%t** specifier must be of type **Calendar**, **Date**, **Long**, `long`, or **TemporalAccessor**.

| Suffix | Replaced By |
|---|---|
| a | Abbreviated weekday name |
| A | Full weekday name |
| b | Abbreviated month name |
| B | Full month name |
| c | Standard date and time string formatted as day month date hh::mm:ss tzone year |
| C | First two digits of year |
| d | Day of month as a decimal (01—31) |
| D | month/day/year |
| e | Day of month as a decimal (1—31) |
| F | year-month-day |
| h | Abbreviated month name |
| H | Hour (00 to 23) |
| I | Hour (01 to 12) |
| j | Day of year as a decimal (001 to 366) |
| k | Hour (0 to 23) |
| l | Hour (1 to 12) |
| L | Millisecond (000 to 999) |
| m | Month as decimal (01 to 13) |
| M | Minute as decimal (00 to 59) |
| N | Nanosecond (000000000 to 999999999) |
| p | Locale’s equivalent of AM or PM in lowercase |
| Q | Milliseconds from 1/1/1970 |
| r | hh:mm:ss (12-hour format) |
| R | hh:mm (24-hour format) |
| S | Seconds (00 to 60) |
| s | Seconds from 1/1/1970 UTC |

**Table 21-13**

The Time and Date Format Suffixes *(continued)*

<!-- CR p.682 -->

| Suffix | Replaced By |
|---|---|
| T | hh:mm:ss (24-hour format) |
| y | Year in decimal without century (00 to 99) |
| Y | Year in decimal including century (0001 to 9999) |
| z | Offset from UTC |
| Z | Time zone name |

**Table 21-13**

The Time and Date Format Suffixes

Here is a program that demonstrates several of the formats:

```java
// Formatting time and date.
import java.util.*;

class TimeDateFormat {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();

    // Display standard 12-hour time format.
    fmt.format("%tr", cal);
    System.out.println(fmt);
    fmt.close();

    // Display complete time and date information.
    fmt = new Formatter();
    fmt.format("%tc", cal);
    System.out.println(fmt);
    fmt.close();

    // Display just hour and minute.
    fmt = new Formatter();
    fmt.format("%tl:%tM", cal, cal);
    System.out.println(fmt);
    fmt.close();

    // Display month by name and number.
    fmt = new Formatter();
    fmt.format("%tB %tb %tm", cal, cal, cal);
    System.out.println(fmt);
    fmt.close();
  }
}
```

Sample output is shown here:

```text
03:15:34 PM
Sat Jan 01 15:15:34 CST 2022
3:15
January Jan 01
```

<!-- CR p.683 -->

### The %n and %% Specifiers

The **%n** and%% format specifiers differ from the others in that they do not match an argument. Instead, they are simply escape sequences that insert a character into the output sequence. The **%n** inserts a newline. The %% inserts a percent sign. Neither of these characters can be entered directly into the format string. Of course, you can also use the standard escape sequence **\n** to embed a newline character.

Here is an example that demonstrates the **%n** and %% format specifiers:

```java
// Demonstrate the %n and %% format specifiers.
import java.util.*;

class FormatDemo3 {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    fmt.format("Copying file%nTransfer is %d%% complete", 88);
    System.out.println(fmt);
    fmt.close();
  }
}
```

It displays the following output:

```text
Copying file
Transfer is 88% complete
```

### Specifying a Minimum Field Width

An integer placed between the % sign and the format conversion code acts as a *minimum field-width specifier*. This pads the output with spaces to ensure that it reaches a certain minimum length. If the string or number is longer than that minimum, it will still be printed in full. The default padding is done with spaces. If you want to pad with 0’s, place a 0 before the field-width specifier. For example, **%05d** will pad a number of less than five digits with 0’s so that its total length is five. The field-width specifier can be used with all format specifiers except **%n**.

The following program demonstrates the minimum field-width specifier by applying it to the **%f** conversion:

```java
// Demonstrate a field-width specifier.
import java.util.*;

class FormatDemo4 {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    fmt.format("|%f|%n|%12f|%n|%012f|",
               10.12345, 10.12345, 10.12345);
    System.out.println(fmt);
    fmt.close();

  }
}
```

<!-- CR p.684 -->

This program produces the following output:

```text
|10.123450|
|   10.123450|
|00010.123450|
```

The first line displays the number 10.12345 in its default width. The second line displays that value in a 12-character field. The third line displays the value in a 12-character field, padded with leading zeros.

The minimum field-width modifier is often used to produce tables in which the columns line up. For example, the next program produces a table of squares and cubes for the numbers between 1 and 10:

```java
// Create a table of squares and cubes.
import java.util.*;

class FieldWidthDemo {
  public static void main(String[] args) {
    Formatter fmt;

    for(int i=1; i <= 10; i++) {
      fmt = new Formatter();
      fmt.format("%4d %4d %4d", i, i*i, i*i*i);
      System.out.println(fmt);
      fmt.close();
   }

  }
}
```

Its output is shown here:

```text
  1    1
  4    8
  9   27
 16   64
 25  125
 36  216
 49  343
 64  512
 81  729
100 1000
```

<!-- CR p.685 -->

### Specifying Precision

A *precision specifier* can be applied to the **%f**, **%e**, **%g**, and **%s** format specifiers, among others. It follows the minimum field-width specifier (if there is one) and consists of a period followed by an integer. Its exact meaning depends upon the type of data to which it is applied.

When you apply the precision specifier to floating-point data using the **%f** or **%e** specifiers, it determines the number of decimal places displayed. For example, `%10.4f` displays a number at least ten characters wide with four decimal places. When using **%g**, the precision determines the number of significant digits. The default precision is 6.

Applied to strings, the precision specifier specifies the maximum field length. For example, `%5.7s` displays a string of at least five and not exceeding seven characters long. If the string is longer than the maximum field width, the end characters will be truncated.

The following program illustrates the precision specifier:

```java
// Demonstrate the precision modifier.
import java.util.*;

class PrecisionDemo {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    // Format 4 decimal places.
    fmt.format("%.4f", 123.1234567);
    System.out.println(fmt);
    fmt.close();

    // Format to 2 decimal places in a 16 character field
    fmt = new Formatter();
    fmt.format("%16.2e", 123.1234567);
    System.out.println(fmt);
    fmt.close();

    // Display at most 15 characters in a string.
    fmt = new Formatter();
    fmt.format("%.15s", "Formatting with Java is now easy.");
    System.out.println(fmt);
    fmt.close();
  }
}
```

It produces the following output:

```text
123.1235
        1.23e+02
Formatting with
```

<!-- CR p.686 -->

### Using the Format Flags

**Formatter** recognizes a set of format *flags* that lets you control various aspects of a conversion. All format flags are single characters, and a format flag follows the % in a format specification. The flags are shown here:

| Flag | Effect |
|---|---|
| – | Left justification |
| # | Alternate conversion format |
| 0 | Output is padded with zeros rather than spaces |
| space | Positive numeric output is preceded by a space |
| + | Positive numeric output is preceded by a + sign |
| , | Numeric values include grouping separators |
| ( | Negative numeric values are enclosed within parentheses |

Not all flags apply to all format specifiers. The following sections explain each in detail.

### Justifying Output

By default, all output is right-justified. That is, if the field width is larger than the data printed, the data will be placed on the right edge of the field. You can force output to be left-justified by placing a minus sign directly after the %. For instance, `%–10.2f` left-justifies a floating-point number with two decimal places in a 10-character field. For example, consider this program:

```java
// Demonstrate left justification.
import java.util.*;

class LeftJustify {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    // Right justify by default
    fmt.format("|%10.2f|", 123.123);
    System.out.println(fmt);
    fmt.close();

    // Now, left justify.
    fmt = new Formatter();
    fmt.format("|%-10.2f|", 123.123);
    System.out.println(fmt);
    fmt.close();
  }
}
```

It produces the following output:

```text
|    123.12|
|123.12    |
```

<!-- CR p.687 -->

As you can see, the second line is left-justified within a 10-character field.

### The Space, +, 0, and ( Flags

To cause a + sign to be shown before positive numeric values, add the + flag. For example,

```java
fmt.format("%+d", 100);
```

creates this string:

```text
+100
```

When creating columns of numbers, it is sometimes useful to output a space before positive values so that positive and negative values line up. To do this, add the space flag. For example,

```java
// Demonstrate the space format specifiers.
import java.util.*;

class FormatDemo5 {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();

    fmt.format("% d", -100);
    System.out.println(fmt);
    fmt.close();

    fmt = new Formatter();
    fmt.format("% d", 100);
    System.out.println(fmt);
    fmt.close();

    fmt = new Formatter();
    fmt.format("% d", -200);
    System.out.println(fmt);
    fmt.close();

    fmt = new Formatter();
    fmt.format("% d", 200);
    System.out.println(fmt);
    fmt.close();
  }
}
```

The output is shown here:

```text
-100
 100
-200
 200
```

Notice that the positive values have a leading space, which causes the digits in the column to line up properly.

<!-- CR p.688 -->

To show negative numeric output inside parentheses, rather than with a leading –, use the ( flag. For example,

```java
fmt.format("%(d", -100);
```

creates this string:

```text
(100)
```

The 0 flag causes output to be padded with zeros rather than spaces.

### The Comma Flag

When displaying large numbers, it is often useful to add grouping separators, which in English are commas. For example, the value 1234567 is more easily read when formatted as 1,234,567. To add grouping specifiers, use the comma (,) flag. For example,

```java
fmt.format("%,.2f", 4356783497.34);
```

creates this string:

```text
4,356,783,497.34
```

### The # Flag

The # can be applied to **%o**, **%x**, **%e,** and **%f**. For **%e,** and **%f**, the # ensures that there will be a decimal point even if there are no decimal digits. If you precede the **%x** format specifier with a #, the hexadecimal number will be printed with a **0x** prefix. Preceding the **%o** specifier with # causes the number to be printed with a leading zero.

### The Uppercase Option

As mentioned earlier, several of the format specifiers have uppercase versions that cause the conversion to use uppercase where appropriate. The following table describes the effect.

| Specifier | Effect |
|---|---|
| %A | Causes the hexadecimal digits a through f to be displayed in uppercase as A through F. Also, the prefix 0x is displayed as 0X, and the p will be displayed as P. |
| %B | Uppercases the values true and false. |
| %E | Causes the e symbol that indicates the exponent to be displayed in uppercase. |
| %G | Causes the e symbol that indicates the exponent to be displayed in uppercase. |
| %H | Causes the hexadecimal digits a through f to be displayed in uppercase as A through F. |
| %S | Uppercases the corresponding string. |
| %X | Causes the hexadecimal digits a through f to be displayed in uppercase as A through F. Also, the optional prefix 0x is displayed as 0X, if present. |

For example, this call:

```java
fmt.format("%X", 250);
```

<!-- CR p.689 -->

creates this string:

```text
FA
```

This call:

```java
fmt.format("%E", 123.1234);
```

creates this string:

```text
1.231234E+02
```

### Using an Argument Index

**Formatter** includes a very useful feature that lets you specify the argument to which a format specifier applies. Normally, format specifiers and arguments are matched in order, from left to right. That is, the first format specifier matches the first argument, the second format specifier matches the second argument, and so on. However, by using an *argument index*, you can explicitly control which argument a format specifier matches.

An argument index immediately follows the % in a format specifier. It has the following format:

*n*$

where *n* is the index of the desired argument, beginning with 1. For example, consider this example:

```java
fmt.format("%3$d %1$d %2$d", 10, 20, 30);
```

It produces this string:

```text
30 10 20
```

In this example, the first format specifier matches 30, the second matches 10, and the third matches 20. Thus, the arguments are used in an order other than strictly left to right.

One advantage of argument indexes is that they enable you to reuse an argument without having to specify it twice. For example, consider this line:

```java
fmt.format("%d in hex is %1$x", 255);
```

It produces the following string:

```text
255 in hex is ff
```

As you can see, the argument 255 is used by both format specifiers.

There is a convenient shorthand called a *relative index* that enables you to reuse the argument matched by the preceding format specifier. Simply specify < for the argument index. For example, the following call to **format( )** produces the same results as the previous example:

```java
fmt.format("%d in hex is %<x", 255);
```

<!-- CR p.690 -->

Relative indexes are especially useful when creating custom time and date formats. Consider the following example:

```java
// Use relative indexes to simplify the
// creation of a custom time and date format.
import java.util.*;

class FormatDemo6 {
  public static void main(String[] args) {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();

    fmt.format("Today is day %te of %<tB, %<tY", cal);
    System.out.println(fmt);
    fmt.close();
  }
}
```

Here is sample output:

```text
Today is day 1 of January, 2022
```

Because of relative indexing, the argument `cal` need only be passed once, rather than three times.

### Closing a Formatter

In general, you should close a **Formatter** when you are done using it. Doing so frees any resources that it was using. This is especially important when formatting to a file, but it can be important in other cases, too. As the previous examples have shown, one way to close a **Formatter** is to explicitly call **close( )**. However, **Formatter** also implements the **AutoCloseable** interface. This means that it supports the `try`-with-resources statement. Using this approach, the **Formatter** is automatically closed when it is no longer needed.

The `try`-with-resources statement is described in Chapter 13, in connection with files, because files are some of the most commonly used resources that must be closed. However, the same basic techniques apply here. For example, here is the first **Formatter** example reworked to use automatic resource management:

```java
// Use automatic resource management with Formatter.
import java.util.*;

class FormatDemo {
  public static void main(String[] args) {

    try (Formatter fmt = new Formatter())
    {
      fmt.format("Formatting %s is easy %d %f", "with Java",
                  10, 98.6);
      System.out.println(fmt);
    }
  }
}
```

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

<!-- CR p.696 -->

The program reads numbers from the keyboard, summing them in the process, until the user enters the string "done". It then stops input and displays the average of the numbers. Here is a sample run:

```text
Enter numbers to average.
1.2
2
3.4
4
done
Average is 2.65
```

The program reads numbers until it encounters a token that does not represent a valid `double` value. When this occurs, it confirms that the token is the string "done". If it is, the program terminates normally. Otherwise, it displays an error.

Notice that the numbers are read by calling **nextDouble( )**. This method reads any number that can be converted into a `double` value, including an integer value, such as 2, and a floating-point value like 3.4. Thus, a number read by **nextDouble( )** need not specify a decimal point. This same general principle applies to all `next` methods. They will match and read any data format that can represent the type of value being requested.

One thing that is especially nice about `Scanner` is that the same technique used to read from one source can be used to read from another. For example, here is the preceding program reworked to average a list of numbers contained in a text file:

```java
// Use Scanner to compute an average of the values in a file.
import java.util.*;
import java.io.*;

class AvgFile {
  public static void main(String[] args)
    throws IOException {

    int count = 0;
    double sum = 0.0;

    // Write output to a file.
    FileWriter fout = new FileWriter("test.txt");
    fout.write("2 3.4 5 6 7.4 9.1 10.5 done");
    fout.close();

    FileReader fin = new FileReader("Test.txt");

    Scanner src = new Scanner(fin);

    // Read and sum numbers.
    while(src.hasNext()) {
      if(src.hasNextDouble()) {
        sum += src.nextDouble();
        count++;
      }
      else {
        String str = src.next();
        if(str.equals("done")) break;
        else {
          System.out.println("File format error.");
          return;
        }
      }
    }

    src.close();
    System.out.println("Average is " + sum / count);
  }
}
```

<!-- CR p.697 -->

Here is the output:

```text
Average is 6.2
```

The preceding program illustrates another important feature of `Scanner`. Notice that the file reader referred to by `fin` is not closed directly. Rather, it is closed automatically when `src` calls **close( )**. When you close a `Scanner`, the **Readable** associated with it is also closed (if that **Readable** implements the **Closeable** interface). Therefore, in this case, the file referred to by `fin` is automatically closed when `src` is closed.

`Scanner` also implements the **AutoCloseable** interface. This means that it can be managed by a `try`-with-resources block. As explained in Chapter 13, when `try`-with-resources is used, the scanner is automatically closed when the block ends. For example, `src` in the preceding program could have been managed like this:

```java
try (Scanner src = new Scanner(fin))
{
  // Read and sum numbers.
  while(src.hasNext()) {
    if(src.hasNextDouble()) {
      sum += src.nextDouble();
      count++;
    }
    else {
      String str = src.next();
      if(str.equals("done")) break;
      else {
        System.out.println("File format error.");
        return;
      }
    }
  }
}
```

To clearly demonstrate the closing of a `Scanner`, the following examples will call **close( )** explicitly, but you should feel free to use `try-`with-resources in your own code when appropriate.

<!-- CR p.698 -->

One other point: To keep this and the other examples in this section compact, I/O exceptions are simply thrown out of **main( )**. However, your real-world code will normally handle I/O exceptions itself.

You can use `Scanner` to read input that contains several different types of data—even if the order of that data is unknown in advance. You must simply check what type of data is available before reading it. For example, consider this program:

```java
// Use Scanner to read various types of data from a file.
import java.util.*;
import java.io.*;

class ScanMixed {
  public static void main(String[] args)
    throws IOException {

    int i;
    double d;
    boolean b;
    String str;

    // Write output to a file.
    FileWriter fout = new FileWriter("test.txt");
    fout.write("Testing Scanner 10 12.2 one true two false");
    fout.close();

    FileReader fin = new FileReader("Test.txt");

    Scanner src = new Scanner(fin);

    // Read to end.
    while(src.hasNext()) {
      if(src.hasNextInt()) {
        i = src.nextInt();
        System.out.println("int: " + i);
      }
      else if(src.hasNextDouble()) {
        d = src.nextDouble();
        System.out.println("double: " + d);
      }
      else if(src.hasNextBoolean()) {
        b = src.nextBoolean();
        System.out.println("boolean: " + b);
      }
      else {
        str = src.next();
        System.out.println("String: " + str);
      }
    }

    src.close();
  }
}
```

<!-- CR p.699 -->

Here is the output:

```java
String: Testing
String: Scanner
int: 10
double: 12.2
String: one
boolean: true
String: two
boolean: false
```

When reading mixed data types, as the preceding program does, you need to be a bit careful about the order in which you call the `next` methods. For example, if the loop reversed the order of the calls to **nextInt( )** and **nextDouble( )**, both numeric values would have been read as `double`s, because **nextDouble( )** matches any numeric string that can be represented as a `double`.

### Setting Delimiters

`Scanner` defines where a token starts and ends based on a set of *delimiters*. The default delimiters are the whitespace characters, and this is the delimiter set that the preceding examples have used. However, it is possible to change the delimiters by calling the **useDelimiter( )** method, shown here:

Scanner useDelimiter(String *pattern*)

Scanner useDelimiter(Pattern *pattern*)

Here, *pattern* is a regular expression that specifies the delimiter set.

Here is the program that reworks the average program shown earlier so that it reads a list of numbers that are separated by commas, and any number of spaces:

```java
// Use Scanner to compute an average a list of
// comma-separated values.
import java.util.*;
import java.io.*;

class SetDelimiters {
  public static void main(String[] args)
    throws IOException {

    int count = 0;
    double sum = 0.0;

    // Write output to a file.
    FileWriter fout = new FileWriter("test.txt");

    // Now, store values in comma-separated list.
    fout.write("2, 3.4,     5,6, 7.4, 9.1, 10.5, done");
    fout.close();

    FileReader fin = new FileReader("Test.txt");

    Scanner src = new Scanner(fin);
    // Set delimiters to space and comma.
    src.useDelimiter(", *");

    // Read and sum numbers.
    while(src.hasNext()) {
      if(src.hasNextDouble()) {
        sum += src.nextDouble();
        count++;
      }
      else {
        String str = src.next();
        if(str.equals("done")) break;
        else {
          System.out.println("File format error.");
          return;
        }
      }
    }

    src.close();
    System.out.println("Average is " + sum / count);
  }
}
```

<!-- CR p.700 -->

In this version, the numbers written to `test.txt` are separated by commas and spaces. The use of the delimiter pattern ", * " tells `Scanner` to match a comma and zero or more spaces as delimiters. The output is the same as before.

You can obtain the current delimiter pattern by calling **delimiter( )**, shown here:

Pattern delimiter( )

### Other Scanner Features

`Scanner` defines several other methods in addition to those already discussed. One that is particularly useful in some circumstances is **findInLine( )**. Its general forms are shown here:

String findInLine(Pattern *pattern*) String findInLine(String *pattern*)

This method searches for the specified pattern within the next line of text. If the pattern is found, the matching token is consumed and returned. Otherwise, `null` is returned. It operates independently of any delimiter set. This method is useful if you want to locate a specific pattern. For example, the following program locates the Age field in the input string and then displays the age:

```java
// Demonstrate findInLine().
import java.util.*;

class FindInLineDemo {
  public static void main(String[] args) {
    String instr = "Name: Tom Age: 28 ID: 77";

    Scanner conin = new Scanner(instr);
    // Find and display age.
    conin.findInLine("Age:"); // find Age

    if(conin.hasNext())
      System.out.println(conin.next());
    else
      System.out.println("Error!");

    conin.close();
  }
}
```

<!-- CR p.701 -->

The output is **28**. In the program, **findInLine( )** is used to find an occurrence of the pattern "Age". Once found, the next token is read, which is the age.

Related to **findInLine( )** is **findWithinHorizon( )**. It is shown here:

String findWithinHorizon(Pattern *pattern*, int *count*)

String findWithinHorizon(String *pattern*, int *count*)

This method attempts to find an occurrence of the specified pattern within the next *count* characters. If successful, it returns the matching pattern. Otherwise, it returns `null`. If *count* is zero, then all input is searched until either a match is found or the end of input is encountered.

You can bypass a pattern using **skip( )**, shown here:

Scanner skip(Pattern *pattern*)

Scanner skip(String *pattern*)

If *pattern* is matched, **skip( )** simply advances beyond it and returns a reference to the invoking object. If pattern is not found, **skip( )** throws **NoSuchElementException**.

Other `Scanner` methods include **radix( )**, which returns the default radix used by the `Scanner`; **useRadix( )**, which sets the radix; **reset( )**, which resets the scanner; and **close( )**, which closes the scanner. JDK 9 added the methods **tokens( )**, which returns all tokens in the form of a **Stream<String>**, and **findAll( )**, which returns tokens that match the specified pattern in the form of a **Stream<MatchResult>**.

## The ResourceBundle, ListResourceBundle, and PropertyResourceBundle Classes

The `java.util` package includes three classes that aid in the internationalization of your program. The first is the abstract class **ResourceBundle**. It defines methods that enable you to manage a collection of locale-sensitive resources, such as the strings that are used to label the user interface elements in your program. You can define two or more sets of translated strings that support various languages, such as English, German, or Chinese, with each translation set residing in its own bundle. You can then load the bundle appropriate to the current locale and use the strings to construct the program’s user interface.

Resource bundles are identified by their *family name* (also called their *base name*). To the family name can be added a *language code* which specifies the language. In this case, if a requested locale matches the language code, then that version of the resource bundle is used. For example, a resource bundle with a family name of **SampleRB** could have a German version called `SampleRB_de` and a Russian version called `SampleRB_ru`. (Notice that an underscore links the family name to the language code.) Therefore, if the locale is `Locale.GERMAN`, `SampleRB_de` will be used.

<!-- CR p.702 -->

It is also possible to indicate specific variants of a language that relate to a specific country by specifying a *country code* after the language code, such as **AU** for Australia or **IN** for India. A country code is also preceded by an underscore when linked to the resource bundle name. Other variations are also supported. A resource bundle that has only the family name is the default bundle. It is used when no language-specific bundles are applicable.

**NOTE** The language codes are defined by ISO standard 639 and the country codes by ISO standard 3166.

The methods defined by **ResourceBundle** are summarized in Table 21-17. One important point: `null` keys are not allowed and several of the methods will throw a **NullPointerException** if `null` is passed as the key. Notice the nested class `ResourceBundle.Control`. It is used to control the resource-bundle loading process.

| Method | Description |
|---|---|
| static final void clearCache( ) | Deletes all resource bundles from the cache that were loaded by the class loader. Beginning with JDK 9, this method deletes all resource bundles from the cache that were loaded by the module from which this method is called. |
| static final void clearCache(ClassLoader ldr) | Deletes all resource bundles from the cache that were loaded by ldr. |
| boolean containsKey(String k) | Returns true if k is a key within the invoking resource bundle (or its parent). |
| String getBaseBundleName( ) | Returns the resource bundle’s base name if available. Returns null otherwise. |
| static final ResourceBundle getBundle(String familyName) | Loads the resource bundle with a family name of familyName using the default locale. Throws MissingResourceException if no resource bundle matching the name is available. |
| static ResourceBundle getBundle( String familyName, Module mod) | Loads the resource bundle with a family name of familyName for the module specified by mod. The default locale is used. Throws MissingResourceException if no resource bundle matching the name is available. |
| static final ResourceBundle getBundle(String familyName, Locale loc) | Loads the resource bundle with a family name of familyName using the specified locale. Throws MissingResourceException if no resource bundle matching the name is available. |

**Table 21-17**

The Methods Defined by **ResourceBundle** *(continued)*

<!-- CR p.703 -->

| Method | Description |
|---|---|
| static ResourceBundle getBundle( String familyName, Locale loc, Module mod) | Loads the resource bundle with a family name of familyName using the locale passed in loc for the module specified by mod. Throws MissingResourceException if no resource bundle matching the name is available. |
| static ResourceBundle getBundle(String familyName, Locale loc, ClassLoader ldr) | Loads the resource bundle with a family name of familyName using the specified locale and the specified class loader. Throws MissingResourceException if no resource bundle matching the name is available. |
| static final ResourceBundle getBundle(String familyName, ResourceBundle.Control cntl) | Loads the resource bundle with a family name of familyName using the default locale. The loading process is under the control of cntl. Throws MissingResourceException if no resource bundle matching the name is available. |
| static final ResourceBundle getBundle(String familyName, Locale loc, ResourceBundle.Control cntl) | Loads the resource bundle with a family name of familyName using the specified locale. The loading process is under the control of cntl. Throws MissingResourceException if no resource bundle matching the name is available. |
| static ResourceBundle getBundle(String familyName, Locale loc, ClassLoader ldr, ResourceBundle.Control cntl) | Loads the resource bundle with a family name of familyName using the specified locale and the specified class loader. The loading process is under the control of cntl. Throws MissingResourceException if no resource bundle matching the name is available. |
| abstract Enumeration<String> getKeys( ) | Returns the resource bundle keys as an enumeration of strings. Any parent’s keys are also obtained. |
| Locale getLocale( ) | Returns the locale supported by the resource bundle. |
| final Object getObject(String k) | Returns the object associated with the key passed via k. Throws MissingResourceException if k is not in the resource bundle. |
| final String getString(String k) | Returns the string associated with the key passed via k. Throws MissingResourceException if k is not in the resource bundle. Throws ClassCastException if the object associated with k is not a string. |
| final String[ ] getStringArray(String k) | Returns the string array associated with the key passed via k. Throws MissingResourceException if k is not in the resource bundle. Throws MissingResourceException if the object associated with k is not a string array. |
| protected abstract Object handleGetObject(String k) | Returns the object associated with the key passed via k. Returns null if k is not in the resource bundle. |
| protected Set<String> handleKeySet( ) | Returns the resource bundle keys as a set of strings. No parent’s keys are obtained. |

**Table 21-17**

The Methods Defined by **ResourceBundle** *(continued)*

<!-- CR p.704 -->

| Method | Description |
|---|---|
| Set<String> keySet( ) | Returns the resource bundle keys as a set of strings. Any parent keys are also obtained. |
| protected void setParent(ResourceBundle parent) | Sets parent as the parent bundle for the resource bundle. When a key is looked up, the parent will be searched if the key is not found in the invoking resource object. |

**Table 21-17**

The Methods Defined by **ResourceBundle**

**NOTE** Notice that JDK 9 added methods to **ResourceBundle** that support modules. Furthermore, the addition

of modules raises several issues related to the use of resource bundles that are beyond the scope of this discussion. Consult the API documentation for details on how modules affect the use of **ResourceBundle**.

There are two subclasses of **ResourceBundle**. The first is **PropertyResourceBundle**, which manages resources by using property files. **PropertyResourceBundle** adds no methods of its own. The second is the abstract class **ListResourceBundle**, which manages resources in an array of key/value pairs. **ListResourceBundle** adds the method **getContents( )**, which all subclasses must implement. It is shown here:

protected abstract Object[ ][ ] getContents( )

It returns a two-dimensional array that contains key/value pairs that represent resources. The keys must be strings. The values are typically strings, but can be other types of objects.

Here is an example that demonstrates using a resource bundle in an unnamed module. The resource bundle has the family name **SampleRB**. Two resource bundle classes of this family are created by extending **ListResourceBundle**. The first is called **SampleRB**, and it is the default bundle (which uses English). It is shown here:

```java
import java.util.*;
public class SampleRB extends ListResourceBundle {
  protected Object[][] getContents() {
    Object[][] resources = new Object[3][2];

    resources[0][0] = "title";
    resources[0][1] = "My Program";

    resources[1][0] = "StopText";
    resources[1][1] = "Stop";

    resources[2][0] = "StartText";
    resources[2][1] = "Start";

    return resources;
  }
}
```

<!-- CR p.705 -->

The second resource bundle, shown next, is called `SampleRB_de`. It contains the German translation.

```java
import java.util.*;

// German version.
public class SampleRB_de extends ListResourceBundle {
  protected Object[][] getContents() {
    Object[][] resources = new Object[3][2];

    resources[0][0] = "title";
    resources[0][1] = "Mein Programm";

    resources[1][0] = "StopText";
    resources[1][1] = "Anschlag";

    resources[2][0] = "StartText";
    resources[2][1] = "Anfang";

    return resources;
  }
}
```

The following program demonstrates these two resource bundles by displaying the string associated with each key for both the default (English) version and the German version:

```java
// Demonstrate a resource bundle.
import java.util.*;

class LRBDemo {
  public static void main(String[] args) {
    // Load the default bundle.
    ResourceBundle rd = ResourceBundle.getBundle("SampleRB");

    System.out.println("English version: ");
    System.out.println("String for Title key : " +
                       rd.getString("title"));

    System.out.println("String for StopText key: " +
                       rd.getString("StopText"));

    System.out.println("String for StartText key: " +
                       rd.getString("StartText"));

    // Load the German bundle.
    rd = ResourceBundle.getBundle("SampleRB", Locale.GERMAN);

    System.out.println("\nGerman version: ");
    System.out.println("String for Title key : " +
                       rd.getString("title"));

    System.out.println("String for StopText key: " +
                       rd.getString("StopText"));
    System.out.println("String for StartText key: " +
                       rd.getString("StartText"));
  }
}
```

<!-- CR p.706 -->

The output from the program is shown here:

```text
English version:
String for Title key : My Program
String for StopText key: Stop
String for StartText key: Start

German version:
String for Title key : Mein Programm
String for StopText key: Anschlag
String for StartText key: Anfang
```
