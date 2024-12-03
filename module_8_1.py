#"Try и Except"

def add_everything_up(a, b):
    try:
        return round((a + b) ,3)
    except TypeError as exc:
        #print(f"{exc} : {exc.args}")
        return str(a)+str(b)
    except Exception as exc:
        print(f"Operation is unable : {exc}")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))