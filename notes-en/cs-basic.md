# Computer Science Fundamentals

- [Internet Technology](#internet-technology)
- [Database](#database)

## Internet Technology
https://zhuanlan.zhihu.com/p/147370653

![alt text](img-cn/osi-tcpip.png)

## TCP/IP (4 layers)
- **Datalink Layer:**
   - The datalink layer defines **`how data should be sent`**, handles **`the physical act of sending and receiving data`**, and is responsible for **transmitting data between applications or devices on a network**.
   - MAC address, Error handling
   - Examples: IEEE 802.3 Ethernet, IEEE 802.11 WIFI
- **Internet Layer:**
   - Responsible for **`sending packets from a network and controlling their movement`** across a network to **`ensure they reach their destination`**.
   - Routing, Load Balance
   - Examples:
     - IP Protocol (Internet Protocol);
     - ICMP Protocol (Internet Control Message Protocol);
     - ARP Protocol (Address Resolution Protocol);
     - RARP Protocol (Reverse Address Resolution Protocol).

- **Transmission Layer:**
   - Responsible for **`providing a solid and reliable data connection`**.
   - Examples: TCP, UDP (User Datagram Protocol)

- **Application Layer:**
   - The application layer refers to **`programs`** that need TCP/IP to help them communicate with each other. 
   - Examples: HTTP, HTTPS

## IP Address
- IP address, 256:256:256:256, so a total of 32 bits, 4 bytes
- 2^8 (2 to the power of 8) = 256
- 8 bits = 1 Byte
- LAN (Local Area Network)

## MAC
The unique ID of a device. MAC address acquisition is implemented through the ARP (Address Resolution Protocol).

Each MAC address is a 48-bit identifier, usually written as six groups of hexadecimal numbers (e.g., 8a:3f:80:c9:9a:28). These MAC addresses are assigned during hardware manufacturing to ensure each interface on the network has a unique identifier.

## Private IP, Public IP
- **Private IP**
   - Private IP refers to IP addresses used within a local area network (LAN)
   - These addresses are defined in RFC 1918, including:
   - 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
   - 172.16.0.0 - 172.31.255.255 (172.16.0.0/12)
   - 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)
 - Each device connected to a LAN (such as home WiFi) receives a unique private IP
 - These IPs are only valid within the LAN and cannot be used directly for Internet communication

- **Public IP**
   - Public IP is a globally unique IP address assigned by an Internet Service Provider (ISP)
   - Used to identify and locate networks on the global Internet
   - In home or small office networks, usually only the router has a public IP
   - Multiple devices using private IPs share this single public IP through NAT

- **NAT (Network Address Translation)**
   - NAT is implemented in routers and maintains a translation table
   - The table records the correspondence between internal private IP addresses, ports, and external connections
   - When data packets leave the LAN, NAT replaces the source private IP with the public IP and records this mapping
   - When a response returns, NAT consults the table to correctly forward the data to the corresponding device within the LAN

## Gateway
### Subnet Mask

A subnet mask is used to divide the network portion and host portion of an IP address, telling devices which IP addresses are within the same network segment.
* **Format**: Same as IP address (e.g., 255.255.255.0)
* **Function**: By performing a bitwise AND operation between the IP address and subnet mask, the network address can be determined
* **Common notations**:
  * 255.255.255.0 is equivalent to /24 (indicating the first 24 bits are the network portion)
  * 255.255.0.0 is equivalent to /16
  * 255.0.0.0 is equivalent to /8

### Network Segment

A network segment is a logical partition in the IP address space where devices can communicate directly without a router.
* **Determination method**: Perform a bitwise AND operation between the IP address and subnet mask to get the network address
* **Example**:
  * IP address: 192.168.1.100
  * Subnet mask: 255.255.255.0 (/24)
  * Network address: 192.168.1.0
  * Network segment range: 192.168.1.0 - 192.168.1.255

### Gateway

A gateway is a device that connects two different networks, usually a router, responsible for forwarding data packets between different network segments.
* **Default gateway**: When a data packet's destination is not in the local network segment, the device sends the packet to the default gateway
* **Function**: Acts like a city exit, serving as a "portal" from the local network to external networks
* **Example**: Home routers typically have two IP addresses
  * WAN port IP: Assigned by ISP, used to connect to the Internet
  * LAN port IP: Usually 192.168.1.1, serving as the default gateway for internal devices

## Database

### CAP (Consistency, Availability, Partition Tolerance)
- C: All nodes see the same data at the same time.

### Data Structures
- **B+Tree**: Binary Search (More **Compact,** rather than **heavy**)
- Each node contain more data than single Normal B Tree.

### Transaction
**Transaction** is a unit of work (Transaction Logic) in a database. (Updating, Adding data)

### ACID (Atomicity, Consistency, Isolation, Durability)
- **Consistency**: Consistent when it is started and ended.
- Any Data written to the database must be valid according to all the **defined rules**.

### Transaction Types
- **Flat Transaction**: Each transaction is independent and has a clear beginning and end. In flat transactions, operations on data on different servers are performed sequentially, meaning each operation is completed before the next one begins. This model ensures that if part of a transaction fails, the entire transaction can be terminated, thereby maintaining the integrity and consistency of the database.
- **Nested Transaction** (Father - Children): Roll-back depends on the father.
- **Wormhole**: Loop Transaction

### Locks and Deadlocks
- **Deadlock**: XLOCK A is held by T1, XLOCK B is held by T2. They both wait for the XLOCK that the other one held.
- Intention Lock can prevent this.
- **Dekker's algorithm** primarily works by using two flags (usually boolean variables) and a variable indicating which process's turn it is to enter the critical section. Before attempting to enter the critical section, each process first sets its flag to true (indicating it wants to enter the critical section), then checks the other process's flag

### Lock Types
- **Shared Lock**: i.e. Read Lock, allow read at the same time.
- **Intention Lock**: Intent to have (Between exclusive and shared, avoid deadlock)

### Isolation Issues
- **Phantom Read**: When a transaction, in the same query, returns different sets of rows in two reads. **Reading uncommitted data from other transactions.** Reason: Other transactions inserted new rows between the two reads
- **Unrepeatable Read**: Due to other transactions modifying and committing the data during this period, multiple reads within the same transaction return different results. **Reading committed data from other transactions**

### Isolation Levels
- **Degree 1: Read Uncommitted**: May result in dirty reads, non-repeatable reads, and phantom reads
- **Degree 2: Read Committed**: Prevents dirty reads, but may have non-repeatable reads and phantom reads
- **Degree 3: Repeatable Read**: Prevents dirty reads and non-repeatable reads, but may have phantom reads
- **Serializable**: Prevents all these issues, but has the lowest concurrent performance

### Locking Protocols
- **Two-phase Locking**: In the standard two-phase locking (**2PL**) protocol, transactions are divided into two phases:
 - **Growing Phase**: At the beginning of the transaction, new locks can be acquired, but no locks are released.
 - **Shrinking Phase**: Once the transaction has acquired all necessary locks, it enters the shrinking phase, during which the transaction can begin releasing locks but cannot acquire new locks.
- **Strict Two-phase Locking**: No Shrinking Phase
- **Two-version Locking**