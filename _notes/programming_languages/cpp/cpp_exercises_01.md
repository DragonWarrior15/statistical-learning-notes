---
title: "C++ Exercises 01"
---

# C++ Exercises
## Course 01: Classes in C++
***

### Quiz 01
1. One of these statements below is true and the other three are false. Which one is true?
    1. Every variable in C++ holds either an integer, a character, a Boolean or a floating point value (of some precision).
    1. A Boolean variable can only be assigned a value from this set of three reserved words: {true, false, undefined}.
    1. Every function in C++ must return a value.
    1. Every variable in C++ has to be associated with a specific type

2. According to the C++ standard, what is the name of the function is the starting point for a program?
    1. begin()
    1. start()
    1. main()
    1. init()

3. One of these statements below is true and the other three are false. Which one is true?
    1. A class can consist of multiple member data variables, but the type of each data variable does not need to be specified until the class is used to declare a variable.
    1. A class can consist of multiple member data variables of different types, but each member variable must be one of the built-in types.
    1. A class can consist of multiple member data variables, but all must be of the same type.
    1. A class can consist of multiple member data variables of different types, but each type must be specified when the class is defined.

4. One of these statements below is true and the other three are false. Which one is true?
    1. Any functions that operate on a class’s member data variables must be implemented independent of the class in a separate .cpp file.
    1. The member functions of a class always have access to every member data variable of that class.
    1. The member functions of a class can only operate on member data variables of that class.
    1. The member data variables in a class can only be accessed by the member functions of that class.

5. Which C++ directive is used to insert the contents of another file at the current location while processing the current file?
    1. `#library`
    1. `#using`
    1. `#import`
    1. `#include`

6. Given only the following code:
    ```c++
    namespace uiuc {
        class Pair {
            double a,b;
        };
    }
    ```
    which of the following syntax can be written outside of the namespace declaration to properly create a variable named “p” of type Pair?
        1. (uiuc) Pair p;
        1. uiuc/Pair p;
        1. Pair p;
        1. uiuc::Pair p;

7. Which keyword is used to indicate which namespace(s) to search to find classes and variables when they are referenced throughout the rest of the program?
    1. namespace
    1. std
    1. using
    1. uiuc

8. Why do we use namespaces in C++ programming?
    1. Because all variable and class names must be defined using a namespace.
    1. Because it allows a library to claim a variable or class name that cannot be used by any other library.
    1. Because all references to variable and class names must be made through namespace.
    1. Because two different libraries might use the same label for a class or variable

9. What is the namespace of the C++ Standard Library?
    1. std
    1. csl
    1. stdio
    1. cstl

10. Which operator is used to send a sequence of strings, numbers and other values to the standard library's cout object in a specific order so that they will be printed to the console?
    1. `&`
    1. `=`
    1. `+`
    1. `<<`

***

#### Answers 01

| Question | Answer |
| -------- | ------ |
| 1 | iv |
| 2 | iii |
| 3 | iv |
| 4 | ii |
| 5 | iv |
| 6 | iv |
| 7 | iii |
| 8 | iv |
| 9 | i |
| 10 | iv |

***

### Quiz 02
1. Recall that every variable in C++ has these four things: a name, a type, a value and a memory location.
    ```c++
    int *p;
    p = new int;
    *p = 0;
    ```
    For the code above, which one of the following is NOT true for variable p?
    1. The name of the variable is `p`
    1. The type of the variable is a pointer to an integer, specifically the type `int *`
    1. The value of the variable is 0
    1. The memory address of the variable is the value returned by the expression `&p`

2. Which one of the following is true?
    1. The "new" operator allocates memory on the stack that gets removed from the stack by the "delete"operator.
    1. The address of any memory location in the stack is larger than the address of any memory location in the heap.
    1. You should avoid using the memory address 0x0 for pointers whose value is not yet set, because memory location 0x0 is a valid location for the system to allocate to hold the contents of a variable.
    1. The C++ statement “int i;” allocates memory for one integer on the heap.

3. Suppose we are writing the following function that is intended to return a pointer to a location in memory holding an integer value initialized to zero.
    ```c++
    int *allocate_an_integer() {
    // declare variable i here
    *i = 0;
    return i;
    }
    ```
    How should variable i be declared?
    1. `int *i = new int;`
    1. `int *i;`
    1. `int i;`
    1. `int j; int *i = &j;`

4. Suppose we have this alternative function that returns a pointer to a memory location to an integer value of zero.
    ```c++
    int *allocate_an_integer() {
        int i = 0;
        return &i;
    }
    int main() {
        int *j;
        j = allocate_an_integer();
        int k = *j;
        return 0;
    }
    ```
    What value is variable k assigned and why?
    1. Variable k is not assigned a value, because even if the compiler is set to ignore warnings and continue with compilation, the compiled program will still automatically detect that a local variable’s address is being used after the function has returned, and exit to the operating system with a non-zero error code.
    1. Assuming that the program compiles with just a warning and not an error due to the settings, the variable k will not be assigned a value, because the running program will crash the whole operating system.
    1. Variable k is certainly assigned the value zero, because the C++ runtime will automatically move the local variable to the heap and return the address of that heap variable instead.
    1. Unknown. Depending on the compiler settings, the compiler may report that a local variable address is being returned, which could be treated as a warning or as a compilation error; Or, if the program is allowed to compile, then at runtime the variable k could be assigned zero, or some other value, or the program may terminate due to a memory fault.

5. Suppose we declare a variable as `int i;` Which of the following expressions returns the address of the memory location containing the contents of variable i?
    1. `*i`
    1. `i.addr`
    1. `&i`
    1. `i->addr`

6.
    ```c++
    int i = 0;
    int *j = &i;
    ```
    How many memory allocations are made on the stack and on the heap for the above code? For example, declaring an integer would count as one memory allocation.
    1. One allocation on the stack and one allocation on the heap.
    1. Two allocations on the stack and zero allocations on the heap.
    1. Zero allocations on the stack and one allocation on the heap.
    1. Zero allocations on the stack and two allocations on the heap.
    1. One allocation on the stack and zero allocations on the heap.

7.
    ```c++
    int *i = new int;
    ```
    How many memory allocations are made on the stack and on the heap for the above code? For example, allocating space for one integer would count as one memory allocation.
    1. One allocation on the stack and zero allocations on the heap.
    1. Zero allocations on the stack and one allocation on the heap.
    1. Two allocations on the stack and zero allocations on the heap.
    1. Zero allocations on the stack and two allocations on the heap.
    1. One allocation on the stack and one allocation on the heap.

8.
    ```c++
    int *i = new int;
    *i = 0;
    int &j = *i;
    j++;
    ```
    What does the last line of the above code segment do?
    1. Increments the value of j by one, where the value of j is a local copy stored on the stack of the value of i stored on the heap.
    1. Increments the value pointed to by variable i by one.
    1. Causes an error.
    1. Increments the address pointed to by variable i by one.

9. ```c++
    int i = 0, j = 1;
    int *ptr = &i;
    i = 2;
    *ptr = 3;
    ptr = &j;
    j = i;
    *ptr = 4;
    ```
    Enter the number of different values stored in the same address that variable i has during the execution of the code above. (Your answer should be a single integer, which is the total number of different values assigned to that address.)

10. ```c++
    class Pair {
        public: double a,b;
    };
    int main() {
        Pair *p = new Pair;
        p->a = 0.0;
        return 0;
    }
    ```
    The expression p->a is equivalent to which one of the following?
    1. `*(p.a)`
    1. `(*p).a`
    1. `p.*a`
    1. `p.a`

***

#### Answers 02

| Question | Answer |
| -------- | ------ |
| 1 | iii |
| 2 | ii |
| 3 | i |
| 4 | iv |
| 5 | iii |
| 6 | ii |
| 7 | v |
| 8 | ii |
| 9 | 3 |
| 10 | ii |

***

### Quiz 03

1. Which one of these is the only true statement about a class constructor.
    1. A class can only have one constructor.
    1. When declaring a constructor for a class, the name of the constructor must be the name of the class.
    1. When declaring a constructor for a class, the return type of the constructor must be the type of the class.
    1. A class must have at least one constructor declared for it.

2. Which of the following examples does NOT call a copy constructor at least once?
    (If you already have advanced knowledge of C++ that makes this seem like a trick question, then we'll also specify this: Assume that compiler optimizations are mostly disabled.)
    1. ```c++
        Cube a, b(10);
        a = b;
        ```
    2. ```c++
        // Function prototype for "contains":
        int contains(Cube outer, Cube inner);
        // ...
        Cube a(10),b(5);
        int a_bounds_b = contains(a,b);
        ```
    3. ```c++
        Cube b(10);
        Cube a = b;
        ```
    4. ```c++
        // Function prototype for "intersect":
        Cube intersect(Cube &left, Cube &right);
        // ...
        Cube a(10),b(5);
        Cube c;
        c = intersect(a,b);
        ```

3. Recall that a custom assignment operator can be declared such that line 2 of the code below executes a user-defined function to perform the assignment.
    ```c++
    Cube a,b(10);
    a = b(10);
    ```
    Which one of the following statements regarding the declaration of such a custom assignment operator allowing is **true**?
    1. The custom assignment operator function is declared with two arguments: the source and target objects of the assignment.
    1. The custom assignment operator is a function declared with the name "operator::assignment".
    1. The type of the custom assignment operator function should be void.
    1. The custom assignment operator is a public member function of the class.

4. Consider the following class:
    ```c++
    class Orange {
        public:
            Orange(double weight);
            ~Orange();
            double getWeight();

        private:
            double weight_;
    };
    ```
    Select **all** functions that are present in this class (including any automatic/implicit functions added by the compiler):
    1. Default constructor
    1. At least one custom, non-default constructor
    1. Copy constructor
    1. Assignment operator
    1. Destructor

5. Consider the following class:
    ```c++
    class Blue {
        public:
            double getValue();
            void setValue(double value);

        private:
            double value_;
    };
    ```
    Select **all** functions that are present in this class (including any automatic/implicit functions added by the compiler):
    1. Default constructor
    1. At least one custom, non-default constructor
    1. Copy constructor
    1. Assignment operator
    1. Destructor

6. Consider the following class:
    ```c++
    class Animal {
        public:
            Animal();
            Animal(std::string name);
            Animal(std::string name, int age);
            Animal(std::string name, int age, double weight);

            Animal(const Animal & other);

            void setName(std::string name);
            std::string getName();

        private:
            // ...
    };
    ```
    How many **explicit** (non-automatic) **constructors** are present in the class?
    1. 2
    1. 3
    1. 4
    1. 5
    1. 6
    1. 7

7. When you use the `new` operator to create a class object instance in heap memory, the `new` operator makes sure that memory is allocated in the heap for the object, and then it initializes the object instance by automatically calling the class constructor.
    After a class object instance has been created in heap memory with `new`, when is the destructor usually called?
    1. The destructor is called automatically when the variable goes out of scope.
    1. The destructor is called automatically when the `delete` operator is used with a pointer to the instance of the class.
    1. The programmer always needs to call the destructor manually in order to free up memory.
    1. The destructor is called automatically when the program returns from the function where the `new` operator was used to create the class object instance.

8. Consider the following program:
    ```c++
    double magic(uiuc::Cube cube) {
        cube.setLength(1);
        return cube.getVolume();
    }

    int main() {
        uiuc::Cube c(10);
        magic(c);
        return 0;
    }
    ```
    How many times is the `uiuc::Cube`'s copy constructor invoked?
    1. Never
    1. Once
    1. Twice
    1. Three times

9. We have looked at examples where the assignment operator returned the value `*this`. The variable `this` is available by default in most class member functions. What is the value of this built-in class variable `this`?
    1. A pointer to the current object instance.
    1. An alias of the current object.
    1. A pointer to a heap-memory copy of the current object.
    1. A reference to the current object.

10. Consider the code below that includes a class that has a custom constructor and destructor and both utilize a global variable (which has global scope and can be accessed anywhere and initialized before the function main is executed).
    ```c++
    int reference_count = 0;

    class Track {
        public:
            Track() { reference_count++; }
            ~Track() { reference_count--; }
    };
    ```
    Which one of the following procedures (void functions) properly ensures the deallocation of all the memory allocated for objects of type Track so the memory can be re-used for something else after the procedure returns?
    For the correct answer, the variable reference_count should be zero after all calls to track_stuff() and all of the memory should be deallocated properly. This will dependably occur after only one of the following procedures.
    1. ```c++
        void track_stuff() {
            Track t;
            // ...
            delete t;
            return;
        }
        ```
    2. ```c++
        void track_stuff() {
            Track t;
            Track *p = new Track;
            // ...
            delete p;
            return;
        }
        ```
    3. ```c++
        void track_stuff() {
            Track *t = new Track;
            // ...
            t->~Track();
            return;
        }
        ```
    4. ```c++
        void track_stuff() {
            Track t;
            Track *p = &t;
            // ...
            delete p;
            return;
        }
        ```

***

#### Answers 03

| Question | Answer |
| -------- | ------ |
| 1 | ii |
| 2 | i |
| 3 | iv |
| 4 | ii, iii, iv, v |
| 5 | i, iii, iv, v |
| 6 | iv |
| 7 | ii |
| 8 | ii |
| 9 | i |
| 10 | ii |

Question 4: option iv returns a cube object when the function returns and this is copied to the main stack
Question 6: Include copy constructor in the count as well

***

### Assignment 03

A class called Pair has already been declared, but the constructors have not been implemented yet. Pair has two public member variables:

`int *pa,*pb;`

These two _pointers to int_ are intended to point to heap memory locations that store integers. The remainder of the Pair class expects the following functionality.

* A single constructor `Pair(int a, int b)`: This should set up `pa` and `pb` to point to newly allocated memory locations on the heap. The integers at those memory locations should be assigned values according to the constructor's integer arguments `a` and `b`.
* A copy constructor `Pair(const Pair& other)`: This takes as its argument a read-only reference to another Pair. It should set up the newly constructed Pair as a "deep copy," that is, it should create a `new` Pair that is equivalent to the other Pair based on dereferenced values but does not reuse any of the same memory locations. In other words, the copy constructor should set up its own instance's member variables pa and pb to point to newly allocated memory locations for integers on the heap; those memory locations must be new, not the same locations pointed to by the other Pair, but the integers at these new locations should be assigned values according to the integers that the other Pair is pointing to.
* A destructor `~Pair()` that de-allocates all of the the heap memory that had previously been allocated for this Pair's members.

The types of these member functions have already been declared in the declaration of Pair. Now you need to provide the implementation of each of these three member functions.

(**Note**: The function declarations shown in the code comment below do not include parameter names for the arguments. They show only the types of the arguments. This is allowed for a declaration, but when you define the implementation of those functions, you should give names to the parameters so that you can refer to them.)

```c++
/* Class Pair has already been declared
 * as shown in the following comments:
 *
 * class Pair {
 * public:
 *   int *pa,*pb;
 *   Pair(int, int);
 *   Pair(const Pair &);
 *  ~Pair();
 * };
 *
 * Implement its member functions below.
 */



 /* Here is a main() function you can use
  * to check your implementation of the
  * class Pair member functions.
  */

int main() {
    Pair p(15,16);
    Pair q(p);
    Pair *hp = new Pair(23,42);
    delete hp;

    std::cout << "If this message is printed,"
        << " at least the program hasn't crashed yet!\n"
        << "But you may want to print other diagnostic messages too." << std::endl;
    return 0;
}
```

***

#### Solution Assignment 03

```c++
Pair::Pair(int a, int b){
    // assign heap memory and copy values of arguments
    pa = new int; *pa = a;
    pb = new int; *pb = b;
};
Pair::Pair(const Pair &p){
    // assign heap memory and copy values from passed Pair
    pa = new int; *pa = *(p.pa);
    pb = new int; *pb = *(p.pb);
};
Pair::~Pair(){
    // delete the memory allocated on the heap
    delete pa; pa = nullptr;
    delete pb; pb = nullptr;
};

int main() {
    Pair p(15,16);
    Pair q(p);
    Pair *hp = new Pair(23,42);
    delete hp;

    std::cout << "If this message is printed,"
        << " at least the program hasn't crashed yet!\n"
        << "But you may want to print other diagnostic messages too." << std::endl;
    return 0;
}
```

***

### Quiz 04

1. Which one of the following is **NOT** true?
    1. C++ allows a variable to be declared in a user-defined function with an unknown type that can be defined when the function is called.
    1. C++ allows a variable to be declared in a user-defined member function of a user-defined class that can be defined when the function is called.
    1. C++ allows a member variable to be declared in a user-defined class with an unknown type that can by defined when an object of that class is created.
    1. C++ allows a local variable to be declared in main() with an unknown type that can be defined when the program is executed.

2. Suppose you want to create a vector of integers. Which of the following creates an instance of the std::vector class that can contain integers?
    1. `int<std::vector> v;`
    1. `int *v;`
    1. `std::vector<int> v;`
    1. `int v[256];`

3. Which of the following will generate an error at compile time?
    1. `std::vector<char[256]> v;`
    1. `std::vector v;`
    1. `std::vector<double> v;`
    1. `std::vector<std::vector<int>> v;`

4. ```c++
    template <typename Type>
        Type max(Type a, Type b) {
        return (a > b) ? a : b;
    }
    ```
    Which one of the following exampled is a proper way to call the max function declared above in template form?
    1. `max<Type = double>(5.0,10.0)`
    1. `max(5.0,10.0)`
    1. `max<double>(5.0,10.0)`
    1. `<Type = double>max(5.0,10.0)`

5. ```c++
    template <typename Type>
    Type max(Type a, Type b) {
        return (a > b) ? a : b;
    }
    class Just_a_double {
    public:
        double num;
    };
    int main() {
        Just_a_double a,b;
        a.num = 5.0;
        b.num = 10.0;
        // ...
    }
    ```
    Given the above code, which one of the expressions below, if used at line 15, will compile and not generate a compile error?
    1. `max(a.num,b.num)`
    1. `max("five",10.0)`
    1. `max(a,10.0)`
    1. `max(a,b)`

6. Which one of the following properly declares the class RubikCube derived from the base class Cube?
    1. `class Cube(RubikCube) {...};`
    1. `class RubikCube : public Cube {...};`
    1. `class RubikCube(Cube) {...};`
    1. `class Cube : public RubikCube {...};`

7. ```c++
    class Pair {
        public:
            double a,b;
            Pair(double x, double y) { a = x; b = y; }
    };
    ```
    If a class equalPair is derived from the above base class (but specializes it by adding a single boolean "isequal" member variable) then which one of the options below is a proper declaration of a constructor for equalPair?

    (As a side note: Although the member variables are of type double, for the sake of this question, we are not concerned about making approximate comparisons of floating-point types, only exact comparisons. Usually, in practical usage, when you compare floating-point values, you should write a function for approximate comparison. That is, you should allow numbers to be considered equal if they have a very small absolute difference, even if they are not exactly the same.)
    1. ```c++
        equalPair(double a, double b) {
            this->Pair(a,b);
            isequal = (a == b);
        }
        ```
    2. ```c++
        equalPair(double a, double b) : Pair(a,b) {
            isequal = (a == b);
        }
        ```
    3. ```c++
        equalPair(double a, double b) {
            Pair(a,b);
            isequal = (a == b);
        }
        ```
    4. ```c++
        equalPair(double a, double b) {
            isequal = (a == b);
        }
        ```

8. ```c++
    class Pair {
        private:
            double a,b;
    };
    class equalPair : public Pair {
        private:
            bool isequal;
        public:
            int status();
    }
    ```
    When the function status() is implemented, which variables will it have access to?
    1. Both the member variables a,b or Pair and isequal of equalPair.
    1. No member variables of either equalPair or Pair.
    1. Just the member variables a,b of Pair.
    1. Just the member variable isequal of equalPair.

9. ```c++
    class Just_a_double {
        public:
            double a;
            Just_a_double(double x) : a(x) { }
            Just_a_double() : Just_a_double(0) { }
    }
    ```
    Which constructors, if any, compile properly?
    1.  Both constructors on lines 5 and 6 compile properly
    1.  The constructor on line 5 results in a compiler error but the constructor on line 6 compiles properly,
    1.  The constructor on line 5 compiles properly, but the constructor on line 6 results in a compiler error.
    1.  Both constructors on lines 5 and 6 result in compiler errors.

10. C++ is
    1. a great language for programming data structures.
    1. the greatest language for programming data structures ever!
    1. meh.

***

#### Answers 04

| Question | Answer |
| -------- | ------ |
| 1 | iv |
| 2 | iii |
| 3 | ii |
| 4 | ii |
| 5 | i |
| 6 | ii |
| 7 | ii |
| 8 | iv |
| 9 | i |
| 10 | i |

***

### Assignment 04
A base class `Pair` contains a single constructor `Pair(a,b)` that initializes the pair with the two integer arguments `a` and `b`. A derived class `sumPair` inherits the base class `Pair`, and specializes it with a new constructor `sumPair(a,b)` and a new variable `sum`.

Both of these classes have already been defined.

Implement the new constructor `sumPair(a,b)`, which was declared already in class `sumPair`. The new constructor `sumPair(a,b)` should initialize the inherited class Pair with integer values `a,b` and set the member variable `sum` to the sum of `a` and `b`.

```c++
/* Class Pair has already been
 * declared and defined with the
 * following constructor:
 *
 *   Pair(int,int)
 *
 * that stores its two arguments in
 * two private member variables of Pair.
 *
 * Class sumPair has also already been
 * defined as follows:
 *
 * class sumPair : public Pair {
 * public:
 *   int sum;
 *   sumPair(int,int);
 * };
 *
 * Implement the constructor
 * sumPair(int,int) such that it
 * loads the two member variables of
 * the base Pair class with its
 * arguments, and initializes the
 * member variable sum with their sum.
 */

/* Below is a main() function
 * you can use to test your
 * implementation of the
 * sumPair constructor.
 */

int main() {
  sumPair sp(15,16);
  std::cout << "sp(15,16).sum =" << sp.sum << std::endl;
  return 0;
}
```

#### Solution Assignment 04

The required definition is
```c++
sumPair::sumPair(int a, int b) : Pair(a, b){
  sum = a + b;
}
```

***
