#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QtCore/QCoreApplication>
#include <xkcd.h>
#include <dilbert.h>
#include <gocomics.h>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle("Komedia");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setOrientation(ScreenOrientation orientation)
{
#if defined(Q_OS_SYMBIAN)
    // If the version of Qt on the device is < 4.7.2, that attribute won't work
    if (orientation != ScreenOrientationAuto) {
        const QStringList v = QString::fromAscii(qVersion()).split(QLatin1Char('.'));
        if (v.count() == 3 && (v.at(0).toInt() << 16 | v.at(1).toInt() << 8 | v.at(2).toInt()) < 0x040702) {
            qWarning("Screen orientation locking only supported with Qt 4.7.2 and above");
            return;
        }
    }
#endif // Q_OS_SYMBIAN

    Qt::WidgetAttribute attribute;
    switch (orientation) {
#if QT_VERSION < 0x040702
    // Qt < 4.7.2 does not yet have the Qt::WA_*Orientation attributes
    case ScreenOrientationLockPortrait:
        attribute = static_cast<Qt::WidgetAttribute>(128);
        break;
    case ScreenOrientationLockLandscape:
        attribute = static_cast<Qt::WidgetAttribute>(129);
        break;
    default:
    case ScreenOrientationAuto:
        attribute = static_cast<Qt::WidgetAttribute>(130);
        break;
#else // QT_VERSION < 0x040702
    case ScreenOrientationLockPortrait:
        attribute = Qt::WA_LockPortraitOrientation;
        break;
    case ScreenOrientationLockLandscape:
        attribute = Qt::WA_LockLandscapeOrientation;
        break;
    default:
    case ScreenOrientationAuto:
        attribute = Qt::WA_AutoOrientation;
        break;
#endif // QT_VERSION < 0x040702
    };
    setAttribute(attribute, true);
}

void MainWindow::showExpanded()
{
    showFullScreen();
    //show();
}

void MainWindow::openXKCD()
{
    xkcd *xkcdG = new xkcd();
    //xkcdG->showFullScreen();
    xkcdG->setParent(this);
    xkcdG->setAutoFillBackground(true);
    xkcdG->showMaximized();
}

void MainWindow::openDilbert()
{
    dilbert *dilbertG = new dilbert(this);
    //dilbertG->showFullScreen();
    dilbertG->setAutoFillBackground(true);
    dilbertG->showMaximized();
}

void MainWindow::openGarfield()
{
    gocomics *garfield = new gocomics(this);
    garfield->setWindowTitle(QString("Garfield"));
    garfield->setStart(1978, 6, 19);
    garfield->setComicName("garfield");
    garfield->setAutoFillBackground(true);
    garfield->show();
}

void MainWindow::openCalvin()
{
    gocomics *calvin = new gocomics(this);
    calvin->setWindowTitle(QString("Calvin & Hobbes"));
    calvin->setStart(1985, 11, 18);
    calvin->setComicName("calvinandhobbes");
    calvin->setAutoFillBackground(true);
    calvin->show();
}

void MainWindow::openPeanuts()
{
    gocomics *peanuts = new gocomics(this);
    peanuts->setWindowTitle(QString("Peanuts"));
    peanuts->setStart(1950, 10, 02);
    peanuts->setComicName("peanuts");
    peanuts->setAutoFillBackground(true);
    peanuts->show();
}

void MainWindow::openWizofid()
{
    gocomics *wizofid = new gocomics(this);
    wizofid->setWindowTitle(QString("Wizard of Id"));
    wizofid->setStart(2002, 8, 12);
    wizofid->setComicName("wizardofid");
    wizofid->setAutoFillBackground(true);
    wizofid->show();
}

