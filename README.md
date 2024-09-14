# HITSZ OSA 镜像站告警分析服务

## 启动命令
```bash
### 首先创建虚拟环境并进入，然后继续下一步 ###
pip install -r requirements.txt
# 启动开发用服务器
uvicorn src.main:app --port 10086 # 执行时的路径位置应在 alerter/，即本 README.md 同级目录
```
## 正常工作

POST 目标路径为 `localhost:10086/notification`

## 进一步开发

### 挑选 JSON 参数
`alerter/src/forwarder/router.py` 中有 `forward` 函数，修改其中的 message 变量