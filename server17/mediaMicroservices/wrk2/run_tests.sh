for i in 500 10000 15000 20000 25000 30000 35000 40000 45000 50000
do
    ./wrk -t1 -c50 -d5s -R"$i" --latency http://127.0.0.1:8080	
done
