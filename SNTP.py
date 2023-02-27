A = input()
B = input()
C = input()
A_list = A.split(':')
B_list = B.split(':')
C_list = C.split(':')
time_diff = 0
if int(C_list[0] < A_list[0]):
    time_diff= 24*3600
time_diff += (int(C_list[0]) - int(A_list[0]))*3600 +  (int(C_list[1]) - int(A_list[1]))*60 + (int(C_list[2]) - int(A_list[2]))

time_diff = time_diff//2 + time_diff %2
hour_diff = time_diff // 3600
minute_diff = time_diff//60 - hour_diff*60
seconds_diff = time_diff - minute_diff*60 - hour_diff*3600

hour_final = int(B_list[0])
minutes_final = int(B_list[1])
seconds_final = int(B_list[2])

hour_final +=hour_diff
hour_final %=24
minutes_final += minute_diff
if minutes_final >=60:
    hour_final += minutes_final//60
    minutes_final%=60
seconds_final+=seconds_diff
if seconds_final >=60:
    minutes_final+= seconds_final//60
    seconds_final%=60

char_1 = hour_final
if hour_final <10:
    char_1 = '0' + str(hour_final)
char_2 = minutes_final
if minutes_final <10:
    char_2 = '0' + str(minutes_final)
char_3 = seconds_final
if seconds_final <10:
    char_3 = '0' + str(seconds_final)
print(f"{char_1}:{char_2}:{char_3}")
