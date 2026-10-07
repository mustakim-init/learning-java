---
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
chapter: "ch02 2.1 Introduction"
printed_pages: "64-75"
pdf_offset: "pdf page = printed page + 23"
generated_by: tools/extract_refs.py --full
---
# ch02 2.1 Introduction

<!-- LI p.64 -->

## 2.18 Case Study: Counting Monetary Units

*This section presents a program that breaks a large amount of money into smaller units.*

Suppose you want to develop a program that changes a given amount of money into smaller

**Key Point**

monetary units. The program lets the user enter an amount as a `double` value representing a total in dollars and cents, and outputs a report listing the monetary equivalent in the maximum number of dollars, quarters, dimes, nickels, and pennies, in this order, to result in the minimum number of coins. Here are the steps in developing the program:

<!-- LI p.65 -->

1. Prompt the user to enter the amount as a decimal number, such as `11.56`.
2. Convert the amount (e.g., `11.56`) into cents (`1156`).
3. Divide the cents by `100` to find the number of dollars. Obtain the remaining cents using the cents remainder `100`.
4. Divide the remaining cents by `25` to find the number of quarters. Obtain the remaining cents using the remaining cents remainder `25`.
5. Divide the remaining cents by `10` to find the number of dimes. Obtain the remaining cents using the remaining cents remainder `10`.
6. Divide the remaining cents by `5` to find the number of nickels. Obtain the remaining cents using the remaining cents remainder `5`.
7. The remaining cents are the pennies.
8. Display the result.

The complete program is given in Listing 2.10.

**Listing 2.10 ComputeChange.java** *(line N of the listing = Nth line of the block)*

```java
import java.util.Scanner;

public class ComputeChange {
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);

    // Receive the amount
    System.out.print(
      "Enter an amount in double, for example 11.56: ");
    double amount = input.nextDouble();

    int remainingAmount = (int)(amount * 100);

    // Find the number of one dollars
    int numberOfOneDollars = remainingAmount / 100;
    remainingAmount = remainingAmount % 100;

    // Find the number of quarters in the remaining amount
    int numberOfQuarters = remainingAmount / 25;
    remainingAmount = remainingAmount % 25;

    // Find the number of dimes in the remaining amount
    int numberOfDimes = remainingAmount / 10;
    remainingAmount = remainingAmount % 10;

    // Find the number of nickels in the remaining amount
    int numberOfNickels = remainingAmount / 5;
    remainingAmount = remainingAmount % 5;

    // Find the number of pennies in the remaining amount
    int numberOfPennies = remainingAmount;

    // Display results
    System.out.println("Your amount " + amount + " consists of");
    System.out.println(" " + numberOfOneDollars + " dollars");
    System.out.println(" " + numberOfQuarters + " quarters ");
    System.out.println(" " + numberOfDimes + " dimes");
    System.out.println(" " + numberOfNickels + " nickels");
    System.out.println(" " + numberOfPennies + " pennies");
  }
}


 Enter an amount in double, for example, 11.56: 11.56
 Your amount 11.56 consists of
       11 dollars
       2 quarters
       0 dimes
       1 nickels
       1 pennies
```

<!-- LI p.66 -->

```text
             line#
                      11
                              13
                                    16
                                         17
                                              20
                                                   21
                                                       24
                                                            25
                                                                 28
                                                                     29
                                                                          32

variables

amount
                      11.56

remainingAmount
                              1156
                                         56
                                                   6
                                                            6
                                                                     1

numberOfOneDollars
                                    11

numberOfQuarters
                                              2

numberOfDimes
                                                       0

numberOfNickels
                                                                 1

numberOfPennies
                                                                          1
```

The variable `amount` stores the amount entered from the console (line 11). This variable is not changed, because the amount has to be used at the end of the program to display the results. The program introduces the variable `remainingAmount` (line 13) to store the changing remaining amount.

The variable `amount` is a `double` decimal representing dollars and cents. It is converted to an `int` variable `remainingAmount`, which represents all the cents. For instance, if `amount` is `11.56`, then the initial `remainingAmount` is `1156`. The division operator yields the integer part of the division, so `1156 / 100` is `11`. The remainder operator obtains the remainder of the division, so `1156 % 100` is `56`.

The program extracts the maximum number of singles from the remaining amount and obtains a new remaining amount in the variable `remainingAmount` (lines 16–17). It then extracts the maximum number of quarters from `remainingAmount` and obtains a new `remainingAmount` (lines 20–21). Continuing the same process, the program finds the maximum number of dimes, nickels, and pennies in the remaining amount.

One serious problem with this example is the possible loss of precision when casting a `double` amount to an `int remainingAmount`. This could lead to an inaccurate result. If you try to enter the amount `10.03`, `10.03 * 100` becomes `1002.9999999999999`. You will find that the program displays `10` dollars and `2` pennies. To fix the problem, enter the amount as an integer value representing cents (see Programming Exercise 2.22).

**2.18.1** Show the output of Listing 2.10 with the input value `1.99`. Why does the program

**Check Point**

produce an incorrect result for the input 10.03?

<!-- LI p.67 -->

## 2.19 Common Errors and Pitfalls

> **Key Point** Common elementary programming errors often involve undeclared variables, uninitialized variables, integer overflow, unintended integer division, and round-off errors.

**Common Error 1: Undeclared/Uninitialized Variables and Unused Variables** A variable must be declared with a type and assigned a value before using it. A common error is not declaring a variable or initializing a variable. Consider the following code:

```java
double interestRate = 0.05;
double interest = interestrate * 45;
```

This code is wrong, because `interestRate` is assigned a value `0.05`; but `interestrate` has not been declared and initialized. Java is case sensitive, so it considers `interestRate` and `interestrate` to be two different variables.

If a variable is declared, but not used in the program, it might be a potential programming error. Therefore, you should remove the unused variable from your program. For example, in the following code, `taxRate` is never used. It should be removed from the code.

```java
double interestRate = 0.05;
double taxRate = 0.05;
double interest = interestRate * 45;
System.out.println("Interest is " + interest);
```

If you use an IDE such as Eclipse and NetBeans, you will receive a warning on unused variables.

**Common Error 2: Integer Overflow** Numbers are stored with a limited numbers of digits. When a variable is assigned a value that is too large (*in size*) to be stored, it causes *overflow*. For example, executing the following statement causes overflow, because the largest value that can be stored in a variable of the `int` type is `2147483647`. `2147483648` will be too large for an `int` value:

```java
int value = 2147483647 + 1;
```

`// value will actually be` -`2147483648`

Likewise, executing the following statement also causes overflow, because the smallest value that can be stored in a variable of the `int` type is -`2147483648`. -`2147483649` is too large in size to be stored in an `int` variable.

```java
int value = –2147483648 – 1;
// value will actually be 2147483647
```

Java does not report warnings or errors on overflow, so be careful when working with integers close to the maximum or minimum range of a given type.

When a floating-point number is too small (i.e., too close to zero) to be stored, it causes *underflow*. Java approximates it to zero, so normally you don’t need to be concerned about underflow.

**Common Error 3: Round-off Errors** A *round-off error*, also called a *rounding error*, is the difference between the calculated approximation of a number and its exact mathematical value. For example, 1/3 is approximately 0.333 if you keep three decimal places, and is 0.3333333 if you keep seven decimal places. Since the number of digits that can be stored in a variable is limited, round-off errors are inevitable. Calculations involving floating-point numbers are approximated because these numbers are not stored with complete accuracy. For example,

<!-- LI p.68 -->

`System.out.println(1.0` - `0.1` - `0.1` - `0.1` - `0.1` - `0.1);`

displays `0.5000000000000001`, not `0.5`, and

`System.out.println(1.0` - `0.9);`

displays `0.09999999999999998`, not `0.1`. Integers are stored precisely. Therefore, calculations with integers yield a precise integer result.

**Common Error 4: Unintended Integer Division** Java uses the same divide operator, namely /, to perform both integer and floating-point division. When two operands are integers, the / operator performs an integer division. The result of the operation is an integer. The fractional part is truncated. To force two integers to perform a floating-point division, make one of the integers into a floating-point number. For example, the code in (a) displays that `average` as `1` and the code in (b) displays that `average` as `1.5`.

```java
int number1 = 1;
                                                 int number1 = 1;
int number2 = 2;
                                                 int number2 = 2;
double average = (number1 + number2) / 2;
                                                 double average = (number1 + number2) / 2.0;
System.out.println(average);
                                                 System.out.println(average);
```

(a) (b)

**Common Pitfall 1: Redundant Input Objects** New programmers often write the code to create multiple input objects for each input. For example, the following code in (a) reads an integer and a double value:

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter an integer: ");
int v1 = input.nextInt();
```

`Scanner input1 = new Scanner(System.in);` **BAD CODE**

```java
System.out.print("Enter a double value: ");
double v2 = input1.nextDouble();
```

The code is not good. It creates two input objects unnecessarily and may lead to some subtle errors. You should rewrite the code in (b):

`Scanner input = new Scanner(System.in);` **GOOD CODE**

```java
System.out.print("Enter an integer: ");
int v1 = input.nextInt();
System.out.print("Enter a double value: ");
double v2 = input.nextDouble();
```

**2.19.1** Can you declare a variable as `int` and later redeclare it as `double`?

**Check Point**

**2.19.2** What is an integer overflow? Can floating-point operations cause overflow?

**2.19.3** Will overflow cause a runtime error?

**2.19.4** What is a round-off error? Can integer operations cause round-off errors? Can

floating-point operations cause round-off errors?

**Key Terms**

algorithm, 34

casting, 59 assignment operator (=), 42

constant, 43 assignment statement, 42

data type, 35 `byte` *type*, 45

declare variables, 35 decrement operator (– –), 57

<!-- LI p.69 -->

postdecrement, 57 `double` *type*, 45

postincrement, 57 expression, 42

*predecrement*, 57 `final` keyword, 43

preincrement, 57 `float` *type*, 45

primitive data type, 35 floating-point number, 35

pseudocode, 34 identifier, 40

requirements specification, 61 increment operator (++), 57

scope of a variable, 41 *incremental coding and testing*, 64

`short` *type*, 45 `int` *type*, 45

specific import, 38 IPO, 39

system analysis, 61 literal, 48

system design, 61 `long` *type*, 45

underflow, 67 narrowing a type, 59

UNIX epoch, 54 operand, 46

variable, 35 *operator*, 46

widening a type, 59 *overflow*, 67

wildcard import, 38

**Chapter Summary**

**1.** *Identifiers* are names for naming elements such as variables, constants, methods, classes, and packages in a program.

**2.** An identifier is a sequence of characters that consists of letters, digits, underscores (`_`), and dollar signs ($). An identifier must start with a letter or an underscore. It cannot start with a digit. An identifier cannot be a reserved word. An identifier can be of any length.

**3.** *Variables* are used to store data in a program. To declare a variable is to tell the compiler what type of data a variable can hold.

**4.** There are two types of `import` statements: *specific import* and *wildcard import*. The specific import specifies a single class in the import statement. The wildcard import imports all the classes in a package.

**5.** In Java, the equal sign (=) is used as the *assignment operator.*

**6.** A variable declared in a method must be assigned a value before it can be used.

**7.** A *named constant* (or simply a *constant*) represents permanent data that never changes.

**8.** A named constant is declared by using the keyword `final`.

**9.** Java provides four integer types (`byte`, `short`, `int`, and `long`) that represent integers of four different sizes.

**10.** Java provides two *floating-point types* (`float` and `double`) that represent floating-point numbers of two different precisions.

**11.** Java provides *operators* that perform numeric operations: + (addition), – (subtraction), * (multiplication), / (division), and % (remainder).

**12.** Integer arithmetic (/) yields an integer result.

**13.** The numeric operators in a Java expression are applied the same way as in an arithmetic expression.

<!-- LI p.70 -->

**14.** Java provides the augmented assignment operators += (addition assignment), –= (subtraction assignment), *= (multiplication assignment), /= (division assignment), and %= (remainder assignment).

**15.** The *increment operator* (++) and the *decrement operator* (––) increment or decrement a variable by `1`.

**16.** When evaluating an expression with values of mixed types, Java automatically converts the operands to appropriate types.

**17.** You can explicitly convert a value from one type to another using the `(type)value` notation.

**18.** *Casting* a variable of a type with a small range to a type with a larger range is known as *widening a type*.

**19.** Casting a variable of a type with a large range to a type with a smaller range is known as *narrowing a type.*

**20.** Widening a type can be performed automatically without explicit casting. Narrowing a type must be performed explicitly.

**21.** In computer science, midnight of January 1, 1970, is known as the *UNIX epoch.*

**Quiz**

Answer the quiz for this chapter online at the Companion Website.

**Programming Exercises**

**Debugging Tip**

> The compiler usually gives a reason for a syntax error. If you don’t know how to correct it, compare your program closely, character by character, with similar examples in the text.

> **Pedagogical Note** Instructors may ask you to document your analysis and design for selected exercises. Use your own words to analyze the problem, including the input, output, and what needs to be computed, and describe how to solve the problem in pseudocode.

> **Pedagogical Note** The solution to most even-numbered programming exercises are provided to students. These exercises serve as additional examples for a variety of programs. To maximize the benefits of these solutions, students should first attempt to complete the even-numbered exercises and then compare their solutions with the solutions provided in the book. Since the book provides a large number of programming exercises, it is sufficient if you can complete all even-numbered programming exercises.

**Sections 2.2–2.13**

**2.1**

(*Convert Celsius to Fahrenheit*) Write a program that reads a Celsius degree in a `double` value from the console, then converts it to Fahrenheit, and displays the result. The formula for the conversion is as follows:

```text
fahrenheit = (9 / 5) * celsius + 32
```

Hint: In Java, `9 / 5` is `1`, but `9.0 / 5` is `1.8`. Here is a sample run:

<!-- LI p.71 -->

```text
Enter a degree in Celsius: 43.5
43.5 Celsius is 110.3 Fahrenheit
```

**2.2**

(*Compute the volume of a cylinder*) Write a program that reads in the radius and length of a cylinder and computes the area and volume using the following formulas:

```text
area = radius * radius * π
volume = area * length
```

Here is a sample run:

```text
Enter the radius and length of a cylinder: 5.5 12
The area is 95.0331
The volume is 1140.4
```

**2.3**

(*Convert feet into meters*) Write a program that reads a number in feet, converts it to meters, and displays the result. One foot is `0.305` meter. Here is a sample run:

```text
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters
```

**2.4**

(*Convert pounds into kilograms*) Write a program that converts pounds into kilograms. The program prompts the user to enter a number in pounds, converts it to kilograms, and displays the result. One pound is `0.454` kilogram. Here is a sample run:

```text
Enter a number in pounds: 55.5
55.5 pounds is 25.197 kilograms
```

***2.5**

(*Financial application: calculate tips*) Write a program that reads the subtotal and the gratuity rate, then computes the gratuity and total. For example, if the user enters `10` for subtotal and `15%` for gratuity rate, the program displays `$1.5` as gratuity and `$11.5` as total. Here is a sample run:

```text
Enter the subtotal and a gratuity rate: 10 15
The gratuity is $1.5 and total is $11.5
```

****2.6**

(*Sum the digits in an integer*) Write a program that reads an integer between `0` and `1000` and adds all the digits in the integer. For example, if an integer is `932`, the sum of all its digits is `14`. *Hint*: Use the % operator to extract digits, and use the / operator to remove the extracted digit. For instance, `932 % 10 = 2` and `932 / 10 = 93`. Here is a sample run:

```text
Enter a number between 0 and 1000: 999
The sum of the digits is 27
```

<!-- LI p.72 -->

***2.7**

(*Find the number of years*) Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays the maximum number of years and remaining days for the minutes. For simplicity, assume that a year has `365` days. Here is a sample run:

```text
Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
```

***2.8**

(*Current time*) Listing 2.7, ShowCurrentTime.java, gives a program that displays the current time in GMT. Revise the program so it prompts the user to enter the time zone offset to GMT and displays the time in the specified time zone. Here is a sample run:

`Enter the time zone offset to GMT:` -`5`

```text
The current time is 4:50:34
```

**2.9**

(*Physics: acceleration*) Average acceleration is defined as the change of velocity divided by the time taken to make the change, as given by the following formula:

*a* = *v*1 - *v*0 *t* Write a program that prompts the user to enter the starting velocity *v*0 in meters/ second, the ending velocity *v*1 in meters/second, and the time span *t* in seconds, then displays the average acceleration. Here is a sample run:

```text
Enter v0, v1, and t: 5.5 50.9 4.5
The average acceleration is 10.0889
```

**2.10**

(*Science: calculating energy*) Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water. The formula to compute the energy is

```text
Q = M * (finalTemperature – initialTemperature) * 4184
```

where `M` is the weight of water in kilograms, initial and final temperatures are in degrees Celsius, and energy `Q` is measured in joules. Here is a sample run:

```text
Enter the amount of water in kilograms: 55.5

Enter the initial temperature: 3.5

Enter the final temperature: 10.5

The energy needed is 1625484.0
```

**2.11**

(*Population projection*) Rewrite Programming Exercise 1.11 to prompt the user to enter the number of years and display the population after the number of years. Use the hint in Programming Exercise 1.11 for this program. Here is a sample run of the program:

```text
Enter the number of years: 5
The population in 5 years is 325932969
```

<!-- LI p.73 -->

**2.12**

(*Physics: finding runway length*) Given an airplane’s acceleration *a* and take-off speed *v,* you can compute the minimum runway length needed for an airplane to take off using the following formula:

length = *v*2 2*a* Write a program that prompts the user to enter *v* in meters/second (m/s) and the acceleration *a* in meters/second squared (m/s2), then, displays the minimum runway length.

```text
Enter speed and acceleration: 60 3.5
The minimum runway length for this airplane is 514.286
```

****2.13**

(*Financial application: compound value*) Suppose you save `$100` *each* month into a savings account with an annual interest rate of 5%. Thus, the monthly interest rate is 0.05/12 = 0.00417. After the first month, the value in the account becomes

```text
100 * (1 + 0.00417) = 100.417
```

After the second month, the value in the account becomes

```text
(100 + 100.417) * (1 + 0.00417) = 201.252
```

After the third month, the value in the account becomes

```text
(100 + 201.252) * (1 + 0.00417) = 302.507
```

and so on. Write a program that prompts the user to enter a monthly saving amount and displays the account value after the sixth month. (In Programming Exercise 5.30, you will use a loop to simplify the code and display the account value for any month.)

```text
Enter the monthly saving amount: 100
After the sixth month, the account value is $608.81
```

***2.14**

(*Health application: computing BMI*) Body Mass Index (BMI) is a measure of health on weight. It can be calculated by taking your weight in kilograms and divid-

**VideoNote**

ing, by the square of your height in meters. Write a program that prompts the user to

> Compute BMI

enter a weight in pounds and height in inches and displays the BMI. Note one pound is `0.45359237` kilograms and one inch is `0.0254` meters. Here is a sample run:

```text
Enter weight in pounds: 95.5

Enter height in inches: 50
```

mula for computing the distance is 2(*x*2 - *x*1)2 + (*y*2 - *y*1)2. Note you can use

```text
BMI is 26.8573
```

`Math.pow(a, 0.5)` to compute 2*a*. Here is a sample run:

**2.15**

(*Geometry: distance of two points*) Write a program that prompts the user to enter two points `(x1, y1)` and `(x2, y2)` and displays their distance. The for-

`Enter x1 and y1: 1.5` -`3.4`

```text
Enter x2 and y2: 4 5

The distance between the two points is 8.764131445842194
```

<!-- LI p.74 -->

Area = 323

**2.16**

(*Geometry: area of a hexagon*) Write a program that prompts the user to enter the side of a hexagon and displays its area. The formula for computing the area of a hexagon is

*s*2, 2 where *s* is the length of a side. Here is a sample run:

```text
Enter the length of the side: 5.5
The area of the hexagon is 78.5918
```

***2.17**

(*Science: wind-chill temperature*) How cold is it outside? The temperature alone is not enough to provide the answer. Other factors including wind speed, relative humidity, and sunshine play important roles in determining coldness outside. In 2001, the National Weather Service (NWS) implemented the new wind-chill temperature to measure the coldness using temperature and wind speed. The formula is

*twc* = 35.74 + 0.6215*ta* - 35.75*v*0.16 + 0.4275*tav*0.16

where *ta* is the outside temperature measured in degrees Fahrenheit, *v* is the speed measured in miles per hour, and *twc* is the wind-chill temperature. The formula cannot be used for wind speeds below 2 mph or temperatures below -58°F or above 41°F. Write a program that prompts the user to enter a temperature between -58°F and 41°F and a wind speed greater than or equal to `2` then displays the wind-chill temperature. Use `Math.pow(a, b)` to compute *v*0.16. Here is a sample run:

`Enter the temperature in Fahrenheit between` -`58`°F `and 41°F:`

```text
5.3
```

`Enter the wind speed (`7 = `2) in miles per hour: 6 The wind chill index is` -`5.56707`

**2.18**

(*Print a table*) Write a program that displays the following table. Cast floating-point numbers into integers.

```text
a    b    pow(a, b)
  2    1
  3    8
  4    81
  5    1024
  6    15625
```

***2.19**

(*Geometry: area of a triangle*) Write a program that prompts the user to enter three points, `(x1, y1)`, `(x2, y2)`, and `(x3, y3)`, of a triangle then displays

area = 2*s*(*s* - side1)(*s* - side2)(*s* - side3) its area. The formula for computing the area of a triangle is

*s* = (side1 + side2 + side3)/2;

Here is a sample run:

```text
Enter the coordinates of three points separated by spaces
```

`like x1 y1 x2 y2 x3 y3: 1.5` -`3.4 4.6 5 9.5` -`3.4`

```text
The area of the triangle is 33.6
```

<!-- LI p.75 -->

**Sections 2.13–2.18**

***2.20**

(*Financial application: calculate interest*) If you know the balance and the annual percentage interest rate, you can compute the interest on the next monthly payment using the following formula:

interest = balance × (`annualInterestRate`/1200) Write a program that reads the balance and the annual percentage interest rate and displays the interest for the next month. Here is a sample run:

```text
Enter balance and interest rate (e.g., 3 for 3%): 1000 3.5
The interest is 2.91667
```

***2.21**

(*Financial application: calculate future investment value*) Write a program that reads in investment amount, annual interest rate, and number of years and displays the future investment value using the following formula:

`futureInvestmentValue` =

For example, if you enter amount `1000`, annual interest rate `3.25%`, and number of years `1`, the future investment value is `1032.98`. Here is a sample run:

```text
Enter investment amount: 1000.56

Enter annual interest rate in percentage: 4.25

Enter number of years: 1

Future value is $1043.92
```

***2.22**

(*Financial*

*application: monetary units*) Rewrite Listing 2.10, ComputeChange.java, to fix the possible loss of accuracy when converting a `double` value to an `int` value. Enter the input as an integer whose last two digits represent the cents. For example, the input `1156` represents `11` dollars and `56` cents.

***2.23**

(*Cost of driving*) Write a program that prompts the user to enter the distance to drive, the fuel efficiency of the car in miles per gallon, and the price per gallon then displays the cost of the trip. Here is a sample run:

```text
Enter the driving distance: 900.5

Enter miles per gallon: 25.5

Enter price per gallon: 3.55

The cost of driving is $125.36
```

> **Note** More than 200 additional programming exercises with solutions are provided to the instructors on the Instructor Resource Website.
