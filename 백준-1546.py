score_count = int(input())
score_list = list(map(int, input().split()))
new_score_list = [0 for _ in range(len(score_list))]
new_score = 0
result = 0
def new_avg():
    for i in range(len(score_list)):
        new_score = (score_list[i] / max(score_list)) * 100
        new_score_list[i] = new_score
    result = sum(new_score_list) / score_count
    print(result)

new_avg()

