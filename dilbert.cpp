#include "dilbert.h"
#include "ui_dilbert.h"
#include <QtWebKit/QWebElement>
#include <QtWebKit/QWebPage>
#include <QtWebKit/QWebFrame>
#include <QtWebKit/QWebElementCollection>
#include <QtWebKit/QWebView>
#include <QDebug>
#include <QDate>

dilbert::dilbert(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::dilbert)
{
    latest = QDate::currentDate();
    comicid = QDate::currentDate();
    ui->setupUi(this);
    ui->next->setEnabled(false);
    this->setWindowTitle(QString("Dilbert"));
    dilbert::view = new QWebView();
    dilbert::view->setUrl(QUrl(QString("http://dilbert.com/fast/")));
    QObject::connect(view, SIGNAL(loadFinished(bool)), this, SLOT(scrap(bool)));
    QObject::connect(view, SIGNAL(loadProgress(int)), this, SLOT(progress(int)));
    QObject::connect(view, SIGNAL(loadStarted()), this, SLOT(unhideProgress()));
}

dilbert::~dilbert()
{
    delete ui;
}

void dilbert::scrap(bool ok)
{
    if (ok)
    {
        ui->progressBar->hide();
        QWebElementCollection imgs = view->page()->mainFrame()->findAllElements("img");
        QWebElement img;
        if (comicid == latest || comicid == QDate(1989, 04, 16))
            img = imgs.at(1);
        else
            img = imgs.at(2);
        QString imgLink = QString("http://dilbert.com").append(img.attribute("src").toAscii().constData());
        ui->webView->setUrl(QUrl(imgLink));
        if (comicid == QDate(1989, 04, 16))
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

void dilbert::prev()
{
    comicid = comicid.addDays(-1);
    QString url = QString("http://dilbert.com/fast/%1/").arg(comicid.toString(QString("yyyy-MM-dd")));
    view->setUrl(QVariant(url).toUrl());
}

void dilbert::next()
{
    comicid = comicid.addDays(1);
    QString url = QString("http://dilbert.com/fast/%1/").arg(comicid.toString(QString("yyyy-MM-dd")));
    view->setUrl(QVariant(url).toUrl());
}

void dilbert::randComic()
{
    QDate start(1989, 04, 16);
    comicid = start.addDays(rand() %(start.daysTo(latest)) +1);
    QString url = QString("http://dilbert.com/fast/%1/").arg(comicid.toString(QString("yyyy-MM-dd")));
    view->setUrl(QVariant(url).toUrl());
}

void dilbert::progress(int x)
{
    ui->progressBar->setValue(x);
}

void dilbert::unhideProgress()
{
    ui->progressBar->show();
}
