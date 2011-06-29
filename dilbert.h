#ifndef DILBERT_H
#define DILBERT_H

#include <QWidget>
#include <QtWebKit/QWebView>
#include <QDate>

namespace Ui {
    class dilbert;
}

class dilbert : public QWidget
{
    Q_OBJECT

public:
    explicit dilbert(QWidget *parent = 0);
    ~dilbert();

private:
    Ui::dilbert *ui;
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

#endif // DILBERT_H
