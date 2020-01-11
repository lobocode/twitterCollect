# twitterCollect
A data filtering tool

### Prerequisites

To install twitter collect you will need to install the docker, and docker compose:

```
sudo curl -sSL https://get.docker.com/ | sh
```

```
sudo curl -L --fail https://github.com/docker/compose/releases/download/1.25.0/run.sh -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
```

### Install venv

```
pip3 install virtualenv --user && virtualenv /path/to/apop/twitterCollect .venv
```



---

### How to install


1. Clone project repo and enter the project folder:

```
git clone https://github.com/lobocode/twitterCollect && cd twitterCollect && pip install -r requirements
```

2. Enter the docker directory and run the following command to install mongodb and mongo express:

```
docker-compose up -d 
```

3. Enable venv

```
source .venv/bin/activate
```

4. RUn the app

```
python twittercollect.py
```

---

### How to use

Access with your browser the following url:

```
localhost:5000/twittercollect
```