point=(2, 2)
match point:
    case (x, y):
        if(x==y): print("x and y are equal")
    case (x, y) if x > y:
        print("x is greater than y")
    case (x, y) if x < y:
        print("x is less than y")
        