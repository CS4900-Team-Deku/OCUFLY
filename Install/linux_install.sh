#!/bin/sh

echo 'Installing dependencies'
echo 'You may need to enter your password'

cd ..

sudo pip install opencv-python tensorflow
sudo pip install cvlib
sudo pip install --upgrade cvlib
sudo pip install matplotlib

echo 'Installation done.'
