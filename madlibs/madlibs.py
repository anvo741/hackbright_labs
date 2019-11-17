"""A madlib game that compliments its users."""

from random import choice, sample, randint

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, randint(1, 14))

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    response = request.args.get("game")
    if response == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib', methods=["POST", "GET"])
def show_madlib():
    madlibs = ["madlib.html", "madlib2.html", "madlib3.html"]
    person = request.values.get("person")
    colors = request.values.getlist("colors")
    noun = request.values.get("noun")
    adjective = request.values.get("adjective")
    return render_template(choice(madlibs),
                            person=person,
                            colors=colors,
                            noun=noun,
                            adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
