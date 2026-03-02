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