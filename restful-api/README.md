# RESTful API


# Key Differences Between HTTP and HTTPS

The **HTTP** (Hypertext Transfer Protocol) and its secure variant, **HTTPS** (Hypertext Transfer Protocol Secure), are the foundation of web communication. The core difference lies in **security**. HTTP is an unencrypted protocol that uses default port 80.
    
Data is transmitted in plain text, meaning anyone intercepting the packet can read it, making it unsuitable for sensitive information like passwords or financial data. In contrast, **HTTPS** uses **SSL/TLS** (***Secure Sockets Layer/Transport Layer Security***) encryption to secure the communication. It operates on default port 443. This encryption ensures confidentiality (data is unreadable), integrity (it hasn't been tampered with), and authentication (the server's identity is verified via a certificate). Using HTTPS is now the standard for all modern websites.

## 1. HTTP

- **Protocol:** Hypertext Transfer Protocol
- **Port:** 80 (default)
- **Encryption:** None (data is transmitted in plain text)
- **Security:** Not secure; data can be intercepted and read by anyone
- **Use Case:** Suitable for non-sensitive information

> Example risk: Sending passwords or financial data over HTTP can be easily intercepted by attackers.

## 2. HTTPS

- **Protocol:** Hypertext Transfer Protocol Secure
- **Port:** 443 (default)
- **Encryption:** SSL/TLS (Secure Sockets Layer / Transport Layer Security)
- **Security Benefits:**
  - **Confidentiality:** Data is encrypted and unreadable to third parties
  - **Integrity:** Ensures data has not been tampered with
  - **Authentication:** Server identity is verified via a certificate
- **Use Case:** Standard for all modern websites; mandatory for sensitive data

## 3. Summary of Key Differences

| Feature         | HTTP            | HTTPS                           |
|-----------------|----------------|--------------------------------|
| Port            | 80              | 443                            |
| Encryption      | None            | SSL/TLS                        |
| Security        | Not secure      | Secure (Confidentiality, Integrity, Authentication) |
| Use Case        | Non-sensitive   | Sensitive / all modern websites |


HTTPS has become the **standard for secure web communication**. Websites handling sensitive data must always use HTTPS to protect users' information and ensure trustworthiness.

---

## 2️ Structure of an HTTP Request and Response

HTTP communication follows a simple request/response model. A client (your browser) sends a Request to a server, and the server replies with a Response.

## 1. Structure of HTTP Communication

| Element | Main Components | Description |
|---------|----------------|-------------|
| **Request (Client → Server)** | 1. **Start Line**<br>HTTP Method (e.g., GET), Path (e.g., /index.html), Protocol Version (e.g., HTTP/1.1)<br>2. **Headers**<br>Metadata about the client and the request (e.g., Host, User-Agent, Accept)<br>3. **Body**<br>Contains data being sent to the server, primarily for POST or PUT requests (e.g., form data) | Sends data or requests resources from the server |
| **Response (Server → Client)** | 1. **Status Line**<br>Protocol Version (e.g., HTTP/1.1), Status Code (e.g., 200), Status Phrase (e.g., OK)<br>2. **Headers**<br>Metadata about the response (e.g., Content-Type, Content-Length, Set-Cookie)<br>3. **Body**<br>The actual content of the requested resource (e.g., HTML page) | Delivers the requested resource or status information |


### Example of HTTP request (GET)

```http

GET /contact.html HTTP/1.1
Host: mysite.com
User-Agent: Chrome/90.0.4430.212

**Response:**

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024
<!DOCTYPE html>... (The HTML content)
```

The request contains the method (GET), the resource path (/contact.html) and headers (Host, User-Agent...).

The answer contains a status code (200 OK), headers (Content-Type, Content-Length) and the body (HTML here).

---

## 3. Common HTTP Methods

    HTTP Methods, also called HTTP Verbs, define the action the client wishes to perform on the identified resource.


    | Method | Description (Function) | Use Case |
|--------|----------------------|---------|
| **GET** | Retrieves (reads) the representation of a specified resource. Data is passed in the URL. | Loading a webpage or fetching a blog post |
| **POST** | Submits data to a specified resource, often resulting in a change of state or creation of a resource. Data is passed in the request body. | Submitting a signup form or adding a new comment |
| **PUT** | Replaces all current representations of the target resource with the content of the request body. (Idempotent) | Updating a user's entire profile information |
| **DELETE** | Removes the specified resource | Deleting a file, a user account, or a database record |

---

# 4. HTTP Status Codes

HTTP status codes are **three-digit numbers** returned by the server in the response to indicate the outcome of the request and whether further action is needed. They are classified by families:

- **1xx**: Informational  
- **2xx**: Success  
- **3xx**: Redirection  
- **4xx**: Client Error  
- **5xx**: Server Error  

| Code | Description | Scenario |
|------|------------|---------|
| **200 OK** | The request has succeeded. | The web page loaded correctly |
| **301 Moved Permanently** | The requested resource has been permanently moved to a new URL. | An old link is permanently redirected to its new location |
| **401 Unauthorized** | The request requires user authentication. The client lacks valid credentials. | A user tries to access a protected administration page without logging in |
| **404 Not Found** | The server could not find the requested resource. | The user tries to navigate to a non-existent page |
| **503 Service Unavailable** | The server is currently unable to handle the request due to temporary overload or maintenance. | The server is down for routine maintenance or experiencing high traffic |

---
# Summary and Conclusion
Web communication is built upon the **HTTP** (***Hypertext Transfer Protocol, port 80***), which allows clients and servers to exchange data using a simple Request–Response model. However, HTTP is **fundamentally insecure** because all data travels in plain text, leaving it vulnerable to interception.

To address this, **HTTPS** (***port 443***) introduces a crucial security layer through **SSL/TLS encryption**. This ensures ***confidentiality*** (data can’t be read by others), ***integrity*** (data isn’t modified in transit), and authentication (the client communicates with the right server). For this reason, HTTPS is **mandatory for handling any sensitive information**.

Every HTTP exchange revolves around:
**Methods (Verbs)** defining the action to perform —
e.g., **GET** (read), **POST** (create), **PUT** (update), **DELETE** (remove).
**Status Codes**, which inform the client about the result —
e.g., ***200 OK*** (success), ***404 Not Found*** (client error), ***500 Internal Server Error*** (server error).

# Conclusion


HTTP is the **core engine of the web**, defining how information is requested and delivered.
However, the evolution to HTTPS marks a turning point in digital communication — transforming an open, insecure protocol into a ***reliable, encrypted, and trustworthy*** medium.
A solid understanding of the ***request/response structure***, the **methods (verbs)**, and the ***status codes*** is essential for anyone working with web technologies.
Adopting HTTPS is no longer just a best practice — it’s a **requirement** for ensuring ***security, trust, and privacy*** in today’s connected world.