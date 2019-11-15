import rospy
from std_msgs.msg import String

def messageCallback(data):
    rospy.loginfo(rospy.get_caller_id() + ": I heard %s", data.data)

nodeName = "Node1"

print("Running node " + name)
rospy.init_node(nodeName, anonymous=True)
rospy.Subscriber("topic_name", String, messageCallback)
rospy.spin()
