import rospy
from clover import srv
from std_srvs.srv import Trigger


def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='', auto_arm=False, tolerance=0.3):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if (telem.x ** 2 + telem.y ** 2 + telem.z ** 2) ** 0.5 < tolerance:
            break
        rospy.sleep(0.2)

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)


while True:
    try:
        telemetry = get_telemetry()
        print(f'x={telemetry.x} y={telemetry.y} z={telemetry.z}')
        dx, dy, dz = list(map(int, input('Enter dx, dy, dz: ').split()))
        print(f'Drone goes dx={dx} dy={dy} dz={dz}')
        navigate_wait(x=dx, y=dy, z=dz, frame_id='body', auto_arm=True)
        rospy.sleep(5)
    except (KeyboardInterrupt, ValueError):
        land()
        break
