# description
- Shared_memory, image_processing, deep_learning, machine_learning for manufacturing
- Research and development library useful in manufacturing

</br>

# mfglab philosophy
- life is too short
- The difference between 1 and 0 is greater than the difference between 100 and 1

</br>

# use data format
- numpy, pandas, csv
- txt, bmp, png, jpg, jpeg, onnx
- object detection : yolo style

</br>

# dev-env
- win 10, 11 / ubuntu 22.04
- cuda 11.8
- python 3.10
- C# NetFramework 4.8.1

</br>

# set-up
- pip mode
``` shell
python -m pip install --upgrade pip setuptools wheel

pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118

pip install mfglab
```

- edit mode
``` shell
git clone https://github.com/qqrr33/mfglab.git

cd mfglab

python -m venv _venv_mfglab

# windows
.\_venv_mfglab\Scripts\activate

python -m pip install --upgrade pip setuptools wheel

pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118

# edit mode
pip install -e .
```

</br>

# To Do
- dshm 3ch 이미지도 메모리에 올릴 수 있게하되, CSharp과 같이 진행필요
- dshm header format도 CSharp과 같이 진행필요


