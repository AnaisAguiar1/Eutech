<center>

# Task2: Implementing Firewall Rules

</center>

***Author:*** Anais G. Aguiar Contreras.

***Company:*** EUtech Assignments.

***Date:*** 24th March of 2023.

## **Index**

+ [Description](#id1)
+ [Requirements](#id2)
+ [Used tools](#id3)
+ [Development](#id4)
+ [Closure](#id5)

<center>

## ***Description***. <a name="id1"></a>

</center>
<br>

UFW stands for "Uncomplicated Firewall" and is a firewall tool integrated in Ubuntu that allows you to easily configure firewall rules to protect your system against unauthorized connections from the network.

UFW allows for a wide range of firewall configurations, including the ability to allow or block incoming and outgoing traffic based on source and destination IP addresses, ports, and protocols. It also supports advanced configurations such as logging, rate limiting, and connection tracking.

To this proyect we have been hired as a Network Security Engineer for a small company. The company has a network infrastructure consisting of multiple devices, including servers, switches, and routers. Your task is to configure and implement firewall rules to secure the network infrastructure.

<br>

<center>

## ***Requirements.*** <a name="id2"></a>

</center>

<br>

You have to configure and implement firewall rules to secure the network infrastructure, but you have some requirements that you must apply in the project.

Requirements that you have to include in this proyect are the next ones:

<br>

* Install and configure a firewall on both Windows and Linux operating systems.

<br>

* Create firewall rules to allow inbound and outbound traffic for specific ports, protocols, and IP addresses.

(habilitar reglas: puerto 22 ssh, puerto 80 http, puerto 443 https, puerto 25 smtp)

https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands

<br>

* Test the firewall rules to ensure that they are working correctly.

<br>

* Create a report detailing the configuration and implementation of the firewall rules.

<br>


<center>

## ***Used tools.*** <a name="id3"></a>

</center>

We will use two differents Virtual Machines

|   MV  |      OS      |     Version     |   IP   |   ROL  |
|-------|--------------|-----------------|--------|--------|
|   1   | Windows 2010 | Enterprice 2016 |        | Cliente|
|   2   |    Ubuntu    |   Ubuntu 20.04  |        | Cliente|

### ***Development.*** <a name="id4"></a>

<center>


## ***Install and configure a firewall on both Windows and Linux operating systems.***

</center>

<br>

<center>

## ***UBUNTU.***

</center>

<br>

We are going to start with Linux. First of all we check that the ufw is installed and running, if it is not we can install it using the command ``"sudo apt-get install ufw"``, in our case we had it installed, we use the command ``"ufw status"`` to check if it was runnig, in case the ufw it's installed but not runnig we can start it with the command `"ufw enable"`.

```
sudo apt-get install ufw ----> To Install.

sudo ufw status ----> To check the status.

sudo ufw enable ----> To start it.
```
<center>

![](img/04.png)

![](img/03.png)

</center>

After we have the ufw enable and running we can see wich rules we have configurated using the command ``ufw status numbered``, this command it's going to show us all the rules that we have configurated and it will order them by numbers.

*** INSERTAR IMAGEN DEL CORTAFUEGOS SIN NINGUNA REGLA APLICADA***


We needed to now our IP address, so we also use the command ``ip a``, we are goind to need it later.

<center>

![](img/02.png)

</center>

<center>

## **Create firewall rules to allow inbound and outbound traffic for specific ports, protocols, and IP addresses.**

</center>

<br>

Now that we have the UFW enable and without any rules allow we can start to create them. 

<br>

## **Protocol SSH:**

<br>

**SSH (Secure Shell)** is a secure network protocol that allows users to connect to a remote system securely and execute commands remotely. SSH is often used to connect to remote servers, whether to manage them, transfer files, or run applications on them.

To establish an SSH connection, it is necessary to have SSH client software installed on the local machine and enable the SSH service on the remote server. Then, a SSH client such as **PuTTY (on Windows)** or SSH command line (on Linux and macOS) can be used to connect to the remote server and access its resources.

The first rule it's going to be the ``"SSH"`` conexion by port 22, UFW we use the command ``"ufw allow ssh"``, with this line the rule will be allow and it will start to work inmediatly.

<center>

<br>

![](img/05.png)

<br>

</center>

We used the command ``"ufw status numbered"`` so, now we can see the rule runnig and applied, till this momment we only have this rule in our firewall.

We can connect by **ssh** from another computer to this one using **ssh**.

<center>

<br>

![](img/11.png)

<br>

</center>

We can also deny or allow the ssh conection to an specific ip address or to an ip range in case you don't want someone in specific conecting to your computer or in case you only want to accept connection ssh just with one computer.

To allow just one specific ip addresswe create this rule, we used the command ``"sudo ufw allow from 192.168.43.19 proto tcp to any port 22"``.
So now, only the machine with that ip can make a ssh conection with us.

<br>

**insertar foto de solo allow esa ip para ssh**
<br>

If we want to reject or deny the ssh conection we add the next rule ``"ufw deny from any to any port 22 proto tcp"`` (here we are rejecting to all ip directions, so only the one that we accepted before can be able to conect by ssh with us)

<br>

**insertar foto de la restriccion de red o de la restriccion de ip**
<br>

Checked that the rules were apllied correctly using the command ``"ufw status"``, we will see our rules running, so, now we can test them.


<center>

## **Test that the applied firewall rules are working correctly.**

</center>

<br>

## **TESTING SSH PROTOCOL**

Now you can see that the rules about the **SSH Protocol** are working.

Only the machine with the ip address **192.168.43.19** can conect by ssh with our ubuntu machine, and the rest of machines with any ip address are going to be rejected.

To test if the rule ait`s working, the machine with the ip allow to ssh, in this case it's windows, so we had to install the program putty to make the conection by ssh with our ubuntu machine.

<br>

![](img/15.png)

<br>

Insert the ip address of the machine that we want to connect with, in this case it's **192.168.43.193**, by **port 22**, connection type **"SSH"**, then you just have to open it.

<br>

![](img/16.png) 

<br>

We will need the ``"username"`` and ``"password"``, without this two requirements you can`t connect, after this it's connected to the ubuntu machine by ssh from the windows machine

<br>

![](img/17.png)

<br>

**INSERTAR GIFT DEMOSTRANDO QUE LA IP PERMITIDA CONECTA Y CUANDO INTENTAMOS O OTRAS IP NO**

<br>

## **Protocol HTTP:**

<br>

**HTTP (Hypertext Transfer Protocol)** is a communication protocol used on the **World Wide Web (WWW)** for transferring information between servers and clients.

The HTTP protocol is based on the client-server model, where a client (such as a web browser) sends a request to a server, and the server responds with a response that contains the requested resource (such as a web page).

**The HTTP protocol by default uses port 80** for communication between clients and servers.

When a client, such as a web browser, sends an HTTP request to a server, the request is sent through the server's port 80, unless another port is explicitly specified. Similarly, when a web server responds to an HTTP request, the response is sent back to the client through port 80, unless another port is specified in the response.

We are going to create the rule to make the protocol HTTP allow, we have to make sure that the HTTP rule is enabled in ufw. To do this, we run the following command:

```
sudo ufw app list.
```

<br>

**CAPTURAAAAA**
<br>

After having the HTTP rule enabled, we have to look for the entry for **"Apache"** and make sure that it is enabled. If the input is not enabled, you can enable it with the following command: 

```
sudo ufw allow 'Apache'.
```
<br>

**CAPTURAAAAA**
<br>

In case you are using another web server, or if you want to configure the HTTP rule manually, it can also be done with the following command:

```
sudo ufw allow 80/tcp
```

With this command we will enable incoming traffic through **port 80** for the **TCP protocol**.

To be sure the rule was apllied correctly we use the command line ``sudo ufw status``, this command will show us the actual status of our ufw rules,including the port 80 if this one were configurated correctly.

<br>

## **TESTING HTTP PROTOCOL**

<br>

To verify that the rule was applied correctly we have a couples of options:

**1) Using the ``curl`` command** from the command line:

```
curl http:/localhost/
```

If the response includes the content of the default web page of the web server, it means that the rule for port 80 has been configured correctly and is working.

<br>

**CAPTURAAAAA**
<br>

**2) Accessing the website from a browser:** Open a web browser on your computer and type the IP address of your server or domain name in the browser address bar, followed by ":80".

```
http://your-server-ip-address:80/
```

If the web page loads correctly, it means that the rule for port 80 has been configured correctly and is working.

<br>

**CAPTURAAAAA**
<br>

**3) Checking the status of the rule in UFW:** Open a terminal and run the following command:

```
sudo ufw status
```

This will show the current status of the UFW rules, including the rule for port 80 if it has been configured correctly. If the rule is shown as "ALLOW" and has the correct port number, it means that the rule is active and working correctly.

<br>

**CAPTURAAAAA**
<br>


<br>

## **Protocol HTTPS:**

<br>

**HTTPS (Hypertext Transfer Protocol Secure)** is a communication protocol used to transfer data securely over the Internet. **HTTPS is a more secure version of the HTTP protocol**, which is used for transferring unencrypted data.

The main **difference between HTTP and HTTPS is that HTTPS uses an additional security layer** called SSL/TLS (Secure Sockets Layer/Transport Layer Security) to encrypt the data transmitted between the server and the client. This makes it more difficult for attackers to intercept and read the data while it is being transferred between the client and server.

HTTPS is commonly used in financial transactions, online purchases, and in any situation where secure data transfer is required. Websites that use HTTPS have a lock icon in the browser address bar and their **URL begins with "https://" instead of "http://"**. 

> It is important to note that other protocols, such as HTTPS, also use port 80 by default for communication with the server, but **port 443 is typically used for secure communication over HTTPS**.

We are going to add this rule to our firewall, first of all we need to verify that the rule to the port 443 it's enabled in ufw.

```
sudo ufw status ---> To check if the rule exist.
sudo ufw allow 443/tcp ---> To add the rule to our firewall and make the port 443 enable.
```
<br>

***CAPTUURAAAA***
<br>

Once we created the rule for protocol HHTPS using the port 443 we can check it using again the command ``sudo ufw status`` and this time we have to be ables to see the port an protocol being able and open to use.

<br>

***CAPTUURAAAA***
<br>

With this rule working we can use the browser in a more secure way and create web domains more secures than with the HTTP protocol.

<br>

## **TESTING HTTPS PROTOCOL**

<br>

To check and prove if the firewall rule that we added about the **HTTPS protocol** it's working we can go to the browser and now we are going to be ables to open a HTTPS direction, this give us more security and a safe domain.

<br>

***CAPTUURAAAA***
<br>

<br>

## **Protocol SMTP:**

<br>


<br>

## **Protocol MySQL:**

<br>


<br>

## ***Closure***. <a name="id5"></a>

</center>

<br>

