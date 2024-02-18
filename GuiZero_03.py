from guizero import App, Text, TextBox, PushButton, Box


def rot13 (plaintext):
    ciphertext = ""
    for pt_chr in plaintext:
        # Check if it's an alpha character (otherwise leave unchanged)
        # convert to a number
        pt_int = ord(pt_chr)
        if (pt_int >= ord('A') and pt_int <= ord('Z')):
            # it's upper case
            # add 13
            ct_int = pt_int + 13
            # check to see if we need to wrap around
            if ct_int > ord('Z'):
                ct_int -= 26
            ciphertext += chr(ct_int)
        elif (pt_int >= ord('a') and pt_int <= ord('z')):
            # it's  lower case
            # add 13
            ct_int = pt_int + 13
            # check to see if we need to wrap around
            if ct_int > ord('z'):
                ct_int -= 26
            ciphertext += chr(ct_int)
        else:
            # not alpha char so just add
            ciphertext += pt_chr
    return ciphertext


def encrypt():
    encrypted_text = rot13 (plaintext_text.value)
    ciphertext_text.value = encrypted_text


def decrypt():
    decrypted_text = rot13 (ciphertext_text.value)
    plaintext_text.value = decrypted_text


def clear_text():
    plaintext_text.value = ""
    ciphertext_text.value = ""


app = App(title="ROT13", width=800, height=600)
title = Text(app, text="Convert to/from ROT 13", size=24, height=2)
plaintext_title = Text(app, text="Plaintext:")
plaintext_text = TextBox(app, width=90, height=10, multiline=True)
buttons_box = Box(app, height=80, width=220)
# Buttons are contained within the Box
encrypt_button = PushButton(buttons_box, text="Encrypt", align="left", command=encrypt)
decrypt_button = PushButton(buttons_box, text="Decrypt", align="left", command=decrypt)
clear_button = PushButton(buttons_box, text="Clear", align="left", command=clear_text)
ciphertext_title = Text(app, text="Ciphertext:")
ciphertext_text = TextBox(app, width=90, height=10, multiline=True)

app.display()