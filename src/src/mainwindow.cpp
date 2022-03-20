#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    pub_msg = nh.advertise<materi_3::value>("materi_3", 1000);
    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::send_data);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::send_data()
{
    int data_x = ui->lineEdit_x->text().toInt();
    int data_y = ui->lineEdit_y->text().toInt();

    pub_data(data_x, data_y);
}

void MainWindow::pub_data(int x, int y)
{
    dataPublish.x = x;
    dataPublish.y = y;
    pub_msg.publish(dataPublish);
}