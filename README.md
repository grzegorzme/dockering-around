# dockering-around

implementing a simple container architecture:
 - redis: common nosql data container
 - app1: simple flask app implementing
   - GET `/`: hello world
   - POST `/my_list/`: push a dict structure to be 'processed'
 - app2: simple flask app implementing
   - GET `/`: hello world
   - GET `/my_list/`: retrieve 'processed' data
 - processor: simple loop process watching for new `/my_list/` posts and processing them

## running the project
build the images:
```
$ docker-compose build
```
starting containers:
```
$ docker-compose up
```
teardown containers
```
$ docker-compose down
```
[optional] remove build images
```
$ docker rmi <image_id>
```
or remove EVERYTHING
```
$ docker rmi $(docker images -q)
```
