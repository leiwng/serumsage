# Design Notices

## Base Fact

罗氏拔盖机拍摄的血清试管图片分辨率：123x486, 124x476, ... 140x504, 142x509, 151x514
程序界面选定的血清试管图片分辨率为：160x545 (宽x高)
程序界面上用于显示血清试管图片和判读结果的区域分辨率为：1014x693 (宽x高) -> 338:231 -> 112:77 -> 16:11

## MobileNetV2 实现

这段代码是一个简化版的MobileNetV2模型的PyTorch实现。

首先，从`__init__`函数开始，模型的主要部分被定义。在这个模型中，我们可以看到有两个主要部分：`backbone`和`fc`。

`backbone`是卷积网络的主体部分，包含了一系列的卷积层、ReLU激活函数、最大池化层和被称为Block的自定义层。每个Block可能包含多个卷积层、激活函数和其他操作。这里的Block没有给出具体的定义，所以我无法给出更详细的解释。然而，根据参数，我们可以推测每个Block可能包含一个或多个卷积层，以及可能的下采样（步长大于1）。

`fc`是全连接层部分，它在卷积网络部分之后，用于分类任务。这里有两个线性层，第一个线性层的输入维度是16*4*4 + 32*8*8，输出维度是64；第二个线性层的输入维度是64，输出维度是3。

在`forward`函数中，输入数据x通过每一层，并在每一步之后进行处理。注意这里的两个特点：首先，在通过layer7之后，我们保存了x的副本（`x_temp`）。然后，在通过layer13之后，我们将`y1`和`x_temp`连接起来。这是一种常见的技术，称为跳过连接或残差连接，可以帮助网络学习恒等函数，并有助于梯度反向传播。

最后，我们将数据传递给全连接层，并对输出应用指数函数。这可能是为了确保输出是正数（因为指数函数的输出总是正数），但这取决于具体的应用场景。

总的来说，这是一个相对简单的MobileNetV2模型实现，用于图像分类任务。具体的细节（例如Block的实现和模型参数）可能会根据具体的应用需求和数据集进行调整。

## 对于QT5的APP检查许可证的时机

在使用Python和Qt5开发应用程序时，将用户许可证验证逻辑放入`MainWindow`的`__init__`构造函数中是可行的，但不一定是最佳的做法。这样做可以保证在主窗口显示之前进行许可证验证，但也有可能影响应用程序的启动时间和用户体验。以下是一些考虑因素和建议：

### 考虑因素

1. **用户体验**：许可证验证可能包括文件读取、网络请求等操作，这些操作可能导致延迟。在`__init__`中直接进行验证会阻塞主线程，可能导致应用启动时出现明显的延迟。

2. **错误处理**：如果将验证逻辑放在`__init__`中，必须小心处理验证失败的情况。例如，如果许可证无效，你可能需要显示一个错误消息并关闭应用，或者提供重新输入许可证的选项。

3. **代码组织**：将许可证验证逻辑直接放在`MainWindow`的构造函数中可能会使这个类变得过于复杂和难以维护。最好是将业务逻辑与界面逻辑分离。

### 建议的做法

1. **使用启动画面（Splash Screen）**：
   使用启动画面是处理初始化长时间操作的常用方法。在显示主窗口之前显示一个启动画面，可以在后台进行许可证验证，同时提供用户反馈，说明应用正在加载。

2. **异步操作**：
   如果许可证验证包括网络请求或其他可能导致阻塞的操作，考虑使用异步方法来处理这些操作，从而不会阻塞UI线程。

3. **独立的验证函数**：
   在`MainWindow`类外创建一个或多个函数来处理许可证验证逻辑。在`__init__`中调用这些函数，根据返回值决定是否继续加载主窗口。

4. **异常处理**：
   确保处理所有可能的错误情况，例如许可证文件缺失、格式错误或网络问题等，以便应用能够优雅地处理这些情况。

### 示例代码

下面是一个使用启动画面和异步验证的简单示例：

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QLabel
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self, license_valid):
        super(MainWindow, self).__init__()
        if not license_valid:
            raise Exception("许可证无效")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qt Application")
        self.setGeometry(300, 300, 250, 150)
        self.show()

def validate_license():
    # 模拟许可证验证过程
    # 在这里添加实际的验证逻辑
    return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen()
    splash.showMessage("正在验证许可证...", Qt.AlignLeft | Qt.AlignBottom, Qt.black)
    splash.show()
    QApplication.processEvents()

    # 延时模拟异步操作
    QTimer.singleShot(2000, splash.close)  # 假设验证需要2秒钟

    license_valid = validate_license()
    if license_valid:
        main_win = MainWindow(license_valid)
        main_win.show()
    else:
        QLabel("许可证验证失败！").show()

    sys.exit(app.exec_())
```

在这个示例中，我们使用了`QTimer`来模拟异步操作，并使用启动画面来给用户一个正在加载的提示。这种方法既优化了用户体验，也保证了代码的整洁和易于维护。

## 在SplashScreen中显示图片和文字

在Qt5中使用`QSplashScreen`添加图片和文字的方法相对简单。你首先需要一个图片文件，通常是PNG格式，可以透明匹配启动画面的形状和大小。以下是一个包括图片和文字的启动画面的示例步骤：

### 1. 准备图片

确保你有一个合适的图片文件。这个图片通常应该是应用程序的logo或者与应用程序主题相关的图形。图片路径应正确指向该文件。

### 2. 创建和显示`QSplashScreen`

使用图片创建一个`QSplashScreen`对象，并在显示它之前设置显示的文字和位置。

### 示例代码

下面是一个使用图片和文字的`QSplashScreen`示例：

```python
import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qt Application")
        self.setGeometry(300, 300, 250, 150)
        self.show()

def main():
    app = QApplication(sys.argv)

    # 加载启动画面图片
    pixmap = QPixmap("path_to_your_image.png")  # 确保路径正确
    splash = QSplashScreen(pixmap)
    splash.showMessage("正在加载...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
    splash.show()

    # 允许处理其他事件
    QApplication.processEvents()

    # 延时以模拟加载过程
    QTimer.singleShot(3000, splash.close)  # 延时3秒关闭启动画面

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

### 代码说明

- `QPixmap("path_to_your_image.png")`用于加载图片。替换`"path_to_your_image.png"`为你的图片文件的实际路径。
- `QSplashScreen(pixmap)`创建一个启动画面对象，其中`pixmap`是你加载的图片。
- `splash.showMessage("正在加载...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)`在启动画面上显示消息。这里你可以调整文本内容、位置和颜色。
- `QTimer.singleShot(3000, splash.close)`设置一个计时器，3秒后关闭启动画面。

确保在使用启动画面时，长时间运行的任务不会阻塞主事件循环。可以考虑使用线程或其他异步机制来管理耗时的初始化任务，这样可以保持界面的响应性。同时，也需要处理好在初始化任务完成前和后启动画面的适当显示和隐藏。这样的用户体验会更流畅，界面也显得更专业。

## 在SplashScreen中显示进度条

在Qt5的`QSplashScreen`中添加一个进度条涉及到一些工作，因为`QSplashScreen`本身并没有直接支持进度条。你可以使用绘图功能来模拟进度条的外观，或者使用透明窗口在`QSplashScreen`之上放置一个真正的进度条控件。下面，我将提供两种方法的示例：

### 方法1：使用绘图功能绘制进度条

这种方法通过在`QSplashScreen`上直接绘制进度条来实现。我们将覆盖`drawContents`方法来自定义绘图。

```python
import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QColor

class CustomSplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super(CustomSplashScreen, self).__init__(pixmap)
        self.progress = 0

    def drawContents(self, painter):
        super(CustomSplashScreen, self).drawContents(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(58, 134, 255))
        painter.drawRect(10, self.height() - 20, self.width() - 20, 10, self.progress / 100 * (self.width() - 20))

    def setProgress(self, progress):
        self.progress = progress
        self.showMessage(f"Loading... {progress}%", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        self.repaint()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qt Application")
        self.setGeometry(300, 300, 250, 150)
        self.show()

def main():
    app = QApplication(sys.argv)
    pixmap = QPixmap("path_to_your_image.png")
    splash = CustomSplashScreen(pixmap)
    splash.show()

    # Update progress
    for i in range(1, 101):
        QTimer.singleShot(i * 30, lambda i=i: splash.setProgress(i))
        QApplication.processEvents()

    main_win = MainWindow()
    main_win.show()
    splash.finish(main_win)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

### 方法2：在Splash Screen上放置一个进度条控件

这种方法稍微复杂一些，因为你需要处理一个透明的窗口和一个进度条控件。

```python
import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow, QProgressBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qt Application")
        self.setGeometry(300, 300, 250, 150)
        self.show()

def main():
    app = QApplication(sys.argv)
    pixmap = QPixmap("path_to_your_image.png")
    splash = QSplashScreen(pixmap)
    splash.show()

    # Add progress bar
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(10, splash.height() - 20, splash.width() - 20, 10)
    progressBar.setStyleSheet("QProgressBar {background-color: #EEE; border: 2px solid grey; border-radius: 5px;}"
                              "QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")

    # Update progress
    for i in range(1, 101):
        QTimer.singleShot(i * 30, lambda val=i: progressBar.setValue(val))
        QApplication.processEvents()

    main_win = MainWindow()
    main_win.show()
    splash.finish(main_win)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

在这两种方法中，你需要替换`"path_to_your_image.png"`为你的启动图片路径。这两种方法都使用了`QTimer`和`processEvents()`来模拟加载进度，并确保UI在加载时仍然响应用户操作。使用第二种方法时，通过自定义样式表（CSS）来美化进度条的外观，使其与你的启动画面更协调。