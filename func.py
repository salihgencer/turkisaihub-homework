def loginControl(usernameInput, surnameInput):
    username= "Salih"
    surname = "Gencer"

    if username == usernameInput and surname == surnameInput:
        return True
    else:
        return False

def pointControl(point):
    new_point = 0
    
    try:
        new_point = int(point)
    except ValueError:
        pass

    if new_point > 0 and new_point <= 100:
        return point
    else:
        return 0