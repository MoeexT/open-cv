# open-cv

看书手抄的代码，随性更新中。

## 《OpenCV 3 计算机视觉 Python语言实现》

### Cameo项目, 人脸跟踪和图像处理的交互式应用

#### managers 高级I/O流接口

+ **CaptureManager()** 类读取帧，并将其分配到一个或多个输出中，这些输出包括图像、视频、以及窗口（通过WindowManager实现）。
+ **WindowManager()** 使代码以面向对象的形式处理窗口和事件。

#### cameo

*Cameo()* 类提供两种方法启动应用程序：run()和onkeypress()。初始化时，*Cameo()* 类会把onkeypress()作为回调函数创建 *WindowManager()* 类，而 *CaptureManager()* 类会使用摄像头和 *WindowManager()* 类。当调用run()函数时，在主循环里处理帧和事件，事件的处理通过调用onkeypress()函数完成。

+ 空格：截图保存到当前目录
+ tab：开始/停止录像
+ esc：退出应用程序

#### filters

通过不同的滤波处理给帧，从而在窗口看到不同的效果。

SharpenFilter 锐化滤波

![锐化滤波](/cameo/SharpenFilter.png)

FindEdgesFilter 边缘检测滤波

![边缘检测滤波](/cameo/FindEdgesFilter.png)

BlurFilter 模糊滤波

![模糊滤波](/cameo/BlurFilter.png)

EmbossFilter 浮雕滤波

![浮雕滤波](/cameo/EmbossFilter.png)
