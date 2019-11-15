import numpy
import cv2
import time 
import rospy
from std_msgs.msg import String


cap = cv2.VideoCapture(1)

pub = rospy.Publisher("computer_vision", String, queue_size=10)
rospy.init_node("OpenCVNode", anonymous=True)
rate = rospy.Rate(1) 

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    output = "Published from OpenCV"
    rospy.loginfo(output)
    pub.publish(output)
    rate.sleep()
cv2.destroyAllWindows()
cap.release()
