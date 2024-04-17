# Chat with chatGPT for code generation

## MainWindow Requirements

```text
I am going to use pyqt5 to develop a standalone App working on Windows11 for serum index interpretation. The App will have the following parts:
1) Use QMainWindow for App  main window;
2) A config icon on top left corner, to config the input folder of blood test tube picture and the output folder of the result;
3) the menu bar will only have one item - "About" , after click will pop up a About dialog window show the App software version, company infomation, license, and thansk information;
4) the toolbar, current have no requirement on it, and will not show;
5) in status bar will show current work mode and statue, like how many blood test tube picture checked since today, and how many since App startup;
6) in central widget, it's in the center of the window. it will have a QTabWidget for three working modes:  "Continue interpretation", "One-Time interpretation“ and "Result Browsing"；
7) For "continue interpretation" Tab, in the top, there will be a ON/OFF button for start/stop the checking process; in the middle-left have a box to show the current blood test tube picture, which is on checking for interpretation; in its middle-right will show the checking result on Celiac serum index, Hemolytic serum index and Jaundice serum index; in the bottom will show a progress bar for the progress of every picture;
8)  For "One-Time interpretation" Tab, the layout is simliar to "continue interpretation" Tab, the difference is in the top, it have a button and a text edit box, click the button will let user to choose a picture, and after done, the full path of the selected file will showed in the text edit box; Others are the same as "continue interpretation" Tab;
9) For "Result Browsing" Tab, in left is will show a file list, which list all the checked picture from the output folder, when click a file in the list, the file will be highted to show it has been selected; and in the right of file list, it will show the picture of the selected file; and then in the right of the picture, it will show the checking result on Celiac serum index, Hemolytic serum index and Jaundice serum index of the selected file.
That's all for my current thinking on this App GUI, can you help to generate the code base on it? After that I will continue work on the code to finish all requirement.
```
