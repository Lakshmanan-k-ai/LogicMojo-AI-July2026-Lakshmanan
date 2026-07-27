#SCORES DICTIONARY
scores = {"Ada": 91, "Alan": 72, "Grace": 85}
score_sum = 0
for(name, score) in scores.items():  
    print(f"{name}: {score}")
    score_sum += score

print(f"Average score:{score_sum/len(scores):.2f}")