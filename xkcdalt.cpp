#include "xkcdalt.h"
#include "ui_xkcdalt.h"

xkcdAlt::xkcdAlt(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::xkcdAlt)
{
    ui->setupUi(this);
}

xkcdAlt::~xkcdAlt()
{
    delete ui;
}
