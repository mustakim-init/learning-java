---
topic: branching
lessons: "M5_L1, M5_L2"
book: "Head First Java, 3rd ed. (Sierra, Bates, Gee)"
printed_pages: "15-15"
pdf_offset: "pdf page = printed page + 38"
generated_by: tools/extract_refs.py
---
# Branching (if/else) and nested branching - Head First Java, 3rd ed. (Sierra, Bates, Gee)

<!-- HF p.15 -->

### Conditional branching

In Java, an *if* test is basically the same as the boolean test in a *while* loop—except instead of saying, “***while*** there’s still chocolate,” you’ll say, “***if*** there’s still chocolate...”

```java
class IfTest {
  public static void main (String[] args) {
    int x = 3;
    if (x == 3) {
      System.out.println("x must be 3");
    }
    System.out.println("This runs no matter what");
  }
}

% java IfTest
x must be 3
This runs no matter what
```

The preceding code executes the line that prints “x must be 3” only if the condition (*x* is equal to 3) is true. Regardless of whether it’s true, though, the line that prints “This runs no matter what” will run. So depending on the value of *x*, either one statement or two will print out.

But we can add an *else* to the condition so that we can say something like, “*If* there’s still chocolate, keep coding, *else* (otherwise) get more chocolate, and then continue on...”

```java
class IfTest2 {
  public static void main(String[] args) {
    int x = 2;
    if (x == 3) {
      System.out.println("x must be 3");
    } else {
      System.out.println("x is NOT 3");
    }
    System.out.println("This runs no matter what");
  }
}

% java IfTest2
x is NOT 3
This runs no matter what
```

If you’ve been paying attention (of course you have), then you’ve noticed us switching between **print** and **println.**

**Did you spot the difference?**

System.out.***println*** inserts a newline (think of print***ln*** as **print*****new*****line**), while System.out.***print*** keeps printing to the *same* line. If you want each thing you print out to be on its own line, use print**ln**. If you want everything to stick together on one line, use print.

#### Sharpen your pencil

***Given the output:***

```text
% java DooBee
DooBeeDooBeeDo
```

***Fill in the missing code:***

```java
public class DooBee {
  public static void main(String[] args) {
    int x = 1;
    while (x < _____ ) {
      System.out._________("Doo");
      System.out._________("Bee");
      x = x + 1;
    }
    if (x == ______  ) {
      System.out.print("Do");
    }
  }
}
```

> *Figure/sidebar text on this page:* System.out.print vs. / System.out.println / Code output / New output / Answers on page 25.
