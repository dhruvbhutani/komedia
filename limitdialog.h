#ifndef LIMITDIALOG_H
#define LIMITDIALOG_H

#include <QDialog>

namespace Ui {
    class limitDialog;
}

class limitDialog : public QDialog
{
    Q_OBJECT

public:
    explicit limitDialog(QWidget *parent = 0);
    ~limitDialog();
    void setText(QString);

private:
    Ui::limitDialog *ui;
};

#endif // LIMITDIALOG_H
