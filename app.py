from flask import Flask, render_template, redirect, request, url_for, flash, session
import mysql.connector
import bcrypt
from authlib.integrations.flask_client import OAuth
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
from dotenv import load_dotenv
import os

from flask import Flask

app = Flask(__name__)
app.secret_key = 'Tulus nak Meletuup'

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
