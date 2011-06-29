#include "mainwindow.h"

#include <QtGui/QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    //QApplication::setStyle(QString("meegotouch"));
    MainWindow mainWindow;
    mainWindow.setOrientation(MainWindow::ScreenOrientationLockLandscape);
    mainWindow.showExpanded();
    return app.exec();
}
