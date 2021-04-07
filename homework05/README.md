# Homework05

For this homework assignment, the goal was to follow an exercise and  create a pod in Kubernetes to print a message with an environment variable 

## A.

1. yaml file used:

```bash
phart-hw5-pod.yml
```

Command used to create the pod:

```bash
kubectl apply -f phart-hw5-pod.yml
```

2. Command to get pod

```bash
 kubectl get pods phart-hw5
```

Output from command:

```bash
NAME        READY   STATUS    RESTARTS   AGE
phart-hw5   1/1     Running   0          17m
```

3. Checking logs of the pod

```bash
kubectl logs phart-hw5
```

Output:

```bash
Hello
```
I was expecting an error since $NAME is not defined

4. Deleting the pod

```bash
kubectl delete pods phart-hw5
```

# B.

1. yaml file used

```bash
phart-hw5-pod.yml
```

command used to create pod:

```bash
kubectl apply -f phart-hw5-pod.yml
```

2. Output of checking the logs for the pod

```bash
[phart@isp02 homework05]$ kubectl logs phart-hw5
Hello Preston
```

3. Deleting the pod

```bash
kubectl delete pods phart-hw5
```

# C.

1. File used and create deployment

```bash
phart-hw5-deployment.yml
```

```bash
kubectl apply -f phart-hw5-deployment.yml
```

2. Get all the pods and their IP's in the deployment

```bash
kubectl get pods phart-hw5-deployment-55fd97745d-9t994 phart-hw5-deployment-55fd97745d-h4bbb phart-hw5-deployment-55fd97745d-h4sxs -o wide
```

Output

```bash
NAME                                    READY   STATUS    RESTARTS   AGE   IP             NODE   NOMINATED NODE   READINESS GATES
phart-hw5-deployment-55fd97745d-9t994   1/1     Running   0          13m   10.244.7.98    c05    <none>           <none>
phart-hw5-deployment-55fd97745d-h4bbb   1/1     Running   0          13m   10.244.5.102   c04    <none>           <none>
phart-hw5-deployment-55fd97745d-h4sxs   1/1     Running   0          13m   10.244.6.142   c03    <none>           <none>
```

3. Checking logs with correct IP's

```bash
[phart@isp02 homework05]$  kubectl logs phart-hw5-deployment-55fd97745d-9t994
Hello Preston from 10.244.7.98
```

```bash
[phart@isp02 homework05]$  kubectl logs phart-hw5-deployment-55fd97745d-h4bbb
Hello Preston from 10.244.5.102
```

```bash
[phart@isp02 homework05]$  kubectl logs phart-hw5-deployment-55fd97745d-h4sxs
Hello Preston from 10.244.6.142
```

