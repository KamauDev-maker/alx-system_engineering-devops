# Distributed Web Infrastructure

![Image of a distributed web infrastructure]
(distributed_web_infrastructure.png)

[Visit Board](https://miro.com/app/board/uXjVPjLyaes=/#tpicker-content)

## Description

A distributed web infrastructure that attempts to reduce traffic to the primary server by distributing some of the load on the replica servers, with the server responsible for load balancing between the two servers.

## About This Infrastructure

+ For every additional element, why you are adding it. <br/>The new configuration consists of two master servers and one slave server. Since the core server runs active-active, the configuration must be identical, so each additional element must be added to the simple web infrastructure we had in the previous branch. The load is managed by a load balancer that distributes requests according to the Robin-Round algorithm. Finally, additional servers are needed to provide replica servers or slave servers that help offload read requests from the master server.

+ What distribution algorithm your load balancer is configured with and how it works. <br/>The load balancer uses round robin distribution. This means that requested requests are propagated to each server in turn. And after sending the request to the last server, it starts the algorithm from the first server. This results in an average and approximately 50% server load balancing for each of the two server configurations.

+ Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both. <br/>In an active-active configuration, the load balancer spreads out the workload's traffic among multiple nodes. Their goal is to achieve load balancing by distributing work across multiple servers to avoid overloading them. You can use one or more servers (nodes) for serious processing, improving service times.<br/>In an active-passive configuration, the server load balancer recognizes a failed node and redirects traffic to the next available node. In this configuration, as in the active-active configuration, it is important that the primary and standby nodes have the correct server configuration so that clients cannot tell the difference when the failover server takes over.

+ How a database Primary-Replica (Master-Slave) cluster works. <br/>Master-slave replication allows data to be replicated from one database server (master) to one or more other database servers (slaves). The master registers for updates and then sends them to the slaves. The slave displays a message that the update has been successfully received so it can send subsequent updates. Master-slave replication can be synchronous or asynchronous. The difference is simply in the propagation time of the changes. <br/>
If changes are made to the master and slave at the same time, they are synchronized. Asynchronous as changes are queued and written later.

+ What is the difference between the Primary node and the Replica node in regard to the application. <br/>One of the key differences between primary and replica nodes is that the primary database is treated as the authoritative source while replica databases are synchronized. The primary node acts as an information manager, and "real" data is stored on it, only logging is done. On the other hand, reads only happen on replica or slave nodes. The purpose of this architecture is to ensure site stability. If your site receives a lot of traffic, the replica node will prevent the master node from overloading with read and write requests.<br/>
This reduces the load on the entire system and prevents destruction.

## Issues with this Infrastructure

+ There are multiple SPOF (Single Point Failure). <br/>If the underlying MYSQL database server goes down, the entire site cannot make site changes. The server containing the load balancer and the application server connecting to the primary database server are also SPOF.

+ Security issues. <br/>Data transmitted over the network is not encrypted with the SSL certificate, so hackers can spy on the network. All servers are not equipped with firewalls, so rogue IP addresses cannot be blocked.

+ No monitoring.<br/>We have no way of knowing the status of each server since they're not being monitored.