import rospy
from std_msgs.msg import String

rospy.init_node('SmartPole', anonymous=True)
publisher = rospy.Publisher('/DroneStation', String, queue_size=1)
data = { 
        "Status": "Ready",
        "Voltage": "10",
 }

while not rospy.is_shutdown():
    publisher.publish(str(data))
    print(data)

    

