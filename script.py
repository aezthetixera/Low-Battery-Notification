from threading import Thread
import psutil
import plyer.platforms.win.notification
from plyer import notification
from playsound import playsound
import time


battery = psutil.sensors_battery()
is_plugged = battery.power_plugged
AlreadyNotifiedLow = False
AlreadyNotifiedHigh = False


def sound():
    playsound(r"files\notify.mp3")


def notification_low():
    notification.notify("Low Battery", f"""Battery is on {battery.percent}%.
Please, plug the charger.""")


def notification_high():
    notification.notify(
        "There is enough energy.",
        f"""Battery is on {battery.percent}!%.
Please, unplug the charger."""
    )


while True:
    if battery.percent <= 20 and AlreadyNotifiedLow is False and is_plugged is False:
        Thread(target=sound).start()
        Thread(target=notification_low).start()
        print("battery low notification started.")
        AlreadyNotified = True
    elif battery.percent <= 20 and is_plugged is True and AlreadyNotifiedLow is True:
        AlreadyNotified = False

    elif battery.percent >= 80 and is_plugged is True and AlreadyNotifiedHigh is False:
        Thread(target=sound).start()
        Thread(target=notification_high).start()
        print("battery high notification started.")
        AlreadyNotifiedHigh = True
    elif battery.percent >= 80 and is_plugged is False and AlreadyNotifiedHigh is True:
        AlreadyNotifiedHigh = False

    battery = psutil.sensors_battery()
    is_plugged = battery.power_plugged

    print("Sleep mode:")

# making a dependence of the sleep time on the percentage of battery charge
    if 80 <= battery.percent <= 100:
        print(f"Sleep mode on: {battery.percent}%, time: 14400")
        time.sleep(14400)
    elif 70 <= battery.percent < 80:
        print(f"Sleep mode on: {battery.percent}%, time: 12200")
        time.sleep(12200)
    elif 50 <= battery.percent < 70:
        print(f"Sleep mode on: {battery.percent}%, time: 7200")
        time.sleep(7200)
    elif 40 <= battery.percent < 50:
        print(f"Sleep mode on: {battery.percent}%, time: 2500")
        time.sleep(2500)
    elif 30 <= battery.percent < 40:
        print(f"Sleep mode on: {battery.percent}%, time: 500")
        time.sleep(500)
    elif 25 <= battery.percent < 30:
        print(f"Sleep mode on: {battery.percent}%, time: 300")
        time.sleep(300)
    else:
        print(f"Sleep mode on: {battery.percent}%, time: 100")
        time.sleep(100)
