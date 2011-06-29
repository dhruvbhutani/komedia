#include "gocomics.h"
#include "ui_gocomics.h"
#include <QtWebKit/QWebElement>
#include <QtWebKit/QWebPage>
#include <QtWebKit/QWebFrame>
#include <QtWebKit/QWebElementCollection>
#include <QtWebKit/QWebView>
#include <QDebug>
#include <QDate>

gocomics::gocomics(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::gocomics)
{
    latest = QDate::currentDate();
    comicid = QDate::currentDate();
    ui->setupUi(this);
    ui->next->setEnabled(false);
}

gocomics::~gocomics()
{
    delete ui;
}

void gocomics::scrap(bool ok)
{
    if (ok)
    {
        ui->progressBar->hide();
        QWebElementCollection imgs = view->page()->mainFrame()->findAllElements("img.strip");
        QWebElement img = imgs.at(0);
        QString imgLink = QString(img.attribute("src").toAscii().constData()).append(QString("?width=782.0"));
        ui->webView->setUrl(QUrl(imgLink));
        if (comicid == start)
        {
            ui->prev->setEnabled(false);
        }
        else
        {
            ui->prev->setEnabled(true);
        }
        if (comicid == latest)
        {
            ui->next->setEnabled(false);
        }
        else
        {
            ui->next->setEnabled(true);
        }
    }
}

void gocomics::prev()
{
    comicid = comicid.addDays(-1);
    QString url = QString("http://www.gocomics.com/%1/%2").arg(comicName).arg(comicid.toString(QString("yyyy/MM/dd")));
    view->setUrl(QVariant(url).toUrl());
}

void gocomics::next()
{
    comicid = comicid.addDays(1);
    QString url = QString("http://www.gocomics.com/%1/%2").arg(comicName).arg(comicid.toString(QString("yyyy/MM/dd")));
    view->setUrl(QVariant(url).toUrl());
}

void gocomics::randComic()
{
    comicid = start.addDays(rand() %(start.daysTo(latest)) +1);
    QString url = QString("http://www.gocomics.com/%1/%2").arg(comicName).arg(comicid.toString(QString("yyyy/MM/dd")));
    view->setUrl(QVariant(url).toUrl());
}

void gocomics::progress(int x)
{
    ui->progressBar->setValue(x);
}

void gocomics::unhideProgress()
{
    ui->progressBar->show();
}

void gocomics::setStart(int y, int m, int d)
{
    start = QDate(y, m, d);
}

void gocomics::setComicName(QString x)
{
    comicName = x;
    gocomics::view = new QWebView();
    gocomics::view->setUrl(QUrl(QString("http://www.gocomics.com/%1/").arg(comicName)));
    QObject::connect(view, SIGNAL(loadFinished(bool)), this, SLOT(scrap(bool)));
    QObject::connect(view, SIGNAL(loadProgress(int)), this, SLOT(progress(int)));
    QObject::connect(view, SIGNAL(loadStarted()), this, SLOT(unhideProgress()));
}
