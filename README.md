# tvencoder

Requiments
-----------------

* Redis
* Python
  * pip
  * virtualenv
* Chinachu
* FFmpeg (x264 must be enabled)

How to install
--------------------

Make a virtualenv

```
virtualenv ~/env/encode
cd ~/env/encode
source bin/activate
```

Install packages

```
pip install -r requiments.txt
```

Add enqueue.sh to your Chinachu

Example:

```
"recordedCommand": "/home/chinachu/src/tvencoder/enqueue.sh",
```

Run the worker

```
cd tvencoder
rqworker
```

To check encoding status, access the dashboard:

```
http://hostname:9181/default
```
