# Reading 2: AWS Architecture Blog - Compute Abstractions on AWS: A Visual Story

[Resource: Compute Abstractions on AWS: A Visual Story](https://aws.amazon.com/blogs/architecture/compute-abstractions-on-aws-a-visual-story/)

**1. Explain the levels of abstraction in AWS to someone without a technical background:**
- AWS provides different levels of computing services that can be thought of as layers. Imagine it like building blocks:

  - **Instances**: These are like virtual computers you can use to run your software. You have control over everything on them, like your own computer.

  - **Containers**: Think of these as smaller, self-contained pieces of software that run on instances. They're like apps on your smartphone. They're more efficient and portable.

  - **Lambda**: This is like a magical service. You don't need to worry about instances or containers; you just give it your code, and it runs when needed. It's like hiring a chef to cook when you're hungry without dealing with the kitchen.

  - **Bare Metal**: This is like having your own private server in the cloud. It's for when you need to do something really specific and want full control.

  - **Fargate**: Imagine this as a restaurant where you order food, and they bring it to your table. You don't see the kitchen or worry about cooking; you just enjoy your meal.

**2. What are the control plane and data plane responsible for in container abstraction:**
- **Control Plane**: Think of it as the manager of a restaurant. It decides what dishes to serve, how many tables to set, and when to take orders. In AWS, it's responsible for managing and organizing containers.

- **Data Plane**: This is like the kitchen in a restaurant. It's where the actual cooking happens. In AWS, it's responsible for providing resources (like CPU and memory) for containers to run and connect to the network.

**3. Where does AWS Lambda fall in the layers of abstraction and what makes it so special:**
- **AWS Lambda** sits at the highest level of abstraction. It's like a food delivery service; you tell them what you want to eat (your code), and they bring it to your door when you're hungry (when an event triggers it). What makes it special is that you don't need to worry about the kitchen (infrastructure). AWS handles everything, so you focus only on your code. It's great for saving time and money, especially for small tasks or when you want to respond quickly to events.
