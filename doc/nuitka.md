# Nuitka Pack Project to EXE

## pyinstaller同nuitka对比

PyInstaller 和 Nuitka 都是流行的 Python 代码打包工具，它们用于将 Python 脚本转换成独立的可执行文件。虽然它们的目标相似，即使 Python 应用程序可以脱离 Python 运行时独立运行，但它们的实现方式和使用场景有所不同。以下是 PyInstaller 和 Nuitka 的对比：

### 1. **实现方式**
- **PyInstaller**：
  - 将 Python 程序打包成一个文件夹或单个可执行文件。它不是编译器，而是一个冻结程序（freezing tool），将 Python 字节码、解释器以及所有依赖打包进一个包或可执行文件中。
  - 运行时，PyInstaller 解包这些文件到一个临时目录并从中执行程序。

- **Nuitka**：
  - Nuitka 是一个真正的编译器，它将 Python 代码编译成优化的 C++ 代码，然后调用 C++ 编译器（如 GCC 或 Clang）来生成机器码。
  - 生成的程序是一个独立的二进制文件，性能通常比直接解释执行的 Python 代码要好。

### 2. **性能**
- **PyInstaller**：
  - 因为只是将解释器和字节码一起打包，并没有进行优化，所以打包后的程序性能与直接用 Python 解释器运行相比并无显著提升。

- **Nuitka**：
  - 由于 Nuitka 生成的是编译后的代码，因此在许多情况下可以显著提高性能。特别是在计算密集型任务中，编译后的程序通常比解释执行更快。

### 3. **易用性和兼容性**
- **PyInstaller**：
  - 相对更容易使用。大多数情况下，仅需简单的命令就可以将脚本打包成可执行文件。
  - 有广泛的社区支持，可以解决各种打包问题，如隐藏控制台窗口、添加图标、处理不同操作系统的特定问题等。

- **Nuitka**：
  - 配置可能稍复杂，特别是涉及到编译环境的设置。需要用户具备一定的编译知识。
  - 兼容性良好，尤其是对复杂脚本的支持较好。因为它通过彻底的编译优化，可以处理更多复杂的代码结构。

### 4. **应用场景**
- **PyInstaller**：
  - 适合大多数常规的 Python 应用打包需求，特别是那些依赖大量第三方库或需要快速打包的场景。
  - 可以很好地处理图形用户界面应用程序，如使用 PyQt、Tkinter 开发的程序。

- **Nuitka**：
  - 适合需要性能优化的项目，比如科学计算、数据处理等计算密集型任务。
  - 也适合需要将 Python 代码转换为更加难以逆向工程的形式的场景。

### 5. **资源消耗和打包时间**
- **PyInstaller**：
  - 打包过程相对较快，但生成的可执行文件可能较大，因为包括了整个 Python 运行环境和所有依赖。

- **Nuitka**：
  - 打包时间可能较长，因为涉及到编译过程。生成的文件大小通常比 PyInstaller 小，因为它只包含编译后的二进制代码。

总之，选择 PyInstaller 还是 Nuitka 取决于你的具体需求，包括打包的简便性、性能要求、程序的复杂性以及对反编译的考虑等因素。对于大多

数日常开发任务，PyInstaller 提供了足够的功能和更简单的使用方法；而对于性能敏感或需要编译保护的应用，Nuitka 则是更优的选择。

## nuitka 命令行参数  --follow-import-to 是什么意思

在使用 Nuitka 编译 Python 代码时，`--follow-import-to` 是一个用来指定编译器如何处理特定模块或包的命令行参数。这个参数可以用来告诉 Nuitka 对特定的导入进行更彻底的处理，尤其是在处理复杂依赖和确保性能优化时非常有用。

### 作用

`--follow-import-to` 参数允许你精确控制哪些模块或包应该被包含在编译结果中，而不是简单地作为外部依赖处理。默认情况下，Nuitka 会尽可能编译所有可识别的导入，但通过使用 `--follow-import-to`，你可以进一步指定一些特定的、可能不容易自动确定是否包含的模块或包。

### 应用场景

1. **确保模块包含**：如果你的代码依赖了一些特定的第三方库或模块，而这些模块在自动编译处理中可能因为某些原因（如动态导入）被遗漏，使用 `--follow-import-to` 可以确保这些模块被编译进最终的可执行文件。

2. **优化编译过程**：通过指定只编译特定模块，你可以减少编译时间和生成的可执行文件的大小，尤其是在你清楚知道哪些模块是必须的情况下。

### 使用示例

假设你有一个依赖于某个特定第三方库（例如 `numpy`）的应用，你可以使用 `--follow-import-to` 来确保 `numpy` 被编译到输出中：

```bash
nuitka --follow-import-to=numpy your_script.py
```

这条命令会告诉 Nuitka 编译器跟踪到 `numpy` 包的所有导入并将其编译，确保应用的编译版本包含了这个重要的依赖。

### 注意事项

使用 `--follow-import-to` 参数时，需要确保正确理解哪些模块和包是你的应用必须直接编译的。错误的使用这个参数可能会导致编译过程不必要的复杂化，或者漏掉了一些必要的依赖，影响应用的正常运行。

总的来说，`--follow-import-to` 是 Nuitka 提供的一种强大的控制工具，允许开发者在编译过程中有更细致的控制权，特别是在处理复杂的依赖关系时非常有用。

## nuitka 的命令行参数 --standalone --onefile 是否能完全将程序运行需要的依赖包导入并进行编译

在使用 Nuitka 编译 Python 程序时，`--standalone` 和 `--onefile` 是两个非常重要的命令行参数，它们都旨在生成独立的可执行文件，使得编译后的程序可以在没有安装 Python 或其他依赖的环境中运行。每个参数的具体作用如下：

### 1. `--standalone`
当使用 `--standalone` 参数时，Nuitka 会尝试将所有程序运行时可能需要的依赖包括Python解释器、库文件、支持模块等编译进一个独立的包内。这意味着编译出的程序将不依赖于外部的 Python 环境或额外安装的库，从而实现“独立运行”。

- **包含内容**：该参数会导致 Nuitka 包括所有静态可识别的导入。对于动态导入的内容，例如通过 `__import__`、`importlib.import_module` 等动态加载的模块，可能需要手动指定或保证它们能被正确解析。
- **执行过程**：在生成的输出目录下，除了主可执行文件外，通常还会有许多依赖的 DLLs、SO 文件（在 Linux 上）、Python 标准库和其他模块等。

### 2. `--onefile`
`--onefile` 参数通常与 `--standalone` 结合使用，用于将 `--standalone` 生成的所有文件打包成一个单一的可执行文件。

- **操作方式**：此模式下，Nuitka 使用一个启动器来打包所有的依赖和资源。当可执行文件运行时，它会在临时目录解压这些内容，并从该临时位置执行程序。
- **使用效果**：生成的单一文件使得部署和分发应用更加简单，用户无需关心依赖和文件结构，但首次启动可能会稍慢，因为需要解压所有内容到临时目录。

### 完整性
虽然 `--standalone` 和 `--onefile` 配置旨在包括所有依赖，但在一些复杂的情况下（如前所述的动态导入），可能需要开发者手动介入，确保所有必要的依赖都被正确地识别和包括。此外，某些特别的库或者依赖，如图形界面库（PyQt, Tkinter 等）或者某些复杂的第三方库，可能需要特别的配置或者使用 Nuitka 提供的插件来确保正确编译。

### 建议
- **测试**：在部署编译后的程序前，应该在目标环境进行充分的测试，确保所有功能正常工作，没有遗漏关键依赖。
- **文档和社区**：利用 Nuitka 的文档和社区资源来解决特定的问题。例如，使用 `--include-module` 或 `--include-package` 参数手动指定需要包括的模块。

总之，`--standalone` 和 `--onefile` 参数使得将 Python 程序编译成一个独立的、可直接运行的可执行文件成为可能，但可能需要开发者进行适当的配置和调整以确保所有依赖都被包括进来。

## --include-module 或 --include-package 参数中的模块或包如何指定

The content of the file you uploaded, which is generated from the `pip freeze` command, lists the Python packages and their versions that are installed in your project. To determine which dependencies might need to be explicitly included when packaging your project with Nuitka using the `--include-module` or `--include-package` parameters, we should look at specific types of packages that often require special handling.

**Analysis Approach:**
1. **Dynamic Imports**: Libraries that use dynamic imports (e.g., using `__import__`, `importlib.import_module`) might not be detected correctly by static analysis tools like Nuitka.
2. **Compiled Binary Extensions**: Packages that include binary extensions (.pyd, .so files) often need explicit inclusion because they may not be automatically detected or properly handled during the compilation process.
3. **Complex Dependency Trees**: Packages with complex dependencies or those that load resources in a non-standard way (e.g., data files, configuration outside of Python code) might require explicit instructions to Nuitka.

Given that I don't have direct visibility into the file content from your description, I can suggest a general approach:
- Review the list for any known packages that fit the above categories.
- Libraries such as `numpy`, `pandas`, and scientific computing tools often come with compiled binaries and might need explicit inclusion.
- GUI frameworks like `PyQt`, `Tkinter`, or `Kivy` are examples where not only the main package but also associated plugins and additional modules might need to be explicitly included.

**Next Steps with Nuitka:**
To ensure all necessary modules are included, you could start by packaging with the `--standalone` option and then running the resultant executable to see if there are any runtime errors indicating missing modules. If such errors occur, use the `--include-module=module_name` or `--include-package=package_name` options to add those missing pieces.

```bash
nuitka --standalone --onefile your_script.py
```

If errors occur:
```bash
nuitka --standalone --onefile --include-module=module_name1 --include-module=module_name2 your_script.py
```

Replace `module_name1`, `module_name2` with actual names of the modules that you find are missing or problematic based on runtime errors or based on the knowledge of the packages that commonly have issues.

**Recommendation:**
If you provide the list of packages from the file, I could give more specific advice on which packages might commonly require special attention when using Nuitka.

## 翻译：--include-module 或 --include-package 参数中的模块或包如何指定

当然可以，以下是对前面英文分析的中文翻译：

您上传的文件是通过 `pip freeze` 命令生成的，其中列出了您项目中安装的 Python 包及其版本。为了确定在使用 Nuitka 对项目进行 exe 打包时，哪些依赖包可能需要通过 `--include-module` 或 `--include-package` 参数显式包含，我们应当关注那些经常需要特殊处理的包类型。

**分析方法：**
1. **动态导入**：使用动态导入（例如，使用 `__import__`、`importlib.import_module`）的库可能不会被静态分析工具如 Nuitka 正确检测。
2. **编译的二进制扩展**：包含二进制扩展（.pyd, .so 文件）的包经常需要显式包含，因为它们可能不会被自动检测或在编译过程中正确处理。
3. **复杂的依赖树**：具有复杂依赖关系或以非标准方式加载资源（例如，数据文件、配置文件等）的包可能需要向 Nuitka 提供显式指令。

由于我无法直接看到您描述的文件内容，我可以建议一个通用的方法：
- 审查列表中任何已知的符合上述类别的包。
- 像 `numpy`、`pandas` 这样的库以及科学计算工具经常包含编译的二进制文件，可能需要显式包含。
- GUI 框架如 `PyQt`、`Tkinter` 或 `Kivy` 是一些不仅需要包括主包，还可能需要包括相关插件和额外模块的例子。

**使用 Nuitka 的下一步：**
为了确保包含所有必要的模块，您可以首先使用 `--standalone` 选项进行打包，然后运行生成的可执行文件，看看是否有任何运行时错误指示缺少模块。如果出现这样的错误，使用 `--include-module=module_name` 或 `--include-package=package_name` 选项添加那些缺失的部分。

```bash
nuitka --standalone --onefile your_script.py
```

如果出现错误：
```bash
nuitka --standalone --onefile --include-module=module_name1 --include-module=module_name2 your_script.py
```

将 `module_name1`, `module_name2` 替换为您发现缺失或有问题的模块的实际名称，这些名称可以基于运行时错误或基于那些已知通常有问题的包。

**建议：**
如果您提供文件中的包列表，我可以更具体地建议哪些包在使用 Nuitka 时通常需要特别注意。

## --include-module 和 --include-package 的区别



对于复杂的 Python 库如 `numpy`、`pandas`、`torch`、`torchvision` 和 `opencv-python`，当使用 Nuitka 进行编译打包时，通常需要特别关注这些库是否被正确地包含在最终的可执行文件中。这些库可能包含 C 语言扩展或特定的依赖文件，这使得自动检测和包含变得更加复杂。

### 如何使用 `--include-module` 和 `--include-package`

- **`--include-module`**：这个参数用于显式地指定单个 Python 模块应被包含在编译输出中。如果你知道某个具体的模块（通常是一个单文件模块）需要包含，那么可以使用这个参数。

- **`--include-package`**：这个参数用于显式地指定一个完整的 Python 包应被包含在编译输出中。这对于那些包含多个模块和子包的大型库尤其有用。

对于您提到的库：
- `numpy` 和 `pandas`：这两个包通常作为完整的包被包含。尽管 Nuitka 通常能够自动处理这些库，如果遇到问题，推荐使用 `--include-package=numpy` 和 `--include-package=pandas`。
- `torch` 和 `torchvision`：这些包涉及大量的底层和跨平台的依赖，以及可能的动态加载。推荐使用 `--include-package=torch` 和 `--include-package=torchvision` 来确保所有相关的模块和数据都被包含。
- `opencv-python`（通常称为 `cv2`）：这是一个复杂的库，包含许多本地依赖和外部文件。使用 `--include-package=opencv-python` 或针对其主要模块 `cv2` 使用 `--include-module=cv2`。

### 示例命令

如果您想确保这些库都被包含，您可以在命令行中添加相应的参数：

```bash
nuitka --standalone --onefile --include-package=numpy --include-package=pandas --include-package=torch --include-package=torchvision --include-package=opencv-python your_script.py
```

### 注意事项

尽管这些参数有助于确保这些复杂库的正确包含，但在某些情况下，您可能还需要考虑其他依赖性管理，例如系统级库或特定的配置文件。务必在不同的目标环境中彻底测试编译后的可执行文件，以验证其功能完整性和性能。

使用 `--include-package` 参数是一种保守的策略，它可以最大化地确保库及其所有依赖的正确包含，但可能会增加最终可执行文件的大小。如果对文件大小有严格的要求，可以进一步调整和优化需要包含的模块。

## --include-module 和 --include-package 的区别

在使用 Nuitka 编译 Python 程序时，理解 `--include-module` 和 `--include-package` 参数的区别是关键，因为这两个参数决定了哪些 Python 模块或包被包括在编译后的可执行文件中。下面详细解释这两个参数的不同用途：

### `--include-module`
- **用途**：`--include-module` 参数用来显式地指定单个 Python 模块应该被包括在 Nuitka 编译后的输出中。这个参数适用于确保特定的模块被包含，特别是当这个模块对程序的运行至关重要时。
- **适用场景**：当你知道某个特定模块可能由于动态加载等原因被 Nuitka 编译过程忽略，或者你想确保该模块无论如何都被编译进最终产物时，使用此参数。
- **实例**：如果你的程序使用了某个第三方库中的特定模块，并且这个模块不是自动包括的，你可以这样指定：`--include-module=some_module`

### `--include-package`
- **用途**：`--include-package` 参数用来显式地指定整个 Python 包应该被包括在 Nuitka 编译后的输出中。这包括包内的所有子模块和子包。
- **适用场景**：用于确保包含一个完整的包及其所有组件，尤其是那些包含多个模块和子目录的复杂包。这非常适用于确保像 `numpy` 或 `pandas` 这样的大型库完整无缺地被包括在内。
- **实例**：如果你使用了 `numpy` 并且想确保其所有依赖性都被包括，你可以使用：`--include-package=numpy`

### 主要区别
- **粒度控制**：`--include-module` 提供了更细粒度的控制，只针对单个模块；而 `--include-package` 提供了更宽泛的控制，涵盖了整个包及其所有子模块。
- **编译结果**：使用 `--include-package` 可能会导致编译后的文件体积更大，因为它包括了整个包的所有内容，而 `--include-module` 只增加了特定模块的体积。
- **使用场合**：选择使用哪个参数取决于你的需求是否只是围绕特定模块，还是需要确保一个包的完整性。

在实际应用中，选择适当的参数可以帮助确保你的编译产物既完整又高效。如果你对哪些模块或包需要显式包含有疑问，可以先尝试编译，然后运行测试来识别哪些部分没有被正确包含。此外，参考 Nuitka 的文档和社区也可以提供额外的指导和支持。

## EXE Build Command for Nuitka

When using Nuitka to compile Python scripts into standalone executables, you need to provide specific command-line options to customize the build process. Below is an example command that demonstrates how to build an executable using Nuitka:

### --windows-disable-console

```PowerShell
python -m nuitka --standalone --onefile --enable-plugin=pyqt5 --windows-disable-console --output-dir=".\\exe_output" --windows-icon-from-ico=".\\ui_img\\logo_icon_kemoshen.ico" --windows-company-name="SiChuan-Kemoshen" --windows-product-name="SerumSage" --windows-file-version="1.0.0.0" --windows-product-version="1.0.0" --windows-file-description="main-window" ./main_window.py
```

### NO --windows-disable-console

```PowerShell
python -m nuitka --standalone --onefile --enable-plugin=pyqt5 --output-dir=".\\exe_output" --windows-icon-from-ico=".\\ui_img\\logo_icon_kemoshen.ico" --windows-company-name="SiChuan-Kemoshen" --windows-product-name="SerumSage" --windows-file-version="1.0.0.0" --windows-product-version="1.0.0" --windows-file-description="main-window" ./main_window.py
```

### NO --enable-plugin=pyqt5 NO 产品信息

```PowerShell
python -m nuitka --standalone --onefile --output-dir=".\\exe_output" ./main_window.py
```
