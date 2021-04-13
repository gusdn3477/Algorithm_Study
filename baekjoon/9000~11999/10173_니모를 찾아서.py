while True:

    a = input()
    if a == "EOI":
        break

    a = a.upper()

    if "NEMO" in a:
        print("Found")

    else:
        print("Missing")