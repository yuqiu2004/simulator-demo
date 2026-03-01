from ns import ns
# 运行ns测试环境

ns.LogComponentEnable("Simulator", ns.LOG_LEVEL_ALL)

ns.Node node

ns.Simulator.Stop(ns.Seconds(10))
ns.Simulator.Run()
ns.Simulator.Destroy()