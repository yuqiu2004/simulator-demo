## ns-3

文档地址
- 概述         https://pypi.org/project/ns3/#building-ns-3
- 详细api介绍   https://www.nsnam.org/doxygen/index.html
- 第三方学习资料 
    - https://github.com/osedu/ns3-introduction-video-tutorial-2025/tree/main
    - https://github.com/Vivek-anand-jain/Implementation-of-TCP-Fit-in-ns-3/blob/master/doc/manual/source/python.rst
    - https://www.nsnam.org/wiki/Python_bindings
    - https://forsworns.github.io/zh/blogs/20200616/
    - https://ns3-code.com/ns3-python/ 


### 环境问题

- 使用pip下载ns3的时候 即`pip install ns3` 可能会发生构建错误 提示这是一个与pip无关的错误 那么原因可能是系统中缺少基础的构建工具

    `sudo apt install build-essential python3-dev libffi-dev clang` 下载相关工具再尝试是否可以正常下载ns3库

- pip环境下python3.10似乎不能成功调用ns3

    需要尝试降低python version or 使用源码构建

### todo

我们先针对性看吧, 有线怎么设置网络拓扑, 怎么设置有线属性
无线怎么设置发送方, 设置接收方, 怎么设置干扰, 怎么设置各种属性

你能不能先确认 examples 支持哪些

```shell
# https://zoejiang2222.github.io/2025/02/14/ns3%E5%AE%89%E8%A3%85/
apt install g++ python3 cmake ninja-build git gir1.2-goocanvas-2.0 python3-gi 
python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3 tcpdump wireshark sqlite 
sqlite3 libsqlite3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools openmpi-bin 
openmpi-common openmpi-doc libopenmpi-dev doxygen graphviz imagemagick python3-sphinx 
dia imagemagick texlive dvipng latexmk texlive-extra-utils texlive-latex-extra 
texlive-font-utils libeigen3-dev gsl-bin libgsl-dev libgslcblas0 libxml2 libxml2-dev 
libgtk-3-dev lxc-utils lxc-templates vtun uml-utilities ebtables bridge-utils libxml2 
libxml2-dev libboost-all-dev

git clone https://gitlab.com/nsnam/ns-3-dev.git
cd ns-3-dev
git checkout -b ns-3.46 ns-3.46

./ns3 configure --enable-examples --enable-tests
./test.py

# https://gitlab.com/cttc-lena/nr
cd contrib
git clone https://gitlab.com/cttc-lena/nr.git
cd nr
git checkout -b 5g-lena-v4.1.1 origin/5g-lena-v4.1.1

./ns3 configure --enable-examples --enable-tests
# 需要看到
# SQLite support                : ON
# Eigen3 support                : ON

./ns3 build

./ns3 show targets | grep nr
# nix-vector-routing            nr
# cttc-lte-ca-demo              cttc-nr-3gpp-calibration-user
# cttc-nr-cc-bwp-demo           cttc-nr-demo
# cttc-nr-mimo-demo             cttc-nr-multi-flow-qos-sched
# cttc-nr-notching              cttc-nr-simple-qos-sched
# cttc-nr-traffic-3gpp-xr       cttc-nr-traffic-ngmn-mixed

./ns3 run cttc-nr-demo
```


## 预测模型

### trace-model

F:(cpu,memory,resolution)→(latency,accuracy)

- 输入：资源配额与输入规模 
- 输出：任务执行性能指标

### execution-model

1. 根据输入的分辨率创建docker容器任务
2. 等待容器执行结束
3. 在指定的唯一的路径下提取采集结果
4. 将结果返回 删除容器
