
scores = [(90, 80), (85, 75), (90, 100)]

for i, score in enumerate(scores, start=1):
    total = sum(score)
    avg = total / len(score)
    print(f"{i}번 학생의 총점은 {total}점이고, 평균은 {avg:.1f}입니다.")
