#include "xkcd.h"
#include "ui_xkcd.h"
#include "mainwindow.h"
#include <QtWebKit/QWebElement>
#include <QtWebKit/QWebPage>
#include <QtWebKit/QWebFrame>
#include <QtWebKit/QWebElementCollection>
#include <stdio.h>
#include <QtWebKit/QWebView>
#include "limitdialog.h"

xkcd::xkcd(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::xkcd)
{
    ui->setupUi(this);
    xkcd::view = new QWebView();
    xkcd::view->setUrl(QUrl("http://xkcd.com"));
    xkcd::altFlag = 0;
    ui->altText->hide();
    xkcd::latestSet=0;
    QObject::connect(view, SIGNAL(loadFinished(bool)), this, SLOT(scrap(bool)));
    QObject::connect(view, SIGNAL(loadProgress(int)), this, SLOT(progress(int)));
    QObject::connect(view, SIGNAL(loadStarted()), this, SLOT(unhideProgress()));
}

xkcd::~xkcd()
{
    delete ui;
}

void xkcd::scrap(bool ok)
{
    if (ok)
    {
        ui->progressBar->hide();
        QWebElementCollection imgs = view->page()->mainFrame()->findAllElements("img");
        QWebElement img = imgs.at(1);
        ui->webView->setUrl(QUrl(img.attribute("src").toAscii().constData()));
        ui->altText->setText(QString(img.attribute("title")));
        QWebElement link = view->page()->mainFrame()->findFirstElement("h3");
        if (latestSet == 0)
        {
            QString latest = QString(link.toPlainText());
            Latest = latest.split("/", QString::SkipEmptyParts);
            xkcd::latest = Latest.at(2).toInt();
            xkcd::comicid = xkcd::latest;
            latestSet = 1;
        }
    }
}

void xkcd::alt()
{
    if (xkcd::altFlag == 0)
    {
        ui->altText->show();
        xkcd::altFlag = 1;
    }
    else
    {
        ui->altText->hide();
        xkcd::altFlag = 0;
    }

}

void xkcd::prev()
{
    if (xkcd::comicid == 0)
    {
        limitDialog *dlg = new limitDialog();
        dlg->setText(QString("This is the first comic. No older comic available."));
        dlg->show();
    }
    else
    {
        xkcd::comicid -= 1;
        QString url = QString("http://xkcd.com/%1/").arg(QVariant(xkcd::comicid).toString());
        xkcd::view->setUrl(QVariant(url).toUrl());
    }

}

void xkcd::next()
{
    if (xkcd::comicid == xkcd::latest)
    {
        limitDialog *dlg = new limitDialog();
        dlg->setText(QString("This is the last comic. Please wait for an update."));
        dlg->show();
    }
    else
    {
        xkcd::comicid += 1;
        QString url = QString("http://xkcd.com/%1/").arg(QVariant(xkcd::comicid).toString());
        xkcd::view->setUrl(QVariant(url).toUrl());
    }
}

void xkcd::randComic()
{
    xkcd::comicid = rand() %911 + 1;
    QString url = QString("http://xkcd.com/%1/").arg(QVariant(xkcd::comicid).toString());
    xkcd::view->setUrl(QVariant(url).toUrl());
}

void xkcd::progress(int x)
{
    ui->progressBar->setValue(x);
}

void xkcd::unhideProgress()
{
    ui->progressBar->show();
}
