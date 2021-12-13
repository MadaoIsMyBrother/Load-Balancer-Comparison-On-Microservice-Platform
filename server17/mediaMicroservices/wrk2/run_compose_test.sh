
for i in 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500
do
	./wrk -D exp -t 1 -c 100 -d 10 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R "$i"
        sleep 3
done
