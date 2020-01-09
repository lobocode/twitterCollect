# twitterCollect
A data filtering tool

### Prerequisites

To install twitter collect you will need to install the docker, and docker compose:

```bash
sudo curl -sSL https://get.docker.com/ | sh
```

```bash
sudo curl -L --fail https://github.com/docker/compose/releases/download/1.25.0/run.sh -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
```

---

### How to install


1. Clone project repo and enter the project folder:

```bash
git clone https://github.com/lobocode/twitterCollect && cd twitterCollect
```

2. Enter the docker directory and run the following command:
```bash
docker-compose up -d 
```

Or if you prefer an easier way, just run the command below:

```bash
curl -s url | bash
```

---

### How to use