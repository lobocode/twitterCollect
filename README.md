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

---

### How to install


1. Clone project repo and enter the project folder:

```
git clone https://github.com/lobocode/twitterCollect && cd twitterCollect
```

2. Enter the docker directory and run the following command:
```
docker-compose up -d 
```

Or if you prefer an easier way, just run the command below:

```
curl -s url | sudo bash
```

---

### How to use

Access with your browser the following url:

```
localhost:3000/twittercollect
```