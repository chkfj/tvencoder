# tvencoder

Requirements
-----------------

* Redis
* Python
  * pip
  * virtualenv
* Chinachu
* FFmpeg (x264 must be enabled)
* Supervisor

How to install
--------------------

### Make a virtualenv

```
virtualenv ~/env/encode
cd ~/env/encode
source bin/activate
```

### Install packages

```
pip install -r requiments.txt
```

### Add enqueue.sh to your Chinachu

Example:

```
"recordedCommand": "/home/chinachu/src/tvencoder/enqueue.sh",
```

### Run a worker

```
cd tvencoder
rqworker
```

### To check encoding status

Run a rq-dashboard

```
rq-dashboard
```

Access the dashboard:
```
http://hostname:9181/default
```

Other Tips
----------------

### Enqueue via shell

```
find /media/hdd/recorded/ -name *ゆるゆり* -exec ./enqueue.sh {} hoge \;
```
