#one.py
def func():
    print("Func() in ONE.PY")

print("Top Level in One.PY")

if __name__ == "__main__":
    print("ONE.PY is being run directly!")
else:
    print("ONE.PY has been imported!")