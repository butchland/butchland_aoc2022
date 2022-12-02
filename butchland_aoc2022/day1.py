
def generate_totals(input:list[str]):
    total = 0
    for l in input:
        if len(l) == 0:
            yield total

            total = 0        
        else:
            total += int(l)

    yield total

def sum_top_n(input, n):
    max_n = [0] * n
    low_max = 0 # track lowest
    low_index = 0 # index of lowest
    total = 0
    for total in generate_totals(input):
        if low_max < total:
            max_n[low_index] = total
            low_max = min(max_n)
            low_index = 0
            for i,m in enumerate(max_n):
                if m == low_max:
                    low_index = i
                    break                   
    
    return sum(max_n)