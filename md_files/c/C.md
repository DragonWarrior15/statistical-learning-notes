# C Notes
***
### `'` vs `"`
Single quotes refer to a single character in C. `char c = 'x'` is a valid statement. Double quotes will refer to string literals. `char c = "x"` is not valid. String literals can be used to return strings corresponding to various cases in a switch statement.
***

### Structs
These are useful when we want to group a set of variables together that makes logical sense to do (using structs for grouping unrelated variables together, for passing values in function arguments etc is considered bad practice). For instance, we need a data type rectangle, that can store the coordinates and size of a rectangle. ```struct```  defines this in one place and this new data type can be used multiple times in the code.

#### Declaration
There are a couple of different ways to define a struct and use it
```c
struct rect_t{
    int x;
    int y;
    int width;
    int height;
};

// usage in function
struct rect_t myRect;
```
The ```_t``` in the name of the struct is a convention that helps identify a type. ```myRect``` will be the new instance of ```struct rect_t```.


We can also define the struct "tag" and then use a ```typedef``` to define its alias. The instantiation of the struct will change
```c
struct rect_tag{
    int x;
    int y;
    int width;
    int height;
};
typedef struct rect_tag rect_t

rect_t myRect
```
the keyword ```typedef``` defines a new type ```rect_t``` which is nothing but ```struct rect_tag```. The usage in the code is more simpler now.


We can define the data type in the struct declaration itself
```c
typedef struct rect_tag{
    int x;
    int y;
    int width;
    int height;
}rect_t;

rect_t myRect;
```
which is a compact version of the previous definition


One more way is possible, but comes with its downside that the struct cannot refer to itself
```c
typedef struct{
    int x;
    int y;
    int width;
    int height;
}rect_t;

rect_t myRect;
```

#### Accessing fields
`.` can be used to access the fields of a struct
```c
rect_t myRect;
myRect.x = 4;
printf("x coordinate %d", myRect.x);
```
***

### typedef
`typedef` lets us declare an alias for an existing data type. For instance, we can declare a shorthand for `unsigned int`
```c
typdef unsigned int uint;
uint x = 10;
printf('x is %u', x);
```

These can help reduce reuse of some constructs in the code and make the code less error prone. For instance, now we do not need to change `unsigned int` to `int` everywhere in the code, in case we make some modifications to our program. Just changing it near the `typedef` will suffice.
***

### Enumerated types
These is a useful abstraction in case when we have a set of values that need to be referred, but it doesn't really matter how they are stored internally. `enum` keyword helps create such types.
```c
enum threat_level_t{
    LOW,    //0
    MEDIUM, //1
    HIGH    //2
};
```
The values inside the comments are integer representations of these levels, meaning we can compare one threat level with another in the program
As a convention, the values/levels taken by an `enum` are written in capital letters. This data type can then be used in a switch case
```c
void printThreat(enum threat_level_t threat){
    switch(threat){
        case LOW:
            printf('Low');
            break;
        case MEDIUM:
            printf('Medium');
            break;
        case HIGH:
            printf('High');
            break;
        default:
            printf('Nothing');
            break;
    }
}

bool threatCompare(enum threat_level_t threat){
    if(threat >= MEDIUM){
        return true;
    }else{
        return false;
    }
}

enum threat_level_t myThreat = LOW;
printThreat(myThreat);
```
***

### Includes
The following common syntax for the include directive
```c
#include <stdio.h>
#include <stdlib.h>
```
is the instruction to tell the compiler what additional code is required for running our C program. The headers that are predefined in C are usually included in `<>` angular brackets. Any custom written header like `myHeader.h` must be inlucded with quotes as convention `#include "myHeader.h"`.

Header files can also contain macro definitions. For example
```c
#define EXIT_SUCCESS 0;
```
will `define` a variable `EXIT_SUCCESS` with value `0` that can be referenced to anywhere in the program, provided we have included the corresponding header file (`stdlib.h` in this case). `define` is also a directive. Defining the constant is the simplest use case of a macro.

We can also define one line macros in the header files
```c
#define SQUARE(x) x * x
```
This defines a function `SQUARE` with argument `x`. Notice that we have not defined any data type. The function is evaluated in a textual format, meaning that the compiler writes the expression as a text and then evaluates it.
`SQUARE(3)` becomes `3 * 3` which is evaluated using strings. Using double will also work. However, `SQUARE(4 - 3)` becomes `4 - 3 * 4 - 3` which is not what we inteded. We can redefine the macro as
```c
#define SQUARE(x) ((x) * (x))
```
to get the correct result.
***

### Function Prototype
This is similar to a function definition, but with a `:` instead of the body. It defines return and argument types of the function. With the prototype, compiler can check if the correct number and types of arguments have been passed to the function, and whether the returned value is correctly used. This does not need the actual definition of the function to be available. `stdio.h` contains the prototype for `printf`.
***

### `make`
`make` is a useful utility to compile large projects. It is especially useful when there are changes only to a few programs and we need not compile those files that do not depend on this particular file. A `makefile` contains a description of the targets we need to produce and it's dependencies, along with the specific commands that are required to generate the target from the sources.

**Every command specifying how to build target from source must begin with a `tab` character. Spaces will not work. This is the main source of errors many a times.**

An example make file
```shell
final: file1.o file2.o
    gcc -o final file1.o file2.o
file1.o: file1.c oneHeader.h header1.h
    gcc -Wall -c file1.c
file2.o: file2.c header2.h header1.h
    gcc -Wall -c file2.c
```
where we first define a target followed by a colon, and then a space separated list of dependencies. `make` tries to build the first target it encounters in the file by default. In the above example, it tries to build `final` first. Under the hood, the timestamps are checked to ensure that the dependencies have been modified before the target file. If this check fails at any point, `make` will rebuild the corresponding dependencies and target with respect to the changed file. It is akin to first preparing an entire dependency tree and checking which nodes are modified after all parents, and rebuilding all the nodes along the path from root to the changed node.

#### Variables
It is possible to use variables to specify certain common build flags being used in multiple places. This makes the code less verbose and easier to modify.
```shell
CFLAGS=-Wall -Werror
final: file1.o file2.o
    gcc -o final file1.o file2.o
file1.o: file1.c header1.h header2.h
    gcc $(CFLAGS) -c file1.c
```
note that changing the `makefile` itself will not lead to recompiling of targets using the new flags. This is because the underlying programs themselves might not have been changed. One hack to force rebuild is to make the targets dependent on the makefile as well.

#### Clean
`clean` is useful to remove any built targets/backup files created by the compiler. This is useful when we want to rebuild everything after making changes to the makefile (and no changes to the source file).
```shell
.PHONY: clean
clean:
    rm -f final *.o *.c~ *.h~
```
The keyword `PHONY` helps `make` recognize that it does not need to create a new file when building.
***

### gcc
There are several available options to compile the `C` code
| Flag | Description |
| ---- | ----------- |
| `-o` | Specifies the output file, `gcc -o outputFile inputFile.c` |
| `-std` | Specifies which C standard to use when compiling the code. Common option is to use C99 standard as `-std=gnu99` |
| `-Wall` | Forces the compiler to issue warnings for questionable behaviour which might go unnoticed when compiling normally |
| `-Werror` | Forces the compiler to treat warnings as errors. This flag will force the user to remove all warnings before the program can be successfully compiled |
| `-fsanitize=address` | Forces the compiler to check for any potential memory errors, useful especially when working with pointers. |
***

### `assert`
`assert(condition)` is the statement used to check if the given condition holds in the program or not. If the condition holds, the program continues execution as it is. Otherwise, the program will terminate immediately.
Asserts have minimal impact on performance, and are hence advised to keep in the prgram. In cases when performance is really critical, we can pass the flag `-DNDEBUG` to the compiler while building the program to instruct the compiler to ignore all the asserts.
***

### `valgrind`
A debugger to help find a variety of errors. Syntax to use valgrind is
`valgrind name_of_executable`. To ask valgrind to remember where uninitialized variables come from, we can use the syntax `valgrind --track-origins=yes name_of_executable`. This is even useful when using uninitialized heap memory.

valgrind has a memcheck tool that can be used for checking memory leakges and malloc related errors. To use valgrind, simply run `valgrind executable arguments`. It will print lines starting with `==PID==` containing any print statements in the code, as well as information related to the heap memory allocations. If the programs prints `valgrinded cleanly` in the end, the memory handling has been done correctly. Otherwise the errors must be fixed in a step by step manner as the later errors can simply be the result of earlier ones.

`-fsanitize=address` can be used for checking invalid read and writes from locations where the memory is probably uninitialized, array is out of bounds or the pointer is invalid. All possible memory errors cannot be found this way, but a lot of subtle ones which might usually slip through can be found and debugged.

Running valgrind with gdb (discussed below) is also possible using the flags `--vgdb=full --vgdb-error=0`. valgrind will give us the relvant commands to recreate the encountered error in gdb (since these are two separate processes). `monitor leak_check full reachable any` allows monitoring memory leaks when running the two together, and `monitor who_points_at` allows monitoring memory addresses pointed by all the pointers when running both together.

If we find memory leaks in the summary of valgrind, the full trace can be found by running valgrind with the flags ` --leak-check=full`.


***

### `gdb`
The GNU DeBugger helps gather information about what is going inside the code to fix bugs. To run gdb, we first need to instruct the compiler to include debugging information in the compiled code. This can be done with `-g` flag when compiling. To get more breadth of information, use the `-ggdb3` flag. This flag must be used for compiling all dependencies when the source depends on multiple files.
when `gdb` is started, it will instantiate its own command terminal which can accept several commands
| Command | Description |
| ------- | ----------- |
| `q` | Quit the debugger. |
| `start` | Begin (or restart) the program's execution. |
| `run` | Run the program (or possibly restart it). The execution will not stop until a stop condition is encountered. |
| `step` or `s` | Step through one line of the code. In case of conditionals, the appropriate condition based on the current state of the program is picked. Similar to working through the code by hand, one line at a time. |
| `next` or `n` | Advance the program by one line of code. Unlike `step`, in case the program encounters a function, the entire function is executed at once. |
| `print` or `p` | Allows printing the value of a variable, or a statement. We can pass the same in the arguments to `print`. Note that `print(x=3)` will change the value of `x` in the internal state of the program. Accessing elements of arrays can be done by `print(a[0]@5)` to print 5th element. `print` will remember the variables in its argument via variables `$1` etc. This is printed when executing the `print` statement. |
| `display` | prints any expression/variable passed to the argument everytime gdb stops and displays a prompt. |
| `enter` or `return key` | Repeats the last executed statement. |
| `backtrace` | Allows movement through different stack frames currently present in the program state. The navigation can be done with `up` and `down` keys. This is useful when we are in a particular function, but need the variable values in another function. |
| `break arg` | The arg can be a line number or a function name. This command will instruct `gdb` to continue running the program until this `arg` is encountered. This is very useful when we want to skip to a particular part of the program. We specify this line/function in `break` and `run`. |
| | We can also have conditional breakpoint using `break 7 if i == 10`, which would be otherwise difficult by the simple arguments. |
| `until` | Will execute a loop until completion and stop at the first line after the loop. This statement needs to be executed at the start of loop to take effect. |
| `finish` or `fin` | Executes until the current function is complete/returns. |
| `watch some_var` | Prepares a watcher such the gdb stops whenever it observes that the value of `some_var` has changed. In case this variable is defined in a local scope, we use `print some_var` to get the assignment of this variable in gdb scope. Then simply doing `watch $a_num` where gdb has stored reference to `some_var` in `$a_num`. This is handy when working with pointers. |

***

### Pointers
Pointers are used to store the location of a variable (it's address in the computer memory). Hence, instead of storing a value like `5` or `'c'`, they will store the address `1213`. On a 32-bit machine, each address is 32-bit or 4-bytes long. Since pointers store such addresses, a pointer is also 4-byte long (irrespective of whether it points to an int or char).

In C, pointer is not a separate type but a *type constructor*. This means that when used with an existing data type, a new data type is obtained. Pointers are declared by placing an asterik after a data type
```c
int *my_int_ptr;
char *my_char_ptr
```
The above two statements declare different types of pointers. The first is an `int` pointer while the second is a `char` pointer. Both will have different sizes and memory allocations.

The following declarations are same
```c
int* ptr;
int * ptr;
int *ptr;
```

Changing the value of a pointer is same as changing the location to where the pointer is pointing to. If done incorrectly, we could point to memroy locations not part of the current program, or even illegal locations (locked by OS). Note that it is not possible to change the location of a variable present in the program.

We usually use pointers to point to the memory address of a variable. To access the memory address, use the ampersand operator (also called address of variable)
```c
int x = 10;
int *x_ptr;
x_ptr = &x;
```
It is important to note that pointers can only point to things that are addressable. Variables fall in this category. However, expressions like `x+y` do not refer to any address, and statements like `ptr = &(x+y)` will raise an error.

We can also access the value of the variable pointed by the pointer. This is done by placing an asterisk before the pointer (also called dereferencing a pointer)
```c
*x_ptr = 20;
printf("%d", x);
```
will print 20 and not 10. This is because assignment to `*x_ptr` is same as assignment to `x`.

#### NULL
The NULL value is a special constant. On a 32-bit machine, it is the address `0x00000000`. This special address is not used anywhere else. It is useful when we want to return something like no answer was found. `ptr = NULL` allows us to make the pointer to refer to the NULL location.

#### How a program views memory
Considering a 32-bit machine, each location (a byte long) will be addressed by 32-bits. A program divides memory into several chunks
| Name | Description |
| ---- | ----------- |
| Code | The assembly code generated by a compiler is a series of instructions (all converted to numbers) and is stored in this area by the program. Equivalently, the code itself lives in the memory as a sequence of numbers which correspond to different operations.|
| Static Data | This locations stores the data that is available throughout the lifetime of a code, global variables for instance. This area exists just adjacent to the Code.|
| Heap | Stores dynamically allocated data. Such as Arrays of unknown size initialized after the program starts execution. |
| Stack | Stores the local variables created by each function. There are different stack frames that correspond to different functions. For any given function, its stack frame is a contiguous piece of memory allocated when the function starts execution, and freed when the execution ends. Each stack frame sits below the stack frame of the function that called it.|
***

### Pointers to structs
The following code illustrates how to use pointers to structs
```c
struct coord_t{
    int *x;
    int y;
}

int main(){
    struct coord_t a;
    struct coord_t *a_ptr;
    int s = 9;
    a.x = &s; // assign the address of s to x
    a.y = 5;
    a_ptr = &a; // assign address of struct
    printf("%d\n", *a.p) // first . then *
    printf("%d\n", (*a_ptr).x); // preferable to use a_ptr->x
    return 0;
}
```

Assigning a struct to a struct pointer is same as what was done for data types like int. We just use `&` to get the address of the struct. However, to access fields using this pointer, we use `->`, `a_ptr->x` for instance. This is same as `(*a_ptr).x` which first selects the struct refered to by the pointer, and then access the field. `->` can be chained together when we have pointers in chain. `a_ptr->x->x_1` for instance first selects the pointer pointed by `a_ptr`, then its field `x` which itself is a pointer to a struct, and finally we select the field `x_1` of that pointer. This is useful in trees, when we can a struct node, and node contains a field left which is a pointer to another struct.

#### Pointers to Pointers
The chain can be as long as we want. Simply put those many asteriks. Pointer to pointers are common, while pointers to pointers to pointers are less common and the higher ups are used even more rarely.
```c
int *x;
int **y;
int a = 8;
x = &a; // x now points to a
y = &x // y now points to x which points to a
printf("%d\n", **y) // prints 8
```

Putting two asteriks does the dereferencing twice. `*y` gives the value stored in `x` which is the address of `a`. Modifying `*y` means changing the address pointed by `x` (`y` will still point to `x`). Using the second asterik, `**y` is same as `*x` and equals 8. For more deeper levels, we will use more asteriks to reach the actual value of the variable pointed to.

The `->` operator shouldnt be used here as that is specific to structs.
***

### `const`
This keyword can be used with an existing data type to create a variable whose value cannot be changed. This is useful when we want to use some constants like pi in our code and do not want to accidentally modify their values. Doing so will raise an error when compiling.
```c
const int x = 4;
```
means that `x` has value 4 which cannot be changed.

Pointers with const are little tricky and comes with various options as to what is to be kept constant, the pointed address or the value stored in the pointed address.

| Declaration | Description |
| ----------- | ----------- |
| `const int *p = &x` | We have declared a pointer to `const int`. This means changing the value of the variable pointed by p is not allowed, although we can change the variable pointed to by p. `p = &y` is valid while `*p = 5` is not. |
| `int const *p = &x` | Same as above. |
| `int * const p = &x` | A constant pointer that points to a variable of type int. Thus, changing the variable pointed to by x cannot be changed, while the value of the variable can be changed. `p = &y` is not valid while `*p = 5` is valid. |
| `const int * const p = &x` | Restricts both changing the variable pointed to and the value of the variable itself. `p = &y` and `*p = 5` both become invalid. |

The same set of rules apply to pointers to pointers
| Declaration | Can we change `**p` |  Can we change `*p` | Can we change `p` |
| `int ** p` | Yes | Yes | Yes |
| `const int ** p` | No | Yes | Yes |
| `int * const * p` | Yes | No | Yes |
| `int ** const p` | Yes | Yes | No |
| `const int * const * p` | No | No | Yes |
| `const int ** const p` | No | Yes | No |
| `int * const * const p` | Yes | No | No |
| `const int * const * const p` | No | No | No |

#### Pointer Arithmetic
Pointers support addition and subtraction operations, but in a slightly different manner than the usual arithmetic.
```c
int x = 4;
int *p = &x;
p = p + 1;
```
This snippet will make the compiler jump 4 bytes. Why, because the pointer is of integer type, and the next valid integer location in memory will be after we have traversed the memory the size of an integer. Since an integer occupies 4 bytes, the next integer in memory will lie after 4 bytes. Were we working with a struct of size 32 bytes, then increasing the pointer by 1 would jump to the address after 32 bytes, since that is the next valid location another struct might possibly be.

In general, if `N = sizeof(T)` where N is the size of data type T in bytes, `p = p + n` moves p by `N * n` bytes of memory in total. Usage of pointer arithmetic makes sense in arrays and not general variables.


#### Pointers to Functions
The name of a function is also a pointer to the function. This definition is useful when we have a complex code most of which is similar across different function and only varies slightly. We can make smaller functions out of these different parts.
```c
int square(int x){
    return x * 2;
}

void ChangeEachElement(int * arr, size_t n, int (*f)(int)){
    for(int i = 0; i < n; ++i){
        arr[i] = f(arr[i]);
    }
}

int arr[] = {1, 2, 3};
ChangeEachElement(arr, 3, square);
```
`return type (*function name)(argument type)` is defines a pointer to a function. This is similar to a normal function defintion, except we put an asterik before the function name and do not specify the name of parameters. The last line of the code above works ince function name is the pointer to a function.

We can also use a typedef
```c
typedef int (*func)(int);
void ChangeEachElement(int * arr, size_t n, func f){
    for(int i = 0; i < n; ++i){
        arr[i] = f(arr[i]);
    }
}
```

The inbuilt qsort function uses this concept to sort an array of any type of elements
```c
void qsort(void *base, size_t nmemb, size_t size,
                int (*compar)(const void *, const void *));
```
where `compar` is the function we must define to compare any two elements of the array, and `const void*` will point to an element of the array (const because the comparing function must not modify the elements, void because we do not know the type of element beforehand). `compar` must return 1 if first element is greater, 0 if they are same, and -1 if first is less than second.
```c
int compareInts(const void * n1vp, const void * n2vp) {
  const int * n1ptr = n1vp; // convert back to int* so we can dereference
  const int * n2ptr = n2vp;
  return *n1ptr - *n2ptr;   // subtracting the two numbers compares them
}

void sortIntArray(int * array, size_t nelements) {
  qsort(array, nelements, sizeof(int), compareInts);
}
```
It is important to convert to a constant pointer as shown above, otherwise the code might show unexpected behaviour.

***

### Arrays
Arrays allow us to store multiple data of the same type in a sequential format. Arrays can be initialized as
```c
int myArray[5];
int myArray2[5] = {1,2,3,4,5};
int myArray2[] = {1,2,3,4,5};
```
where the last two methods allows us to initialize the array with values. When we declare an array, the program allocates the designated memory size based on the data type. Thus, the array declared above would require 20 bytes of space. The name `myArray` is a pointer to the first element of the array. Pointer arithmetic will work, however an easier way to access elements of the array is using `myArray[1]` and so on (in C, **array indexing begins from 0**). If we access the elements outside the size, an error might occur. Also, the location pointed by `myArray` is fixed and hence, we cannot modify this variable.

For initialization, we must not give more elements than the array size. Doing so results in an error. However, we can speciy fewer elements than the array size and the remaining are automatically filled with 0. To initialize with all zeros, `int myArray[5] = {0};` works perfectly fine.

Starting with C99, arrays with size defined during the program's execution can be declared. Also, note that we can have an array of any type, even a struct `struct myStruct_t myStruct[5]`.

#### Passing Arrays to Function
In C, the preffered way to pass an array to a function is to pass both the array pointer and the size. There is no way to get the array size in C.
```c
int myFunction(int *myArray, int size){..}
```
The variable size can be used to check the bounds of array when iterating over it. Another correct way to do the same is
```c
int myFunction(int myArray[], int size){..}
```
which makes it explicit that myArray is indeed an array and not a pointer. or the compiler, it's still the pointer to the first element of a sequence of integers.

#### Dangling Pointers
Functions cannot return arrays. If we create an array in our funtion, and in the end return the pointer to this array, the code will look fine. But, as soon as the function ended, the corresponding stack was deleted from memory. This means, the array we created inside the function no longer exists. Thus, the pointer returned points to an unknown value and such pointers are called Dangling Pointers.

It might be difficult to find these problems in our code because such pointers have unpredictable behaviour and in the eyes of compiler, all of this may look correct. To correctly return arrays, we must create an array inside the function that calls this array returning function `f`, pass it to `f` and ask it to modify the array in place. If necessary, a temporary copy can be created inside `f`. This will ensure correctness and consistency in our code.

#### Multidimensional Arrays
We just use multiple square brackes while declaring higher dimensional arrays.
`int myArray[4][3];` declares an array of size 4 x 3, with a total size of `4 * 3 * sizeof(int)`. Conceptually, there are 4 elements in this array, and each element is an array of size 3. In memory, this array is laid down in a linear fashion, i.e., first three elements of first row will be sequentially laid down, then 3 elements of the next array and so on. A total of 12 memory blocks will be sequentially laid down.

To access any element of the array, we simply call `myArray[2][3]` (with 0 based indexing on both the axes) because `myArray[2]` returns a pointer (using pointer arithmetic) to the thrid array of `myArray` and `myArray[2][3]` will return the third element of that array. Higher order arrays can be created as `int myArray[4][3][3]`.

Initialization is similar to a 1D array
```c
myArray[][] = { {1, 0, 0},
                {0, 1, 0},
                {0, 0, 1}};
```

#### Array of Pointers
This is a very useful concept when we may wish to create an array whose elements are of different sizes
```c
int row1[2], row2[3], row3[6], row4[2];
int *myArray[4] = {row1, row2, row3, row4};
```
This can be a more memory efficient storage method when we already know the sizes of each individual array.

#### Array of Strings
These are multidimensional arrays of characters. We need to ensure that enough space is provided to store the longest string too. Also, the second dimension of the array must incorporate the null terminating character. Otherwise, we will not know how long each individual string is and it may cause unexpected behaviour.

***

### Tips for testing
Consider all major categories of inputs, and be sure you cover them.
  * For numerical inputs, these would generally be negative, zero, and positive. One is also usually a good number to be sure you cover
  * For sequences of data, your tests should cover an empty sequence, a single element sequence, and a sequence with many elements.
  * For characters: lowercase letters, uppercase letters, digits, punctuation, spaces, non-printable characters
  * For many algorithms, there are problem-specific categories that you should consider. For example, if you are testing a function related to prime numbers (e.g., isPrime), then you should consider prime and composite (not prime) numbers as input categories to cover.
  * When you combine two ways to categorize data, cover all the combinations. For example, if you have a sequence of numbers, you should test with an empty list, a one element sequence with 0, a one element sequence with a negative number, a one element sequence with a positive number, and have each of negative, zero, and positive numbers appearing in your many-element sequences.
  * An important corollary of the previous rules is that if your algorithm gives a set of answers where you can list all possible ones (true/false, values from an enum, a string from a particular set, etc), then your test cases should ensure that you get every answer at least once. Furthermore, if there are other conditions that you think are important, you should be sure that you get all possible answers for each of these conditions. For example, if you are getting a yes/no answer, for a numeric input, you should test with a negative number that gives yes, a negative number that gives no, a positive number that gives yes, a positive number that gives no, and zero [zero being only one input, will have one answer].
  * All of this advice is a great starting point, but the most important thing for testing is to think carefully: imagine all the things that could go wrong, think carefully about how to test them, and make sure your test cases are actually testing what you think they are testing.
  * Some definitions
    * Statement coverage means that every statement in the function is executed
    * Decision coverage—in which all possible outcomes of decisions are exercised. For boolean tests, this means we construct a test case where the expression evaluates to true, and another where it evaluates to false. If we have a switch/case statement, we must construct at least one test case per choice in the case statement, plus one for the default case, even if it is implicit, i.e., if we do not write it down, and it behaves as if we wrote default: break;.
    * Decision coverage corresponds to having a suite of test cases which covers every edge in the graph of decisions.
***

### Strings
#### String Literals
String literals are a sequence of characters written within double quotes. They can be declared as
```c
const char *str = "Hello World\n";
```
In the memory, we have a pointer `str` to a sequence of characters, and the last character will be `\0`which is called _null terminator character_ (its only in the memory added by the compiler to know at which location the string ends, it is not visible to us).

The const keyword means that we cannot modify the value of the string. In memory, it is usually stored with static data in the read only portion. Segmentation fault can be raised if the keyword const is not used and we modify the string unknowingly.

#### Mutable Strings
Mutable strings are a collection of characters (including the null terminator). The can be declared in multiple ways
```c
char *str[] = "Hello\n";
char *str2[] = {'H', 'e', 'l', 'l', 'o', '\n', '\0'};
char *str2[100] = "Hello\n";
```
The size of the array will include the null terminator as well. Thus, `str` is of size 5 (Hello) + 1 (\n) + 1 (\0). If that is not done, undefined behaviour can occur.
The last statement is totally valid since we have declared an array of size 100 with only first few characters fille in. This is useful when we want to extend the string size in the future. In all cases, explicitly remembering size is advised since C cannot calculate the array size automatically.

#### `strcmp`, `strcasecmp`
This function is present in the `string.h` library in C. A 0 is returned if the strings are equal and a non zero number is returned otherwise (positive if first string comes first in lexographical order and vice versa). Note that simply comparing `str1 == str2` will not work as this will just compare whether both pointers point to the same location which is rarely the case.
A case-insensitive version also exists called `strcasecmp`.

#### `strcpy`, `strncpy`, `strdup`
As the name suggests, these functions are used to copy the contents of one string to another. Simply doing `str1 = str2` will just make both pointers point at the same location and not create a separate copy of the string.
```c
char *strcpy(char *dest, const char *src)
char *strncpy(char *dest, const char *src, size_t n)
```
For the second function `strncpy`, `n` is the number of characters to copy. If `n` is more than the `src` size, `dest` will be padded with null bytes. If `n` is more than `src` size, `dest` will not be null terminated.

#### `isalpha`
`int isalpha(int arg)` is signature of this function, which checks whether the given character is an alphabet or not.

#### `atoi`, `strtoI`
```c
const char * str = "12345";
int x = str;
```
will not work as `str` is a pointer and not an ASCII characters. The program does not know how to convert a pointer to integer.
C has the inbuilt function `atoi` which allows converting from string to integer provided the first character is a number. `strtoI` is a more advanced version which handles multiple types of bases, and also ignores any trailing non number characters.

#### `strchr`
Returns a pointer to the first occurence of a character in the string
```c
char *strchr(const char *str, int c)
```
NULL is returned if the character is not found.

***

### System Calls
System calls allow the program to interact with the operating system which in turn interacts with the hardware to execute the relevant code. OS as an important intermediary since it takes care of things like permission and accesses.
#### errno
A system call can fail for a variety of reasons and whenever this happens, and `errno` is returned which is a **global** variable corresponding to the error. Calling the `perror` function (this function has a single argument which is the string to be printed before the error) maps this error number to a human readable string. One must be careful not to call anything before `perror` which can potentially modify the `errno` variable (since it is a global variable).

***

### Command Line Arguments
To provide command line arguments to the program, the syntax of main is modified as below
```c
int main(int argc, char ** argv) {
  // code for main goes here
}
```
where the first argument `argc` is the **arg**ument **c**ount and the second argument is an array of strings **arg**ument **v**ector. The 0th element of `argv` is the name of the program as it was invoked on the command line. Relevant arguments for the program will start from the 1st index till `argc-1`. Typically the arguments are separated by whitespaces.
Remember that since the arguments are strings, the program must convert any argument that it expects as a number before beginning any processing.

For working with option based command line arguments (example can be `gcc -o out.name in.name`) `getopt` which is a part of the C library is used. It can be looked up using `man -S3 getopt`.

There is also the third optional argument to main using which main has access to environment variables. Other functions like `getenv`, `setenv`, `putenv`, and `unsetenv` are also available for similar tasks.

### File IO
#### Opening and Reading Files
Opening a file (for any operation, read or write) creates an associated stream `FILE *` which is a sequence of data (characters). File can be opened using the `fopen` function which has the signature
```c
FILE * fopen(const char * filename, const char * mode);
```
`mode` will specify whether to open the file for read and/or write, create the file if it does not exist etc. This is a string literal, `"r"` for instance. Whenever `fopen` fails, it returns the NULL stream and the corresponding d=errorno as well. It is important to check whether the stream is NULL or not before using it.

| Mode | Read and/or write | Does not exist ? | Existing contents discarded ? | Position |
| ---- | ----------------- | --------------- | --------- | -------- |
| r | read only | fails | no | beginning |
| r+ | read/write | fails | no | beginning |
| w | write only | created | yes | beginning |
| w+ | read/write | created | yes | beginning |
| a | writing | created | no | end |
| a+ | read/write | created | no | end |

After the file has been opened for read, we can use `fgetc`, `fgets`, or `fread` to get the file stream.

##### `fgetc`
`fgetc` will read the input one character at a time (this function returns an int and not a char), and it takes the file stream as the argument. To get the end of file, a special constant `EOF` is defined in `stdio.h`. Every call to `fgetc` will advance the file stream pointer by one character.

```c
//fixed
FILE * f = fopen(inputfilename, "r");
if (f == NULL) { /* error handling code omitted */ }
int c;
while ( (c=fgetc(f)) != EOF ) {
  printf("%c",c);
}
//...other code...
```
where we first do the assignment to a variable, and then check if it is indeed a valid char. The brackets ensure the correct order of operations. The value is stored in an int and not a char as EOF is -1 on most systems and using a char would automatically discard value 255, ending the loop prematurely.

##### `fgets`
`fgets` is useful when we wish to read the file one line at a time with a certain maximum length of characters per line. Its signature is
```c
char * fgets(char * str, int size, FILE * stream);
```
The first argument is the pointer to the array wherein to store the line that is read. Second argument decides how many characters to read per line. Final argument is the file stream from which to read. The data stored in the string is null terminated. In case of an error (due to end of file before reading any character or some other error), NULL string is returned. `feof` and `ferror` can be used to determine whether error occurred due to end of file or something else. Avoid using `gets` as it reads till the end of line, ignoring the limit on the array. This means that the function can continue to write beyond the array as well exposing security vulnerabilities.

##### `fread`
`fread` is used for reading binary data like images and audio files. In such cases, the actual integer is not written in the file, rather the byte representation. The correct way to read such a file is specified in the format specification section of the file. Its signature is as follows
```c
size_t fread (void * ptr, size_t size, size_t nitems, FILE * stream);
```
#### Writing to Files
Similar to reading files, several functions are available to write output to a file
##### `fprintf`
Very similar to the printf function, this also prints formatted text, but takes an additional argument specifying the file stream to write the output to. Its signature is
```c
fprintf(FILE * stream, "string to write", list of arguments for format specifiers);
```

##### `fputc`, `fputs`
write a single character and a string to the output stream respectively. Note that `fputs` will write the string as it is, `fputs("%d")` will write `%d` to the output stream.

##### `fwrite`
exists similar to `fread` and has the signature
```c
size_t fwrite(const void * ptr, size_t size, size_t nitems, FILE * stream);
```
where the data is read from the location pointed to by ptr and written to the stream pointed to by stream.
In all these functions, errors may not be returned immediately as the OS will buffer some data before beginning the write process since making system calls and writing to the disk are both slow processes with fixed overheads, and the performance is improved by writing larger chunks.

#### Closing Files
##### `fclosef`
It has the signature
```c
int fclose(FILE * stream);
```
where the stream to be closed is specified. Any calls to functions like fgetc after this point is erroneous. The returned integer is 0 if the operation was success, and EOF along with setting the errorno in case of failure. What needs to be done in response as corrective measure is highly situation dependent. For instance, if the disk is full, the user needs to intervene and clear out space before redoing all the tasks of reading, writing and closing the file, which may now work correctly. In any case, printing out the error is a good practice.

#### Everything is a File
C library provides methods that are similar in nature in the sense that they allow the programs to interact with different systems as a file stream. `stdout` is also a file stream whose output is directed to the terminal. Similar standard exists using `socket` to interact with a network and sending/reading data.

***

### Dynamic Memory Allocation
Suppose we want to pass around data from a function in complex structs. This is not possible since the struct initialized in the function stack will vanish as soon as the function returns. Dynamic memory allocation allows us to allocate memory in the heap which is present even after the function returns and must be freed by us in the code if not in use anymore. `malloc` allows dynamic memory allocation, `free` allows to free the allocated space, and `realloc` allows reallocating the allocated memory, in case more is needed.

#### `malloc`
Its signature is
```c
void * malloc(size_t size);
```
where size is the requested size of memory in bytes. `void *` simply means that it points to a memory location. this way, same malloc function will work for different data types. We can assign the result of malloc to a pointer of a specific data type for intended use in the program.
In case there is an error allocating the memory, the pointer returned by malloc will be NULL. After checking for this, appropriate error handling can be performed.
malloc can be used with any complex structure as `malloc(sizeof(a_struct_t) * n)` to create a pointer to an array of structs, or simply one struct. The struct itself can have complex definitions inside. However, it is important to note that until we explicitly assign something to this memory location, calling the members of struct will result in segmentation fault. In other words, the memory allocated must be initialized before using/accessing it.

#### Deep and Shallow copy
Suppose we have a stuct `rect` which itself contains pointers to an integer `x`. The statements
```c
rect r1; r1->x = 42;
rect * r2 = &r1;
rect * r3 = r2;
```
clearly make r2 and r3 pointing to the same locations for both the struct and x. With malloc, we can create a specific memory block for r3
```c
rect * r3 = malloc(sizeof(r3));
*r3 = *r2;
```
Now, r2 and r3 point to different memory locations. However, they point to the same location of x. This is a shallow copy. To create a deep copy, malloc needs to be called for assigning x as well.
```c
r3->x = malloc(sizeof(r1->x));
```
Now r2 and r3 are two distinct copies, pointing to different memory locations.

#### `free`
Once the allocated memory on the heap is no longer in use, we must use free to remove the allocated memory. This is necessary as the program could keep allocating new and new memory without releasing it, making the available memory for OS less and less which slows down larger programs that run for long durations of time. Its signature is
```c
void free(void * ptr);
```
where **ptr must point to the beginning of the allocated memory**. If ptr points elsewhere, the behaviour can be undefined and likely crash the program. Calling free twice on an allocated block of memory can cause segmentation fault, or crash the program. It is even possible that the program crashes on the next call to malloc/free in the code making debugging difficult. Using valgrind can help expose these subtle mistakes in the code. Freeing memory not on the heap (but say in the function stack) can also crash the program.
Every block of memory allocated with malloc must be freed by a corresponding call to free. In case of deep copy or when blocks inside allocated memory point to other locations in the heap, the latter should be freed first before freeing the base/first allocated block. In the previous example of rect struct,
```c
free(r3->x); free(r3);
```
is the correct execution order. The reverse order will result in dangling pointers.

#### `realloc`
This function is useful to reallocate memory, in case the size requirements have changed. Its signature is
```c
void * realloc(void * ptr, size_t new_size)
```
where ptr points to the location where the memory was originally allocated, and new_size is the new size of the allocated memory requested by us (could be more or less). It is entirely possible that the new memory is located elsewhere and realloc will conveniently copy the relevant original memory to the new location. It will also free the original location from the heap since it will no longer be required. In case the desired size of memory is not available, NULL is returned by realloc.

#### `calloc`
It is similar to malloc, except that it zeroes out the newly allocated memory. malloc leaves the allocated memory uninitialized.

#### `getline`
Is useful for reading lines of variable size from a file. Its signature is
```c
ssize_t getline(char ** linep, size_t * linecapp, FILE * stream);
```
where linep points to the malloced location (NULL if getline needs to perform the malloc), linecapp is a pointer to the size of the malloced buffer, and stream is the pointer to the file to be read. This function returns the number of characters written (counting the newline character, but not counting the null terminator of a string) and -1 in case of an error (including the end of file). Note that `\0` is placed at the end of buffer in the memory and `\n` is also included in the buffer.

When using in a loop, following pattern is recommended
```c
char * line = NULL; size_t s;
while(getline(&line, &s, stream) >= 0){
    // process line
    free(line); line = NULL;
}
free(line);
```

The key difference from fgets is that getline uses malloc and realloc internally to resize the buffer as needed. In case the buffer is updated, the pointer linep  and size linecapp will be updated to their new locations and the user need not worry about memory.

It is a good idea to free the last allocated memory by getline in case an error was returned since the memory allocation happens first.

***
