def main():
    pulse_rate = int(input("Enter your pulse rate"))
    heart_beat_rate = int(input("enter your heart_beat_rate"))
    blood_pressure = float(input("Enter your blood pressure"))
    temperature = float(input("Enter your temperature rate"))
    try:
        if pulse_rate == int(76) and heart_beat_rate == int(76) and blood_pressure == float(180.20) and temperature == float(37.0):
            print("Vital Signs Normal")
        elif pulse_rate == int(40) and heart_beat_rate == int(55) and blood_pressure == float(100.20) and temperature == float(37.0):
            print("Vital signs critical")
        else:
            print("Life functions critical")
    except ValueError:
        print("Enter a number")

