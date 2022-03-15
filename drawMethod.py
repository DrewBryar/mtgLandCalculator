def drawToHand(arr1, arr2):
    if(len(arr2) != 0):
        arr1.append(arr2[0])
        arr2.pop(0)
    else:
        print("You drew yourself out! You lose.")
        return 0