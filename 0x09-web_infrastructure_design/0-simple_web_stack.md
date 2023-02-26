# Simple Web Stack

! [Image of a simple web stack](Simple web stack.jpg)

[visit Board](https://miro.com/app/board/uXjVPjLyaes=/#tpicker-content)

## Description

This is a simple web infrastructure that hosts a website that can be reached via `www.foobar.com`.

## About The Infrastructure

+ What is a Server. <br/>A server is a physical machine (as hardwares), virtual machine or software that provide functionality to other programs or devices called "Clients". 

+ What is the role of the domain name. <br/> The role of the domain name is to replace complex IP addresses numbers into easily understandable names so humans can remember and communicate with the domain in a better way.

+ What type of DNS record www is in `www.foobar.com`. <br/>DNS record of www belongs to a subdomain of the `www.foobar.com`.

+ What is the role of the web server. <br/>The primary role of the web server is to store, process, and deliver requested information to end users.

+ What is the role of the application server. <br/>Its main role is to provide a dedicated space where applications can run, and it provides a range of services and features to support application development and excution.
The primary role of the application server is to handle requests from clients, which could be web browsers, mobile devices. The application server processes these requests and provides the appropriate response.

+ What is the role of the database. <br/>The role of the database is to make the information gathered organized so it can be easily accessed, managed, and updated. 

+ What is the server using to communicate with the computer of the user requesting the website.<br/>When a user requests the website, the server communicates with the user's computer using the Hypertext Transfer Protocol(HTTP). HTTP is the primary protocol used for communication between servers and clients on the World Wide Web. The server sends response to the user's computer in the form of a HTTP message, which typically contains the requested content, such as a HTML page or an image file. The message also includes status codes and headers that provide additional information about the response. The commucation between the server and the user's computer occurs over a network "internet".

## Issues with the simple web infrastructure

+ One of the challenges of simple web infrastructure is related to Single Point of Failure (SPOF). In the event of a system component failure, the entire system is incapacitated and collapses as there is no backup available to maintain the continuity of system functioning.

+ Additionally, whenever a structure or node in the system needs to be serviced, the entire system must be shut down while maintenance is being performed. Then we will not be able to meet the customer's request during this period.

+ Traffic congestion can be a risk to server bandwidth. This is because there is no way to scale the service using additional servers as backups. This can cause traffic to exceed the server's capacity and cause web page and client requests to fail.