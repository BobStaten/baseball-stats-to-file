# this program will store player stats in a file and update to produce a running average
def j_stats(hits,abs):
    tot_hits = 0
    tot_abs = 0
    avg = 0.0

    with open('stats.txt', 'a+') as f:
        f.write(str(hits) +'\n')
        f.write(str(abs) + '\n')

    with open('stats.txt', 'r') as f:
        for line in f.readlines():
           # print(line)
            for i in range(len('stats.txt')):
            #    print(i)
                if i == 0:
                    tot_hits = hits
             #       print(tot_hits)
                    tot_abs = abs
                elif i != 0 and i % 2 == 0:
                    tot_hits += hits
              #      print("HITS" + ' ' + str(tot_hits))
                else:
                    tot_abs += int(abs)
               #     print("AT BATS" + str(tot_abs))
        avg = tot_hits/tot_abs
              #  avg = int(line[0])/int(line[1])
    return round(avg, 3)

print(j_stats(2,3))
print(j_stats(0,3))
#print(j_stats(1,3))
