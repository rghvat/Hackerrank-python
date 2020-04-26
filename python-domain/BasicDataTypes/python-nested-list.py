if __name__ == '__main__':
    score_cards = list()
    scores = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        score_cards.append([name, score])
    
    # find second min in list
    first = min(scores)
    second = max(scores)
    for ele in scores:
        if first<ele and ele<second:
            second = ele
            
    # collecting all names who have second rank
    names = list()
    for ele in score_cards:
        if ele[1] == second:
            names.append(ele[0])
    names.sort()
    print(*names, sep='\n')
