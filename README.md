
---

# Web Crawler Service

## Overview

This project implements a simple web crawler service consisting of two parts: a **server** and a **client**. The server listens for requests from the client to crawl a URL, generates a sitemap of all links within the same domain, and returns it back to the client in a tree structure format. The client sends a URL to the server and prints the generated sitemap on the console.

### Features:
- Crawl a given URL and generate a sitemap.
- Only crawl links within the same domain (ignores external links).
- Returns the sitemap as a JSON object.
- Written in Python (Flask for the server) and Node.js for the client.
  
---

## Table of Contents
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Client Usage](#client-usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Requirements

- **Python** (for the server):
  - Python 3.6 or higher
  - Flask
  - Requests
  - BeautifulSoup4
  - Lxml

- **Node.js** (for the client):
  - Node.js 14.x or higher
  - Axios

You will also need **Git** to clone the repository and **cURL** or **Postman** for testing the API.

---

## Project Structure

The project consists of two main folders: `server` and `client`.

```
webCrawler/
├── server/
│   ├── app.py                # Flask server application
│   ├── requirements.txt      # Python dependencies
│
└── client/
    ├── index.js              # Node.js client application
    ├── package.json          # Node.js dependencies
```

---

## Installation

### 1. **Server (Python)**

#### Install Dependencies:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd webCrawler
   ```

2. Navigate to the `server` directory:

   ```bash
   cd server
   ```

3. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include:

   ```txt
   Flask==2.0.1
   requests==2.26.0
   beautifulsoup4==4.10.0
   lxml==4.6.3
   ```

### 2. **Client (Node.js)**

#### Install Dependencies:

1. Navigate to the `client` directory:

   ```bash
   cd ../client
   ```

2. Install the required Node.js dependencies:

   ```bash
   npm install
   ```

   The `package.json` file should include:

   ```json
   {
     "name": "web-crawler-client",
     "version": "1.0.0",
     "description": "Client to fetch sitemap from the web crawler server.",
     "main": "index.js",
     "dependencies": {
       "axios": "^0.21.1"
     }
   }
   ```

---

## Running the Application

### 1. **Start the Flask Server**

To start the Flask server, run the following command in the `server` directory:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000/`. You should see output like:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The server listens for `POST` requests on the `/crawl` endpoint.

### 2. **Run the Client**

To run the client and fetch the sitemap from the server, use the following command in the `client` directory:

```bash
node index.js <url>
```

Replace `<url>` with the URL you want to crawl, such as `https://www.redhat.com`. For example:

```bash
node index.js https://www.redhat.com
```

The client will send a request to the server and print the generated sitemap in the terminal.

---

## Client Usage

The client sends a `POST` request to the Flask server with a URL in the body. The server responds with the sitemap for that URL.

### Example:

```bash
node index.js https://www.redhat.com
```

This will return a tree-like structure of all links within the `https://www.redhat.com` domain.

Example output:

```
Sitemap:
https://www.redhat.com
- /en
- /blog
- /about
- /contact
```

The client will print the sitemap in a tree format.

---

## Troubleshooting

### 1. **Server Not Responding**

- Ensure the Flask server is running by checking the output in the terminal where you ran `python app.py`. You should see something like:
  
  ```
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

- If you are using Windows, ensure you are not running any firewall or antivirus software that might block the connection between the client and the server.

### 2. **Invalid JSON Response**

- If the server returns an error, ensure that the request body is properly formatted in JSON. The client sends the URL in the following format:

  ```json
  {
    "url": "https://www.redhat.com"
  }
  ```

- Use tools like **Postman** or **cURL** to manually test the server's `/crawl` endpoint:

  ```bash
  curl -X POST http://127.0.0.1:5000/crawl -H "Content-Type: application/json" -d '{"url": "https://www.redhat.com"}'
  ```

### 3. **No Output in Terminal**

- Ensure that the client is calling the correct URL and port. The default is `http://127.0.0.1:5000/crawl`.
- If the client receives a response but does not print the output, ensure that the `printSitemap` function is correctly handling the sitemap data.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following this README, you should be able to set up and run the web crawler service, allowing you to crawl any URL and generate a sitemap for all internal links on the same domain.
