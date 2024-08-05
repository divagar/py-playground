from string import Template


def main():
    try:
        #string vs bytes
        s = "I am python"
        print(s)

        b = bytes([0x40, 0x41, 0x42, 0x43])
        print(b)

        print(s + b.decode("utf-8"))
        print(s.encode("utf-8") + b)

        #template string
        s = "Hello {0} {1}".format("Divagar", "Mohandass")
        print(s)

        t = Template("Hello ${firstname} ${lastname}")
        s1 = t.substitute(firstname = "Divagar", lastname = "Mohandass")
        print(s1)

        obj = {"firstname": "Divagar", "lastname": "Mohandass"}
        s2 = t.substitute(obj)
        print(s2)
    except Exception as e:
        print("unknown error occured ", e)
    finally:
        pass


main()
