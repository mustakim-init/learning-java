---
topic: sorting
lessons: "M9"
book: "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"
printed_pages: "888-892"
pdf_offset: "pdf page = printed page + 23"
sections_in_scope: "23.1, 23.2, 23.3"
generated_by: tools/extract_refs.py
---
# Sorting - Introduction to Java Programming and Data Structures, 12th ed. (Liang)

<!-- LI p.888 -->

## 23.1 Introduction

*Sorting algorithms are good examples for studying algorithm design and analysis.*

**Key**

**Point**

When president Barack Obama visited Google in 2007, the Google CEO Eric Schmidt asked Obama the most efficient way to sort a million 32-bit integers (www.youtube .com/watch?v=k4RRi_ntQc8). Obama answered that the bubble sort would be the wrong way to go. Was he right? We will examine different sorting algorithms in this chapter and see if he was correct.

Sorting is a classic subject in computer science. There are three reasons to study sorting algorithms.

- First, sorting algorithms illustrate many creative approaches to problem solving, and these approaches can be applied to solve other problems.
- Second, sorting algorithms are good for practicing fundamental programming tech-niques using selection statements, loops, methods, and arrays.
- Third, sorting algorithms are excellent examples to demonstrate algorithm performance.

The data to be sorted might be integers, doubles, characters, or objects. Section 7.11, Sorting Arrays, presented selection sort. The selection-sort algorithm was extended to sort an array of objects in Section 19.5, Case Study: Sorting an Array of Objects. The Java API contains several overloaded sort methods for sorting primitive-type values and objects in the `java .util.Arrays` and `java.util.Collections` classes. For simplicity, this chapter assumes

1. data to be sorted are integers,
2. data are stored in an array, and
3. data are sorted in ascending order.

The programs can be easily modified to sort other types of data, to sort in descending order, or to sort data in an `ArrayList` or a `LinkedList`.

There are many algorithms for sorting. You have already learned selection sort. This chapter introduces insertion sort, bubble sort, merge sort, quick sort, bucket sort, radix sort, and external sort.

## 23.2 Insertion Sort

*The insertion-sort algorithm sorts a list of values by repeatedly inserting a new element into a sorted sublist until the whole list is sorted.*

**Key**

Figure 23.1 shows how to sort a list {`2`, `9`, `5`, `4`, `8`, `1`, `6`} using insertion sort. For an interactive

**Point**

demo on how insertion sort works, go to liveexample.pearsoncmg.com/dsanimation/InsertionSortNeweBook.html.

The algorithm can be described as follows:

```java
for (int i = 1; i < list.length; i++) {
  insert list[i] into a sorted sublist list[0..i−1] so that
  list[0..i] is sorted.
}
```

To insert `list[i]` into `list[0..i−1]`, save `list[i]` into a temporary variable, say `currentElement`. Move `list[i−1]` to `list[i]` if `list[i−1] > currentElement`, move `list[i−2]` to `list[i−1]` if `list[i−2] > currentElement`, and so on, until `list[i−k] <= currentElement` or `k > i` (we pass the first element of the sorted list). Assign `currentElement` to `list[i−k+1]`. For example, to insert `4` into {`2`, `5`, `9`} in Step 4 in Figure 23.2, move `list[2]` (`9`) to `list[3]` since `9 > 4` and move `list[1]` (`5`) to `list[2]` since `5 > 4`. Finally, move `currentElement` (`4`) to `list[1]`.

<!-- LI p.889 -->

**Figure 23.1** Insertion sort repeatedly inserts a new element into a sorted sublist.

```text
     [0][1][2][3][4][5]
                        [6]
list
                              currentElement:  4


     [0][1][2][3][4][5]
                        [6]
list


     [0][1][2][3][4][5]
                        [6]
list


     [0][1][2][3][4][5]
                        [6]
list
```

**Figure 23.2** A new element is inserted into a sorted sublist.

The algorithm can be expanded and implemented as in Listing 23.1.

**Listing 23.1 InsertionSort.java** *(line N of the listing = Nth line of the block)*

```java
public class InsertionSort {
  /** The method for sorting the numbers */
  public static void insertionSort(int[] list) {
    for (int i = 1; i < list.length; i++) {
      /** Insert list[i] into a sorted sublist list[0..i−1] so that
          list[0..i] is sorted. */
      int currentElement = list[i];
      int k;
      for (k = i − 1; k >= 0 && list[k] > currentElement; k−−) {
        list[k + 1] = list[k];
      }

      // Insert the current element into list[k + 1]
      list[k + 1] = currentElement;
    }
  }
}
```

<!-- LI p.890 -->

The `insertionSort(int[] list)` method sorts an array of `int` elements. The method is implemented with a nested `for` loop. The outer loop (with the loop control variable `i`) (line 4) is iterated in order to obtain a sorted sublist, which ranges from `list[0]` to `list[i]`. The inner loop (with the loop control variable `k`) inserts `list[i]` into the sublist from `list[0]` to `list[i−1]`.

To better understand this method, trace it with the following statements:

```java
int[] list = {1, 9, 4, 6, 5, −4};
InsertionSort.insertionSort(list);
```

The insertion-sort algorithm presented here sorts a list of elements by repeatedly inserting a new element into a sorted partial array until the whole array is sorted. At the *k*th iteration, to insert an element into an array of size *k*, it may take *k* comparisons to find the insertion position and *k* moves to insert the element. Let *T*(*n*) denote the complexity for insertion sort, and *c* denote the total number of other operations such as assignments and additional comparisons in each iteration. Thus,

*T*(*n*) = (2 + *c*) + (2 × 2 + *c*) + g + (2 × (*n* - 1) + *c*)

= 2(1 + 2 + g + *n* - 1) + *c*(*n* - 1)

= 2 (*n* - 1)*n* + *cn* - *c* = *n*2 - *n* + *cn* - *c* 2 = *O*(*n*2)

Therefore, the complexity of the insertion-sort algorithm is *O*(*n*2). Hence, the selection and insertion sorts are of the same time complexity.

**23.2.1** Describe how an insertion sort works. What is the time complexity for an insertion

**Check**

sort?

**Point**

**23.2.2** Use Figure 23.1 as an example to show how to apply an insertion sort on {45, 11,

50, 59, 60, 2, 4, 7, 10}. **23.2.3** If a list is already sorted, how many comparisons will the `insertionSort` method

perform?

## 23.3 Bubble Sort

> **Key Point** A bubble sort sorts the array in multiple passes. Each pass successively swaps the neighboring elements if the elements are not in order.

The bubble-sort algorithm makes several passes through the array. On each pass, successive neighboring pairs are compared. If a pair is in decreasing order, its values are swapped; otherwise, the values remain unchanged. The technique is called a *bubble sort* or *sinking sort* because the smaller values gradually “bubble” their way to the top and the larger values sink to the bottom. After the first pass, the last element becomes the largest in the array. After the second pass, the second-to-last element becomes the second largest in the array. This process is continued until all elements are sorted.

Figure 23.3a shows the first pass of a bubble sort on an array of six elements (2 9 5 4 8 1). Compare the elements in the first pair (2 and 9) and no swap is needed because they are already in order. Compare the elements in the second pair (9 and 5) and swap 9 with 5 because 9 is greater than 5. Compare the elements in the third pair (9 and 4) and swap 9 with 4. Compare the elements in the fourth pair (9 and 8) and swap 9 with 8. Compare the elements in the fifth pair (9 and 1) and swap 9 with 1. The pairs being compared are high-lighted and the numbers already sorted are italicized in Figure 23.3. For an interactive demo on how bubble sort works, go to liveexample.pearsoncmg.com/dsanimation/BubbleSortNeweBook.html.

<!-- LI p.891 -->

*8 9 5 8 9 1 2 4 5 8 9*

*8 9 4 5 8 9 5 8 9*

**Figure 23.3** Each pass compares and orders the pairs of elements sequentially.

The first pass places the largest number (9) as the last in the array. In the second pass, as shown in Figure 23.3b, you compare and order pairs of elements sequentially. There is no need to consider the last pair because the last element in the array is already the largest. In the third pass, as shown in Figure 23.3c, you compare and order pairs of elements sequentially except the last two elements because they are already in order. Thus, in the *k*th pass, you don’t need to consider the last *k* - 1 elements because they are already ordered.

The algorithm for a bubble sort is described in Listing 23.2.

**Listing 23.2** *(line N of the listing = Nth line of the block)*

```java
                Bubble-Sort Algorithm
for (int k = 1; k < list.length; k++) {
  // Perform the kth pass
  for (int i = 0; i < list.length − k; i++) {
    if (list[i] > list[i + 1])
      swap list[i] with list[i + 1];
  }
}
```

Note if no swap takes place in a pass, there is no need to perform the next pass because all the elements are already sorted. You can use this property to improve the algorithm in Listing 23.2, as in Listing 23.3.

**Listing 23.3** *(line N of the listing = Nth line of the block)*

```java
                Improved Bubble-Sort Algorithm
boolean needNextPass = true;
for (int k = 1; k < list.length && needNextPass; k++) {
  // Array may be sorted and next pass not needed
  needNextPass = false;
  // Perform the kth pass
  for (int i = 0; i < list.length – k; i++) {
    if (list[i] > list[i + 1]) {
      swap list[i] with list[i + 1];
      needNextPass = true; // Next pass still needed
    }
  }
}
```

The algorithm can be implemented in Listing 23.4.

**Listing 23.4 BubbleSort.java** *(line N of the listing = Nth line of the block)*

```java
public class BubbleSort {
  /** Bubble sort method */
  public static void bubbleSort(int[] list) {
    boolean needNextPass = true;

    for (int k = 1; k < list.length && needNextPass; k++) {
      // Array may be sorted and next pass not needed
      needNextPass = false;
      for (int i = 0; i < list.length − k; i++) {
        if (list[i] > list[i + 1]) {
          // Swap list[i] with list[i + 1]
          int temp = list[i];
          list[i] = list[i + 1];
          list[i + 1] = temp;

          needNextPass = true; // Next pass still needed
        }
      }
    }
  }

  /** A test method */
  public static void main(String[] args) {
    int[] list = {2, 3, 2, 5, 6, 1, −2, 3, 14, 12};
    bubbleSort(list);
    for (int i = 0; i < list.length; i++)
      System.out.print(list[i] + " ");
  }

}

 −2 1 2 2 3 3 5 6 12 14
```

<!-- LI p.892 -->

In the best case, the bubble-sort algorithm needs just the first pass to find that the array is already sorted—no next pass is needed. Since the number of comparisons is *n* - 1 in the first pass, the best-case time for a bubble sort is *O*(*n*).

In the worst case, the bubble-sort algorithm requires *n* - 1 passes. The first pass makes *n* - 1 comparisons, the second pass makes *n* - 2 comparisons, and so on; the last pass makes 1 comparison. Thus, the total number of comparisons is as follows:

(*n* - 1) + (*n* - 2) + g + 2 + 1

= (*n* - 1)*n* = *n*2 2 - *n* 2 = *O*(*n*2) 2 Therefore, the worst-case time for a bubble sort is *O*(*n*2).

**23.3.1** Describe how a bubble sort works. What is the time complexity for a bubble sort?

**Check**

**23.3.2** Use Figure 23.3 as an example to show how to apply a bubble sort on {45, 11, 50,

**Point**

59, 60, 2, 4, 7, 10}. **23.3.3** If a list is already sorted, how many comparisons will the `bubbleSort` method

perform?
