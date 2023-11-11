First of all, I have to say that I don't have enough time to dockerize this project and implement a real solution to handle
huge requests.
<br>
So I apologize, and I'll try to describe it in this text.

For handling substantial requests during times of high user traffic, we can perform the buying task using asynchronous solutions.
<br>
For example, we can receive buy ticket requests and generate an event for another microservice to purchase the ticket from the external API.
<br>
If the external API is overloaded and cannot respond anymore, we must implement the circuit breaker pattern on microservices.
<br>
To optimize access to our tables (such as Seat or Ticket), we must separate read and write operations.
<br>
This can improve speed in our databases, and we can also implement caching. Additionally, we need to limit requests from clients.
<br>
We should have a flexible architecture by using orchestration scenarios with Kubernetes.
<br>
However, if the number of requests exceeds our capacity,we need to carefully consider whether
<br>
to prioritize handling the current load or prevent the creation of new requests by clients using throttling strategies.
<br>
In the end, we must optimize our queries and utilize load balancing strategies.