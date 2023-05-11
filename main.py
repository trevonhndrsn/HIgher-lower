from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def home():
    return '<h1 style="text-align: center">guess the number between 0-9</h1>' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExODQ0ZjM2NDU3NTJhN2I1NWI2ZmNhZDEwZjhmNTNmNGFlNTIxYzcxZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
                '<img src="https://media0.giphy.com/media/xT9Igvcmb2a903sPUk/200w.webp?cid=ecf05e47jto3zdgrzu6vf61oukvd98nburp2yys917bued2y&ep=v1_gifs_search&rid=200w.webp&ct=g">'

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media2.giphy.com/media/L9ClSZpUa0iuNiIH2u/giphy.webp?cid=ecf05e47i4pa9qozdtxlp3d1mkafe62i49ax4fhkomayhzen&ep=v1_gifs_search&rid=giphy.webp&ct=g'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media4.giphy.com/media/rngE31q0PTHbO/200w.webp?cid=ecf05e472wuaddpg36nty8yszvhbfx3jgylliqdkh0i1bx5r&ep=v1_gifs_search&rid=200w.webp&ct=g'/>"


if __name__ == "__main__":
    app.run(debug=True)