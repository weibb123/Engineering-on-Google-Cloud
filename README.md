# Data-with-Google-Cloud

A project to learn about essential features on Google Cloud while doing data anylsis.

This project involve using multiple tools on Google Cloud Platform.

1. Store necessary files in Google Storage Bucket.
2. Write webserver using Flask then provision a VM to host in it. With limited budget, the spec for this VM is e2-micro.
3. Webserver also responsible for storing requests to CloudSQL. To use CloudSQL, I chose to create schema that follow 2ND normal form for database optimization.
![image](https://github.com/weibb123/Data-with-Google-Cloud/assets/84426364/9980761d-0529-4599-8a86-fa29ca689563)



## Tech Stack Used:
CloudSQL, Cloud Compute Engine(VM Creation), Python, Flask, Cloud Logging, PubSub

## Configuration
<ul> Make sure Python3-pip is installed with pymysql, sqlalchemy, cloud-sql-python, Flask, Google-cloud. More details below. </ul>

<ul> Google Cloud Platform: Give service account: cloud sql client and cloud sql admin before creating VM </ul>


## GCP Compute Engine
Create VM and ssh into it. This is the VM that will contain webserver.py

VM used for this project is <b>e2-mircro</b> due to limited budget.

#### install this in the VM terminal
```
tar -xvf mysql-server_XXXXXXX.deb-bundle.tar
sudo apt-get install libaio1
sudo dpkg-preconfigure mysql-community-server_*.deb
sudo dpkg -i mysql*.deb
sudo apt-get -f install
```

```
# Run these line of code after the above code
sudo apt-get update
sudo apt-get install python3-pip

pip3 install pymysql sqlalchemy
pip3 install "cloud-sql-python-connector[pymysql]"
pip3 install Flask google-cloud-pubsub google-cloud-logging google-cloud-storage
```
Finally: Go to VPC Networks and reserve a static ip address and allow firewall port 8080 since this flask application is build in port 8080.

## Schema
The code used to create schema and maintain 2nd NORMAL FORM is in one of the ipynb. For SQL database optimization,

we will create 2nd normal form

1NF

- Each cell in table should contain single value
- Each column in table should be unique

2NF

- satisfy 1NF
- attributes cannot depend on subset of the key(multiple IDs), must depend on entirety of key

## Webserver
To build our webserver.py, we use requests.get to acquire informations and store in our Google Cloud SQL base by making connection using crendentials.


## Data Analysis
Again, making connection to the DB, we can write SQL command to retrieve data from columns and write SQL commands for analysis
![image](https://github.com/weibb123/Data-with-Google-Cloud/assets/84426364/9be39caf-5cc2-4cc2-ba1f-66470a16dd33)





