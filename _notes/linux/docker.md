---
title: Docker
---

## Containers
The shipping industry standardized the container sizes, no matter what are the sizes of the user materials to be transported. This standardization resulted in upstream benefits of all the transportations to be standardized as well. Now, the only choice left is to determine what type of transportation to choose, land, air or water. All the transport media in a given mode of transport are already pre built to specific container sizes, which means improved efficiency and faster construction of these media.

Similarly, digital container exist, making the softwares portable to make them easy to run on any platform. This improves the deployment of a developed software from the developers machine to a virtual cloud, and across staging and production environments efficiently.

A container engine virtualizes the operating system. It is light-weight, fast, isolated, portable, secure and requires less memory space. Binaries/libraries within the container enable the apps to run, and a single machine can host multiple containers.

Containers are platform, operating system, and programming language independent.

{% include image.html url="notes/linux/images/container_arch.png" description="Container Architecture" img_classes="notes-img-40" %}

## Docker
Docker is the most popular software to run containerized applications. Its written in Go language and uses Linux kernel's features to deliver functionality. It uses namespaces technology to provide isolated workspace called a container. It creates a set of namespaces for every container and each aspect runs in a separate namespace with access limited to that namespace.

### Docker objects
* **Dockerfile**
    * a text file containing the instructions to create an image
* **Image**
    * its a read only template with instructions for creating a Docker container
    * built using the instructions in the dockerfile, a new read only image layer is created for each instruction
    * when the image is run as a container, a writeable layer is added
    * layers can be shared between images to save on disk space and network bandwidth
    * naming convention is `hostname/repository:tag`
* **Container**
    * is a runnable instance of an image
    * docker cli can be used to create/delete and start/stop a container
    * can connect to multiple networks, attach storage, and create a new image based on the current container state
    * a container is well isolated from other containers and the host machine
    * docker uses volumes and bind mounts to persist data even after a container stops
    * storage plugins can be used to connect to external storage/platforms
    * networks are used to isolate container communications

### `Dockerfile`
Docker file is a text file containing the instructions needed to create an image
* It must always begin with a `FROM` command which defines the base image
* `RUN` is to execute arbitrary commands
* `CMD` is to run a shell command
    * `CMD["echo", "Hello World!"]` for example to print Hello World.
    * it is the default command for container execution
    * a docker file should have a single `CMD` command
    * in case of multiple `CMD` commands, only the last one will take effect
* `WORKDIR` is to set the work directory for subsequent instructions, to simplify path references
* Its typically followed by a `COPY` instruction to copy a file from the local directory/machine to the container, can be a `requirements.txt` file for installing dependencies
    * If we are writing code in a particular directory, also need to copy the folder's entire contents into the container for executing those files, this is typically done post installation of dependencies
* `EXPOSE {port num}` can be used to expose a port that the container will listen on at runtime
* Use `LABEL` to add metadata to the image
    * `LABEL version="1.0"`
    * `LABEL description="docker image desc"`
    * `LABEL maintainer="Your Name"`
* `HEALTHCHECK` is optional, and can be used to ensure if the container is running correctly
    * `HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -fs http://localhost:$PORT || exit 1`
    * `$PORT` is an environment variable referring to the port number the container will listen on
* For security purposes, set a non-root user for subsequent instructions using `USER`
    * `USER node` will set a user named `node` to run the subsequent commands

### Docker commands
* `docker build .` to build the image from the current directory dockerfile
    * `docker build -t my-app:v1 .` where `-t` is used to provide a tag, which is `my-app` (the repository name) followed by the version, and the last `.` is to refer to the current directory
* once the image is build, we can containerize it using `docker run` followed by the image name
    * if we pull an image from a registry, we can directly run a container from the image using the above command
    * use `-p` to publish a port
* `docker push` and `docker pull` are used to push and pull images from a configured registry
* `docker images` to list all the images
* `docker ps` to list the containers

## References
* [Coursera: Introduction to Containers w/ Docker, Kubernetes & OpenShift](https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift)
