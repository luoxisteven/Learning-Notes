# AWS
- Compute
    - Amazon Elastic Compute Cloud (Amazon EC2)
        - Features
            - On-Demand, Pay-as-you-go
            - Inbound Traffic (Free), Charging Outbound Traffic
            - Using EBS (Elastic Block Store)
                - Scaleable without losing any data in the disk
                - But can not share with different EC2 instances
    - AWS Lightsail
        - Features
            - Subscription (More stable)
    - Lambda
        - Running Code without using server
        - How to use:
            - Use `API Gateway` to create an endpoint
            - Using `Certificate Manager` to create TLS/SSL Certificate and use customised domain
                - Adding the CNAME Record to your DNS to register the Certificate
                - CA (Certificate Authority)
                    - Let's Encrypt
                    - GlobalSign
                - SSL (Secure Sockets Layer) 
                    - Old and Obselete
                - TLS (Transport Layer Security)
                    - Mordern
        - Layers
            - Adding python package
    - App Runner
- Container
    - Docker
        - Creating an isolated enviornment for any application with containers
        - Image
            - `docker run` to compile `Dockerfile` to `Image`
            - Filesystem Layer
                - OS packages, dependency, version
            - Image layers stacked on top of each other
            - Union of read-only layers with a writable layer on top
        - Container
            - An isolated enviornment for any application
            - Able to expose endpoints
        - Registry
    - ECR (Elastic Container Registry)
        - Store and Distribute Images privately
    - ECS (Elastic Container Service)
        - Run Container
            1) AWS Fargate
                - Run Container without server
            2) EC2
        - Configure CNAME Record in DNS for Domain Customisation
- Cloud Storage
    - S3
        - Object Storage (Cloud Storage)
        - Key-Value Store (Key = object name, Value = object data + metadata)
        - Flat structure, but supports prefix-based naming to simulate folders/directories
    - S3 Glacier
        - Lower cost for data archiving and long-term backup
        - Infrequently accessed data, and lower speed access
    - EFS
        - Similar to a virtual hard disk
        - Mount an external hard drive (挂载一个外部硬盘)
        - Shared file storage (Across different EC2 instances)
- Database
    - RDS (Relational Database Service)
        - Aurora (Compatible with MySQL and PostgreSQL)
            - An optmized version of MySQL and PostgreSQL
            - Can connect Aurora using `mysql -h ...` and `psql -h ...`
        - MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server，IBM Db2
    - DocumentDB
        - compatible with MongoDB
    - ElastiCache
        - Cloud version of Cache (like Redis)
- Network
    - VPC
    - API Gateway
- Security, Identity, & Compliance
    - Identity and Access Management (IAM)
        - Authorization and Authentication
        - Notions
            - Polices (Permissions)
            - User Group
                - Having a certain numbers of predefined Polices
            - Users
                - Access Key
                - Secret Key (Only shown when creating it)
                - Setup through `aws configure` or use in API, or in AWS service
    - Cognito
        - WebApp's Authorization and Authentication
        - Embed JWT with WebApp's roles and permissions
- Kubernetes (k8s)
    - Cloud Service
        - Azure Kubernetes Service (AKS)
        - AWS Kubernetes Service (EKS)
        - Google Kubernetes Engine (GKE)
    - Application
        - A Full Sets of Application
        - Including backend, frontend, Pods, Deployments, Services
    - Pod
        - It is the smallest deployable unit
        - Can have one container (More common), or more than one container (Less common, shared resources)
        - Sharing IP, Shared Volumes (Storage Disk)
        - Sharing Lifecycles (when creation and destory)
        - Operating in the same node
    - Deployment
        - In the unit of Pod.
    - Node 
        - A node is corresponding to one virtual server.
        - Normally, node will be automatically created when using Kubernetes Cloud Service like AWS EKS / Azure AKS / GCP GKE.
        - Kubernetes Cluster（集群）
            └── Node 1（服务器 A）
                ├── Pod 1 → Container
                ├── Pod 2 → Container
                └── Pod 3 → Container
            └── Node 2（服务器 B）
                ├── Pod 4 → Container
                └── Pod 5 → Container
            └── Node 3（服务器 C）
                └── Pod 6 → Container
    - Command
        - Connect to aks cluster
            - `az aks get-credentials --resource-group zhhen-prod --name aks-zhhen-prod`
            - `az aks get-credentials --resource-group <your-rg> --name <your-aks-cluster>`
            - `aws eks update-kubeconfig --region <region> --name <eks-cluster-name>`
        - You can see the all contexts you have connected to
            - `kubectl config get-contexts`
        - You can check the current context
            - `kubectl config current-context`
        - You can switch between clusters/contexts
            - `kubectl config use-context <context-name>`
    - Testing
 