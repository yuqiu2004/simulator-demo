## ns-3

### 环境问题

使用pip下载ns3的时候 即`pip install ns3` 可能会发生构建错误 提示这是一个与pip无关的错误 那么原因可能是系统中缺少基础的构建工具

`sudo apt install g++ build-essential python3-dev libffi-dev clang` 下载相关工具再尝试是否可以正常下载ns3库


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