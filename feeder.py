from flask import Flask, flash, redirect, render_template, request, session, abort
import time
import RPi.GPIO as GPIO
from multiprocessing import Process

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)


def feed_pow(feed_time):
  while True:
    input_state = GPIO.input(23)
    if input_state == False:
      print ('DINNER')
      GPIO.output(18, True)
      time.sleep(feed_time)
      GPIO.output(18, False)


@app.route("/feed")
def feed():
    GPIO.output(18, True)
    time.sleep(4)
    GPIO.output(18, False)
    return 'HERE COMES THE BEAST'
  

@app.route("/")
def button():
    return render_template('redbutton.html')


if __name__ == "__main__":
  p2 = Process(target=app.run(host='0.0.0.0'))
  p1 = Process(target=feed_pow(3))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
