for i in "least_conn" "iwlc" "two_choice" "rr"
do
	cp /home/public/DeathStarBench/mediaMicroservices/docker-compose-"$i".yml /home/public/DeathStarBench/mediaMicroservices/docker-compose.yml
	./wrk -D exp -t 1 -c 100 -d 20 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R 800
	cd ..
	docker-compose stop
	docker-compose up -d
	cd wrk2
	sleep 20
done
