from datetime import datetime
import json
from flask import Flask, render_template, request

# json.dump
# json.load
# json.dumps - в строку
# jdon.loads - из строки


def save_messages():
    data = {
        "messages": all_messages
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
  all_messages.append(message)
  save_messages()


# Выводим одно сообщение в данном формате
def print_message(msg):
  print(f"[{msg['author']}]: {msg['text']} / {msg['time']}")


# Выводим все сообщения
def print_all_messages():
    for message in all_messages:
        print_message(message)


def users_count():
    users = set()
    for el in all_messages:
        users.add(el['author'])
    return len(users)


def status():
    return {"users_count": users_count(), "messages_count": len(all_messages)}


all_messages = load_messages()
print(status())

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Hello!(sss)"


@app.route('/chat')
def chat_page():
    return render_template("form.html")


@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages, "status": status()}


@app.route("/send_message")
def send_message():
    name = request.args.get("name", "")
    text = request.args.get("text", "")
    add_message(name, text)
    return "ok"

app.run(host='0.0.0.0', port=8080)
