---
id: chapter-2-ros-communication
title: ROS 2 Communication Primitives
sidebar_position: 2
---

# ROS 2 Communication Primitives

## Introduction: Building on ROS 2 Concepts

In the previous chapter, we established ROS 2 as the "nervous system" of a robot and introduced the basic communication patterns. Now we'll dive deeper into how nodes, topics, and services enable distributed robot control, exploring the technical details and practical applications of these communication primitives.

## Nodes: The Computational Units of ROS 2

Nodes are the fundamental building blocks of any ROS 2 system. Think of a node as a single process that performs a specific computation. In a robotic system, you might have dozens or even hundreds of nodes working together to achieve complex behaviors.

### Node Characteristics

Each node in ROS 2 has several important characteristics:

- **Independence**: Nodes run independently of each other, meaning the failure of one node doesn't necessarily bring down the entire system
- **Language Agnostic**: Nodes can be written in different programming languages (C++, Python, Rust, etc.) and still communicate seamlessly
- **Distributed**: Nodes can run on the same machine or on different machines connected via a network
- **Specialized**: Each node typically performs a specific function, following the Unix philosophy of doing one thing well

### Node Lifecycle

A typical ROS 2 node goes through several lifecycle stages:

1. **Initialization**: The node starts up and initializes its parameters and interfaces
2. **Activation**: The node becomes active and begins processing data
3. **Running**: The node performs its primary function, publishing and subscribing to topics, offering or calling services
4. **Shutdown**: The node gracefully terminates and cleans up resources

### Example Node Types in a Humanoid Robot

In a humanoid robot system, you might find nodes such as:

- **Sensor Drivers**: Nodes that interface with hardware sensors (cameras, IMUs, joint encoders)
- **Perception Nodes**: Nodes that process sensor data to detect objects, recognize faces, or understand speech
- **Planning Nodes**: Nodes that generate motion plans, path plans, or task plans
- **Control Nodes**: Nodes that execute low-level control of actuators and joints
- **Behavior Nodes**: Nodes that implement high-level behaviors like walking, grasping, or navigation

## Topics: Asynchronous Data Streaming

Topics are the primary mechanism for asynchronous communication in ROS 2. They follow a publish/subscribe pattern where one or more nodes publish messages to a topic, and one or more nodes subscribe to that topic to receive messages.

### Topic Architecture

The topic architecture has several key features:

- **Decoupling**: Publishers don't need to know about subscribers, and subscribers don't need to know about publishers
- **Scalability**: Multiple publishers and subscribers can exist for the same topic
- **Asynchronous**: Publishers and subscribers operate independently; no blocking calls
- **Typed Messages**: All messages on a topic conform to a specific message type definition

### Quality of Service (QoS) Settings

ROS 2 provides Quality of Service (QoS) settings that allow you to fine-tune topic behavior for different use cases:

- **Reliability**: Choose between reliable delivery (like TCP) or best-effort delivery (like UDP)
- **Durability**: Specify whether late-joining subscribers should receive old messages
- **History**: Control how many messages are kept in the queue
- **Deadline**: Set maximum time intervals between messages

### Real-World Example: Sensor → Perception Node

Consider a camera sensor node and a perception node in a humanoid robot:

1. The **camera driver node** publishes images to the topic `/camera/image_raw`
2. The **perception node** subscribes to this topic to receive images
3. The perception node processes the images and publishes detected objects to `/detected_objects`
4. Multiple other nodes (navigation, manipulation, etc.) might subscribe to the `/detected_objects` topic

This architecture allows for flexible system design where new perception algorithms can be added without changing the camera driver, and new consumers of object detection data can be added without changing the perception node.

## Services: Synchronous Request/Response Communication

While topics handle asynchronous data streaming, services provide synchronous request/response communication. This is useful when you need a specific response to a specific request, and you want to wait for that response before continuing.

### Service Architecture

Services have the following characteristics:

- **Synchronous**: The client waits for the server to process the request and return a response
- **Request/Response Pattern**: Each service call has a defined request message and response message
- **Single Server**: Typically, only one node provides a specific service
- **Blocking**: The client is blocked until the service call completes

### Service Use Cases

Services are ideal for operations that require immediate results:

- **Configuration**: Changing robot parameters or settings
- **Calibration**: Performing sensor or actuator calibration procedures
- **Action Requests**: Requesting specific actions that have clear success/failure outcomes
- **Diagnostics**: Retrieving system status or performing health checks

### Example: Robot Control Service

A humanoid robot might have a service that allows other nodes to request the robot to move to a specific location:

- **Request**: Contains target coordinates (x, y, theta)
- **Response**: Contains success/failure status and execution time
- **Client**: Any node that needs the robot to move (UI, navigation planner, etc.)
- **Server**: The navigation control node that executes the movement

## Real Humanoid Examples: Communication Patterns in Practice

Let's explore how these communication primitives work together in real humanoid robot applications:

### Sensor → Perception Node Pattern

1. **Sensor Node**: A LIDAR sensor node publishes range data to `/scan`
2. **Perception Node**: A perception node subscribes to `/scan`, processes the data, and publishes obstacle locations to `/obstacles`
3. **Navigation Node**: A navigation node subscribes to `/obstacles` to plan safe paths around detected obstacles

### Planner → Controller Node Pattern

1. **Planning Node**: A motion planner node publishes desired joint positions to `/joint_trajectory`
2. **Controller Node**: A joint controller node subscribes to `/joint_trajectory` and commands the physical actuators
3. **Feedback Loop**: Joint state sensors publish actual positions to `/joint_states`, which the controller uses for feedback control

## When to Use Topics vs Services

Understanding when to use topics versus services is crucial for effective ROS 2 design:

### Use Topics When:
- Data is continuously updated (sensor data, state information)
- Multiple subscribers need the same data
- Decoupling between publishers and subscribers is important
- Asynchronous processing is acceptable
- The data has a "streaming" nature

### Use Services When:
- You need a specific response to a specific request
- The operation has a clear beginning and end
- Synchronous processing is required
- The operation is more like a "function call"
- You need to ensure the operation completed successfully before proceeding

In the next chapter, we'll explore how Python AI agents interface with physical controllers through ROS 2 and how URDF serves as the contract between software and hardware.

## Forward References

The communication patterns covered in this chapter are fundamental to:

- **Module 2 (Simulation)**: Where you'll implement these same communication patterns in simulated robotic environments to test and validate your robotic systems before deploying to real hardware
- **Module 3 (Perception & Planning)**: Where you'll utilize these communication primitives to build sophisticated perception and planning pipelines that process sensor data and generate robot behaviors

Understanding when to use topics versus services will be crucial as you develop more complex robotic applications in these subsequent modules.