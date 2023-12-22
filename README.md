# Data-with-Google-Cloud

A project to learn about essential features on Google Cloud while doing data anylsis.
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

## Schema
The code used to create schema and maintain 2nd NORMAL FORM is in one of the ipynb.

## Webserver
To build our webserver


