from guizero import App, Text, PushButton

def change_message():
    message.value = 'You pressed the button!'

app = App(title='Title App')

message = Text(app, text='Welcome to the Hello World app!')

button = PushButton(app, text='Press me', command=change_message)

app.display()
