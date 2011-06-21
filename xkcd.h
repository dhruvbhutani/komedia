#ifndef XKCD_H
#define XKCD_H

#include <QWidget>
#include <QtWebKit/QWebView>

namespace Ui {
    class xkcd;
}

class xkcd : public QWidget
{
    Q_OBJECT

public:
    explicit xkcd(QWidget *parent = 0);
    ~xkcd();

private:
    Ui::xkcd *ui;
    int comicid;
    int latest;
    QWebView *view;
    int altFlag;
    QStringList Latest;
    int latestSet;

private slots:
    void next();
    void prev();
    void alt();
    void randComic();
    void scrap(bool);
    void progress(int);
    void unhideProgress();
};

#endif // XKCD_H
