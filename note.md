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