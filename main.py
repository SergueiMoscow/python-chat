from datetime import datetime # Импортируем библиотеку
import json
from flask import Flask, render_template, request

# json.dump
# json.load
# json.dumps - в строку
# jdon.loads - из строки




def save_messages():
    data = {
        "messages": all_new_messages
    }
    with open('db.json', 'w', encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)


def load_messages():
    with open('db.json', 'r') as file:
        data = json.load(file)
    return data['messages']


# Объявляем функцию для добавления сообщений
def add_message(author, text):
  message = {
      "author": author,
      "text": text,
      "time": datetime.now().strftime("%H:%M:%S")
  }
  all_new_messages.append(message)
  save_messages()


# Выводим одно сообщение в данном формате
def print_message(msg):
  print(f"[{msg['author']}]: {msg['text']} / {msg['time']}")


# Выводим все сообщения
def print_all_messages():
  for message in all_new_messages:
    print_message(message)


all_new_messages = load_messages()

# Добавляем сообщения в список
# add_message("Саша", "Привет всем")
# add_message(text="Привет, Саша", author="Юлия")
# add_message("Кирилл", "Очень интересно")
# add_message("Дарья", "Завтра точно буду еще участвовать")

save_messages()
#print_all_messages()
print(all_new_messages)

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Hello!(sss)"


@app.route('/chat')
def chat_page():
    return render_template("form.html")


@app.route('/get_messages')
def get_messages():
    return {'messages': all_new_messages}


@app.route("/send_message")
def send_message():
    name = request.args.get("name", "")
    text = request.args.get("text", "")
    add_message(name, text)
    return "ok"

app.run(host='0.0.0.0', port=8080)
