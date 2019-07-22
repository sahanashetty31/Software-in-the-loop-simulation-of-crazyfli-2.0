#!/usr/bin/env python

import rospy
import crazyflie
import time
import uav_trajectory
import math

def circle_trajectory(freq, duration,r):
    x = list()
    y = list()
    t = list()
    for i in range(freq):
        t0 = 2 * math.pi * (1.0/(freq-1)) * duration * i
        x.append(r * math.cos(t0/duration))
        y.append(r * math.sin(t0/duration))
        t.append((1.0/(freq-1)) * duration * i)
    return (t,x,y)

if __name__ == '__main__':
    rospy.init_node('test_high_level')

    cf1 = crazyflie.Crazyflie("cf1", "/cf1")
    cf2 = crazyflie.Crazyflie("cf2", "/cf2")
    cf3 = crazyflie.Crazyflie("cf3", "/cf3")
    cf4 = crazyflie.Crazyflie("cf4", "/cf4")

    cf1.setParam("commander/enHighLevel", 1)
    cf2.setParam("commander/enHighLevel", 2)
    cf3.setParam("commander/enHighLevel", 3)
    cf4.setParam("commander/enHighLevel", 4)

    cf1.takeoff(targetHeight = 1.5, duration = 2.0)
    cf2.takeoff(targetHeight = 1.5, duration = 2.0)
    cf3.takeoff(targetHeight = 1.5, duration = 2.0)
    cf4.takeoff(targetHeight = 1.5, duration = 2.0)
    time.sleep(5.0)

    # (t , x , y) = circle_trajectory(50 , 10 , 0.8)

    # cf.goTo(goal = [0.8, 0, 1.5], yaw=0.0, duration = 4, relative = False)
    # time.sleep(4)

    # for i in range(len(x)):
    #     cf.goTo(goal = [x[i], y[i], 1.5], yaw=0.0, duration = 10.0/50.0, relative = False)
    #     time.sleep(1*10.0/50.0)

    # # # cf.land(targetHeight = 0.0 , duration = 4.0)
    # # # time.sleep(20.0)
    # # # rospy.spin()
    # # cf.goTo(goal = [0.5, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
    # # time.sleep(15.0)

    cf1.land(targetHeight = 0.0, duration = 2.0)
    cf2.land(targetHeight = 0.0, duration = 2.0)
    cf3.land(targetHeight = 0.0, duration = 2.0)
    cf4.land(targetHeight = 0.0, duration = 2.0)
    time.sleep(3.0)
    
    # traj1 = uav_trajectory.Trajectory()
    # traj1.loadcsv("takeoff.csv")

    # traj2 = uav_trajectory.Trajectory()
    # traj2.loadcsv("losange.csv")

    # print(traj2.duration)

    # cf.uploadTrajectory(0, 0, traj2)
    # # cf.uploadTrajectory(1, len(traj1.polynomials), traj2)

    # cf.startTrajectory(0, timescale=1.0)
    # time.sleep(traj2.duration * 2.0)

    # cf.startTrajectory(1, timescale=2.0)
    # time.sleep(traj2.duration * 2.0)

    # cf.startTrajectory(0, timescale=1.0, reverse=True)
    # time.sleep(traj1.duration * 1.0)

    cf1.stop()
    cf2.stop()
    cf3.stop()
    cf4.stop()
