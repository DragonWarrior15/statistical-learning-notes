---
title: "C++"
---

### C++ Classes
C++ classes allow us to encapsulate data and associated functionality into a single object/unit/class.
Data and functionality are divided into two separate protections: public and private. Anything that can use our class is denoted by _client code_. Public members are accessible by the client code while the private members are only accessible within the class itself.
Private member names are ended with an `_` by convention.

### C++ Header File (.h)
A header file defines the interface to the class which includes:
* Declaration of all member variables
* Declaration of all member functions

It sort of provides an API to use the class in a client code, but now information on how the internals work.
Every header file will include `#pragma once` as a line of code and instructs the compiler to compile this file only once.

The syntax for declaration of a class in a header file will be
```c++
#pragma once
class Cube{
    public:
        double getVolume();
        double getSurfaceArea();
        void setLength(double length);
    private:
        double length_;
};
```

The code for implementation of the class will be in the corresponding cpp file
```c++
#include "Cube.h" // use quotes to denote that this is customer defined

double Cube::getVolume(){ // use the keyword Cube to denote which class this function belongs to
    return length_ * length_ * length_;
}

double Cube::getSurfaceArea(){
    return 6 * length_ * length_;
}

void Cube::setLength(double length){
    length_ = length;
}
```

Finally, the class can be used in another program as follows
```c++
#include "Cube.h" /* to allow the compiler to find Cube class
also, using quotes means the compile expects the header
file to be in the same directory as the cpp file */

int main(){
    Cube c;
    c.setLength(3.48);
    double volume = c.getVolume();
    std::cout << "Volume: " << volume << std::endl;
}
```
**When including a header file**, using `""` will force the compiler to look for the header in the same directory as the file being compiled, while using `<>` allows the compiler to look for the header file in the system wide directory path, which may be outside the current directory.
Never include a cpp file this way because the file is compiled separately and then linked with our main script. Each cpp file is separately compiled into a .o object and then linked together.
The header files are there for providing the type information of different classes and functions. Hence, it is not necessary to include the cpp file in the main program.
After all the files have been compiled and linked, we get a single compiled object that we can use to run our program.

### C++ Standard Library
The C++ Standard Library, often abbreviated as std, provides a set of commonly used functionality and data structures to build upon.
The `iostream` header includes operations for reading/writing to files and console itself, including `std::cout`.
All functionality used from the standard library will be part of the `standard` namespace. We use namespaces to avoid any conflicts between a standard and custom class. In the cube example above, we would want to have a dedicated namespace for the Cube class.
If a feature from a namespace is used often, we can import it into the global namespace with `using`
```c++
using std::cout;
```
and then we can simply use cout without any conflicts.

Cube can be a generic class type and maybe defined in other places as well. To separate our definition from others, we put it inside a namespace (uiuc). The code structure remains same as above with following modifications
```c++
// Cube.h
namespace uiuc{
    Class Cube{
        // same definition as above
    };
}

// Cube.cpp
namespace uiuc{
    double Cube::getVolume(){
        // same definition as above
    }
    // other definitions also remain same
}

// main.cpp
uiuc::Cube c; // instead of just Cube c;
```
This encapsulates the class in the namespace uiuc.

### Stack Memory
Every variable in C++ has a name, type, value and location in memory, the memory is allocated in the stack. The address can be obtained using the `&` operator.

Stack memory is associated with the current function and the memory's lifecycle is tied to the function. As soon as the function returns or ends, the stack memory corresponding to that function is also released, free to be used by other programs.
Stack memory always starts from high addresses and grows downwards towards 0.

### Pointer
A pointer is simply a variable that stores the memory address of a variable. It is an indirection of the data that we can follow to reach the location where the particular variable pointed by this pointer is stored. Its type is same as that of the variable it points to, and is declared using the `*` operator. The same operator also allows to get the value of the variable pointed to by the pointer.

```c++
int num = 42;
int * p = &num; // a pointer to a variable of type int

std::cout << p << std::endl; // prints the address of the variable num
std::cout << *p << std::endl; // prints the value of the variable num, 42
*p = 4; // changes the value of num to 4, p still stores the address of num
```

Undefined behaviour can occur if we return the address of a local variable. The following example illustrates this
```c++
#include <iostream>
#include "Cube.h"
using uiuc::Cube;

Cube *CreateUnitCube() {
  Cube cube;
  cube.setLength(15);
  return &cube;
}

int main() {
  Cube *c = CreateUnitCube();
  someOtherFunction();
  double a = c->getSurfaceArea();
  std::cout << "Surface Area: " << a << std::endl;
  double v = c->getVolume();
  std::cout << "Volume: " << v << std::endl;
  return 0;
}
```

Note that the stack frame of CreateUnitCube is allocated below that of main. After the function returns, we know that the stack frame is released, and the OS/program can do anything with that memory, possibly overwrite it. The outputs of main, surface area and volume turn out to be 0 even though the cube length was 15. This output will vary depending on a multitude of factors. Long story short, never return the address of a local variable in order to avoid any undefined behaviour.

### Heap memory
Heap memory allows us to create memory that is completely independent of the functions stack memory/function lifecycle. **If memory needs to exist longer than the lifecycle of the function, it is imperative that we use heap memory.**
This memory can be created using the `new` operator. Remember that this returns the location pointing to the start of the allocated memory and is not the data type itself. When using the `new` keyword, C++ will
1. Allocate memory for our data type/data structure
2. Initialize the data structure
3. Return a pointer to the start of the data structure

Remember that the pointer that stores the address resides on the stack of the function it is part of. The memory is only made available to the operating system when the memory is released with the `delete` keywords. This procedure of heap allocation is similar to `malloc` and `free` in C. Heap memory allocation starts at a lower address and grows up.

#### `nullptr`
`nullptr` is a pointer that points to a special location on the system 0x0, and the pointer is also said to be pointing to nowhere. This location is reserved by the system but never used, and any access to this will generate a segmentation fault. Calls to delete 0x0 are ignored.
After releasing a memory using `delete` it is a good idea to make the pointer pointing to that releases memory, a null pointer. This is important because after releasing the memory, the pointer still points to it and the memory can be overwritten later on during the course of the program. Such a dangling pointer can become the cause of undefined behaviour.
```c++
int *p = new int; // allocate memory on heap
*p = 42 // initialize, or use somewhere else
// some more operations with this pointer
delete p; // release the memory
p = nullptr; // make p a null pointer to evade undefined behaviour
```
This must be a standard practice to be followed for every such allocation of memory. Setting to `nullptr` is also desriable since `delete` has no effect on a `nullptr` and in case we try to release the same memory twice, the program will not crash or give undersired results.

Dereferencing deleted memory can also cause segmentation faults or security vulnerabilities. Hence, dereferencing a `nullptr` is desirable to have an error that can be solved for without a securtiy risk.

#### `->` operator
Whenever we have a pointer to a class object, `->` allows us to access any member function of that object through the pointer. The following two statements are equivalent
```c++
Cube * c;
(*c).getVolume();
c->getVolume();
```
The `->` operator allows a much more clean way to access the member variables/functions.

#### Arrays in Heap
```c++
int *p = new int[3];
delete[] p;
```
allocates and frees an array of integers. The same syntax can be applied to any data type/class.

### Constructors and Deconstructors
#### Constructor
When an instance of a class is created, the class constructor sets up the initial state of the object. If we dont provide one, C++ automatically sets up a default constructor. The automatic default constructor will only initialize all the member variables to their default values. For primitive types, the default value is unknown and hence the default constructor is not always useful in practice.
#### Custom Default Constructor
A custom default constructor is a function and has the following properties
1. It is a member function with the same name as the class
2. The function takes zero parameters
3. The function has no return type
4. If any custom constructor is defined (with parameters or without), no automatic default constructor is defined

On point number 4, if we create an instance of the class with a constructor declaration that is not defined, a fatal error is thrown by the compiler saying no matching constructor was found, since the default constructor is not available anymore.

An examle would be
```c++
// Cube.h
namespace uiuc{
    class Cube{
        public:
            Cube();
            // .. remaining implementation is same as earlier definition
    }
}
// Cube.cpp
namespace uiuc{
    Cube::Cube(){
        length_ = 1;
    }
    // .. remaining implementation is same as earlier definition
}
```

#### Custom Non Default Constructor
We can also define custom non default constructors that require client code to supply arguments
```c++
Cube::Cube(double length){
    length_ = length;
}
```

This definition allows us to define multiple constructor definitions for the same class which can differ based on the number of arguments
```c++
// Cube.h
namespace uiuc{
    class Cube{
        public:
            Cube(); // custom default constructor
            Cube(double length); // one argument constructor
            // .. remaining declaration same
    }
}
// Cube.cpp
namespace uiuc{
    Cube::Cube(){
        length_ = 1;
    }
    Cube::Cube(double length){
        length_ = length;
    }
    // .. remaining declaration same
}
```
Which constructor is used will depend on the number of arguments provided when declaring the class
```c++
int main(){
    uiuc::Cube c1; // length_ will be 1, uses the custom default constructor
    uiuc::Cube c2(5); // length will be 5, uses the custom constructor
}
```

#### Copy Constructor
A copy constructor in C++ is a special constructor that allows making a copy of an existing object. Similar to the class contructor discussed above, C++ defines a default copy constructor. This automatically copies the contents of all member variables. Although this suffices in most cases, we also have the ability to define a custom copy constructor.
**A copy constructor is invoked when creating a new object.**

#### Custom Copy Constructor
Its definition includes a single argument that is a constant reference to an object of the same type as the class.
```c++
Cube::Cube(const Cube & obj){
    length_ = obj.length_;
    // in this case, the automatic copy constructor would do the exact same thing
}
```

Often, copy constructors are invoked automatically when
1. Passing an object as a parameter to a function (by value)
    The class object is copied into the stack frame of the called function
1. Returning an object from a function (by value)
    The class object is copied into the stack frame of the calling function
1. Initializing a **new** object
    Say from the value returned form a function, see the second call of copy constructor below

```c++
Cube foo(){
    Cube c; // calls the default constructor
    return c; // calls the copy constructor for the first time
    // since the value is copied into the stack frame of main
}
int main(){
    Cube c2 = foo(); // calls the copy constructor a second time
    // since the value returned by foo is copied to c2
    Cube c3 = c2; // only calls the copy constructor and not the default constructor
    Cube c4; // default constructor is called
    c4 = c2; // nothing is called since both objects are already "created"
    // this uses the automatic assignment operator instead to copy the contents
    return 0;
}
```

#### Assignment Operator
As one can guess by now, C++ provides an assignment operator that can copy the contents of an existing class object to another existing class object. In most cases this will mean copying of values of member objects. For custom cases, we do have the option to define this operator for specific tasks like making pointers to the same memory location, heap allocation etc.

A custom assignment operator has the following properties
1. Is a **public** member of the class
1. Has the function name `operator=`
1. Has a return value of a reference of the class' type
1. Has exactly one argument, which is a const reference of the class' type

```c++
Cube & Cube::operator=(const Cube & obj){
    length_ = obj.length_;
    return *this;
}
```

#### Destructors
As with constructors, an automatic default destructor is assigned to the class that will automatically call the default destructors of all the member objects of the class.

**A destructor should not be called directly**. Instead, the compiler will put specific calls depending on where the memory is allocated. If the object is allocated on the stack, the destructor is automatically called when the function returns. If the object is allocated on heap, the destructor is automatically called when the heap memory is released using the `delete` operator.

#### Custom Destructor
As with constructors, we can also create a custom destructor. It has the the following properties
* A custom destructor is a member function
* This function is the name of the class preceded by a `~`
* All destructors have 0 arguments without any return type

```c++
Cube::~Cube(){
    // do tasks like releasing allocated memory on the heap
}; // custom destrucutor definition
```
Destructors are critical when we need to release memiry that is allocated on heap, external files or shared memory.

### Variable Storage
A Variable can be stored in three different ways in the memory
1. Direct Storage
    This is the default storage method for storing variables in the memory.
    * The **type** of variable has no modifiers
    * The object takes up exactly its size in the memory
    ```c++
    Cube c; int i; // are some examples
    ```
2. Storage by pointer
    * The type of variable is modified by an `*`
    * The pointer takes a memory address width of memory (example 64 bits on a 64-bit system)
    * The pointer _points_ to the allocated space of the object
    ```c++
    Cube *c; int *i; // are some examples
    ```
3. Storage by reference
    * A reference is an **alias** to an existing memory and is denoted in the type by an ampersand `&`
    * A reference variable does not store memory itself and is simply an alias to another varaible
    * The _alias_ (variable to alias) must be assigned when the _variable_ (the alias we are creating) is initialized
    ```c++
    Cube cube;
    Cube &c = cube; // alias is declared at the time of initialization
    // c is the alias for an already existing variable cube
    //  Cube &c2; // ! is illegal and will not work as no alias is assigned when initializing
    ```
    * Changing the variable through its name or the alias is the same thing
    * The alias stores no extra memory since it is just an alias

#### Passing Arguments to Function
Similar to variable storage, we can pass arguments to function in three ways
* Pass by value (default)
    The variable is passed by value and the original variable is not modified by the function, the copy constructor will be called to create a copy on the function stack
* Pass by pointer (using `*`)
    A pointer to the variable is passed and the function can modify the original variable via this
* Pass by reference (using `&`)
    The alias is just a different name for the variable, no copy of the variable will be created in the function stack

#### Returning from a function
Similar to variable storage and passing arguments to function, we can return by
* value (default)
* pointer (returning the address of memory of the variable)
* reference (returning an alias to a variable)

As always, **returning the reference or address of a variable in the function stack will cause undefined behaviour** and the compiler should usually warn about this at compile time.

### Range based for loops
Range based for loops allow iteration over all objects in a container. This is useful because we will always iterate over valid objects in the array and avoid segmentation faults to some extent. The syntax is
```c++
for ( temporary variable declaration : container ) { loop body }
```
An important point to note about the temporary variable is that it just gets a copy of the actual value of the container item and any changes made to this variable will not affect the item in the container.
```c++
std::vector<int> int_list;
int_list.push_back(1);
int_list.push_back(2);
int_list.push_back(3);
// type 1 of the loop, using a copy of the element
for(int x: int_list){
    x = 99; // no changes are made to the elements of the list
}
// type 2 of the loop, using an alias
for (int &x : int_list) {
  // This version of the loop will modify each item directly, by reference!
  x = 99;
}
// type 3 of the loop, using an alias of contant type
for (const int &x : int_list) {
    // some operation on the elements
    // x = 99; // throws an error
}
```

Type 3 of the loop which uses an alias of the constant type is useful when iterating over objects of large size in a read only fashion, and using the alias will avoid creating copies of the entire objects.

### Template Types and `std::vector`
A template type is a special type that can take different types when the type is initialized. An example is the `std::vector` which can be initialize for different types
```c++
std::vector<char>; // initializes a vector of characters
std::vector<uiuc::Cube> // initializes a vextor of type Cube
```

`std::vector` is a standard library class that provides a dynamically growing array with a _templated_ type. Its key operations are

| Operation | Code |
| --------- | ---- |
| Defined in | `#include <vector>` |
| Initialization | `std::vector<T> t;` |
| Add to back of array | `::push_back(T);` |
| Access specific element | `::operator[](unsigned pos);` |
| Number of elements | `::size()` |

where `T` denotes the type like `int` or `uiuc::Cube`. The type goes in the angular brackets after the keyword vector.

#### Templated Functions
C++ allows using templated variables for use in classes or functions. The template variable is defined by declaring it before the class or function.
```c++
// usage in a class
template <typename T>
class List{
    //...
    private:
        T data_;
}
// usage in a function
template <typename T>
T max(T a, T b){
    if(a > b){return a;}
    return b;
}
```

Template variables are checked at compile time which means that errors can be caught before running the program. This is also called compile time binding.

### Inheritance
A **base** class is a generic form of a specialized **derived** class. The derived class can inherit from the base class. Assume that the Cube class inherits from the Shape class. Then
```c++
Class Shape{
    public:
        Shape();
        Shape(double width);
        double getWidth() const;

    private:
        double width_
}
namespace uiuc{
    Class Cube : public Shape{
        public:
            Cube(double width, Color colour);
            double getVolume() const;

        private:
            Color colour;
    }
}
```

The variable `width_` will also be available in class Cube and accessible via the method `getWidth` already defined in the Shape class. Functions specific to and defined in Cube class are not available in the Shape class.

When initializing a derived class, the base class must be initialized. By default, it can use the default constructor of the base class. However, custom constructor can be used with an **initialzation list**. The syntax will be as follows
```c++
// definition in the cpp file
namespace uiuc{
    // the following syntax directs C++ to first call Shape(double width) contructor
    // with the parameter width, then execute the constructor code specific to Cube
    Cube::Cube(double width, Color colour) : Shape(width){
        _color = colour;
    }
    double getVolume() const{
        // width is a private member of shape, hence unable to directly access it
        // instead we use the publicly available accessor in the Shape class
        return getVolume() * getVolume() * getVolume();
    }
}
```

**Access control**: When a base class is inherited, the derived class can access **all public variables and methods** but **not the private variables and methods** of the base class.

### Arrays
Arrays store data in sequential blocks of memory. The array indexing starts from 0, and the entire block array is stored in a single block of memory. We can create an array of fixed size as
```c++
int arr[3] = {1, 2, 3};
```
We can also declare the array and initialize it later by accessing individual elements by the index and assigning them values.

In c++, we have the `sizeof` function that can be used to calculate the size in bytes of any data type (`int` or a custom class).

Arrays have a few limitations
* All elements of the array must be of the same type. Hence, we can calculate how may bytes away any element is simply by counting the offset and multiplying by the size of an element of the array. The elements of an array need not be of the primitive type only, but can be of a custom class as well.
* Arrays have a fixed capacity, and the capacity decides the maximum number of elements that can be stored in the array.
    * The **size** of an array is the current number of elements stored in the array.
    * The **capacity** of an array is the maximum number of elements that can be stored in the array.
    * `vectors` also have a fixed capacity, but whenever a new elements needs to be added, the vector automatically resizes itslef.

Usually when resizing an array, the strategy used is to double the capacity each time when the size is full. This way, total operations used when growing an array from size 2 to size n is O(n) and the amortized time per element (total n elements) will be O(1).

### Linked Memory
Linked memory stores data along with the location of the next list node in the memory. Thus, every element of this linked list is linked together by pointers, and every element is a combination of the data stored along with a pointer to the location of the next data node.

Due to its structure, the elements of a linked list need not be sequentially placed in memory. Furthermore, adding an element to a linked list is simply adding a new element to the end of the list, and this allows a linked list to be as large as one requires.

However, since the elements are not stored in a sequential manner, accessing any element at a given index will require traversing the entire list upto that index.

Sample code for a linked list element
```c++
template <Typename T>
class ListNode{
    public:
        T & data;
        ListNode * next;
        ListNode(T & data): data(data), next(nullptr) {};
};
```

Linked list is formed by linking together 0 or more elements. To store a linked list we store a pointer to the head/first element of the linked list, and the last element is found by checking whether the next pointer of that element points to the nullptr.

Array and linked list operations compared

| Operation | Array | Linked List |
| --------- | ----- | ----------- |
| Element access | O(1) | O(n) |
| Resizing | O(n) | O(1) |

Hence, there is a tradeoff between element access and resizing. The data structure should be chosen according to which operation will be performed more frequently.

### `std::pair`
C++ provides a useful utility to create pairs of objects by clubbing two different data types together into a single object (thus saving the effor to make a custom class for this purpose). The syntax for creating a pair is
```c++
#include <utility>
std::pair<std::string, int> myPair;
myPair.first = "a string element";
myPair.second = 42;
```

It is also possible to directly make a pair using the helper function `make_pair`
```c++
std::pair<std::string, int> myPair;
myPair = std::make_pair("another string", 56);
```

Some implementations of an unordered map discussed below utilise pairs in their internal representation.

### `std::unordered_map`
These are different from `std::map` because they are unordered. This means that when iterating over the keys of the map, there is no particular order. The key difference between the two can be summarized as

| Map Type | Lookup | Ordering |
| -------- | ------ | -------- |
| `std::unordered_map` | O(1) | Unordered |
| `std::map` | O(log n) | Ordered, stored as tree |

The syntax to declare an unordered map is
```c++
std::unordered_map<Template type for key, Template type for value> name_of_map;
std::unordered_map<std::string, int> count_map; // can be used to store count of occurrences of strings
```

Use the `[]` operator to add keys and retrieve values (referencing any key with `[]` operator will automatically create an entry for the same in the map, somewhat corrupting it)
```c++
count_map["five"] = 1;
std::cout << count_map["five"] << std::endl;
```

The size operator can be used to get the total entries in the map
```c++
std::cout << "total entries in the map " << count_map.size() << std::endl;
```

To check for existence of a key in the map, we can use the count operator. It will return a 1 or 0 indicating the existence of the key, and should not be confused with counting the keys in the map.
```c++
if(count_map.count("five")){
    std::cout << "key five exists in map" << std::endl;
}else{
    std::cout << "key five does not exist in map" << std::endl;
}
```
This is a useful function if we don't wont to corrupt the map with new entries since a lookup with the `[]` operator will create the entry in the map.

The `find` function returns an iterator which is a pair type corresponding to the key value pair. In case the key does not exist in the map, the `end()` iterator of the map is returned.

