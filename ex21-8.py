from collections import Counter
def compute_top_k_variance(students, scores, k):
    counts = Counter(students)
    all_scores = {s: [] for (s, v) in counts.items() if v >= k}
    for s, score in zip(students, scores):
        if s in all_scores:
            all_scores[s].append(score)

    top_k_scores = {}
    for s in all_scores:
        top_k_scores[s] = sorted(all_scores[s])[-k : ]

    result = {}
    for s in top_k_scores:
        mean = sum(top_k_scores[s]) / k
        variance = sum((score - mean)**2 for score in top_k_scores[s])
        result[s] = variance
    return result