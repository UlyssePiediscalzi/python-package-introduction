import time

def try_me():
    test = input('What is orange and sound like a parrot ?')
    success = "Congratulation O Riddle Master, you passed the test!"
    failure = f"' {test} ' is not the right answer... Try again !"
    if test.lower() in ["a carrot", "carrot", "carot", 'the carrot']:
        print(f"You answered '{test}'...")
        time.sleep(1)
        return success
    else:
        print(f"You answered '{test}'...")
        time.sleep(1)
        return failure
