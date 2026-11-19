<!-- docker build  -->

docker-compose up -d --build

<!-- getting into django shell in docker  -->

docker exec -it django /bin/sh

<!-- making end point executable  -->

chmod +x ./entrypoint.sh  