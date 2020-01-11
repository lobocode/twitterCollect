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

Install python virtual env

```
pip3 install virtualenv --user && virtualenv /path/to/apop/twitterCollect .venv
```

Install nodejs

```
pip install nodejs 
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

Access API with your browser the following url:

```
localhost:3000/api/show-fls
localhost:3000/api/group-hrs

```

Access frontEnd:

```
cd front && sudo npm run build && npm install -g serve && serve -s build
```

And now open in your web browser:

```
localhost:5000
```

As you can see below:

![tcollect](https://raw.githubusercontent.com/lobocode/twitterCollect/master/img/tcollect.png)




