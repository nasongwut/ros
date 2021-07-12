import rospy
from std_msgs.msg import String

def callback(data):
    print(data.Status)

def listener():
    rospy.init_node('SmartPole', anonymous=True)
    rospy.Subscriber('DroneStation', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()