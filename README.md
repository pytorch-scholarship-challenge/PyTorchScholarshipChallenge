# PyTorchScholarshipChallenge 2018/2019

## PyTorch installation instruction nVidia Jetson TX1.

### Install JetPack 3.3.

### Optionally speed-up the board.
```bash
~/jetson_clocks.sh
```

### Perform system upgrade.
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt clean
```

### Check if upgrade overwrote nVidia binaries.
```bash
sha1sum -c /etc/nv_tegra_release
sudo cp /usr/lib/aarch64-linux-gnu/tegra/libglx.so /usr/lib/xorg/modules/extensions/
```

### Insert SD card and make temporary swap image otherwise PyTorch will not compile.
```bash
cd /media/mvidia/[...]
sudo dd if=/dev/zero of=/media/nvidia/[...]/swap.img bs=1024k count=5000
sudo mkswap /media/nvidia/[...]/swap.img
sudo swapon /media/nvidia/[...]/swap.img
```

### Install `pip3`.
```bash
sudo apt-get install python-pip3
pip3 install -U pip
export PATH=/home/ubuntu/.local/bin:$PATH
```

### Get __PyTorch__ sources.
```bash
git clone http://github.com/pytorch/pytorch
cd pytorch
git checkout v0.4.1
git submodule update --init
```

### Install prerequisites.
```bash
pip3 install -U setuptools
pip3 install -r requirements.txt
```

### Build PyTorch.
```bash
python3 setup.py build_deps
sudo python3 setup.py install
```

### Go outside of PyTorch repository
```bash
cd ..
```

### Verify installation.
```python
import torch
print(torch.cuda.is_available())
```
