#include "limitdialog.h"
#include "ui_limitdialog.h"

limitDialog::limitDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::limitDialog)
{
    ui->setupUi(this);
}

limitDialog::~limitDialog()
{
    delete ui;
}

void limitDialog::setText(QString text)
{
    ui->textBrowser->setText(text);
}
