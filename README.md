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
