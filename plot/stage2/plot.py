import matplotlib.pyplot as plt
import math

def plot_percentile(path):
    lines = open(path).readlines()
    x = []
    y = []
    for line in lines:
        content = line.split()
        x.append(float(content[1]))
        y.append(math.log(float(content[0])))
        # y.append(float(content[0]))
    l = path.split('.')[0]
    plt.plot(x, y, label=f'{l}')  

def plot_percentiles():
    # ./wrk -D exp -t 1 -c 100 -d 20 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R 1000
    # plot_percentile("r=5 c=10.txt")
    # plot_percentile("r=10 c=10.txt")
    plot_percentile("iwlc_compose_percentil.txt")
    plot_percentile("weighted_least_conn_compose_percentil.txt")
    plot_percentile("weighted_round_robin_compose_percentil.txt")
    plot_percentile("two_choice_compose_percentil.txt")
    # plot_percentile("r=100 c=10.txt")
    plt.xlabel("percentile")
    plt.ylabel("latency (log)")
    plt.grid(True)
    plt.legend()
    plt.title("Latency Percentile for 1000 Request Per Second")
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    plt.rc('font', size=12)
    plt.savefig("percentile4.png")

def plot_throughput():
    # for i in 10000 20000 30000 40000 50000
    # do
    #     ./wrk -t1 -c50 -d5s -R"$i" --latency http://127.0.0.1:8080
    # done
    # x = [10000, 20000, 30000, 40000, 50000]
    # iwlc = [9933.50, 19871.81, 29789.78, 39671.94, 43893.28]
    # two_choice = [9936.94, 19874.54, 29805.78, 39673.40, 44160.51]
    # rr = [9935.34, 15970.35, 29817.37, 39364.03, 40247.22]
    # least_conn = [9932.96, 19869.79, 29820.37, 39669.51, 42159.49]

    # for i in 500 10000 15000 20000 25000 30000 35000 40000 45000 50000
    # do
    #     ./wrk -t1 -c50 -d5s -R"$i" --latency http://127.0.0.1:8080
    # done
    # x = [500, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    # iwlc = [489.73, 9934.96, 14908.13, 19872.88, 24841.08, 29816.60, 34772.76, 39712.30, 44001.65, 43896.96]
    # two_choice = [489.66, 9933.32, 14906.07, 19876.25, 24842.57, 29811.33, 34752.95, 39653.13, 43477.68, 44796.36]
    # rr = [489.58, 9936.62, 14903.11, 19876.34, 24842.07, 29812.52, 34781.36, 39680.40, 41945.18, 42291.12]
    # least_conn = [489.65, 9937.12, 14907.30, 19872.38, 24834.55, 29801.94, 34769.10, 39680.33, 40904.72, 42111.62]

    # for i in 200 300 400 500 600 700 800 900 1000 1100
    # do
    #         ./wrk -D exp -t 1 -c 100 -d 10 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R"$i"
    #         sleep 3
    # done
    # for i in 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500
    # do
    #         ./wrk -D exp -t 1 -c 100 -d 10 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R "$i"
    #         sleep 3
    # done
    x = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
    iwlc = [198.66, 297.92, 397.02, 494.85, 594.48, 691.05, 791.45, 889.38, 966.35, 958.23, 959.67, 961.05, 968.01, 941.90]
    two_choice = [198.72, 297.93, 396.93, 494.93, 594.19, 691.20, 791.64, 879.16, 974.68, 1070.53, 1166.45, 1263.06, 1360.95, 1458.25]
    rr = [198.66, 297.70, 396.94, 494.84, 588.52, 642.99, 647.19, 592.75, 642.38, 651.71, 649.39, 625.05, 638.98, 636.36]
    least_conn = [198.71, 298.01, 396.92, 494.99, 594.60, 691.35, 791.99, 890.48, 935.45, 957.41, 944.99, 946.64, 930.82, 875.57]
    
    plt.plot(x, iwlc, label='iwlc')
    plt.plot(x, two_choice, label='two_choice')
    plt.plot(x, rr, label='weighted_round_robin')
    plt.plot(x, least_conn, label='weighted_least_conn')
    plt.plot(x, x, label='Maximum_Throughput')
    plt.grid()
    plt.ylabel("Throughput")
    plt.xlabel("Request_Per_Second")
    plt.legend()
    plt.title("Throughput Comparison")
    plt.savefig("throughput4.png")

def plot_mean_std():
    # for i in 500 10000 15000 20000 25000 30000 35000 40000 45000 50000
    # do
    #     ./wrk -t1 -c50 -d5s -R"$i" --latency http://127.0.0.1:8080
    # done
    # x = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
    # iwlc_mean = [5.414, 5.750, 6.921, 7.463, 9.462, 10.957, 14.862, 24.143, 50.646, 762.995]
    # iwlc_std = [2.126, 2.324, 3.448, 3.396, 4.848, 5.578, 8.057, 13.716, 31.709, 681.145]
    # two_choice_mean = [5.245, 6.011, 7.025, 7.896, 10.429, 13.231, 14.663, 53.742, 58.172, 67.846]
    # two_choice_std = [2.152, 2.852, 3.934, 4.371, 5.915, 7.892, 34.198, 113.209, 114.010, 115.317]
    # rr_mean = [5.606, 6.297, 7.712, 10.710, 15.023, 319.874, 934.865, 1305.211, 1740.204, 2110.322]
    # rr_std = [2.590, 3.155, 4.643, 10.062, 12.496, 363.775, 726.097, 988.544, 1147.391, 1314.724]
    # least_conn_mean = [5.362, 5.695, 6.578, 7.449, 10.325, 12.113, 17.956, 168.697, 499.054, 940.186]
    # least_conn_std = [2.710, 2.075, 2.955, 3.383, 8.706, 7.058, 11.645, 147.458, 486.236, 785.396]

    # for i in 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500
    # do
    #         ./wrk -D exp -t 1 -c 100 -d 10 -L -s ./scripts/media-microservices/compose-review.lua http://localhost:8080/wrk2-api/review/compose -R "$i"
    #         sleep 3
    # done
    x = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
    iwlc_mean = [5.959, 5.956,6.817, 7.790, 8.933, 10.668, 14.750, 28.387, 160.907, 617.170, 906.286, 1192.221, 1413.780, 1737.797]
    iwlc_std = [3.161, 2.583, 3.258, 3.795, 4.421, 5.597, 8.706, 24.203, 129.043, 551.248, 736.456, 929.407, 1036.634, 1246.666]

    two_choice_mean = [5.780, 6.137, 7.157, 8.622, 10.297, 13.608, 19.481, 30.619, 55.497, 67.707, 74.745, 80.617, 84.667, 95.802]
    two_choice_std = [2.421, 2.837, 3.696, 4.824, 6.424, 7.907, 17.836, 35.871, 106.292, 117.712, 124.606, 129.911, 119.159, 127.223]

    rr_mean = [5.414, 5.994, 7.615, 9.700, 22.149, 358.932, 863.376, 1492.178, 1720.660, 1922.819, 2190.973, 2500.207, 2660.776, 2828.177]
    rr_std = [2.269, 2.693, 5.527, 6.467, 31.042, 358.249, 753.047, 1146.275, 1181.174, 1320.752, 1408.652, 1565.471, 1614.774, 1697.832]

    least_conn_mean = [5.355, 5.630, 6.580, 7.383, 8.823, 11.072, 15.493, 26.917, 326.252, 587.170, 958.021, 1231.951, 1431.174, 2033.647]
    least_conn_std = [1.918, 2.221, 3.386, 3.478, 4.460, 6.368, 9.780, 19.500, 298.838, 527.823, 782.261, 993.604, 1129.159, 1379.804]
    plt.subplot(2,2,1)
    plt.errorbar(x, iwlc_mean, iwlc_std, linestyle='None', marker='.', label = 'iwlc', color='r')
    plt.legend(loc='upper left')

    plt.subplot(2,2,2)
    plt.errorbar(x, two_choice_mean, two_choice_std, linestyle='None', marker='.', label = 'two_choice', color='g')
    plt.legend(loc='upper left')
    
    plt.subplot(2,2,3)
    plt.errorbar(x, rr_mean, rr_std, linestyle='None', marker='.', label = 'weighted_round_robin', color='y')
    plt.legend(loc='upper left')

    plt.subplot(2,2,4)
    plt.errorbar(x, least_conn_mean, least_conn_std, linestyle='None', marker='.', label = 'weighted_least_conn', color='b')
    plt.legend(loc='upper left')

    # plt.subplot(3,1,3)
    # plt.plot(x, iwlc_mean, label = 'iwlc', color='r', marker='.')
    # plt.plot(x, two_choice_mean, label = 'two_choice', color='g', marker='.')
    # plt.plot(x, rr_mean, label = 'weighted_round_robin', color='y', marker='.')
    # plt.plot(x, least_conn_mean, label = 'weighted_least_conn', color='b', marker='.')
    # plt.xlabel("Request Per Second")
    # plt.legend(loc='upper left')
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)
    plt.show()
    plt.savefig("mean_std4.png")

def plot_mean():
    x = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
    iwlc_mean = [5.959, 5.956,6.817, 7.790, 8.933, 10.668, 14.750, 28.387, 160.907, 617.170, 906.286, 1192.221, 1413.780, 1737.797]

    two_choice_mean = [5.780, 6.137, 7.157, 8.622, 10.297, 13.608, 19.481, 30.619, 55.497, 67.707, 74.745, 80.617, 84.667, 95.802]

    rr_mean = [5.414, 5.994, 7.615, 9.700, 22.149, 358.932, 863.376, 1492.178, 1720.660, 1922.819, 2190.973, 2500.207, 2660.776, 2828.177]

    least_conn_mean = [5.355, 5.630, 6.580, 7.383, 8.823, 11.072, 15.493, 26.917, 326.252, 587.170, 958.021, 1231.951, 1431.174, 2033.647]
    plt.plot(x, iwlc_mean, label = 'iwlc', color='r', marker='.')
    plt.plot(x, two_choice_mean, label = 'two_choice', color='g', marker='.')
    plt.plot(x, rr_mean, label = 'weighted_round_robin', color='y', marker='.')
    plt.plot(x, least_conn_mean, label = 'weighted_least_conn', color='b', marker='.')
    plt.xlabel("Request Per Second")
    plt.legend(loc='upper left')
    plt.title("Average Latency Comparison")
    plt.show()
    plt.savefig("mean4.png")

# plot_percentiles()
# plot_throughput()
# plot_mean_std()
plot_mean()
