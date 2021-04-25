# Homework 07

For Homework 07, the goal was to create an architecture for using the Flask app by creating job requests to ping the specific routes within app.py. This architecture involves a worker, api, and job manager in addition to the previous Flask app and redis database previously running on kubernetes.

## Part A

From an in class exercise, the code for the api, worker, and the job manager were added to the preexsiting web folder and a new docker image was built from an updated dockerfile that now includes these files in the source code. The old Flask app code was updated with the new IP address of the Redis service running on Kubernetes.

The following commands were run to get all the deployments and servies needed for this homework assignment up and run
ning.

```bash
kubectl apply -f phart-hw7-flask-deployment.yml
```
```bash
kubectl apply -f phart-hw7-flask-service.yml
```
```bash
kubectl apply -f phart-hw7-redis-deployment.yml
```
```bash
kubectl apply -f phart-hw7-redis-pvc.yml
```
```bash
kubectl apply -f phart-hw7-redis-service.yml
```
```bash
kubectl apply -f phart-hw7-worker-deployment.yml
```

To exec into the python debug pod to curl the route to the Flask app to test the functionality of the job messaging system:

```bash
kubectl exec -it py-debug-deployment-5cc8cdd65f-7cb68 -- /bin/bash
```

Once inside the following curl statement was used three times to create three new jobs:
```bash
curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
```

Output from the curl statements produced by the api.py route:
```bash
{"id": "0a0c1ca1-2f1c-4575-92c2-56cdc634352d", "status": "submitted", "start": "Start Now", "end": "End Now"}
```

To make sure the worker is successfully completing the job, go into a python shell and run the follwing script:
```bash
>>> import redis
>>> rd = redis.StrictRedis(host='10.102.185.56', port=6379, db=0)
>>> rd.keys()
[b'job.0a0c1ca1-2f1c-4575-92c2-56cdc634352d']
>>> rd.hgetall('job.0a0c1ca1-2f1c-4575-92c2-56cdc634352d')
{b'id': b'0a0c1ca1-2f1c-4575-92c2-56cdc634352d', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now'}
```

## Part B

In order to add the IP address of the worker pod that completed the job request, the os library was imoprted into jobs.py and a new worker tag was added to the JSON data for the job when the update\_job\_status() function is called fro m the worker.

```bash
def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)
    if job:
        job['status'] = new_status
        job['worker'] = os.environ['WORKER_IP']
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
```

## Part C

After the worker pod was scaled to two deployments, 10 POST requests creating new jobs were run:

```bash
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "3cfbf506-97c9-4810-90ef-2775d37325cb", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "fed60f96-ec91-40d3-b370-509f971321b9", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "8c7dbf81-dd4f-459e-93b7-e0320476076f", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "b7f26c82-c622-4756-bdad-29cb4e86377a", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "2404c288-9e52-4fdb-bc05-533a3213b720", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "57e47ab2-3738-492c-b1cf-64bc9bcf8ea2", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "25439216-cb27-4969-ac8a-8a81615d1da8", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "cd6982e4-5d5d-4ac3-8434-7cab116f9b1c", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end": "End Now"}' 10.109.147.196:5000/jobs
{"id": "afec7e4a-ff98-4e8e-b06e-612e01a2583c", "status": "submitted", "start": "Start Now", "end": "End Now"}
root@py-debug-deployment-5cc8cdd65f-r68b4:/# curl -X POST -H "content-type: application/json" -d '{"start": "Start Now", "end":"End Now"}' 10.109.147.196:5000/jobs
{"id": "9b17e5ba-87ac-41b1-87a3-2e7d8628ec4b", "status": "submitted", "start": "Start Now", "end": "End Now"}
```

Now going into a python shell and running the following python script that iterates through all the keys in the database, we can see that all the jobs have gone to completion and the IP address of the worker pod they were run on is in their JSON output

```bash
Python 3.9.4 (default, Apr 10 2021, 15:31:19)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd = redis.StrictRedis(host='10.102.185.56', port=6379, db=0)
>>> for key in rd.keys():
...   rd.hgetall(key)
...
{b'id': b'9b17e5ba-87ac-41b1-87a3-2e7d8628ec4b', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.15.210'}
{b'id': b'fed60f96-ec91-40d3-b370-509f971321b9', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.15.210'}
{b'id': b'57e47ab2-3738-492c-b1cf-64bc9bcf8ea2', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.15.210'}
{b'id': b'cd6982e4-5d5d-4ac3-8434-7cab116f9b1c', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.15.210'}
{b'id': b'b7f26c82-c622-4756-bdad-29cb4e86377a', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.15.210'}
{b'id': b'afec7e4a-ff98-4e8e-b06e-612e01a2583c', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.10.179'}
{b'id': b'25439216-cb27-4969-ac8a-8a81615d1da8', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.10.179'}
{b'id': b'2404c288-9e52-4fdb-bc05-533a3213b720', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.10.179'}
{b'id': b'3cfbf506-97c9-4810-90ef-2775d37325cb', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.10.179'}
{b'id': b'8c7dbf81-dd4f-459e-93b7-e0320476076f', b'status': b'complete', b'start': b'Start Now', b'end': b'End Now', b'worker': b'10.244.10.179'}
```

Each worker worked 5 jobs each.

From the code output above, you can see that the first 5 jobs were completed by the worker pod IP: 10.244.15.210, and the other 5 jobs were completed by the worker pod with IP: 10.244.10.179.

 
