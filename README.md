rtshell_core  [![Build Status](https://travis-ci.org/start-jsk/rtshell_core.png)](https://travis-ci.org/start-jsk/rtshell_core)
=====================

Metapackage that contains commonly used toolset for RT-Middleware-based modules (namely openrtm_aist_core). Although each of these packages by themselves are ROS-agnostic, you can use them over ROS together with the packages in rtmros_common.


Test Status
=====================
[Hydro](http://jenkins.ros.org/job/devel-hydro-rtshell_core/) [![Build Status](http://jenkins.ros.org/job/devel-hydro-rtshell_core/badge/icon)](http://jenkins.ros.org/job/devel-hydro-rtshell_core/)


[![Hydro Test Satus](http://jenkins.ros.org/job/devel-hydro-rtshell_core/test/trend)](http://jenkins.ros.org/job/devel-hydro-rtshell_core/)

[Groovy](http://jenkins.ros.org/job/devel-groovy-rtshell_core/) [![Build Status](http://jenkins.ros.org/job/devel-groovy-rtshell_core/badge/icon)](http://jenkins.ros.org/job/devel-groovy-rtshell_core/)

[![Groovy Test Satus](http://jenkins.ros.org/job/devel-groovy-rtshell_core/test/trend)](http://jenkins.ros.org/job/devel-groovy-rtshell_core/)

Usage
=====================


Get the list of running RT components
--------------------------------------------

```
$ rosrun rtshell rtls %HOST_ROBOT%:15005/
```

Note that the trailing backslash is required.
`%HOST_ROBOT%` is where `omniNames` and your `OpenRTM`-based components are running. For example if `nextage` is where your RT components are running:

```
$ rosrun rtshell rtls nextage:15005/
```