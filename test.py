import japi

j = japi.Joystick(0)
while True:
    try:
        j.read()
        print('axes:    ', j.axis_states, j.button_states)
        print('buttona: ', j.button_states)
    except KeyboardInterrupt:
        j.close()
        break