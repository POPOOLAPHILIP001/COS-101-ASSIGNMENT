def calculate_speed():
    distance = float(input('enter distance  ='))
    time = float(input('enter time ='))
    speed = distance * time
    print('speed=', speed, 'm/s(meter/second')
calculate_speed()

def calculate_volume():
        length = float(input('what is the value of length='))
        breadth = float(input('what is the value of breadth='))
        width = float(input('what is the value of width='))
        volume = length * breadth * width
        print('volume =', volume, 'M^3(meter cube')
calculate_volume()

def calculate_displacement():
        velocity = float(input('enter velocity'))
        time = float(input('enter time'))
        displacement = velocity * time
        print(displacement)
calculate_displacement()


def calculate_area():
        length = float(input('what is the value of length = '))
        breadth = float(input('what is the value of breadth = '))
        area = length * breadth
        print('area = ', area, 'M(meters')
        calculate_area()

def calculate_work():
            force = float(input('enter force ='))
            displacement = float(input('enter displacement ='))
            work = force * displacement
            print('work =',work, 'j(joules)')
calculate_work()
