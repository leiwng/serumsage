# PyInstaller

## 使用pyinstaller打包项目

PyInstaller is a program that converts Python programs into stand-alone executables, under Windows, Linux, and Mac OS X. To package your project with PyInstaller, you'd generally follow these steps:

1. Install PyInstaller using pip:

   ```
   pip install pyinstaller
   ```

2. Navigate to your project directory in the command line.

3. Run PyInstaller with your main script name:

   ```
   pyinstaller --onefile main_script.py
   ```

   - `--onefile`: Tells PyInstaller to package everything into a single executable. If you have additional data files or dependencies, you may need to include more options.
   - `main_script.py`: Replace this with the path to your actual main Python script.

4. After PyInstaller completes, it will create a `dist` folder where you'll find the executable.

5. Test the executable to ensure it works correctly on the target environment.

Remember that complex projects, especially those with non-Python dependencies or specific data files, may require additional PyInstaller options. You might need to use a `.spec` file for fine-grained configuration or additional command-line flags to include external files, set the icon, etc.

## 打包的其他参数

Yes, PyInstaller offers several useful options for packaging projects:

- `--distpath dir`: Specifies the directory where the final executable should be stored (default is `./dist`).
- `--workpath dir`: Sets the directory where PyInstaller should put temporary work files (default is `./build`).
- `--add-data <SRC;DEST or SRC:DEST>`: Includes additional data files into the packaged executable. The format for specifying source and destination depends on your operating system.
- `--icon=ICON_FILE`: Assigns an icon (ICO file for Windows, ICNS for macOS) to the executable.
- `--noconsole`: Useful on Windows to prevent a console window from appearing when the application is run (typically used with GUI applications).

You can combine these to tailor the build process according to your specific needs. For complex setups, managing these options through a `.spec` file might be more maintainable.

## Build Command

```PowerShell
pyinstaller --onefile --distpath=".\\pyinstaller_dist" --workpath=".\\pyinstaller_workpath" --icon=".\\ui_img\\logo_icon_kemoshen.ico" .\main.py
```
