---
title: Kubernetes
---

## Kubernetes
Also known as K8s, its an open source system for automating deployment, scaling, and management of containerized applications.

It supports a wide variety of applications like stateful, stateless and data intensive apps.

Important concepts related to kubernetes
* Pods and workloads
    * Pods are smalles deployable object in kubernetes and the higher level abstractions to run workloads
* Services
    * A service exposes an application running on a set of Pods
    * Each Pod is assigned a unique IP address, and a set of Pods have a single DNS name
* Storage
    * Both temporary and persistent storage are supported
* Configuration
    * Provisions resources that kubernetes provides for configuring Pods
* Security
    * Security for cloud native workloads enforces security for Pod and API access
* Policies
    * Create policies for groups of resources helps ensure that Pods match to the nodes so that the kubelet can find them and run the Pod
* Schedule, Eviction
    * Runs and proactively terminates one or more Pods on resource starved nodes
* Preemption
    * Terminates lower priority Pods so that the higher priority ones can run on nodes
* Administration
    * Management details necessary to administer a kubernetes cluster
* Automated rollouts and rollbacks
    * progressively roll out the changes (say one Pod at a time) so that the service is always running and never down
* Storage orchestration
    * Automatically mounts the chosen storage system, whether from local, network or public cloud
* Horizontal scaling
    * automatically, based on metrics or via commands
* Automated bin packing
* Secret and configuration management
    * deploys and updates secrets/configuration without rebuilding images
* Self-healing
    * exposes containers to clients only if healthy and running
    * restarts, replaces, reschedules and kills failing or unresponsive containers
* Load balancing

### Kubernetes control plane
A deployment of kubernetes is called a kubernetes cluster. Its a cluster of nodes that run a containerized application. Each cluster has one master node, the kubernetes control plane, and one or more worker nodes.

{% include image.html url="notes/linux/images/kubernetes_worker_nodes.png" description="Kubernetes Worker Nodes" img_classes="notes-img" %}

Nodes are not created by kubernetes itself, but by the cloud provider.

The API is exposed by the kubernetes-api-server. It serves as the front end for the control plane.

`etcd` is highly available, distributed key-value store that contains all the cluster data and configurations. It stores deployment configuration data, the desired state and the metadata in a way that its accessible in a common location.

`kube-scheduler` assigns newly created Pods to nodes, and decides where the workload should run within the cluster. It selects the optimal node based on kubernetes scheduling algorithms and available resources.

#### Nodes
Nodes are the worker machines in a kubernetes cluster, and maybe virtual or physical. They are managed by the control plane. They contain the necessary services needed to run applications. Nodes include Pods, which are the smallest deployment units of a kubernetes cluster. Each node can run multiple containers. Containers share all the resouces of a node.

#### Kubelet
Communicates with the API server to ensure that Pods and their containers are running. It reports the health status of the Pods to the control plane.

`container runtime` is configurable, with docker being a popular choice.

#### Namespaces
Namespaces provide a mechanism for isolating groups of resources within a single cluster. Namespaces segregate cluster by team, project etc.

Namespace provides a scope for object names, each object having a name. Names are unique for a resource type within a namespace.

#### Pods
Pods are the simplest unit in kubernetes and can run one or more containers. Its specs are defined using a YAML format. See an example Pod spec below:

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: nginx
spec:
    containers:
    - name: nginx
      image: nginx:1.7.9
      ports:
      - containerPort: 80
```

A Pod spec must contain at least one container.

#### ReplicaSet
A replicaset is a set of identical running replicas of a Pod for horizontal scaling. The yaml specs for a replicaset are slightly different from that of a Pod.

```yaml
apiVersion: v1
kind: ReplicaSet # is specified as a Pod in Pods yaml
metadata:
    name: nginx-replicaset
    labels:
        app: nginx
spec:
    replicas: 3 # number of replicas at any given time
    # if a Pod dies, a new is created to match this number
    selector:
        matchLabels:
            app: nginx
    template:
        metadata:
            labels:
                app: nginx # matches the selector label
        spec:
            containers:
            - name: nginx
              image: nginx:1.7.9
              ports:
              - containerPort: 80
```

Generally encapsulated by a deployment.

#### Deployment
A deployment is a higher level object that provides updates for Pods and replicasets.
Deployments run multiple replicas of an application and are suitable for stateless applications.

```yaml
apiVersion: v1
kind: Deployment # is specified as a Pod in Pods yaml
metadata:
    name: nginx-deployment
    labels:
        app: nginx
# rest is same as a replicaset
spec:
    replicas: 3 # number of replicas at any given time
    # if a Pod dies, a new is created to match this number
    selector:
        matchLabels:
            app: nginx
    template:
        metadata:
            labels:
                app: nginx # matches the selector label
        spec:
            containers:
            - name: nginx
              image: nginx:1.7.9
              ports:
              - containerPort: 80
```

Rolling updates are applied by scaling up the Pods of the new version to the appropriate number, and scaling down the Pods of old version to zero. This is not a feature of replicaset.

#### Service
Service is a REST object like Pods, and acts a logical abstraction for a set of Pods in a cluster. It acts as a load balancer across the Pods. A service is assigned a unique IP addresss for accessing applications deployed on Pods.

```
Client -> Service -> Pod(selects a Pod from the set to direct the client request to)
```

Service eliminates the need for a separate discovery process. A service is needed because
* Pods in a cluster a volatile, they can be created or destroyed based on demand and resources
* The volatility leads to discovery issues because of changing IP addresses
* A service keeps track of the changes and exposes a single IP address or DNS name
* A service utilizes selectors to target a set of Pods

There are four types of services
* **ClusterIP**
    * Its the default and most common service type
    * Is assigned a cluster-internal IP address to the ClusterIP Service that makes the Service only reachable within the cluster
    * Cannot make requests to Service (Pods) from outside the cluster
    * ClusterIP address is set in the Service definition file
    * Provides inter-service communication within the cluster
* **NodePort**
    * Is an extension of ClusterIP Service
    * Creates and routes the incoming requests automatically to the ClusterIP Service
    * Exposes the Service on each Node's IP address at a static port
    * Exposes a single Service, with no load-balancing requirements for multiple services
* **External Load Balancer (ELB)**
    * An extension of the NodePort Service, an ELB creates NodePort and ClusterIP Services automatically
    * Integrates and automatically directs traffic to the NodePort Service with a cloud provider's ELB
    * To expose a Service to the Internet, a new ELB with an IP address is required, where the cloud provider's ELB can be used to host the cluster
* **External Name**
    * Maps to a DNS name and not to any selector
    * Requires the `spec.externalName` parameter
    * Maps the Service to the contents of the externalName field that returns a CNAME record and its value
    * Used to create a Service that represents an external storage and enable Pods from different namespaces to talk to each other, the frontend and backend of an app for instance

#### Ingress
It is an API object (combined with a controller) that provides routing rules to manage external users' access to multiple services in a Kubernetes cluster.
In production, Ingress exposes applications to the Internet via port 80 (HTTP) or port 443 (HTTPS). An ELB is expensive and managed outside the cluster, while the cluster monitors Ingress.

#### DaemonSet
* Is an object that makes sure that Nodes run a copy of a Pod
* As Nodes are added to a cluster, Pods are added to the Nodes
* Pods are garbage collected when removed from a cluster
* If you delete a DaemonSet, all Pods are removed
* Ideally used for storage, logs and monitoring Nodes

#### StatefulSet
Its an object that manages stateful applications, by managing the deployment and scaling of the Pods.
It also provides guarantees about the ordering and uniqueness of the Pods. A sticky identity is maintained for each of the Pods. It also provides persistent storage volumes for the workloads.

#### Job
Its an object that created Pods and tracks its completion process. Jobs are retried until they are completed, and deleting a Job removes the created Pods. Suspending a Job will also delete its active Pods until the Job resumes.
A Job can run several Pods in parallel. A CronJob is regularly used to create Jobs on an iterative schedule.

## `kubectl`
Is the Kubernetes CLI (Kube Command Tool Line). Helps to deploy applications, inspect and manage cluster resources, view logs etc. Key command types are
* Imperative commands
    * easiest to learn
    * no audit trail
    * useful for testing and development
    * The commands follow the structure below
      ```
      kubectl [command] [type] [name] [flags]
      ```
      where
      * command: operation, like create/get/apply/delete
      * type: resource type, like pod/deployment/replicaset
      * name: resource name (if applicable)
      * flags: special options or modifiers that override default values
* Imperative object configuration
    * must contain a full definition of the objects in YAML or JSON
    * `kubectl create -f nginx.yaml`
    * configuraiton templates help replicate identical results
* Declarative object configuration

Some common command examples
```sh
# get commands
kubectl get services
kubectl get pods -all-namespaces
kubectl get deployment my-deployment
kubectl get pods

# apply commands to create resources
kubectl apply -f file.yaml
kubectl apply -f folder/

# scale commands for replicas
kubectl scale --replicas=3 rs/foo
kubectl scale --replicas=3 -f file.yaml
```

## References
* [Coursera: Introduction to Containers w/ Docker, Kubernetes & OpenShift](https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift)
