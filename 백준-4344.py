class_count = int(input())
score_list = [[0] for _ in range(class_count)]
student_num_list = [0 for _ in range(class_count)]
class_avg = [0 for _ in range(class_count)]

def get_all_avg():

    for i in range(len(score_list)):
        class_avg[i] = sum(score_list[i]) / student_num_list[i]

    return  

def compare():
    bad_student = 0

    for i in range(len(score_list)):
        for j in range(len(score_list[i])):
            if(class_avg[i] < score_list[i][j]):
                bad_student += 1
        rate = (bad_student / student_num_list[i]) * 100
        print("{:.3f}%".format(rate))
        bad_student = 0
    
    return

for i in range(class_count):
    student_num_list[i], *score_list[i] = list(map(int, input().split())) 

get_all_avg()
compare()
