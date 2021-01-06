# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greeting(name, greeting_template="Hello", greeting_template_part2=" !"):
    return "\033[3m"+greeting_template+" "+name+greeting_template_part2+"\033[0m"


def force(mass, body="Aarde"):
    bodies = {"Zon": 274,
              "Jupiter": 24.92,
              "Neptunis": 11.15,
              "Saturnus": 10.44,
              "Aarde": 9.798,
              "Uranus": 8.87,
              "Venus": 8.87,
              "Mars": 3.71,
              "Mercurius": 3.7,
              "Maan": 1.62,
              "Pluto": 0.58}
    g = bodies.get(body, "Undefined")
    if (g != "undefined"):
        print(
            f"De zwaartekracht op een voorwerp van {mass} kg op {body} is {round(mass*g,2)} Newton")
        return round(mass*g, 2)
    else:
        return "undefined"


def pull(mass1, mass2, diameter, body):
    g = 6.674*10**(-11)
    if diameter != 0:
        pull = round(g*(mass1*mass2)/diameter**2, 2)
        print(
            f"De zwaartekracht op een voorwerp van {mass1} kg op {body} is {pull} Newton")
        return pull
    else:
        return 0


# of course the greeting can be interpreted a bit differently but i think this approach should suffice
print(greeting("doc"))
print(greeting("Bob", "what's up"))
force(1.2)
force(mass=3.4, body="Maan")
pull(mass1=0.1, mass2=5.972*10**24, diameter=6.371*10**6, body="aarde")
