#ifndef GOCOMICS_H
#define GOCOMICS_H

#include <QWidget>
#include <QDate>
#include <QWebView>
namespace Ui {
    class gocomics;
}

class gocomics : public QWidget
{
    Q_OBJECT

public:
    explicit gocomics(QWidget *parent = 0);
    ~gocomics();
    QDate start;
    QString comicName;
    void setStart(int, int, int);
    void setComicName(QString);

private:
    Ui::gocomics *ui;
    QDate comicid;
    QDate latest;
    QWebView *view;

private slots:
    void next();
    void prev();
    void randComic();
    void scrap(bool);
    void progress(int);
    void unhideProgress();
};

#endif // GOCOMICS_H
