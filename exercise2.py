

def teilabr(x,y):
    if y == 0:
        print("es ist nicht möglich durch 0 zu teilen")
    elif y == x:
        print("x und y sind gleich")
        
    else:
        if x%y == 0:
            print("x ist durch y teilbar")
        else: 
            print ("x ist nicht durch y teilbar")
        