# Homework 06

For Homework 06, the goal was to create a test environment for the Flask API, built in previous homeworks, using Kubernetes.   

## Vizualizing the pods 

After following the steps outlined in the the read the docs for Homework 06, we can run some kubectl commands to see the live services/deployments/pods created for the Flask app and redis database.

Running the command below will give a list of local pods that are up and running

```bash
kubectl get pods
```

For me the above command shows the following output:

```bash
[phart@isp02 homework06]$ kubectl get pods
NAME                                           READY   STATUS    RESTARTS   AGE
hello                                          1/1     Running   416        17d
hello-deployment-6cb9f665c5-vn2ml              1/1     Running   296        12d
helloflask-848c4fb54f-4fzqz                    1/1     Running   0          10d
helloflask-848c4fb54f-p9g9c                    1/1     Running   0          10d
phart-hw5-deployment-55fd97745d-9t994          1/1     Running   117        4d21h
phart-hw5-deployment-55fd97745d-h4bbb          1/1     Running   117        4d21h
phart-hw5-deployment-55fd97745d-h4sxs          1/1     Running   117        4d21h
phart-test-flask-deployment-79d8f9fc5f-2zzlh   1/1     Running   0          3d1h
phart-test-flask-deployment-79d8f9fc5f-d59c5   1/1     Running   0          3d1h
py-debug-deployment-5cc8cdd65f-7cb68           1/1     Running   0          10d
py-debug-deployment-5cc8cdd65f-cwx8j           1/1     Running   0          3d8h
redis-pvc-deployment-667647b8df-t9qjl          1/1     Running   0          5d7h
```

There are two pods currently running for the flask deployment and a pvc pod for the redis deployment


## Visuializing the services

Running the following command will show all the local services running on kubernetes

```bash
[phart@isp02 homework06]$ kubectl get services
NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app1                       NodePort    10.97.171.238   <none>        5000:30774/TCP   4d5h
hello-service              ClusterIP   10.97.63.149    <none>        5000/TCP         10d
phart-test-flask-service   ClusterIP   10.104.201.42   <none>        5000/TCP         3d3h
phart-test-redis-service   ClusterIP   10.107.122.23   <none>        6379/TCP         5d8h 
```

There are two services running locally, one for the flask app on port 5000, and one for the redis database on port 6379.


## Interacting with the Flask App

To run the consumer.py file within the flask app deployment, exec into it by running the following command. Either of the two pods for the flask deployment can be used for this step.

```bash
 kubectl exec -it phart-test-flask-deployment-79d8f9fc5f-d59c5 -- /bin/bash
```

After running the above the command, notice that the user has switched to root, because you are now in the pod's shell, specifically within the app subfolder where the consumer.py file is.

```bash
root@phart-test-flask-deployment-79d8f9fc5f-d59c5:/app# ls
app.py  consumer.py  requirements.txt
```

---
**NOTE**
Dependencies such as requests, redis, and curl were intially pip installed into this shell
---


To run the consumer file and ping the routes already created within the flask app run the following command:

```bash
root@phart-test-flask-deployment-79d8f9fc5f-d59c5:/app# python3 consumer.py
RESETTING DATABASE...
b'Successfully cleared the database and entered in 20 new animals'

ALL ANIMALS
[{'head': 'snake', 'body': 'magpie-eagle', 'arms': 10, 'legs': 12, 'tail': 22, 'created_on': '2009-04-05'}, {'head': 'bull', 'body': 'hawk-fly', 'arms': 6, 'legs': 12, 'tail': 18, 'created_on': '2004-11-02'}, {'head': 'bull', 'body': 'donkey-pug', 'arms': 8, 'legs': 12, 'tail': 20, 'created_on': '2001-05-21'}, {'head': 'raven', 'body': 'ewe-duck', 'arms': 2, 'legs': 3, 'tail': 5, 'created_on': '2003-10-30'}, {'head': 'lion', 'body': 'loon-shrimp', 'arms': 8, 'legs': 12, 'tail': 20, 'created_on': '2003-01-07'}, {'head': 'bull', 'body': 'ape-caiman', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2011-08-26'}, {'head': 'bull', 'body': 'moose-jay', 'arms': 2, 'legs': 3, 'tail': 5, 'created_on': '2010-08-06'}, {'head': 'bunny', 'body': 'man-asp', 'arms': 2, 'legs': 6, 'tail': 8, 'created_on': '2005-11-11'}, {'head': 'snake', 'body': 'jaguar-shrimp', 'arms': 8, 'legs': 6, 'tail': 14, 'created_on': '2020-08-03'}, {'head': 'snake', 'body': 'goat-dog', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2019-06-17'}, {'head': 'bull', 'body': 'ghoul-condor', 'arms': 6, 'legs': 6, 'tail': 12, 'created_on': '2009-06-27'}, {'head': 'snake', 'body': 'gnu-tahr', 'arms': 8, 'legs': 9, 'tail': 17, 'created_on': '2018-07-18'}, {'head': 'snake', 'body': 'possum-mutt', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2000-01-13'}, {'head': 'snake', 'body': 'shiner-lark', 'arms': 2, 'legs': 6, 'tail': 8, 'created_on': '2017-01-19'}, {'head': 'bull', 'body': 'lizard-kiwi', 'arms': 10, 'legs': 3, 'tail': 13, 'created_on': '2020-06-28'}, {'head': 'bunny', 'body': 'piglet-tuna', 'arms': 10, 'legs': 3, 'tail': 13, 'created_on': '2012-12-16'}, {'head': 'raven', 'body': 'whale-guppy', 'arms': 2, 'legs': 3, 'tail': 5, 'created_on': '2002-06-03'}, {'head': 'bunny', 'body': 'hound-pug', 'arms': 10, 'legs': 12, 'tail': 22, 'created_on': '2010-07-22'}, {'head': 'raven', 'body': 'jennet-gull', 'arms': 8, 'legs': 9, 'tail': 17, 'created_on': '2012-02-14'}, {'head': 'bunny', 'body': 'hawk-hen', 'arms': 10, 'legs': 9, 'tail': 19, 'created_on': '2013-08-19'}]

ANIMAL UUIDS
{'1': "b'91aefa8d-116c-4efd-9743-79f32c56dffa'", '2': "b'4f367443-99f0-41c6-8926-4c5d00c5ed78'", '3': "b'1ef5db57-1c65-4291-b743-48b2c074a864'", '4': "b'75929bb2-b7af-479c-a545-9870b7d60751'", '5': "b'2b842943-a3d7-49f1-91b1-5f1bce28b834'", '6': "b'9253a7b9-8e1a-4599-b745-ef32c83452af'", '7': "b'90085ee1-6fab-45a4-a001-ad1f40771dc1'", '8': "b'fd661e91-9457-4da4-bd44-037770a5ce85'", '9': "b'76c28515-8bf6-4b51-bc4c-c768aa8b2800'", '10': "b'5c6020ba-74aa-45d1-9d3b-cf9c2c112e74'", '11': "b'c987a50b-6d27-407f-bffb-0835913986c4'", '12': "b'146bdbbe-6a20-4e14-8c03-7acaaf136ff3'", '13': "b'b208df33-a800-458e-a702-c7c076ff3905'", '14': "b'dd4cc9e7-946f-4e94-9b4b-7996027e37fe'", '15': "b'b0ffa5a2-9629-4e39-8571-1fa1647fedf9'", '16': "b'79063ea4-b607-4c43-8c76-e49505bf2b78'", '17': "b'754a08bb-37a6-4e45-a682-e89da899a7ff'", '18': "b'c2e79536-d0bc-4eaf-a7f4-57df8cc6a52e'", '19': "b'4a77d715-942d-4505-982b-b166f597a575'", '20': "b'ab999f7c-1f78-4d7e-af1b-c27a377d1c3f'"}

ANIMAL WITH UUID

ANIMALS WITHIN A DATE RANGE
[{'head': 'snake', 'body': 'jaguar-shrimp', 'arms': 8, 'legs': 6, 'tail': 14, 'created_on': '2020-08-03'}, {'head': 'snake', 'body': 'goat-dog', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2019-06-17'}, {'head': 'snake', 'body': 'gnu-tahr', 'arms': 8, 'legs': 9, 'tail': 17, 'created_on': '2018-07-18'}, {'head': 'snake', 'body': 'shiner-lark', 'arms': 2, 'legs': 6, 'tail': 8, 'created_on': '2017-01-19'}, {'head': 'bull', 'body': 'lizard-kiwi', 'arms': 10, 'legs': 3, 'tail': 13, 'created_on': '2020-06-28'}]

AVERAGE NUM LEGS PER ANIMAL
b'8.1'

NUMBER OF ANIMALS
b'20'

UPDATED ANIMAL

```

Routes that required a specific animal's uuid were left out in this conusmer file, because the consumer file resets the database with 20 new animals when it is ran.


### Pinging the uuid specific routes

Use curl to utilize the flask app's uuid specific routes

Use the following command and a uuid from the output of running consumer.py

```bash
curl 10.104.201.42:5000/animals/uuid/?uuid=<uuid>
```

Use the following command to update an animals stats
```bash
curl 10.104.201.42:5000/animals/update/?uuid=<uuid>&<stat>=<updated stat>
```

---
**NOTE**
The IP address and port number used in the curl commands are the IP address and port the flask service is running on. These can be obtained by running the kubectl get services command.
---

---
**NOTE**
All Services, Deployments, and Pods were created using the kubectl apply -f <file name> command
--- 
