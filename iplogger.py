from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    with open('ip_log.txt', 'a') as log_file:
        log_file.write(f"{user_ip}\n")
    return f"Your IP address is: {user_ip}"

if __name__ == '__main__':
    app.run(debug=True)
