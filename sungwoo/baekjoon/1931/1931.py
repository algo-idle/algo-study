import sys

read = sys.stdin.readline
N = int(read())
meeting_list = [list(map(int, read().split())) for _ in range(N)]
meeting_list.sort(key=lambda x : (x[1],x[0]))
count = 0
end_time = 0

for start, end in meeting_list:
    if start >= end_time:
        count += 1
        end_time = end
print(count)

# import sys
#
# read = sys.stdin.readline
# N = int(read())
# meeting_list = [list(map(int, read().split())) for _ in range(N)]
# latest_time = max(i[1] for i in meeting_list)
# time_table = [1 for _ in range(latest_time)]
# count = 0
#
# for m in meeting_list:
#     m.append(m[1] - m[0])
# meeting_list.sort(key=lambda a: a[2])
#
# for meeting in meeting_list:
#     enable = 1
#     start_time = meeting[0]
#     end_time = meeting[1]
#     if start_time == end_time:
#         count += 1
#         continue
#     for i in range(start_time, end_time):
#         if not enable:
#             break
#         enable *= time_table[i]
#     if enable:
#         for i in range(start_time, end_time):
#             time_table[i] = 0
#         count += 1
# print(count)