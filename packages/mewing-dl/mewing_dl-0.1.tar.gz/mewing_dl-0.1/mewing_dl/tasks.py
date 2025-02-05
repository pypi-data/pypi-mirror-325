# mewing_dl/tasks.py

import nbformat
from IPython.display import display, Markdown, Code

# Простейший пример задач:
# Каждая задача (ключ = номер задачи) хранит список ячеек (словарей),
# где cell_type = "markdown" или "code", а source = содержимое ячейки.
TASKS = {
    1: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
        {
            "cell_type": "markdown",
            "source": (
                "Используя библиотеку PyTorch, решите задачу одновременного предсказания столбцов Gold_T-7, Gold_T-14, Gold_T-22 и Gold_T+22 (задача регрессии). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Сравните несколько различных оптимизаторов и графически продемонстрируйте, как выбор оптимизатора влияет на процесс обучения и результаты на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('gold.csv')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data.drop(columns = ['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data[['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.float32)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 64)\n"
                "test_loader = DataLoader(test, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 117, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 4),\n"
                ")\n\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)  # AdamW\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_AdamW = epoch_losses\n"
                "test_r2_scores_AdamW = test_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 64)\n"
                "test_loader = DataLoader(test, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 117, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 4),\n"
                ")\n\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.SGD(model.parameters(), lr = 0.01)  # SGD\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_SGD = epoch_losses\n"
                "test_r2_scores_SGD = test_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 64)\n"
                "test_loader = DataLoader(test, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 117, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 4),\n"
                ")\n\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.RMSprop(model.parameters(), lr = 0.01)  # RMSprop\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_RMSprop = epoch_losses\n"
                "test_r2_scores_RMSprop = test_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses_AdamW, label = 'AdamW')\n"
                "plt.plot(epoch_losses_SGD, label = 'SGD')\n"
                "plt.plot(epoch_losses_RMSprop, label = 'RMSprop')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2')\n"
                "plt.plot(test_r2_scores_AdamW, label = 'AdamW')\n"
                "plt.plot(test_r2_scores_SGD, label = 'SGD')\n"
                "plt.plot(test_r2_scores_RMSprop, label = 'RMSprop')\n"
                "plt.ylim(-0.1, 1)\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }

    ],
    2: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Используя библиотеку PyTorch, решите задачу одновременного предсказания столбцов Gold_T-7, Gold_T-14, Gold_T-22 и Gold_T+22 (задача регрессии). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Продемонстрируйте несколько (не менее 2) наборов гиперпараметров модели и сравните качество моделей на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('gold.csv')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data.drop(columns = ['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data[['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.float32)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "# lr = 0.01; batch_size = 64\n"
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 64)\n"
                "test_loader = DataLoader(test, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 117, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 4),\n"
                ")\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_first = epoch_losses\n"
                "test_r2_scores_first = test_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "# lr = 0.001; batch_size = 128\n"
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 128)\n"
                "test_loader = DataLoader(test, batch_size = 128)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 117, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 4),\n"
                ")\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.001)\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_second = epoch_losses\n"
                "test_r2_scores_second = test_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses_first, label = 'lr = 0.01; batch_size = 64')\n"
                "plt.plot(epoch_losses_second, label = 'lr = 0.001; batch_size = 128')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2')\n"
                "plt.plot(test_r2_scores_first, label = 'lr = 0.01; batch_size = 64')\n"
                "plt.plot(test_r2_scores_second, label = 'lr = 0.001; batch_size = 128')\n"
                "plt.legend()\n"
                "plt.ylim(-0.1, 1)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    3: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Используя библиотеку PyTorch, решите задачу предсказания столбца cnt (задача регрессии). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Отобразите графики значений функции потерь и метрики R^2 на обучающем множестве по эпохам. Рассчитайте значение метрики R^2 на тестовом множестве. Добавьте в модель слои BatchNorm1d и графически продемонстрируйте, как это влияет на процесс обучения и результаты на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('bike_cnt.csv', index_col = 'instant')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "categorical_cols = ['dteday']\n\n"
                "data_processed = pd.get_dummies(data, columns = categorical_cols, drop_first = True)\n"
                "data_processed.head()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data_processed.drop(columns = ['cnt']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data_processed[['cnt']].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.float32)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 256)\n"
                "test_loader = DataLoader(test, batch_size = 256)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 742, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 1),\n"
                ")\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.001)\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n"
                "train_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in train_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        train_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_1model = epoch_losses\n"
                "test_r2_scores_1model = test_r2_scores\n"
                "train_r2_scores_1model = train_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2')\n"
                "plt.plot(train_r2_scores, label = 'train')\n"
                "plt.plot(test_r2_scores, label = 'test')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 256)\n"
                "test_loader = DataLoader(test, batch_size = 256)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 742, out_features = 64),\n"
                "    nn.BatchNorm1d(num_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.BatchNorm1d(num_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.BatchNorm1d(num_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 1),\n"
                ")\n\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.001)\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n"
                "train_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in train_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        train_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if epoch % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses_1model, label = '1model')\n"
                "plt.plot(epoch_losses, label = 'BatchNorm1d')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2_test')\n"
                "plt.plot(test_r2_scores_1model, label = '1model')\n"
                "plt.plot(test_r2_scores, label = 'BatchNorm1d')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    4: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Используя библиотеку PyTorch, решите задачу предсказания столбца **cnt** (задача регрессии). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Отобразите графики значений функции потерь и метрики **R²** на обучающем множестве по эпохам. Рассчитайте значение метрики **R²** на тестовом множестве. Добавьте в модель слой **Dropout** и графически продемонстрируйте, как это влияет на процесс обучения и результаты на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('bike_cnt.csv', index_col = 'instant')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "categorical_cols = ['dteday']\n\n"
                "data_processed = pd.get_dummies(data, columns = categorical_cols, drop_first = True)\n"
                "data_processed.head()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data_processed.drop(columns = ['cnt']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data_processed[['cnt']].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.float32)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "train_loader = DataLoader(train, batch_size = 256)\n"
                "test_loader = DataLoader(test, batch_size = 256)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 742, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 1),\n"
                ")\n"
                "criterion = nn.MSELoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.001)\n\n"
                "epoch_losses = []\n"
                "test_r2_scores = []\n"
                "train_r2_scores = []\n\n"
                "for epoch in range(50+1):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in train_loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train_loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in train_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        train_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    with th.no_grad():\n"
                "        y_true, y_pred = [], []\n"
                "        for X_batch, y_batch in test_loader:\n"
                "            y_predict = model(X_batch)\n"
                "            y_true.extend(y_batch.detach().numpy())\n"
                "            y_pred.extend(y_predict.detach().numpy())\n"
                "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_1model = epoch_losses\n"
                "test_r2_scores_1model = test_r2_scores\n"
                "train_r2_scores_1model = train_r2_scores"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2')\n"
                "plt.plot(train_r2_scores, label = 'train')\n"
                "plt.plot(test_r2_scores, label = 'test')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "train_loader = DataLoader(train, batch_size = 256)\n"
        "test_loader = DataLoader(test, batch_size = 256)\n\n"
        "model = nn.Sequential(\n"
        "    nn.Linear(in_features = 742, out_features = 64),\n"
        "    nn.ReLU(),\n"
        "    nn.Dropout(p = 0.3),\n"
        "    nn.Linear(in_features = 64, out_features = 32),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 32, out_features = 16),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 16, out_features = 1),\n"
        ")\n\n"
        "criterion = nn.MSELoss()\n"
        "optimizer = optim.AdamW(model.parameters(), lr = 0.001)\n\n"
        "epoch_losses = []\n"
        "test_r2_scores = []\n"
        "train_r2_scores = []\n\n"
        "for epoch in range(50+1):\n"
        "    model.train()\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in train_loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(train_loader)\n"
        "    epoch_losses.append(epoch_loss.item())\n\n"
        "    model.eval()\n"
        "    with th.no_grad():\n"
        "        y_true, y_pred = [], []\n"
        "        for X_batch, y_batch in train_loader:\n"
        "            y_predict = model(X_batch)\n"
        "            y_true.extend(y_batch.detach().numpy())\n"
        "            y_pred.extend(y_predict.detach().numpy())\n"
        "        train_r2_scores.append(r2_score(y_true, y_pred))\n\n"
        "    with th.no_grad():\n"
        "        y_true, y_pred = [], []\n"
        "        for X_batch, y_batch in test_loader:\n"
        "            y_predict = model(X_batch)\n"
        "            y_true.extend(y_batch.detach().numpy())\n"
        "            y_pred.extend(y_predict.detach().numpy())\n"
        "        test_r2_scores.append(r2_score(y_true, y_pred))\n\n"
        "    if epoch % 5 == 0:\n"
        "        print(epoch, epoch_loss.item())"
    )
},
{
            "cell_type": "code",
            "source": (
                "plt.title('MSELoss')\n"
                "plt.plot(epoch_losses_1model, label = 'no Dropout')\n"
                "plt.plot(epoch_losses, label = 'with Dropout')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('R2_test')\n"
                "plt.plot(test_r2_scores_1model, label = 'no Dropout')\n"
                "plt.plot(test_r2_scores, label = 'with Dropout')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    5: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
    "cell_type": "markdown",
    "source": (
        "Используя библиотеку PyTorch, решите задачу классификации (столбец deposit). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Отобразите график значений функции потерь на обучающем множестве по эпохам. Отобразите confusion matrix и classification report, рассчитанные на основе тестового множества. Сравните несколько различных оптимизаторов и графически продемонстрируйте, как выбор оптимизатора влияет на процесс обучения и результаты на тестовом множестве. (20 баллов)"
    )
},
{
    "cell_type": "code",
    "source": (
        "data = pd.read_csv('bank.csv')\n"
        "data.select_dtypes(include = ['object', 'category']).dtypes"
    )
},
{
    "cell_type": "code",
    "source": (
        "categorical_cols = ['job', 'marital', 'education', 'default', 'housing',\n"
        "                    'loan', 'contact', 'month', 'poutcome', 'deposit']\n\n"
        "data_processed = pd.get_dummies(data, columns = categorical_cols, drop_first = True)\n"
        "data_processed.head()"
    )
},
{
    "cell_type": "code",
    "source": (
        "X = data_processed.drop(columns = ['deposit_yes']).to_numpy().astype(float)\n"
        "X = th.tensor(X, dtype = th.float32)\n\n"
        "y = data_processed['deposit_yes'].to_numpy().astype(float)\n"
        "y = th.tensor(y, dtype = th.long)\n\n"
        "th.manual_seed(42)\n"
        "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
        "X.shape, y.shape"
    )
},
{
    "cell_type": "code",
    "source": (
        "sum(y), len(y)"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size = 64)\n\n"
        "model = nn.Sequential(\n"
        "    nn.Linear(in_features = 42, out_features = 64),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 64, out_features = 32),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 32, out_features = 16),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 16, out_features = 2),\n"
        ")\n"
        "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.AdamW(model.parameters(), lr = 0.01)  # AdamW\n\n"
        "epoch_losses = []\n"
        "for epoch in range(50+1):\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(loader)\n"
        "    epoch_losses.append(epoch_loss.item())\n"
        "    if (epoch) % 5 == 0:\n"
        "        print(epoch, epoch_loss.item())\n\n"
        "epoch_losses_AdamW = epoch_losses"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses)\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
        "y_test = test[:][1]\n\n"
        "confusion_matrix(y_test, y_pred_test)"
    )
},
{
    "cell_type": "code",
    "source": (
        "print(classification_report(y_test, y_pred_test))"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size = 64)\n\n"
        "model = nn.Sequential(\n"
        "    nn.Linear(in_features = 42, out_features = 64),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 64, out_features = 32),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 32, out_features = 16),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 16, out_features = 2),\n"
        ")\n"
        "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.SGD(model.parameters(), lr = 0.01)  # SGD\n\n"
        "epoch_losses = []\n"
        "for epoch in range(50+1):\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(loader)\n"
        "    epoch_losses.append(epoch_loss.item())\n"
        "    if (epoch) % 5 == 0:\n"
        "        print(epoch, epoch_loss.item())\n\n"
        "epoch_losses_SGD = epoch_losses"
    )
},
{
    "cell_type": "code",
    "source": (
        "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
        "y_test = test[:][1]\n\n"
        "confusion_matrix(y_test, y_pred_test)"
    )
},
{
    "cell_type": "code",
    "source": (
        "print(classification_report(y_test, y_pred_test))"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size = 64)\n\n"
        "model = nn.Sequential(\n"
        "    nn.Linear(in_features = 42, out_features = 64),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 64, out_features = 32),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 32, out_features = 16),\n"
        "    nn.ReLU(),\n"
        "    nn.Linear(in_features = 16, out_features = 2),\n"
        ")\n"
        "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.RMSprop(model.parameters(), lr = 0.01)  # RMSprop\n\n"
        "epoch_losses = []\n"
        "for epoch in range(50+1):\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(loader)\n"
        "    epoch_losses.append(epoch_loss.item())\n"
        "    if (epoch) % 5 == 0:\n"
        "        print(epoch, epoch_loss.item())\n\n"
        "epoch_losses_RMSprop = epoch_losses"
    )
},
{
    "cell_type": "code",
    "source": (
        "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
        "y_test = test[:][1]\n\n"
        "confusion_matrix(y_test, y_pred_test)"
    )
},
{
    "cell_type": "code",
    "source": (
        "print(classification_report(y_test, y_pred_test))"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses_AdamW, label='AdamW')\n"
        "plt.plot(epoch_losses_SGD, label='SGD')\n"
        "plt.plot(epoch_losses_RMSprop, label='RMSprop')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
}
    ],
    6: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Используя библиотеку PyTorch, решите задачу классификации (столбец deposit). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Отобразите график значений функции потерь на обучающем множестве по эпохам. Отобразите confusion matrix и classification report, рассчитанные на основе тестового множества. Добавьте в модель слои Dropout и графически продемонстрируйте, как это влияет на процесс обучения и результаты на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('bank.csv')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "categorical_cols = ['job', 'marital', 'education', 'default', 'housing',\n"
                "                    'loan', 'contact', 'month', 'poutcome', 'deposit']\n\n"
                "data_processed = pd.get_dummies(data, columns = categorical_cols, drop_first = True)\n"
                "data_processed.head()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data_processed.drop(columns = ['deposit_yes']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data_processed['deposit_yes'].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.long)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "sum(y), len(y)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 42, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 2),\n"
                ")\n"
                "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(50+1):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_no_dropout = epoch_losses"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
                "y_test = test[:][1]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 42, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Dropout(p = 0.3),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 2),\n"
                ")\n"
                "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(50+1):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_with_dropout = epoch_losses"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
                "y_test = test[:][1]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses_with_dropout, label = 'with dropout')\n"
                "plt.plot(epoch_losses_no_dropout, label = 'no dropout')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    7: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{ "cell_type": "markdown", "source": ( "Используя библиотеку PyTorch, решите задачу классификации (столбец deposit). Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (корректно обработайте случаи категориальных и нечисловых столбцов, при наличии). Отобразите график значений функции потерь на обучающем множестве по эпохам. Отобразите confusion matrix и classification report, рассчитанные на основе тестового множества. Модифицируйте функцию потерь с учетом несбалансированности классов и продемонстрируйте, как это влияет на результаты на тестовом множестве. (20 баллов)" ) },
{
            "cell_type": "code",
            "source": (
                "data = pd.read_csv('bank.csv')\n"
                "data.select_dtypes(include = ['object', 'category']).dtypes"
            )
        },
{
            "cell_type": "code",
            "source": (
                "categorical_cols = ['job', 'marital', 'education', 'default', 'housing',\n"
                "                    'loan', 'contact', 'month', 'poutcome', 'deposit']\n\n"
                "data_processed = pd.get_dummies(data, columns = categorical_cols, drop_first = True)\n"
                "data_processed.head()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "X = data_processed.drop(columns = ['deposit_yes']).to_numpy().astype(float)\n"
                "X = th.tensor(X, dtype = th.float32)\n\n"
                "y = data_processed['deposit_yes'].to_numpy().astype(float)\n"
                "y = th.tensor(y, dtype = th.long)\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(TensorDataset(X, y), [0.8, 0.2])\n\n"
                "X.shape, y.shape"
            )
        },
{
            "cell_type": "code",
            "source": (
                "sum(y), len(y)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 42, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 2),\n"
                ")\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(50+1):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_no_weight = epoch_losses"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
                "y_test = test[:][1]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size = 64)\n\n"
                "model = nn.Sequential(\n"
                "    nn.Linear(in_features = 42, out_features = 64),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 64, out_features = 32),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 32, out_features = 16),\n"
                "    nn.ReLU(),\n"
                "    nn.Linear(in_features = 16, out_features = 2),\n"
                ")\n"
                "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(50+1):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    if (epoch) % 5 == 0:\n"
                "        print(epoch, epoch_loss.item())\n\n"
                "epoch_losses_with_weight = epoch_losses"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = model(test[:][0]).argmax(dim = 1)\n"
                "y_test = test[:][1]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses_with_weight, label = 'with weight')\n"
                "plt.plot(epoch_losses_no_weight, label = 'no weight')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    8 : [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (приведите изображения к одному размеру, нормализуйте и преобразуйте изображения в тензоры). Отобразите confusion matrix и classification report, рассчитанные на основе тестового множества. Выберите один пример из тестового множества, для которого модель ошиблась. Найдите несколько наиболее похожих на данное изображений на основе векторов скрытых представлений, полученных сетью. Визуализируйте оригинальное изображение и найденные похожие изображения. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor()\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'sign_language', transform = transform)\n\n"
                "dataset_loader = DataLoader(dataset, batch_size = 8)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "n = len(dataset) * 32 * 32\n\n"
                "mu = th.zeros((3,), dtype=th.float)\n"
                "sig = th.zeros((3,), dtype=th.float)\n\n"
                "for batch, _ in dataset_loader:\n"
                "    for data in batch:\n"
                "        mu += data.sum(dim=1).sum(dim=1)\n"
                "        sig += (data**2).sum(dim=1).sum(dim=1)\n\n"
                "mu = mu / n\n"
                "sig = th.sqrt(sig / n - mu**2)\n\n"
                "mu, sig"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean=mu, std=sig)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root='sign_language', transform=transform_new)\n\n"
                "print(f'Картинок в датасете: {len(dataset)}')\n"
                "print(f'Количество классов: {len(dataset.classes)}')\n"
                "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(dataset, [0.8, 0.2])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n\n"
                "        self.conv_block1 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=3,\n"
                "                out_channels=6,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.conv_block2 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=6,\n"
                "                out_channels=12,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.classifier = nn.Linear(432, 10)\n\n"
                "    def forward(self, X, return_features=False):\n"
                "        out = self.conv_block1(X)\n"
                "        out = self.conv_block2(out)\n"
                "        out = out.flatten(start_dim=1)\n"
                "        if return_features:\n"
                "            return out\n"
                "        out = self.classifier(out)\n"
                "        return out"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size=8)\n\n"
                "model = CNN()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(5):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = [model(test[i][0].unsqueeze(0)).argmax(dim=1) for i in range(len(test))]\n"
                "y_test = [test[i][1] for i in range(len(test))]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "for i in range(len(test)):\n"
                "    if model(test[i][0].unsqueeze(0)).argmax(dim=1).item() != test[i][1]:\n"
                "        print(f'Номер картинки: {i}')\n"
                "        print(f'Предположительный класс: {model(test[i][0].unsqueeze(0)).argmax(dim=1).item()}')\n"
                "        print(f'Реальный класс: {test[i][1]}')\n"
                "        break"
            )
        },
{
            "cell_type": "code",
            "source": (
                "target = model(test[i][0].unsqueeze(0), return_features=True)\n"
                "similarity = []\n"
                "for i in range(len(test)):\n"
                "    sim = th.cosine_similarity(target, model(test[i][0].unsqueeze(0), return_features=True)).item()\n"
                "    similarity.append((sim, i))\n"
                "similarity = sorted(similarity, key=lambda x: x[0], reverse=True)\n"
                "similarity[:5]"
            )
        },
{
            "cell_type": "code",
            "source": (
                "def show_image(image, mean=mu, std=sig, model=model):\n"
                "    true = image[1]\n"
                "    image = image[0]\n"
                "    pred = model(image.unsqueeze(0)).argmax(dim=1).item()\n\n"
                "    image = image.numpy().transpose((1, 2, 0))\n"
                "    image = std * image + mean\n\n"
                "    plt.title(f'Predict: {pred} | True: {true}')\n"
                "    plt.imshow(image)\n"
                "    plt.axis('off')\n"
                "    plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "show_image(test[2])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "show_image(test[110])"
            )
        }
    ],
    9: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{ "cell_type": "markdown", "source": ( "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (приведите изображения к одному размеру, нормализуйте и преобразуйте изображения в тензоры). Отобразите графики значений функции потерь по эпохам на обучающем множестве. Отобразите confusion matrix и classification report, рассчитанные на основе тестового множества. Уменьшите размерность скрытых представлений изображений с помощью PCA и визуализируйте полученные представления, раскрасив точки в соответствии с классами. (20 баллов)" ) },
{
            "cell_type": "code",
            "source": (
                "transform = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor()\n"
                "])\n"
                "\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'sign_language', transform = transform)\n"
                "\n"
                "dataset_loader = DataLoader(dataset, batch_size = 8)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "n = len(dataset) * 32 * 32\n"
                "\n"
                "mu = th.zeros((3,), dtype=th.float)\n"
                "sig = th.zeros((3,), dtype=th.float)\n"
                "\n"
                "for batch, _ in dataset_loader:\n"
                "    for data in batch:\n"
                "        mu += data.sum(dim=1).sum(dim=1)\n"
                "        sig += (data**2).sum(dim=1).sum(dim=1)\n"
                "\n"
                "mu = mu / n\n"
                "sig = th.sqrt(sig / n - mu**2)\n"
                "\n"
                "mu, sig"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean=mu, std=sig)\n"
                "])\n"
                "\n"
                "dataset = torchvision.datasets.ImageFolder(root='sign_language', transform=transform_new)\n"
                "\n"
                "print(f'Картинок в датасете: {len(dataset)}')\n"
                "print(f'Количество классов: {len(dataset.classes)}')\n"
                "print(f'Размер картинки: {dataset[0][0].shape}')\n"
                "\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(dataset, [0.8, 0.2])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n"
                "\n"
                "        self.conv_block1 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=3,\n"
                "                out_channels=6,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n"
                "\n"
                "        self.conv_block2 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=6,\n"
                "                out_channels=12,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n"
                "\n"
                "        self.classifier = nn.Linear(432, 10)\n"
                "\n"
                "    def forward(self, X, return_features=False):\n"
                "        out = self.conv_block1(X)\n"
                "        out = self.conv_block2(out)\n"
                "        out = out.flatten(start_dim=1)\n"
                "        if return_features:\n"
                "            return out\n"
                "        out = self.classifier(out)\n"
                "        return out"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size=8)\n\n"
                "model = CNN()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n\n"
                "epoch_losses = []\n"
                "for epoch in range(5):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(loader)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "y_pred_test = [model(test[i][0].unsqueeze(0)).argmax(dim=1) for i in range(len(test))]\n"
                "y_test = [test[i][1] for i in range(len(test))]\n\n"
                "confusion_matrix(y_test, y_pred_test)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "print(classification_report(y_test, y_pred_test))"
            )
        },
{
            "cell_type": "code",
            "source": (
                "features = []\n"
                "labels = []\n"
                "for X, y in test:\n"
                "    feature_vector = model(X, return_features=True).detach()\n"
                "    features.append(feature_vector)\n"
                "    labels.append(y)\n"
                "\n"
                "features = th.cat(features).numpy()\n"
                "labels = th.tensor(labels)\n"
                "\n"
                "pca = PCA(n_components=2)\n"
                "reduced_features = pca.fit_transform(features)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "for class_idx in range(len(dataset.classes)):\n"
                "    idxs = [i for i, label in enumerate(labels) if label == class_idx]\n"
                "    plt.scatter(reduced_features[idxs, 0], reduced_features[idxs, 1],\n"
                "                label=dataset.classes[class_idx])\n"
                "\n"
                "plt.title('Визуализация скрытых представлений (PCA)')\n"
                "plt.xlabel('Главная компонента 1')\n"
                "plt.ylabel('Главная компонента 2')\n"
                "plt.legend(title='Классы')\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    10: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений.\n"
                "Разделите набор данных на обучающее и тестовое множество.\n"
                "Выполните предобработку данных (приведите изображения к одному размеру, нормализуйте и преобразуйте изображения в тензоры).\n"
                "Графически отобразите, как качество на тестовом множестве (micro F1) зависит от количества сверточных блоков (свертка, активация, пуллинг).\n"
                "(20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor()\n"
                "])\n"
                "\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'sign_language', transform = transform)\n"
                "\n"
                "dataset_loader = DataLoader(dataset, batch_size = 8)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "n = len(dataset) * 32 * 32\n"
                "\n"
                "mu = th.zeros((3,), dtype=th.float)\n"
                "sig = th.zeros((3,), dtype=th.float)\n"
                "\n"
                "for batch, _ in dataset_loader:\n"
                "    for data in batch:\n"
                "        mu += data.sum(dim=1).sum(dim=1)\n"
                "        sig += (data**2).sum(dim=1).sum(dim=1)\n"
                "\n"
                "mu = mu / n\n"
                "sig = th.sqrt(sig / n - mu**2)\n"
                "\n"
                "mu, sig"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean=mu, std=sig)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root='sign_language', transform=transform_new)\n\n"
                "print(f'Картинок в датасете: {len(dataset)}')\n"
                "print(f'Количество классов: {len(dataset.classes)}')\n"
                "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(dataset, [0.8, 0.2])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN_1block(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n\n"
                "        self.conv_block1 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=3,\n"
                "                out_channels=6,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.classifier = nn.Linear(1350, 10)\n\n"
                "    def forward(self, X):\n"
                "        out = self.conv_block1(X)\n"
                "        out = out.flatten(start_dim=1)\n"
                "        out = self.classifier(out)\n"
                "        return out"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n"
                "\n"
                "loader = DataLoader(train, batch_size = 8)\n"
                "loader_test = DataLoader(test, batch_size = 8)\n"
                "\n"
                "model = CNN_1block()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n"
                "epoch_losses = []\n"
                "\n"
                "f1 = M.F1Score(task = 'multiclass', num_classes = 10, average = 'micro')\n"
                "f1_test = []\n"
                "\n"
                "for epoch in range(5):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred.squeeze(0), y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "\n"
                "    for batch in loader_test:\n"
                "        for i in range(len(batch)):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "\n"
                "    f1_test.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('F1_Score')\n"
                "plt.plot(f1_test)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN_2blocks(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n\n"
                "        self.conv_block1 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=3,\n"
                "                out_channels=6,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.conv_block2 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=6,\n"
                "                out_channels=12,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.classifier = nn.Linear(432, 10)\n\n"
                "    def forward(self, X):\n"
                "        out = self.conv_block1(X)\n"
                "        out = self.conv_block2(out)\n"
                "        out = out.flatten(start_dim=1)\n"
                "        out = self.classifier(out)\n"
                "        return out"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN_3blocks(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n\n"
                "        self.conv_block1 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=3,\n"
                "                out_channels=6,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.conv_block2 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=6,\n"
                "                out_channels=12,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.conv_block3 = nn.Sequential(\n"
                "            nn.Conv2d(\n"
                "                in_channels=12,\n"
                "                out_channels=24,\n"
                "                kernel_size=3,\n"
                "            ),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2, 2),\n"
                "        )\n\n"
                "        self.classifier = nn.Linear(96, 10)\n\n"
                "    def forward(self, X):\n"
                "        out = self.conv_block1(X)\n"
                "        out = self.conv_block2(out)\n"
                "        out = self.conv_block3(out)\n"
                "        out = out.flatten(start_dim=1)\n"
                "        out = self.classifier(out)\n"
                "        return out"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n"
                "\n"
                "loader = DataLoader(train, batch_size=8)\n"
                "loader_test = DataLoader(test, batch_size=8)\n"
                "\n"
                "model = CNN_2blocks()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n"
                "epoch_losses = []\n"
                "\n"
                "f1 = M.F1Score(task='multiclass', num_classes=10, average='micro')\n"
                "f1_test_2 = []\n"
                "\n"
                "for epoch in range(5):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred.squeeze(0), y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "\n"
                "    for batch in loader_test:\n"
                "        for i in range(len(batch)):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "\n"
                "    f1_test_2.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n"
                "\n"
                "loader = DataLoader(train, batch_size=8)\n"
                "loader_test = DataLoader(test, batch_size=8)\n"
                "\n"
                "model = CNN_3blocks()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n"
                "epoch_losses = []\n"
                "\n"
                "f1 = M.F1Score(task='multiclass', num_classes=10, average='micro')\n"
                "f1_test_3 = []\n"
                "\n"
                "for epoch in range(5):\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred.squeeze(0), y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train)\n"
                "    epoch_losses.append(epoch_loss.item())\n"
                "\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "\n"
                "    for batch in loader_test:\n"
                "        for i in range(len(batch)):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "\n"
                "    f1_test_3.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('F1_Score')\n"
                "plt.plot(f1_test, label='1 block')\n"
                "plt.plot(f1_test_2, label='2 blocks')\n"
                "plt.plot(f1_test_3, label='3 blocks')\n"
                "plt.legend()\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    11: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. Разделите набор данных на обучающее, валидационное и тестовое множество. Выполните предобработку данных (вырежьте центральную область изображений одинакового размера и преобразуйте изображения в тензоры). Реализуйте логику ранней остановки (на основе метрики micro F1 на валидационном множестве). Выведите значение micro F1 на тестовом множестве. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.ToTensor()\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform)\n\n"
                "dataset_loader = DataLoader(dataset, batch_size = 8)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "n = len(dataset) * 40 * 40\n"
                "\n"
                "mu = th.zeros((3,), dtype=th.float)\n"
                "sig = th.zeros((3,), dtype=th.float)\n"
                "\n"
                "for batch, _ in dataset_loader:\n"
                "    for data in batch:\n"
                "        mu += data.sum(dim=1).sum(dim=1)\n"
                "        sig += (data**2).sum(dim=1).sum(dim=1)\n"
                "\n"
                "mu = mu / n\n"
                "sig = th.sqrt(sig / n - mu**2)\n"
                "\n"
                "mu, sig"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.CenterCrop((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean=mu, std=sig)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root='eng_handwritten', transform=transform_new)\n\n"
                "print(f'Картинок в датасете: {len(dataset)}')\n"
                "print(f'Количество классов: {len(dataset.classes)}')\n"
                "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
                "th.manual_seed(42)\n"
                "train, val, test = random_split(dataset, [0.7, 0.15, 0.15])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n"
                "        self.features = nn.Sequential(\n"
                "            nn.Conv2d(in_channels=3, out_channels=4, kernel_size=3, padding=1),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2),\n"
                "            nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, padding=1),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2)\n"
                "        )\n"
                "        self.classifier = nn.Linear(8 * 8 * 8, 26)\n"
                "\n"
                "    def forward(self, x):\n"
                "        x = self.features(x)\n"
                "        x = x.view(x.size(0), -1)\n"
                "        x = self.classifier(x)\n"
                "        return x"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size=8)\n"
                "loader_val = DataLoader(val, batch_size=8)\n"
                "loader_test = DataLoader(test, batch_size=8)\n\n"
                "model = CNN()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n"
                "epoch_losses = []\n\n"
                "f1 = M.F1Score(task='multiclass', num_classes=26, average='micro')\n"
                "f1_test = []\n"
                "f1_val_max = 0\n"
                "counter = 0\n\n"
                "for epoch in range(10):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "    for batch in loader_test:\n"
                "        for i in range(len(batch[0])):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "    f1_test.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "    for batch in loader_val:\n"
                "        for i in range(len(batch[0])):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "    f1_val = f1(th.tensor(test_pred), th.tensor(test_true))\n"
                "    if f1_val > f1_val_max:\n"
                "        f1_val_max = f1_val\n"
                "        counter = 0\n"
                "    else:\n"
                "        counter += 1\n\n"
                "    if counter == 3:\n"
                "        print('Ранняя остановка')\n"
                "        print(epoch, epoch_loss.item(), f1_val_max.item())\n"
                "        break\n\n"
                "    print(epoch, epoch_loss.item(), f1_val_max.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('F1_Score')\n"
                "plt.plot(f1_test)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        }
    ],
    12: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
            "cell_type": "markdown",
            "source": (
                "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. "
                "Разделите набор данных на обучающее, валидационное и тестовое множество. "
                "Выполните предобработку данных (вырежьте центральную область изображений одинакового размера и преобразуйте изображения в тензоры). "
                "Выведите значение micro F1 на тестовом множестве. "
                "Выберите случайным образом одно изображение из тестового множества и сделайте три любые случайные модификации. "
                "Визуализируйте измененные изображения и продемонстрируйте, как эти изменения влияют на предсказания модели. (20 баллов)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.ToTensor()\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform)\n\n"
                "dataset_loader = DataLoader(dataset, batch_size = 8)"
            )
        },
{
            "cell_type": "code",
            "source": (
                "n = len(dataset) * 40 * 40\n\n"
                "mu = th.zeros((3,), dtype=th.float)\n"
                "sig = th.zeros((3,), dtype=th.float)\n\n"
                "for batch, _ in dataset_loader:\n"
                "    for data in batch:\n"
                "        mu += data.sum(dim = 1).sum(dim = 1)\n"
                "        sig += (data**2).sum(dim = 1).sum(dim = 1)\n\n"
                "mu = mu / n\n"
                "sig = th.sqrt(sig / n - mu**2)\n\n"
                "mu, sig"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.CenterCrop((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean = mu, std = sig)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform_new)\n\n"
                "print(f'Картинок в датасете: {len(dataset)}')\n"
                "print(f'Количество классов: {len(dataset.classes)}')\n"
                "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
                "th.manual_seed(42)\n"
                "train, test = random_split(dataset, [0.8, 0.2])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "class CNN(nn.Module):\n"
                "    def __init__(self):\n"
                "        super().__init__()\n"
                "        self.features = nn.Sequential(\n"
                "            nn.Conv2d(in_channels=3, out_channels=4, kernel_size=3, padding=1),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2),\n"
                "            nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, padding=1),\n"
                "            nn.ReLU(),\n"
                "            nn.MaxPool2d(2)\n"
                "        )\n"
                "        self.classifier = nn.Linear(8 * 8 * 8, 26)\n\n"
                "    def forward(self, x):\n"
                "        x = self.features(x)\n"
                "        x = x.view(x.size(0), -1)\n"
                "        x = self.classifier(x)\n"
                "        return x"
            )
        },
{
            "cell_type": "code",
            "source": (
                "th.manual_seed(42)\n\n"
                "loader = DataLoader(train, batch_size = 8)\n"
                "loader_test = DataLoader(test, batch_size = 8)\n\n"
                "model = CNN()\n"
                "criterion = nn.CrossEntropyLoss()\n"
                "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n"
                "epoch_losses = []\n\n"
                "f1 = M.F1Score(task = 'multiclass', num_classes = 26, average = 'micro')\n"
                "f1_test = []\n\n"
                "for epoch in range(5):\n"
                "    model.train()\n"
                "    epoch_loss = 0\n"
                "    for X_batch, y_batch in loader:\n"
                "        y_pred = model(X_batch)\n"
                "        loss = criterion(y_pred, y_batch)\n"
                "        epoch_loss += loss\n"
                "        loss.backward()\n"
                "        optimizer.step()\n"
                "        optimizer.zero_grad()\n"
                "    epoch_loss = epoch_loss / len(train)\n"
                "    epoch_losses.append(epoch_loss.item())\n\n"
                "    model.eval()\n"
                "    test_pred = []\n"
                "    test_true = []\n"
                "    for batch in loader_test:\n"
                "        for i in range(len(batch)):\n"
                "            X = batch[0][i].unsqueeze(0)\n"
                "            y = batch[1][i]\n"
                "            test_true.append(y)\n"
                "            test_pred.append(model(X).argmax())\n"
                "    f1_test.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n\n"
                "    print(epoch, epoch_loss.item())"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('CrossEntropyLoss')\n"
                "plt.plot(epoch_losses)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "plt.title('F1_Score')\n"
                "plt.plot(f1_test)\n"
                "plt.grid(True)\n"
                "plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "def show_image(image, mean = mu, std = sig, model = model):\n"
                "    true = image[1]\n"
                "    image = image[0]\n"
                "    pred = model(image.unsqueeze(0)).argmax(dim = 1).item()\n\n"
                "    image = image.numpy().transpose((1, 2, 0))\n"
                "    image = std * image + mean\n\n"
                "    plt.title(f'Predict: {pred} | True: {true}')\n"
                "    plt.imshow(image)\n"
                "    plt.show()"
            )
        },
{
            "cell_type": "code",
            "source": (
                "choice = randint(0, len(test))\n"
                "show_image(test[choice]) # 262"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.CenterCrop((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean = mu, std = sig),\n"
                "    T.ColorJitter(hue = 0.2)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform_new)\n\n"
                "th.manual_seed(42)\n"
                "_, test_1 = random_split(dataset, [0.8, 0.2])\n\n"
                "show_image(test_1[choice])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.CenterCrop((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean = mu, std = sig),\n"
                "    T.RandomHorizontalFlip(p = 1.0)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform_new)\n\n"
                "th.manual_seed(42)\n"
                "_, test_2 = random_split(dataset, [0.8, 0.2])\n\n"
                "show_image(test_2[choice])"
            )
        },
{
            "cell_type": "code",
            "source": (
                "transform_new = T.Compose([\n"
                "    T.Resize((40, 40)),\n"
                "    T.CenterCrop((32, 32)),\n"
                "    T.ToTensor(),\n"
                "    T.Normalize(mean = mu, std = sig),\n"
                "    T.RandomVerticalFlip(p = 1.0)\n"
                "])\n\n"
                "dataset = torchvision.datasets.ImageFolder(root = 'eng_handwritten', transform = transform_new)\n\n"
                "th.manual_seed(42)\n"
                "_, test_3 = random_split(dataset, [0.8, 0.2])\n\n"
                "show_image(test_3[choice])"
            )
        }
    ],
    13: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
    "cell_type": "markdown",
    "source": (
        "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. "
        "Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (приведите изображения к одному размеру, "
        "нормализуйте и преобразуйте в тензоры). Выведите значение F1 на тестовом множестве. Повторите решение задачи, применяя к обучающему "
        "множеству преобразования, случайным образом изменяющие изображения. Выведите значение F1 на тестовом множестве для модели, которая "
        "обучалась на расширенном датасете. (20 баллов)"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor()\n"
        "])\n\n"
        "dataset = torchvision.datasets.ImageFolder(root = 'chars', transform = transform)\n\n"
        "dataset_loader = DataLoader(dataset, batch_size = 8)"
    )
},
{
    "cell_type": "code",
    "source": (
        "n = len(dataset) * 64 * 64\n\n"
        "mu = th.zeros((3,), dtype=th.float)\n"
        "sig = th.zeros((3,), dtype=th.float)\n\n"
        "for batch, _ in dataset_loader:\n"
        "    for data in batch:\n"
        "        mu += data.sum(dim = 1).sum(dim = 1)\n"
        "        sig += (data**2).sum(dim = 1).sum(dim = 1)\n\n"
        "mu = mu / n\n"
        "sig = th.sqrt(sig / n - mu**2)\n\n"
        "mu, sig"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform_new = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor(),\n"
        "    T.Normalize(mean = mu, std = sig)\n"
        "])\n\n"
        "dataset = torchvision.datasets.ImageFolder(root = 'chars', transform = transform_new)\n\n"
        "print(f'Картинок в датасете: {len(dataset)}')\n"
        "print(f'Количество классов: {len(dataset.classes)}')\n"
        "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
        "th.manual_seed(42)\n"
        "train, test = random_split(dataset, [0.8, 0.2])"
    )
},
{
    "cell_type": "code",
    "source": (
        "sum([dataset[i][1] for i in range(len(dataset))]), len(dataset)"
    )
},
{
    "cell_type": "code",
    "source": (
        "class CNN(nn.Module):\n"
        "    def __init__(self):\n"
        "        super().__init__()\n\n"
        "        self.conv_block1 = nn.Sequential(\n"
        "            nn.Conv2d(\n"
        "                in_channels = 3,\n"
        "                out_channels = 6,\n"
        "                kernel_size = 3,\n"
        "            ),\n"
        "            nn.ReLU(),\n"
        "            nn.MaxPool2d(2, 2),\n"
        "        )\n\n"
        "        self.classifier = nn.Linear(5766, 2)\n\n"
        "    def forward(self, X):\n"
        "        out = self.conv_block1(X)\n"
        "        out = out.flatten(start_dim = 1)\n"
        "        out = self.classifier(out)\n"
        "        return out"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size = 8)\n"
        "loader_test = DataLoader(test, batch_size = 8)\n\n"
        "model = CNN()\n"
        "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n"
        "epoch_losses = []\n\n"
        "f1 = M.F1Score(task = 'binary')\n"
        "f1_test = []\n\n"
        "for epoch in range(5):\n"
        "    model.train()\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(train)\n"
        "    epoch_losses.append(epoch_loss.item())\n\n"
        "    model.eval()\n"
        "    test_pred = []\n"
        "    test_true = []\n"
        "    for batch in loader_test:\n"
        "        for i in range(len(batch)):\n"
        "            X = batch[0][i].unsqueeze(0)\n"
        "            y = batch[1][i]\n"
        "            test_true.append(y)\n"
        "            test_pred.append(model(X).argmax())\n"
        "    f1_test.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n\n"
        "    print(epoch, epoch_loss.item())\n\n"
        "epoch_losses_mini = epoch_losses\n"
        "f1_test_mini = f1_test"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses)\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('F1_Score')\n"
        "plt.plot(f1_test)\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform_new = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor(),\n"
        "    T.Normalize(mean = mu, std = sig),\n"
        "    T.RandomRotation(degrees = 10),\n"
        "    T.RandomHorizontalFlip(p = 0.1)\n"
        "])\n\n"
        "dataset_2 = torchvision.datasets.ImageFolder(root = 'chars', transform = transform_new)\n\n"
        "th.manual_seed(42)\n"
        "train_2, _ = random_split(dataset_2, [0.8, 0.2])\n\n"
        "train = ConcatDataset([train, train_2])\n"
        "len(train)"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size = 8)\n"
        "loader_test = DataLoader(test, batch_size = 8)\n\n"
        "model = CNN()\n"
        "criterion = nn.CrossEntropyLoss(weight = th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.AdamW(model.parameters(), lr = 0.01)\n"
        "epoch_losses = []\n\n"
        "f1 = M.F1Score(task = 'binary')\n"
        "f1_test = []\n\n"
        "for epoch in range(5):\n"
        "    model.train()\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(train)\n"
        "    epoch_losses.append(epoch_loss.item())\n\n"
        "    model.eval()\n"
        "    test_pred = []\n"
        "    test_true = []\n"
        "    for batch in loader_test:\n"
        "        for i in range(len(batch)):\n"
        "            X = batch[0][i].unsqueeze(0)\n"
        "            y = batch[1][i]\n"
        "            test_true.append(y)\n"
        "            test_pred.append(model(X).argmax())\n"
        "    f1_test.append(f1(th.tensor(test_pred), th.tensor(test_true)))\n\n"
        "    print(epoch, epoch_loss.item())"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses, label = 'Расширенный датасет')\n"
        "plt.plot(epoch_losses_mini, label = 'Начальный датасет')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('F1_Score')\n"
        "plt.plot(f1_test, label = 'Расширенный датасет')\n"
        "plt.plot(f1_test_mini, label = 'Начальный датасет')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
}
    ],
    14: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
    "cell_type": "markdown",
    "source": (
        "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу классификации изображений. "
        "Разделите набор данных на обучающее и тестовое множество. Выполните предобработку данных (приведите изображения к одному размеру, "
        "нормализуйте и преобразуйте в тензоры). Добавьте следующую логику постобработки прогнозов: если сеть не уверена в предсказании "
        "(максимальная вероятность ниже некоторого заданного порога), классифицируйте изображение как \"неопределенный\" класс. "
        "Оцените, как этот порог отсечения влияет на метрики и количество \"неопределенных\" изображений. (20 баллов)"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor()\n"
        "])\n\n"
        "dataset = torchvision.datasets.ImageFolder(root='chars', transform=transform)\n\n"
        "dataset_loader = DataLoader(dataset, batch_size=8)"
    )
},
{
    "cell_type": "code",
    "source": (
        "n = len(dataset) * 64 * 64\n\n"
        "mu = th.zeros((3,), dtype=th.float)\n"
        "sig = th.zeros((3,), dtype=th.float)\n\n"
        "for batch, _ in dataset_loader:\n"
        "    for data in batch:\n"
        "        mu += data.sum(dim=1).sum(dim=1)\n"
        "        sig += (data**2).sum(dim=1).sum(dim=1)\n\n"
        "mu = mu / n\n"
        "sig = th.sqrt(sig / n - mu**2)\n\n"
        "mu, sig"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform_new = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor(),\n"
        "    T.Normalize(mean=mu, std=sig)\n"
        "])\n\n"
        "dataset = torchvision.datasets.ImageFolder(root='chars', transform=transform_new)\n\n"
        "print(f'Картинок в датасете: {len(dataset)}')\n"
        "print(f'Количество классов: {len(dataset.classes)}')\n"
        "print(f'Размер картинки: {dataset[0][0].shape}')\n\n"
        "th.manual_seed(42)\n"
        "train, test = random_split(dataset, [0.8, 0.2])"
    )
},
{
    "cell_type": "code",
    "source": (
        "sum([dataset[i][1] for i in range(len(dataset))]), len(dataset)"
    )
},
{
    "cell_type": "code",
    "source": (
        "class CNN(nn.Module):\n"
        "    def __init__(self):\n"
        "        super().__init__()\n\n"
        "        self.conv_block1 = nn.Sequential(\n"
        "            nn.Conv2d(\n"
        "                in_channels=3,\n"
        "                out_channels=6,\n"
        "                kernel_size=3,\n"
        "            ),\n"
        "            nn.ReLU(),\n"
        "            nn.MaxPool2d(2, 2),\n"
        "        )\n\n"
        "        self.classifier = nn.Linear(5766, 2)\n\n"
        "    def forward(self, X):\n"
        "        out = self.conv_block1(X)\n"
        "        out = out.flatten(start_dim=1)\n"
        "        out = self.classifier(out)\n"
        "        return out"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n\n"
        "loader = DataLoader(train, batch_size=8)\n"
        "loader_test = DataLoader(test, batch_size=8)\n\n"
        "model = CNN()\n"
        "criterion = nn.CrossEntropyLoss(weight=th.tensor([0.3, 0.7]))\n"
        "optimizer = optim.AdamW(model.parameters(), lr=0.01)\n"
        "epoch_losses = []\n\n"
        "f1 = M.F1Score(task='multiclass', num_classes=3)\n"
        "f1_test_60 = []\n"
        "f1_test_70 = []\n"
        "f1_test_80 = []\n"
        "count_2_60 = []\n"
        "count_2_70 = []\n"
        "count_2_80 = []\n\n"
        "for epoch in range(5):\n"
        "    model.train()\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in loader:\n"
        "        y_pred = model(X_batch)\n"
        "        loss = criterion(y_pred, y_batch)\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(train)\n"
        "    epoch_losses.append(epoch_loss.item())\n\n"
        "    model.eval()\n"
        "    test_pred_60 = []\n"
        "    test_pred_70 = []\n"
        "    test_pred_80 = []\n"
        "    test_true = []\n"
        "    for batch in loader_test:\n"
        "        for i in range(len(batch)):\n"
        "            X = batch[0][i].unsqueeze(0)\n"
        "            y = batch[1][i]\n"
        "            test_true.append(y)\n"
        "            prob = model(X).softmax(dim=1)\n\n"
        "            if prob.max() < 0.6:\n"
        "                test_pred_60.append(2)\n"
        "            else:\n"
        "                test_pred_60.append(prob.argmax())\n\n"
        "            if prob.max() < 0.7:\n"
        "                test_pred_70.append(2)\n"
        "            else:\n"
        "                test_pred_70.append(prob.argmax())\n\n"
        "            if prob.max() < 0.8:\n"
        "                test_pred_80.append(2)\n"
        "            else:\n"
        "                test_pred_80.append(prob.argmax())\n\n"
        "    f1_test_60.append(f1(th.tensor(test_pred_60), th.tensor(test_true)))\n"
        "    count_2_60.append(test_pred_60.count(2))\n"
        "    f1_test_70.append(f1(th.tensor(test_pred_70), th.tensor(test_true)))\n"
        "    count_2_70.append(test_pred_70.count(2))\n"
        "    f1_test_80.append(f1(th.tensor(test_pred_80), th.tensor(test_true)))\n"
        "    count_2_80.append(test_pred_80.count(2))\n\n"
        "    print(epoch, epoch_loss.item())"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses)\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('F1_Score')\n"
        "plt.plot(f1_test_60, label='Порог отсечения 0.6')\n"
        "plt.plot(f1_test_70, label='Порог отсечения 0.7')\n"
        "plt.plot(f1_test_80, label='Порог отсечения 0.8')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('Число неопределённых классов')\n"
        "plt.plot(count_2_60, label='Порог отсечения 0.6')\n"
        "plt.plot(count_2_70, label='Порог отсечения 0.7')\n"
        "plt.plot(count_2_80, label='Порог отсечения 0.8')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
}
    ],
    15: [
{
            "cell_type": "code",
            "source": (
                "import torch as th\n"
                "import torch.nn as nn\n"
                "import torch.optim as optim\n"
                "import torchmetrics as M\n"
                "from torch.utils.data import DataLoader, TensorDataset, random_split, ConcatDataset, Dataset\n"
                "from sklearn.metrics import r2_score, classification_report, confusion_matrix\n"
                "import torchvision\n"
                "import torchvision.transforms.v2 as T\n"
                "import matplotlib.pyplot as plt\n"
                "import pandas as pd\n"
                "from sklearn.decomposition import PCA\n"
                "from random import randint\n"
                "import os\n"
                "from PIL import Image"
            )
        },
{
    "cell_type": "markdown",
    "source": (
        "Реализовав сверточную нейронную сеть при помощи библиотеки PyTorch, решите задачу множественной (multi-label) классификации изображений.\n"
        "Для каждого изображения модель должна предсказывать два класса: цвет и предмет одежды.\n"
        "\n"
        "1. Разделите набор данных на обучающее и тестовое множество.\n"
        "2. Выполните предобработку данных (приведите изображения к одному размеру, нормализуйте и преобразуйте в тензоры).\n"
        "3. Выведите итоговое значение F1 на обучающем множестве и F1 на тестовом множестве.\n"
        "\n"
        "(20 баллов)"
    )
},
{
    "cell_type": "code",
    "source": (
        "class ClothesMultiDataset(Dataset):\n"
        "    def __init__(self, root_directory, transform=None):\n"
        "        folder_names = [f for f in os.listdir(root_directory)\n"
        "                        if os.path.isdir(os.path.join(root_directory, f))]\n"
        "        color_set, item_set = set(), set()\n"
        "        for folder in folder_names:\n"
        "            color_str, item_str = folder.split(\"_\")\n"
        "            color_set.add(color_str)\n"
        "            item_set.add(item_str)\n"
        "        self.color_map = {c: i for i, c in enumerate(sorted(color_set))}\n"
        "        self.item_map  = {i: j for j, i in enumerate(sorted(item_set))}\n"
        "        self.samples = []\n"
        "        for folder in folder_names:\n"
        "            folder_path = os.path.join(root_directory, folder)\n"
        "            color_str, item_str = folder.split(\"_\")\n"
        "            color_label = self.color_map[color_str]\n"
        "            item_label  = self.item_map[item_str]\n"
        "            for image_name in os.listdir(folder_path):\n"
        "                img_path = os.path.join(folder_path, image_name)\n"
        "                self.samples.append((img_path, color_label, item_label))\n"
        "        self.transform = transform\n"
        "\n"
        "    def __len__(self):\n"
        "        return len(self.samples)\n"
        "\n"
        "    def __getitem__(self, index):\n"
        "        path, color_label, item_label = self.samples[index]\n"
        "        image = Image.open(path).convert(\"RGB\")\n"
        "        if self.transform:\n"
        "            image = self.transform(image)\n"
        "        labels = th.tensor([color_label, item_label], dtype=th.long)\n"
        "        return image, labels"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor()\n"
        "])\n"
        "\n"
        "dataset = torchvision.datasets.ImageFolder(root='clothes_multi', transform=transform)\n"
        "\n"
        "dataset_loader = DataLoader(dataset, batch_size=8)"
    )
},
{
    "cell_type": "code",
    "source": (
        "n = len(dataset) * 64 * 64\n"
        "\n"
        "mu = th.zeros((3,), dtype=th.float)\n"
        "sig = th.zeros((3,), dtype=th.float)\n"
        "\n"
        "for batch, _ in dataset_loader:\n"
        "    for data in batch:\n"
        "        mu += data.sum(dim=1).sum(dim=1)\n"
        "        sig += (data**2).sum(dim=1).sum(dim=1)\n"
        "\n"
        "mu = mu / n\n"
        "sig = th.sqrt(sig / n - mu**2)\n"
        "\n"
        "mu, sig"
    )
},
{
    "cell_type": "code",
    "source": (
        "transform_new = T.Compose([\n"
        "    T.Resize((64, 64)),\n"
        "    T.ToTensor(),\n"
        "    T.Normalize(mean=mu, std=sig)\n"
        "])\n"
        "\n"
        "dataset = ClothesMultiDataset(root_directory='clothes_multi', transform=transform_new)\n"
        "\n"
        "print(f'Картинок в датасете: {len(dataset)}')\n"
        "print(f'Цветов в датасете: {len(dataset.color_map)}')\n"
        "print(f'Предметов в датасете: {len(dataset.item_map)}')\n"
        "print(f'Размер картинки: {dataset[0][0].shape}')\n"
        "\n"
        "th.manual_seed(42)\n"
        "train, test = random_split(dataset, [0.8, 0.2])"
    )
},
{
    "cell_type": "code",
    "source": (
        "class CNN(nn.Module):\n"
        "    def __init__(self):\n"
        "        super().__init__()\n"
        "        self.features = nn.Sequential(\n"
        "            nn.Conv2d(in_channels=3, out_channels=4, kernel_size=3, padding=1),\n"
        "            nn.ReLU(),\n"
        "            nn.MaxPool2d(2),\n"
        "            nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, padding=1),\n"
        "            nn.ReLU(),\n"
        "            nn.MaxPool2d(2)\n"
        "        )\n"
        "        self.classifier_color = nn.Linear(2048, 9)\n"
        "        self.classifier_item  = nn.Linear(2048, 8)\n"
        "\n"
        "    def forward(self, x):\n"
        "        out = self.features(x)\n"
        "        out = out.view(out.size(0), -1)\n"
        "        out_color = self.classifier_color(out)\n"
        "        out_item  = self.classifier_item(out)\n"
        "        return out_color, out_item"
    )
},
{
    "cell_type": "code",
    "source": (
        "th.manual_seed(42)\n"
        "\n"
        "train_loader = DataLoader(train, batch_size=8)\n"
        "test_loader  = DataLoader(test, batch_size=8)\n"
        "\n"
        "model = CNN()\n"
        "criterion_color = nn.CrossEntropyLoss()\n"
        "criterion_item  = nn.CrossEntropyLoss()\n"
        "optimizer = optim.Adam(model.parameters(), lr=0.01)\n"
        "epoch_losses = []\n"
        "\n"
        "f1_color = M.F1Score(task='multiclass', num_classes=9, average='micro')\n"
        "f1_item = M.F1Score(task='multiclass', num_classes=8, average='micro')\n"
        "f1_train = []\n"
        "f1_test = []\n"
        "\n"
        "for epoch in range(5):\n"
        "    model.train()\n"
        "    epoch_loss = 0\n"
        "    for X_batch, y_batch in train_loader:\n"
        "        X_batch = X_batch\n"
        "        y_color = y_batch[:, 0]\n"
        "        y_item  = y_batch[:, 1]\n"
        "        out_color, out_item = model(X_batch)\n"
        "        loss_c = criterion_color(out_color, y_color)\n"
        "        loss_i = criterion_item(out_item, y_item)\n"
        "        loss = loss_c + loss_i\n"
        "        epoch_loss += loss\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        optimizer.zero_grad()\n"
        "    epoch_loss = epoch_loss / len(train_loader)\n"
        "    epoch_losses.append(epoch_loss.item())\n"
        "\n"
        "    model.eval()\n"
        "    color_preds = []\n"
        "    color_true = []\n"
        "    item_preds = []\n"
        "    item_true = []\n"
        "    with th.no_grad():\n"
        "        for X_batch, y_batch in train_loader:\n"
        "            X_batch = X_batch\n"
        "            y_color = y_batch[:, 0]\n"
        "            y_item  = y_batch[:, 1]\n"
        "            out_color, out_item = model(X_batch)\n"
        "            pred_color = out_color.argmax(dim=1)\n"
        "            pred_item  = out_item.argmax(dim=1)\n"
        "            color_preds.append(pred_color)\n"
        "            color_true.append(y_color)\n"
        "            item_preds.append(pred_item)\n"
        "            item_true.append(y_item)\n"
        "    color_preds = th.cat(color_preds)\n"
        "    color_true = th.cat(color_true)\n"
        "    item_preds = th.cat(item_preds)\n"
        "    item_true = th.cat(item_true)\n"
        "    f1_color_ = f1_color(color_preds, color_true)\n"
        "    f1_item_  = f1_item(item_preds, item_true)\n"
        "    f1_train.append(0.5 * (f1_color_ + f1_item_))\n"
        "\n"
        "    color_preds = []\n"
        "    color_true = []\n"
        "    item_preds = []\n"
        "    item_true = []\n"
        "    with th.no_grad():\n"
        "        for X_batch, y_batch in test_loader:\n"
        "            X_batch = X_batch\n"
        "            y_color = y_batch[:, 0]\n"
        "            y_item  = y_batch[:, 1]\n"
        "            out_color, out_item = model(X_batch)\n"
        "            pred_color = out_color.argmax(dim=1)\n"
        "            pred_item  = out_item.argmax(dim=1)\n"
        "            color_preds.append(pred_color)\n"
        "            color_true.append(y_color)\n"
        "            item_preds.append(pred_item)\n"
        "            item_true.append(y_item)\n"
        "    color_preds = th.cat(color_preds)\n"
        "    color_true = th.cat(color_true)\n"
        "    item_preds = th.cat(item_preds)\n"
        "    item_true = th.cat(item_true)\n"
        "    f1_color_ = f1_color(color_preds, color_true)\n"
        "    f1_item_  = f1_item(item_preds, item_true)\n"
        "    f1_test.append(0.5 * (f1_color_ + f1_item_))\n"
        "\n"
        "    print(epoch, epoch_loss.item())"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('CrossEntropyLoss')\n"
        "plt.plot(epoch_losses)\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "plt.title('F1_Score')\n"
        "plt.plot(f1_test, label='test')\n"
        "plt.plot(f1_train, label='train')\n"
        "plt.legend()\n"
        "plt.grid(True)\n"
        "plt.show()"
    )
},
{
    "cell_type": "code",
    "source": (
        "f1_test[-1], f1_train[-1]"
    )
}
    ]
}


def task_info():
    """
    Печатает информацию о доступных задачах и количестве ячеек в каждой.
    """
    task_list = ['1. regression/gold.csv. Оптимизаторы', '2. regression/gold.csv. Гиперпараметры', '3. regression/bike_cnt.csv. BatchNorm1d', '4. regression/bike_cnt.csv. Dropout', '5. classification/bank.csv. Оптимизаторы', '6. classification/bank.csv. Dropout', '7. classification/bank.csv. Несбалансированность', '8. images/sign_language.zip. Скрытые представления', '9. images/sign_language.zip. PCA', '10. images/sign_language.zip. Число сверточных блоков', '11. images/eng_handwritten.zip. val, ранняя остановка', '12. images/eng_handwritten.zip. 3 модификации изображения', '13. images/chars.zip. Обычный и расширенный датасеты', '14. images/chars.zip. Неопределенные классы', '15. images/clothes_multi.zip. Задача множественной классификации', ]
    print("Доступные задания:")
    print(*task_list, sep='\n')


def create_task_viewer(cells):
    """
    Возвращает функцию, которая по номеру i выводит i-ую ячейку в нужном формате.
    """
    def view_cell(i):
        if i < 1 or i > len(cells):
            print(f"Нет ячейки с номером {i}. Доступный диапазон: 1..{len(cells)}")
            return
        cell = cells[i-1]
        if cell["cell_type"] == "markdown":
            # Для markdown используем IPython.display.Markdown
            display(Markdown(cell["source"]))
        elif cell["cell_type"] == "code":
            # Для кода используем IPython.display.Code
            # (NB: это выведет подсветку, но не будет исполнять код)
            display(Code(cell["source"], language='python'))
        else:
            # На всякий случай
            print("Неизвестный тип ячейки:", cell["cell_type"])
    return view_cell


def task(n=None):
    """
    Если n не передан, выводит информацию о всех заданиях.
    Если n передан, возвращает функцию, которая выводит i-ую ячейку выбранного задания.
    """
    if n is None:
        task_info()
    else:
        if n not in TASKS:
            print(f"Задания с номером {n} не существует.")
            return None
        cells = TASKS[n]
        return create_task_viewer(cells)
