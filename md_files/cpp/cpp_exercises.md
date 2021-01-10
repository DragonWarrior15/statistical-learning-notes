# C++
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

9. 
    ```c++
    int i = 0, j = 1;
    int *ptr = &i;

    i = 2;
    *ptr = 3;
    ptr = &j;
    j = i;
    *ptr = 4;
    ```
    Enter the number of different values stored in the same address that variable i has during the execution of the code above. (Your answer should be a single integer, which is the total number of different values assigned to that address.)

10. 
    ```c++
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
    1. 
        ```c++
        Cube a, b(10);
        a = b;
        ```
    2. 
        ```c++
        // Function prototype for "contains":
        int contains(Cube outer, Cube inner);
        // ...
        Cube a(10),b(5);
        int a_bounds_b = contains(a,b);
        ```
    3. 
        ```c++
        Cube b(10);
        Cube a = b;
        ```
    4. 
        ```c++
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
    1. 
        ```c++
        void track_stuff() {
            Track t;
            // ...
            delete t;
            return;
        }
        ```
    2. 
        ```c++
        void track_stuff() {
            Track t;
            Track *p = new Track;
            // ...
            delete p;
            return;
        }
        ```
    3. 
        ```c++
        void track_stuff() {
            Track *t = new Track;
            // ...
            t->~Track();
            return;
        }
        ```
    4. 
        ```c++
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

4. 
    ```c++
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

5. 
    ```c++
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

7. 
    ```c++
    class Pair {
        public:
            double a,b;
            Pair(double x, double y) { a = x; b = y; }
    };
    ```
    If a class equalPair is derived from the above base class (but specializes it by adding a single boolean "isequal" member variable) then which one of the options below is a proper declaration of a constructor for equalPair?
    
    (As a side note: Although the member variables are of type double, for the sake of this question, we are not concerned about making approximate comparisons of floating-point types, only exact comparisons. Usually, in practical usage, when you compare floating-point values, you should write a function for approximate comparison. That is, you should allow numbers to be considered equal if they have a very small absolute difference, even if they are not exactly the same.)
    1.
        ```c++
        equalPair(double a, double b) {
            this->Pair(a,b);
            isequal = (a == b);
        }
        ```
    2. 
        ```c++
        equalPair(double a, double b) : Pair(a,b) {
            isequal = (a == b);
        }
        ```
    3. 
        ```c++
        equalPair(double a, double b) {
            Pair(a,b);
            isequal = (a == b);
        }
        ```
    4. 
        ```c++
        equalPair(double a, double b) {
            isequal = (a == b);
        }
        ```

8. 
    ```c++
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

9. 
    ```c++
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

10. C++ is ...
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

## Course 02: some name

***

### Quiz 01

1.  
    ```c++
    int tri(int n) {
        int i,j;
        int count = 0;
        for (j=0; j < n; j++){
            for (i=0; i < j; i++){
                count++;
            }
        }
        return count;
    }
    ```
    Perform a run-time analysis of the code above. Express the number of times the variable count is incremented in terms of "Big Oh" notation.
    Recall that "Big Oh" notation is denoted as O() where the parameter of O() is a simple function of n that indicates how the run-time increases as n increases. For example, if the run-time grows as a polynomial of n, such as `5n^3 + 3n^2` then the "Big-Oh" notation would ignore constants and lower growing terms and simply state O(n^3) growth.
    1. O(n^2 + n)
    1. O(1)
    1. O((1/2) n^2)
    1. O(n^2)

2. You have an array that is currently length one and already contains one item. You need to implement a function Append(i) that adds the item i to the position after the current last item of the array. If the array is full, then your Append() function will need to expand the size of the array so that it can store the additional item i. Recall that expanding the size of an array requires allocating new memory for the expanded size and copying all of the current array items to the new (expanded) array before de-allocating the previous (full) array.
    (It is okay to assume there is always enough memory to allocate for an array.)
    Your Append() function will be called an unknown number of times. Which method for resizing the array would result in the fastest total run-time for calling Append() n times to add n items to the array?
    1. Doubling the length of the array every time an item is added when the array is already full.
    1. Increasing the length of the array by one every time an item is added.
    1. Increasing the length of the array by one billion every time an item is added and the array is already full.
    1. Expanding the array to length n + 1 the first time Append() is called.

3. Which one statement below is **FALSE**? Assume we are using the most efficient algorithms discussed in lecture.
    1. Adding n items, one at a time, to the end of an array takes O(n) time overall.
    1. Finding an item in a sorted array of n items cannot be done in better than O(n) time.
    1. Adding n items, one at a time, to the front of a linked list takes O(n) time overall.
    1. Finding an item in a sorted linked list of n items takes O(n) time.

4. You have a list of 100 items that are not sorted by the item value. Which one task below would run much faster on a list implemented as an array rather than implemented as a linked list?
    1. Inserting a new item between the 24th item and the 25th item.
    1. Searching the list for all items that match a given item.
    1. Finding the first item.
    1. Replacing the 25th item in the list with a different item.

5. You have a list of 100 items that are not sorted by the item value. Which one task below would run much faster on a list implemented as linked list rather than implemented as an array?
    1. Inserting a new item between the 24th item and the 25th item.
    1. Replacing the 25th item in the list with a different item.
    1. Finding the first item
    1. Searching the list for all items that match a given item.

6. Suppose you want to implement a queue ADT using a linked list. Your queue needs to be able to "push" (or "enqueue") a single item in constant time, as well as "pop" (or "dequeue") a single item in constant time. The operations need to happen at opposite ends of the queue, as would be expected of the queue ADT. However, the people who use your queue implementation don't need to know about how exactly it is implemented, so you can be somewhat creative in how you implement it, as long as the "push" and "pop" operations behave as expected. Which of the following implementations can accomplish this? Select all that apply. (For the sake of this question, let's not consider any design strategies that would close the linked list into a circle.)
    1. You can do it with a modified singly-linked list where the list has both a "head" pointer and a "tail" pointer, but each node has only a "next" pointer.
    1. You can't implement a queue as a linked list. You need a more advanced data structure.
    1. You can do it with a doubly-linked list where the list has a "head" pointer and a "tail" pointer and each node has a "next" pointer and a "previous" pointer.
    1. You can do it with a singly-linked list where the list has only a "head" pointer and each node has only a "next" pointer.

7. When implementing a queue which will need to support a large number of calls to its push() and pop() methods, which choice of data structure results in a faster run time according to "Big Oh" O() analysis?
    1. The linked list implementation of a queue has a better run time complexity than does the array implementation.
    1. A linked list because an array cannot be used to implement a queue that supports both push() and pop() methods.
    1. The array implementation of a queue has a better run time complexity than does the linked list implementation.
    1. Both array and linked list implementations of a queue have the same run time complexity.

8. When implementing a stack which will need to support a large number of calls to its push() and pop() methods, which choice of data structure results in a faster run time according to "Big Oh" O() analysis?
    1. The linked list implementation of a stack has a better run time complexity than does the array implementation.
    1. The array implementation of a stack has a better run time complexity than does the linked list implementation.
    1. Both array and linked list implementations of a stack have the same run time complexity.
    1. An array implementation because a linked list cannot be used to implement a stack that supports both push() and pop() methods.

9. Suppose this stack is implemented as a linked list.
    ```c++
    std::stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    ```
    What is the value at the head of the linked list used to implement the stack s?
    1. 1
    1. 3
    1. 2
    1. A stack cannot be implemented using a linked list.

10. Suppose we had the following interface for a stack and queue, along with a correct implementation.
    (Note that in this simple version, the "pop" and "dequeue" methods will remove an item and also return a copy of that same item by value. This is a little different from how the C++ Standard Template Library implementations of a stack and queue work. In STL, you have separate functions for peeking at the next value that would be removed, and for actually removing the item.)
    ```c++
    class Stack{
        public:
            Stack();
            bool push(int x);
            int pop();
            bool isEmpty();
        // other lines omitted
    };
    class Queue{
        public:
            Queue();
            bool enqueue(int x);
            int dequeue();
            bool isEmpty();
        // other lines omitted
    };
    ```
    What output does the following code produce?
    1. 4 3 2 1 0
    1. 0 1 2 3 4 4 3 2 1 0
    1. 4 3 2 1 0 0 1 2 3 4
    1. 0 1 2 3 4

***

#### Answers 01
| Question | Answer |
| -------- | ------ |
| 1 | iv |
| 2 | i |
| 3 | ii |
| 4 | iv |
| 5 | i |
| 6 | ii, iii |
| 7 | iv |
| 8 | iii |
| 9 | ii |
| 10 | iv |

***

### Quiz 02

1. For a linked structure of edges and nodes to be a tree, which of the following is **not** required to be true?
    1. Every node is connected to every other node by some path of edges.
    1. Every node has zero, one or two children.
    1. If any two nodes are connected, they are connected by only one path of unique nodes and edges.
    1. Every node has a parent except for one single root node.

2. Which data structure below supports the fastest run time for finding an item in a sorted list of items?
    1. Array
    1. Linked List
    1. Binary Search Tree
    1. All of these data structures have the same run time complexity for finding an item in a sorted list of items.

3. What is the height of the binary search tree created by inserting the following values one at a time in the following order of insertion: 1 2 3 4 5 6 7 ?
    1. 2
    1. 3
    1. 6
    1. 7

4. Which of the following is **NOT** true of a perfect binary search tree of a list of  n ordered items?
    1. All of the leaf nodes are at the same level.
    1. The worst-case run time to find an item is O(n).
    1. If the height of the tree is h, then n =  2^(h+1) - 1.
    1. Every non-leaf node has two children.

5. Which of the following is **NOT** a full binary tree?
    1. A perfect binary tree.
    1. A single node.
    1. The binary tree consisting of the subtree of ancestors of any node in any perfect binary tree.
    1. The binary search tree created by inserting the following values one at a time: 4 2 3 5 1.

6. Which of the following is **not** a true statement about a complete binary tree?
    1. Any tree that contains a node with a single child is not a complete binary tree.
    1. The worst-case run time for finding an object in a complete binary search tree of an ordered list of n items is O(lg n).
    1. No node in a complete binary tree has only a right child.
    1. The height of a complete binary tree of n nodes is floor(lg n).

7. Which one of the following functions outputs the keys of a binary search tree in item order when the root node is passed to it as its parameter.
    1.
        ```c++
        void print(TreeNode *node){
            if (!node) return;
            std::cout << node->key << " ";
            print(node->left);
            print(node->right);
        }
        ```
    1.
        ```c++
        void print(TreeNode *node){
            if (!node) return;
            print(node->left);
            std::cout << node->key << " ";
            print(node->right);
        }
        ```
    1.
        ```c++
        void print(TreeNode *node){
            if (!node) return;
            print(node->left);
            print(node->right);
            std::cout << node->key << " ";
        }
        ```
    1. None of these outputs all of the keys of the binary search tree in item order.

8. Consider the binary search tree built by inserting the following sequence of integers, one at a time: 5, 4, 7, 9, 8, 6, 2, 3, 1
    Which method below will properly remove node 4 from the binary search tree?
    1. Set the left pointer of node 5 to point to the node pointed to by the left pointer of node 4, and then delete node 4.
    1. Find the in order predecessor (IOP) of node 4, which is node 3. Remove node 3 from the tree by setting the right pointer of its parent (node 2) to nullptr. Then copy the key and any data from node 3 to node 4, turning node 4 into a new node 3, and delete the old node 3. 
    1. Find the in order predecessor (IOP) of node 4, which is node 3. Remove node 3 from the tree by setting the right pointer of its parent (node 2) to point to the node pointed to by the left pointer of node 3. Then copy the key and any data from node 3 to node 4, turning node 4 into a new node 3, and delete the old node 3. 
    1. Set the left pointer of node 5 to nullptr, and then delete node 4.

9. Suppose that we have numbers between 1 and 1000 in a binary search tree and we want to search for the number 363.  Which of the following sequences can **not** be the sequence of nodes visited in the search?
    1. 925, 202, 911, 240, 912, 245, 363  
    1. 2, 399, 387, 219, 266, 382, 381, 278, 363
    1. 2, 252, 401, 398, 330, 344, 397, 363
    1. 924, 220, 911, 244, 898, 258, 362, 363  

10. Given any binary tree with 128 nodes where each node has a left pointer and a right pointer, how many of these pointers are set to nullptr?

***

#### Answers 02
| Question | Answer |
| -------- | ------ |
| 1 | ii |
| 2 | i |
| 3 | iii |
| 4 | ii |
| 5 | iii |
| 6 | i |
| 7 | ii |
| 8 | i |
| 9 | i |
| 10 | 129 |

***

### Quiz 03

**Assume that balance factor is height of right subtree - height of left subtree** 

1. Create a binary search tree by inserting the following five values one at a time:
    4 6 5 7 8
    What is the height of this tree?
    (Recall how we calculate the height of a tree or subtree: The height of a leaf node by itself is 0. The height of a non-existent tree is -1. Otherwise, the height of a tree is the longest path length from the root of that tree to any one of its leaves.)

2. Create a binary search tree by inserting the following eight values one at a time:
    3 1 2 4 6 5 7 8
    What is the balance factor of the root node of this tree? (For this question, do not perform any rotations on this tree as you insert the items. It's just a binary search tree, not necessarily a balanced BST such as an AVL tree.)

3. For the binary search tree created by inserting these items in this order: 4 3 5 1 2, which node among 1 through 5 is the deepest node with a balance factor of magnitude two or greater? (For this question, do not perform any balancing rotations as you insert these items.)

4. Consider the binary search tree that you constructed in the previous question. If we interpret it now as an AVL tree, it has an imbalance that can be fixed with a rotation. (Remember that we focus on the deepest point of imbalance, where the magnitude of the balance factor is 2 or greater, to perform the rotation.)
    After performing the correct balancing rotation about the node that we identified in the previous question, the resulting tree is identical to which one of the following binary search trees? (We'll describe these other trees by listing the order in which you would insert items to create the trees directly.)
    1. Inserting `2 1 4 3 5` one node at a time.
    1. Inserting `3 2 4 1 5` one node at a time.
    1. Inserting `4 2 5 1 3` one node at a time.
    1. Inserting `3 5 2 4 1` one node at a time.

5. The code that ensures the balance of an AVL tree after node insertion or removal only checks if the height balance factor is +2 or -2. What happens if the height balance factor of a node in an AVL tree after node insertion or removal is greater that +2 or less than -2?
    1. When insertion and removal create a node whose height balance factor is greater than +2 or less than -2, that node always has a descendant with a height balance factor equal to +2 or -2 and when all of its descendant nodes are resolved, then its height balance factor will be no greater than +2 or no less than -2.
    1. There is additional code not shown that handles the cases when the height balance factor is greater than +2 or less than -2.
    1. An AVL tree never has a node with a height balance factor greater than +2 or less than -2, even after a node insertion or removal.
    1. We ignore nodes in an AVL tree with height balance factor greater than +2 or less than -2 because they are statistically rare and are unstable, such that they are removed as soon as any tree balancing rotation occurs.

6. If, after inserting a new node into an AVL tree, you now have a node with a height balance factor of -2 with a child with a height balance factor of -1, which of the following operations should be performed?
    1. Left Rotation
    1. Right-Left Rotation
    1. Right Rotation
    1. Left-Right Rotation

7. If, after inserting a new node into an AVL tree, you now have a node with a height balance factor of -2 with a child with a height balance factor of +1, which of the following operations should be performed?
    1. Right-Left Rotation
    1. Right Rotation
    1. Left Rotation
    1. Left-Right Rotation

8. Which one of the following is **NOT** a valid reason to choose the B-Tree representation over a standard AVL binary search tree?
    1. B-Trees require fewer block read accesses for tree operations.
    1. B-Trees have better algorithmic "Big-O" run-time complexity for the find operation.
    1. B-Trees run faster on large data sets than do AVL trees.
    1. B-Trees work faster in networked cloud environments than do AVL trees.

9. Which of the following statements is **NOT** true for a B-Tree of order m?
    1. All leaf nodes are at the same level of the B-Tree.
    1. Each node can have at most one more child than key.
    1. Each node can hold an ordered list of as many as m keys.
    1. Any node that is not the root or a leaf holds at least half of the total number of keys allowed in a node.

10. If a B-Tree is completely filled, meaning every node holds its maximum number of keys and all non-leaf nodes has the maximum number of children, then what happens when an additional key is inserted into the B-Tree?
    1. A new node containing the new key is added above the previous root and becomes the new root. The new root will have one pointer leading to the old root node.
    1. Every leaf node in the entire B-Tree becomes parent to a new leaf node, but all but one of these leaf nodes are "blank" placeholder nodes that contain zero key values.
    1. A new leaf node is simply added to the B-Tree.
    1. After searching for the leaf node where the new key should go, the leaf is split in half as two separate leaf nodes, and then the middle value is thrown up to the layer above as an inserted key, and this insertion and rebalancing repeats until a new root key rises to the top, which adds a layer to the tree.

***

#### Answers 03
| Question | Answer |
| -------- | ------ |
| 1 | 3 |
| 2 | 2 |
| 3 | 3 |
| 4 | iii |
| 5 | iii |
| 6 | iii |
| 7 | iv |
| 8 | ii |
| 9 | iii |
| 10 | iv |

***

### Quiz 04

1. Assume you are storing a complete binary tree as a contiguous list of keys in an array such that the root's key is stored at location 1 of the array, the keys from all of the nodes at the next level of the tree are stored  in left-to-right order in subsequent locations in the array, then similarly for all of the nodes of each subsequent level.
    At what array location would the key stored in the node that is the left child of the right child of the root?

2. When using an array to store a complete tree, why is the root node stored at index 1 instead of at the front of the array at index 0?
    1. We use index zero as a guard to prevent overstepping the root when propagating up the tree from its leaf nodes, which would cause a memory access fault.
    1. We avoid using index 0 to avoid confusion with the value of 0 (nullptr) that we normally store in the child pointer of a node to indicate that child does not exist.
    1. This makes the math for finding children and parents simpler to compute and to explain.
    1. Array index 0 is used to store the number of nodes in the complete tree stored in the array.

3. When is a binary tree a min-heap?
    1. When the leaf nodes represent the smallest values in the tree, and every leaf node is smaller than the root.
    1. When every node's value is less than its parent's value.
    1. When every node's value is greater than its parent's value.
    1. When every node's value lies between the maximum value of its left child's subtree and the minimum value of its right child's subtree.

4. How should one insert a new value into a heap to most efficiently maintain a balanced tree?
    1. Maintain the heap as a complete tree and insert a new value at the one new node position that keeps the tree as a complete tree. Then continually exchange the new value with the value of its parent until the new value is in node where it is greater than the value of its parent.
    1 .Maintain the heap as a balanced binary search tree. Walk down the tree from the root exploring the left children first, then the right children, until a node is found that is greater than the new value. Insert a new node with the new value at that position and make the previous node the left child of that new node. Rebalance the tree if the height balance factor magnitude of the new node or its parent exceeds one.
    1. Maintain the heap as an array. Walk down the tree from the root at position 1 in the array, exploring the left children first, then the right children, until a node position is found whose value is greater than the new value. Copy the value at that position and all subsequent positions in the array to one greater position in the array, and store the new value at that position.
    1. Maintain the heap as an AVL tree. Walk down the tree from the root exploring the left children first, then the right children, until a node is found that is greater than the new value. Insert a new node with the new value at that position and make the previous node the left child of that new node. Then call the appropriate rotation routine to rebalance the tree if the height balance factor magnitude of the new node or its parent reaches two.

5. The removeMin operation removes the root of a min-heap tree. Which of the following implements removeMin efficiently while maintaining a balanced min-heap tree.
    1. Replace the root value with the value of the last leaf (rightmost node at the bottom level) of a complete binary tree, and delete the last leaf. Then repeatedly exchange this last-leaf value with the smaller of the values of its node's children until this last-leaf value is smaller than the values of its node's children, if any.
    1. Delete the root and if the root has two children, then merge its left subtree with its right subtree by inserting each right subtree node value into the left subtree. Then delete the right subtree.
    1. Set the root value to +infinity. If the left child is smaller than the right child, perform a Right-Rotation, otherwise perform a Left-Rotation. Repeat this process at the new infinity-node location until the infinity node is a leaf, then remove and delete it.
    1. Increment the address used to indicate the base location of the array storing the complete binary tree.

6. How many nodes of a complete binary tree are leaf nodes?
    1. About a fourth.
    1. About the square root.
    1. Unknown. Could be one. Could be all.
    1. About half.

7. Recall that the heapifyDown procedure takes a node index whose children (if any) are heaps, but the value of the node might not satisfy the heap property compared to its children's values. This procedure then swaps the node's value with the smallest child value larger than it (if any), and then calls itself on that smallest child node it just swapped values with to further propagate that value down the heap until it finds a valid location for it.
    ```c++
    template <class T>
    void Heap<T>::_heapifyDown(int index) {
        if (!_isLeaf(index)) {
            T minChildIndex = _minChild(index);
            if (item_[index] > item_[minChildIndex] ) {
                std::swap( imem_[index], item_[minChildI]);
                _heapifyDown(minChildIndex);
            }
        }
    }
    ```
    When you call heapifyDown on a given node, what is the maximum number of times heapifyDown is called (including that first call) to find a valid location for the initial value of that node?
    1. The maximum number of times heapifyDown is called is the number of non-leaf nodes in its subtree.
    1. heapifyDown is only called once since its children are already heaps.
    1. The maximum number of times heapifyDown is called is one plus the height of the node.
    1. The maximum number of times heapifyDown is called is the number of nodes in its subtree.

8. What is the run-time algorithmic complexity of calling heapifyDown on every non-leaf node in a complete tree of n nodes?
    1. O(n lg n)
    1. O(1)
    1. O(n^2)
    1. O(n)

9. Which of the following is the fastest way to build a heap of n items?
    1. Create a complete tree of the items in any order, then call heapifyUp on every node in the tree from the root down to the leaf nodes.
    1. Create a complete tree of the items in any order. If this is not a heap, then swap the items between two randomly chosen nodes and check again. Repeat the random swapping until you get a heap.
    1. Create a complete tree of the items in any order, then call heapifyDown on every non-leaf node from the bottom of the tree up to the root.
    1. Create a heap with a single node holding the first item. Then insert the remaining n-1 items into the heap.

10. Which of the following is NOT a step of the heap sort algorithm?
    1. Load the data in any order into a complete tree.
    1. Run heapifyDown on every non-leaf node.
    1. Remove the root node.
    1. Insert the next item into the current heap.

***

#### Answers 04
| Question | Answer |
| -------- | ------ |
| 1 | 6 |
| 2 | iii |
| 3 | iii |
| 4 | i |
| 5 | i |
| 6 | i |
| 7 | iii |
| 8 | iii |
| 9 | iii |
| 10 | iv |

***

### Assignment 1

Implement downHeap(Node \*n) for a min heap data structure, that is here implemented as a node-based binary tree with an integer member variable "value" and left and right child pointers. (Unlike the video lesson which implemented downHeap on an array implementation of a complete binary tree, the binary tree in this challenge problem is not stored as an array and is not necessarily complete; any node might have only a left child, only a right child, both, or neither.) 

The starter code below defines a class called "Node" that has two child pointers ("left" , "right") and an integer "value" member variable. There is also a constructor Node(int val) that initializes the children to nullptr and the node's value to val. 

Your job is to implement the procedure "downHeap(Node \*n)" . The procedure should assume that n->left is the root of a min heap subtree (or nullptr) and the same for n->right.  The value at Node \*n (specifically n->value) might not be less than the values in its left subtree and in its right subtree, and so the tree with Node \*n as its root might not be a min heap (even though its left subtree and right subtree are both min heaps). Your code should modify the tree rooted at Node \*n so it is a min heap. You do not need to balance the tree or turn it into a complete tree. You only need to ensure that the tree satisfies the min heap property: 

For a min heap, it is okay for a node's value to be equal to one or both of its children, but the node's value must not be greater than either of its children. You should not perform swaps with nodes of equal value, as this does needless work.

Again, as is implied by the above description, for this exercise you may assume that only the root node violates the min heap property at the beginning, if any node does (as the left and right subtrees are already valid heaps). This means it's possible to implement the downHeap function as O(log n). If your algorithm has a running time worse than O(logn), it is probably incorrect. The significance of this O(log n) algorithm is that it can be used as an efficient tool in the O(n)-time algorithm that corrects a new heap in multiple steps from the bottom up, as described in lecture.

```c++
/*

Below, please implement the downHeap procedure for
a min heap data structure, which we will represent
as node-based tree for this exercise (not an array).

Suppose you are given a tree where the left and right
subtrees are min heaps, but the root node in particular
might not maintain the min heap property. Your code
should modify the tree rooted at Node* n so it is a
min heap. This means you need to satisfy the min heap
property: it is okay for a node's value to be equal to
one or both of its children, but the node's value must
not be greater than either of its children.

Tips:
Unlike the video lessons which demonstrated downHeap
implemented with an array implementation, this assignment
uses an ordinary binary tree with left and right child
pointers. This ordinary binary tree might not be complete
or balanced: any node might have only one child or the
other, or both, or neither. (You do not have to try to
balance the tree or turn it into a complete tree.)

If the root node exists, and if it has a left or right
child, and if one of the children has a smaller value
than the root node, then you should swap the root node
with the smaller child to move the large value down
into the tree. (This may need to be done recursively.)
Be careful to check whether pointers are null before
dereferencing them, as always; that includes using "->"
to access a class member through a pointer. In addition,
you must be careful not to accidentally compare "left"
and "right" pointers directly if you really intend to
compare the stored values "left->value" and "right->value".

Assume that these headers have already been included
for you:

#include <iostream>
#include <string>

You have the following class Node already defined.
You cannot change this class definition, so it is
shown here in a comment for your reference only:

class Node {
public:
  int value;
  Node *left, *right;
  Node(int val = 0) { value = val; left = right = nullptr; }
  ~Node() {
    delete left;
    left = nullptr;
    delete right;
    right = nullptr;
  }
};

This function has also previously been defined for you:

void printTreeVertical(const Node* n);

You can use it to print a verbose, vertical diagram of
a tree rooted at n. In this vertical format, a left child
is shown above a right child in the same column. If no
child exists, [null] is displayed.

*/


void downHeap(Node *n) {
  Node * swap_with = nullptr;
  // Implement downHeap() here.
}

// You can also use this compact printing function for debugging.
void printTree(Node *n) {
  if (!n) return;
  std::cout << n->value << "(";
  printTree(n->left);
  std::cout << ")(";
  printTree(n->right);
  std::cout << ")";
}

int main() {
  Node *n = new Node(100);
  n->left = new Node(1);
  n->right = new Node(2);
  n->right->left = new Node(3);
  n->right->right = new Node(4);
  n->right->right->right = new Node(5);

  downHeap(n);

  std::cout << "Compact printout:" << std::endl;
  printTree(n);
  std::cout << std::endl << "Vertical printout:" << std::endl;
  printTreeVertical(n);

  delete n;
  n = nullptr;

  return 0;
}

```

#### Answer Assignment 01
```c++
void downHeap(Node *n) {
  Node * swap_with = nullptr;
  // Implement downHeap() here.
  // if no child, do nothing
  if(!n->left && !n->right){}
  else if(!n->left && n->right){
    // check if value is greater than the right child
    if(n->value > n->right->value){
      swap_with = n->right;
    }
  }else if(n->left && !n->right){
    // check if value is greater than the left child
    if(n->value > n->left->value){
      swap_with = n->left;
    }  
  
  }else{
    // both children exist
    if(n->value <= n->left->value && n->value <= n->right->value){}
    else{
      if(n->left->value < n->right->value){
        swap_with = n->left;
      }else{
        swap_with = n->right;
      }
    }
  }

  if(swap_with){
    int temp = n->value;
    n->value = swap_with->value;
    swap_with->value = temp;
    downHeap(swap_with);
  }
}
```

***

## Course 03 : some name

***

### Quiz 01

1. According to video lesson 1.1.1, a hash table consists of three things. Which of these was **NOT** one of those three things?
    1. An array
    1. Collision handling
    1. Encryption
    1. A hash function

2. Given a hash function h(key) that produces an index into an array of size N, and given two different key values key1 and key2, the Simple Uniform Hashing Assumption states which of the following?
    1. The probability that h(key1) == h(key2) is 1/N.
    1. If h(key1) == h(key2) then h needs a running time of O(N) to complete.
    1. If h(key1) == h(key2) then h needs a running time of O(lg N) to complete.
    1. The probability that h(key1) == h(key2) is 0.

3. According to video lesson 1.1.2, which of the following is a **good** hash function h(key) that translates any 32-bit unsigned integer key into an index into an 8 element array?
    (Note that an expression like "2 & 3" uses the bitwise-AND operator, which gives the result of comparing every bit in the two operands using the concept of "AND" from Boolean logic; for example, in Boolean logic with binary numbers, 10 AND 11 gives 10: for the first digit, 1 AND 1 yields 1, while for the second digit, 0 AND 1 yields 0. An expression like "4 % 8" uses the remainder operator that give the remainder from integer division; for example, 4 % 8 yields 4, which is the remainder of 4/8. In some cases, these two different operators give similar results. Think about why that is.)
    1. 
        ```c++
        int h(uint key) {
            int index = 5;
            while (key--)
                index = (index + 5) % 8
            return index;
        }
        ```
    2. 
        ```c++
        int h(uint key) { return key & 7; }
        ```
    3. 
        ```c++
        int h(uint key) { return rand() % 8; }
        ```
    4. 
        ```c++
        int h(uint key) { return max(key,7); }
        ```

4. Suppose you have a good hash function h(key) that returns an index into an array of size N. If you store values in a linked list in the array to manage collisions, and you have already stored n values, then what is the expected run time to store a new value into the hash table?
    1. O(N)
    1. O(1)
    1. O(n) 
    1. O(n/N)

5. Suppose you have a good hash function h(key) that returns an index into an array of size N. If you store values in a linked list in the array to manage collisions, and you have already stored n values, then what is the expected run time to find the value in the hash table corresponding to a given key?
    1. O(n/N)
    1. O(N)
    1. O(n) 
    1. O(1)

6. Which one of the following four hashing operations would run faster than the others?
    1. Finding a value in a hash table of 4 values stored in an array of 8 elements.
    1. Finding a value in a hash table of 100 values stored in an array of 1,000 elements.
    1. Finding a value in a hash table of 20 values stored in an array of 100 elements.
    1. Finding a value in a hash table of 2 values stored in an array of 2 elements.

7. When storing a new value in a hash table, linear probing handles collisions by finding the next unfilled array element. Which of the following is the main drawback of linear probing?
    1. If the hash function returns an index near the end of the array, there might not be an available slot before the end of the array is reached.
    1. There may not be an available slot in the array.
    1. Even using a good hash function, contiguous portions of the array will become filled, causing a lot of additional probing in search of the next available unused element in the array.
    1. The array only stores values, so when retrieving the value corresponding to a key, there is no way to know if the value at h(key) is the proper value, or if it is one of the values at a subsequent array location.

8. When using double hashing to store a value in a hash table, if the hash function returns an array location that already stores a previous value, then a new array location is found as the hash function of the current array location. Why?
    1. Only one additional hash function is called to find an available slot in the array whereas linear probing requires an unknown number of array checks to find an available slot.
    1. Double hashing reduces the chance of a hash function collision on subsequent additions to the hash table.
    1. Double hashing reduces the clumping that can occur with linear probing.
    1. Since the hash function runs in constant time, double hashing runs in O(1) time.

9. Which of the following data structures would be the better choice to implement a memory cache, where a block of global memory (indicated by higher order bits of the memory address) are mapped to the location of a block of faster local memory.
    1. A hash table implemented with linear probing.
    1. A hash table implemented with separate chaining, using an array of linked lists.
    1. A hash table implemented with double hashing.
    1. An AVL tree.

10. Which of the following data structures would be the better choice to implement  a dictionary that not only returns the definition of a word but also returns the next word following that word (in lexical order) in the dictionary.
    1.  An AVL tree.
    1.  A hash table implemented with separate chaining, using an array of linked lists.
    1.  A hash table implemented with linear probing.
    1.  A hash table implemented with double hashing.

***

#### Answers 01
| Question | Answer |
| -------- | ------ |
| 1 | iii |
| 2 | i |
| 3 | ii |
| 4 | ii |
| 5 | i |
| 6 | ii |
| 7 | iii |
| 8 | iii |
| 9 | iii |
| 10 | i |


Answer 4: insert is always O(1), find depends on load factor
Answer 6: calculate load factor

***

### Quiz 02

1. Using the convention followed by the video lessons, given three disjoint sets (1,3,5,7), (2,8) and (4,6), which one of these sets would be referenced by the value 3?
    1. (1,3,5,7)
    1. (2,8)
    1. (4,6)
    1. None of the above.

2. What is the union of the disjoint sets (1,3,5,7) and (2,8)?
    1. (1,2,3,5,7,8)
    1. ((1,2),(1,8),(3,2),(3,8),(5,2),(5,8),(7,2),(7,8))
    1. (2,6,8,10,14,16,24,40,56)
    1. (3,11)

3. What happens when you take the union of two disjoint sets that contain the same value?
    1. Two different disjoint sets by definition can never share the same value.
    1. Any element found in both disjoint sets will appear twice in the union of these two disjoint sets.
    1. The union operation must first check to see if the same element appears in both disjoint sets and then ensures the element appears only once in the resulting union set.
    1. The elements cancel and neither appears in the union of the two disjoint sets.

4. According to the distjoint set array representation in the video lessons, Which of the following arrays would **NOT** be a valid representation of the disjoint set (1,3,5,7)?
    1. 
        ```c++
        index-> | 1 |  2 |  3 |  4 | 5 |  6 | 7 |  8 |
        value-> | 5 | -1 | -1 | -1 | 3 | -1 | 1 | -1 |
        ```
    1. 
        ```c++
        index-> |  1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 |
        ```
    1. 
        ```c++
        index-> | 1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | 3 | -1 | 5 | -1 | 7 | -1 | 1 | -1 |
        ```
    1. 
        ```c++
        index-> |  1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | -1 | -1 | 1 | -1 | 3 | -1 | 5 | -1 |
        ```

5. When encoding **height** into the root of an up-tree, what value should be placed in element 7 of the following array?
    | index | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    | ----- | - | - | - | - | - | - | - |
    | value | 3 | -1 | 7 | -1 | 7 | -1 | ? |
    1. -3
    1. -2
    1. -1
    1. -4

6. When encoding **size** into the root of an up-tree, what value should be placed in element 7 of the following array?
    | index | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    | ----- | - | - | - | - | - | - | - |
    | value | 3 | -1 | 7 | -1 | 7 | -1 | ? |
    1. -3
    1. -1
    1. -4
    1. -2

7. When computing the union of two disjoint sets represented as up-trees in an array, (using proper path compression) which of these strategies results in a better overall run time complexity than the other options?
    1. Always make the up-tree with fewer elements a subtree of the root of the up-tree with more elements.
    1. Always make the up-tree with a shorter height a subtree of the root of the up-tree with a larger height.
    1. The overall run time complexity is not affected by which up-tree is chosen to become a subtree of the other up-tree.
    1. Using either size or height strategies above results in the same overall run time complexity.

8. Recall that the iterated log function is denoted log* (n) and is defined to be
    ```c++
    log* (n) = 0                 for n <= 1, and
               1 + log* (log(n)) for n > 1
    ```
    Let lg* (n) be this iterated log function computed using base 2 logarithms.
    Blue Waters, housed at the University of Illinois, is the fastest university supercomputer in the world. It can run about 2^53 (about 13 quadrillion) instructions in a second. There are about 2^11 seconds in half an hour, so Blue Waters would run 2^64 instructions in about half an hour.
    Which one of the following is equal to lg* (2^64)?
    1. 64
    1. 5
    1. 6
    1. 65536

9. Which of these is considered the least run-time complexity?
    1. O(log log N)
    1. O(log* N)
    1. O(log N)
    1. O(1)

10. Which of the following best describes "path compression" as described in the video lessons to accelerate disjoint set operations? (Here we say "parent pointer" to mean whatever form of indirection is used to refer from a child to its parent; this could be a literal pointer or it could be an array index as in the lectures.)
    1. When the root of an element's node is found, all of the descendants of the root have their parent pointer set to the root.
    1. When traversing the up-tree from an element to its root, if any elements in the traversal (including the first element, but excluding the root itself) do not point directly to the root as their parent yet, they will have their parent pointer changed to point directly to the root.
    1. When the root of the up-tree containing an element is found, both the element and its parent will always have their parent pointers set to point to the root node.
    1. When the root of the up-tree containing an element is found, the element and all of its siblings that share the same parent have their parent pointers reset to point to the root node.

***

#### Answers 02
| Question | Answer |
| -------- | ------ |
| 1 | i |
| 2 | i |
| 3 | i |
| 4 | iii |
| 5 | i |
| 6 | iv |
| 7 | iv |
| 8 | ii |
| 9 | iv |
| 10 | ii |

5. value stores id -(height + 1)
6. count the root too !

***

### Assignment 01

Modify the implementation of `DisjointSets::find(int i)` below so that it uses path compression during queries.

The DisjointSets class here models a collection of one or more disjoint sets of items. This is very similar to the professor's description of *up trees*; imagine that each set is a tree, where the root of the tree represents the set it belongs to, while other items in the same set refer to it (directly or indirectly). 

Given a DisjointSets instance `d`, the array `d.s` contains one `integer` for each item in the entire collection. Currently, this array is statically allocated with 256 integers, so the entire collection can involve at most 256 items. For any given item with index `i`, the value recorded at `d.s[i]` represents either the parent of item `i`, or a more distant ancestor of item `i`, or the root of the entire set that item `i` belongs to. If the value of `d.s[i]` is -1, then this means that item `i` is the root of its own set. 

The provided code for find does this much already:
1. The find function queries for the ultimate root of a given item, with index `i`.
2. If the array entry for index `i` is less than 0, then return `i`, as it is the root of its own set. (This is the base case.)
3. Otherwise, the array entry currently records an ancestor of node `i` in the tree, but not the root. So, recurse on the ancestor index. Assume that `find()` succeeds in recursion: it returns the root of this set. (This assumption would be the inductive hypothesis if you were writing a proof of correctness by induction.)
4. Return the root that was found. (This fulfills the assumption that was made when we recursed in the previous step.)

You need to add the path compression feature to this `find` function. This means you must record the information that was found recursively as an update to the array before the function returns. This optimizes subsequent calls to the function. 

In summary, after calling `find(i)` on one of the elements in the set, `i`, the find function should return the root index of the disjoint set (the index of its root element) and also update the `s` array to ensure that element `i` and every ancestor of `i` will refer directly to the root.

```c++
#include <iostream>

class DisjointSets {
public:
    int s[256];

    DisjointSets() { for (int i = 0; i < 256; i++) s[i] = -1; }

    int find(int i);
};

/* Modify the find() method below to
 * implement path compression so that
 * element i and all of its ancestors
 * in the up-tree refer directly to the
 * root after that initial call to find()
 * returns.
 */

int DisjointSets::find(int i) {
  if ( s[i] < 0 ) {
    return i;
  } else {
    return find(s[i]);
  }
}

int main() {
  DisjointSets d;

  d.s[1] = 3;
  d.s[3] = 5;
  d.s[5] = 7;
  d.s[7] = -1;

  std::cout << "d.find(3) = " << d.find(3) << std::endl;
  std::cout << "d.s(1) = " << d.s[1] << std::endl;
  std::cout << "d.s(3) = " << d.s[3] << std::endl;
  std::cout << "d.s(5) = " << d.s[5] << std::endl;
  std::cout << "d.s(7) = " << d.s[7] << std::endl;

  return 0;
}
```

***

#### Answer Assignment 01

Updated definition of `find`
```c++
int DisjointSets::find(int i) {
  if ( s[i] < 0 ) {
    return i;
  } else {
    int root = find(s[i]);
    s[i] = root;
    return root;
  }
}
```

***
