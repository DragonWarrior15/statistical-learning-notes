---
title: Docker
---

## Containers
The shipping industry standardized the container sizes, no matter what are the sizes of the user materials to be transported. This standardization resulted in upstream benefits of all the transportations to be standardized as well. Now, the only choice left is to determine what type of transportation to choose, land, air or water. All the transport media in a given mode of transport are already pre built to specific container sizes, which means improved efficiency and faster construction of these media.

Similarly, digital container exist, making the softwares portable to make them easy to run on any platform. This improves the deployment of a developed software from the developers machine to a virtual cloud, and across staging and production environments efficiently.

A container engine virtualizes the operating system. It is light-weight, fast, isolated, portable, secure and requires less memory space. Binaries/libraries within the container enable the apps to run, and a single machine can host multiple containers.

Containers are platform, operating system, and programming language independent.

{% include image.html url="notes/linux/images/container_arch.png" description="Container Architecture" img_classes="notes-img" %}

## Docker
Docker is the most popular software to run containerized applications. Its written in Go language and uses Linux kernel's features to deliver functionality. It uses namespaces technology to provide isolated workspace called a container. It creates a set of namespaces for every container and each aspect runs in a separate namespace with access limited to that namespace.

### `Dockerfile`
Docker file is a text file containing the instructions needed to create an image
* It must always begin with a `FROM` command which defines the base image
* `CMD` is to run a shell command
	* `CMD["echo", "Hello World!"]` for example to print Hello World.

### Docker commands
* `docker build .` to build the image from the current directory dockerfile
	`docker build -t my-app:v1 .` where `-t` is used to provide a tag, which is `my-app` (the repository name) followed by the version, and the last `.` is to refer to the current directory
* once the image is build, we can containerize it using `docker run` followed by the image name
	* if we pull an image from a registry, we can directly run a container from the image using the above command
* `docker push` and `docker pull` are used to push and pull images from a configured registry

### Docker objects
* Dockerfile
	* a text file containing the instructions to create an image
* Image
* Container
* Network
* Storage volumes
* Plugins, add-ons
