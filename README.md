# PyTorchScholarshipChallenge 2018/2019

## PyTorch installation instruction on nVidia Jetson TX1.

### 1. Install JetPack 3.3.

### 2. Optionally speed-up the board.
```bash
~/jetson_clocks.sh
```

### 3. Perform system upgrade.
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt clean
```

### 4. Check if upgrade overwrote nVidia binaries.
```bash
sha1sum -c /etc/nv_tegra_release
sudo cp /usr/lib/aarch64-linux-gnu/tegra/libglx.so /usr/lib/xorg/modules/extensions/
```

### 5. Insert SD card and make temporary swap image otherwise PyTorch will not compile.
```bash
cd /media/mvidia/[...]
sudo dd if=/dev/zero of=/media/nvidia/[...]/swap.img bs=1024k count=5000
sudo mkswap /media/nvidia/[...]/swap.img
sudo swapon /media/nvidia/[...]/swap.img
```

### 6. Install `pip3`.
```bash
sudo apt-get install python-pip3
pip3 install -U pip
export PATH=/home/ubuntu/.local/bin:$PATH
```

### 7. Get __PyTorch__ sources.
```bash
git clone http://github.com/pytorch/pytorch
cd pytorch
git checkout v0.4.1
git submodule update --init
```

### 8. Install prerequisites.
```bash
pip3 install -U setuptools
pip3 install -r requirements.txt
```

### 9. Build PyTorch.
```bash
python3 setup.py build_deps
sudo python3 setup.py install
```

### 10. Go outside of PyTorch and remove repository.
```bash
cd ..
sudo rm -rf pytorch
```

### 11. Verify if installation succeeded.
```python
import torch
print(torch.cuda.is_available())
```
## torchvision installation procedure on nVidia Jetson TX1.

```bash
sudo apt-get install libjpeg-dev libpng-dev  python3-matplotlib
sudo bash -c "export PATH=/home/ubuntu/.local/bin:$PATH && pip3 install torchvision"
```

## Jupyter installation procedure on nVidia Jetson TX1.

```bash
sudo apt-get install libzmq3-dev
sudo python3 -m pip install jupyter
```

## Upgrade `matplotlib` to the recent version.

```bash
sudo apt-get install libfreetype6-dev
sudo bash -c "export PATH=/home/ubuntu/.local/bin:$PATH && pip3 install -U matplotlib" 
```

## Install 'opencv'.

### Install prerequisites

```bash
sudo apt-get remove libopencv-python
sudo apt-get install g++-5 cpp-5 gcc-5
sudo apt-get install -y libjpeg-dev libpostproc-dev libtbb-dev zlib1g-dev \         pkg-config
sudo apt-get install build-essential make cmake cmake-curses-gui \
    g++ libavformat-dev libavutil-dev libswscale-dev libv4l-dev libeigen3-dev \
    libglew-dev libgtk2.0-dev
sudo apt-get install libdc1394-22-dev libxine2-dev libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev
sudo apt-get install libjpeg8-dev libjpeg-turbo8-dev libtiff5-dev \
    libjasper-dev libpng12-dev libavcodec-dev
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev \
    libatlas-base-dev gfortran
sudo apt-get install libopenblas-dev liblapack-dev liblapacke-dev
sudo apt-get install qt5-default
sudo apt-get install python3-dev python3-pip python3-tk
```

### Fix OpenGL dependencies.


```bash
cd /usr/lib/aarch64-linux-gnu/
sudo ln -sf tegra/libGL.so libGL.so
```

### Change `/usr/local/cuda/include/cuda_gl_interop.h` to

```c
//#if defined(__arm__) || defined(__aarch64__)
//#ifndef GL_VERSION
//#error Please include the appropriate gl headers before including cuda_gl_interop.h
//#endif
//#else
 #include <GL/gl.h>
//#endif
```

### Install `opencv`.

```bash
sudo cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON -D CUDA_ARCH_BIN="5.3" -D CUDA_ARCH_PTX="" \
    -D WITH_CUBLAS=ON -D ENABLE_FAST_MATH=ON -D CUDA_FAST_MATH=ON \
    -D ENABLE_NEON=ON -D WITH_LIBV4L=ON -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF -D WITH_QT=ON \
    -D WITH_OPENGL=ON -D OPENCV_SKIP_PYTHON_LOADER=ON \
    -D OPENCV_PYTHON3_INSTALL_PATH=/usr/local/lib/python3.5/dist-packages  ..
sudo make -j4
sudo make install
```

### Verify `opencv` was installed sucessfully.
```python
import cv2
print(cv2.__version__)
```