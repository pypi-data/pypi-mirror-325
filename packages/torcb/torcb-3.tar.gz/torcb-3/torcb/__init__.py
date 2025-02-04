import pyperclip as pc

class tonch:
    def imports():
        s = '''import pandas as pd
import numpy as np

import torch
from torch import nn, optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, TensorDataset, random_split
from torchvision import transforms
from torchvision.datasets import ImageFolder

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score


import matplotlib.pyplot as plt
        '''
        return pc.copy(s)

    def image_dataset_load():
        s = '''transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Resize((300, 300))
                                ])
dataset = ImageFolder(root='images/cat_breeds_4', transform=transform)
dataloader = DataLoader(dataset, batch_size = 32, shuffle = False)
        '''
        return pc.copy(s)

    def image_dataset_normalization():
        s = '''mean = torch.zeros(3)
std = torch.zeros(3)
total_images = 0

for images, labels in dataloader:
batch_samples = images.size(0)
images = images.flatten(2)
mean += images.mean(2).sum(0)
std += images.std(2).sum(0)
total_images += batch_samples
mean /= total_images
std /= total_images

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Resize((300, 300)),
                                transforms.Normalize(mean = mean, std = std)])
dataset = ImageFolder(root='images/cat_breeds_4', transform=transform)
dataloader = DataLoader(dataset, batch_size = 32, shuffle = False)
        '''
        return pc.copy(s)

    def image_accuracy():
        s = '''def accuracy(data_loader, model, device):
    y_pred = []
    y_true = []

    model.eval()
    with torch.no_grad():
    for X_batch, y_batch in data_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
    return accuracy_score(y_true, y_pred)
        '''
        return pc.copy(s)

    def train_with_accuracy():
        s = '''optimizer = optim.Adam(model.parameters(), lr = 0.00001)
loss_function = nn.CrossEntropyLoss()
train_losses = []
test_accuracy = []
train_accuracy = []
model.train()
for epoch in range(10):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        predict = model(X_batch)
        loss = loss_function(predict, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    train_losses.append(loss_for_epoch)
    train_accuracy_for_epoch = accuracy(train_loader, model, device)
    test_accuracy_for_epoch = accuracy(test_loader, model, device)
    train_accuracy.append(train_accuracy_for_epoch)
    test_accuracy.append(test_accuracy_for_epoch)
    if epoch % 1 == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch} | Train accuracy: {train_accuracy_for_epoch} | Test accuracy: {test_accuracy_for_epoch}")
        '''
        return pc.copy(s)

    def parameters_count():
        s = '''print(sum(p.numel() for p in model.parameters() if p.requires_grad))
        '''
        return pc.copy(s)


    def show_images_with_predict():
        s = '''def show_examples(model, dataloader, mean, std, k = 5):
    data_iter = iter(dataloader)
    images, y_true = next(data_iter)
    images, y_true = images.to(device), y_true.to(device)
    classes = test_dataset.dataset.classes
    denormalize = transforms.Normalize((-1 * mean / std), (1.0 / std))

    model.eval()
    with torch.no_grad():
        outputs = model(images)
        predicted = torch.argmax(outputs, 1)

    num_images = k
    plt.figure(figsize=(11, 11))
    for i in range(num_images):
        plt.subplot(2, 3, i + 1)
        plt.imshow(denormalize(images[i].cpu()).clamp(0, 1).numpy().transpose(1, 2, 0))
        plt.axis('off')
        plt.title(f'True: {classes[y_true[i].item()]} \nPredict: {classes[predicted[i].item()]}')
    plt.show()
        '''
        return pc.copy(s)

    def cnn_model():
        s = '''model = nn.Sequential(
    nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Flatten(),
    nn.Linear(64 * 37 * 37, 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 4)
).to(device)
        '''
        return pc.copy(s)

    def visualize_conv1_activations():
        s = '''def visualize_conv1_activations(model, dataloader):
    model.eval()
    with torch.no_grad():
        for input_images, labels in dataloader:
            input_image = input_images[0]  # Берем первую картинку в батче

            activations = model[0](input_image.unsqueeze(0).to(device))

            num_filters = activations.size(1)
            fig = plt.figure(figsize = (20, 10))
            for i in range(num_filters):
                plt.subplot(4, 4, i + 1)
                plt.imshow(activations[0][i].cpu(), cmap = 'gray')
                plt.axis('off')
            plt.show()
            break

visualize_conv1_activations(model, test_loader)
        '''
        return pc.copy(s)

    def cnn_dropout_model():
        s = '''model = nn.Sequential(
    nn.Conv2d(3, 32, kernel_size = 5),
    nn.MaxPool2d(2),
    nn.ReLU(),
    nn.Conv2d(32, 64, kernel_size = 5),
    nn.Dropout2d(0.5),
    nn.MaxPool2d(2),
    nn.ReLU(),
    nn.Flatten(1),
    nn.Linear(64 * 22 * 22, 50),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(50, 25),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(25, 10)
).to(device)
        '''
        return pc.copy(s)

    def test_loss():
        s = '''def test_loss(model, test_loader, device):
model.eval()
loss_for_epoch = 0
with torch.no_grad():
for X_batch, y_batch in test_loader:
X_batch, y_batch = X_batch.to(device), y_batch.to(device)
predict = model(X_batch)
loss = loss_function(predict, y_batch)
loss_for_epoch += loss.item()
loss_for_epoch /= len(test_loader)
return loss_for_epoch
        '''
        return pc.copy(s)


    def collect_y_pred_y_true():
        s = '''y_pred = []
y_true = []

model.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
y_pred = torch.tensor(y_pred)
y_true = torch.tensor(y_true)
        '''
        return pc.copy(s)

    def heatmap():
        s = '''y_pred = []
y_true = []

model.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
y_pred = torch.tensor(y_pred)
y_true = torch.tensor(y_true)
sns.heatmap(confusion_matrix(y_true, y_pred), annot = True)
print(classification_report(y_true, y_pred))
        '''
        return pc.copy(s)
        
    def save_load_model():
        s = '''torch.save(model.state_dict(), 'model.pth')
torch.save(optimizer.state_dict(), 'optimizer.pth')

model.load_state_dict(torch.load('model.pth', weights_only=True))
        '''
        return pc.copy(s)    

    def create_dataset():
        s = '''class DiamondsDataset(Dataset):
def __init__(self, data):
    for col in data.columns:
    if data[col].dtype not in ('float64', 'int64'):
        data = data.drop(col, axis = 1)
    self.X = torch.tensor(data.drop('price', axis = 1).values, dtype = torch.float)
    self.y = torch.tensor(data['price'].values, dtype = torch.float)

def __len__(self):
    return len(self.y)

def __getitem__(self, idx):
    return self.X[idx], self.y[idx]

dataset = DiamondsDataset(df)
train_size = int(0.8 * len(dataset))  # 80% для обучения
test_size = len(dataset) - train_size  # 20% для тестирования
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
print(len(train_dataset))
dataloader = DataLoader(train_dataset, 256, shuffle = True)
print(len(dataloader))
        '''
        return pc.copy(s)    

    def create_dataset_with_transform():
        s = '''class DiamondsDataset(Dataset):
def __init__(self, data, transform):
    self.transform = transform
    self.X = data.drop('price', axis = 1).values
    self.y = data['price'].values

def __len__(self):
    return len(self.y)

def __getitem__(self, idx):
    sample = (self.X[idx], self.y[idx])
    if self.transform:
    sample = self.transform(sample)
    return sample

class ToTensorTransform:
def __call__(self, sample):
    X, y = sample
    # <преобразование X и y в тензоры>
    X = torch.from_numpy(X).type(torch.float)
    y = torch.tensor(y, dtype = torch.float)
    return X, y

to_tensor = ToTensorTransform()
dataset = DiamondsDataset(df, transforms.Compose([to_tensor]))
dataloader = DataLoader(dataset, 256, shuffle = True)
        '''
        return pc.copy(s)   

    def labelencoder_to_string_cols():
        s = '''label_encoder = LabelEncoder()
for col in df:
if df[col].dtype == object:
    df[col] = label_encoder.fit_transform(df[col])
df.head()
        '''
        return pc.copy(s)    

    def standardscaler_to_num_cols():
        s = '''standard_scaler = StandardScaler()
for col in df:
if df[col].dtype == 'float':
    df[col] = standard_scaler.fit_transform(np.array(df[col]).reshape(-1, 1))
df.head()
        '''
        return pc.copy(s)    

    def get_dummies():
        s = '''df_one_hot_encoded = pd.get_dummies(df, columns = ['cut', 'color', 'clarity'], dtype = int)
df_one_hot_encoded.head()
        '''
        return pc.copy(s)    

    def linear_model_batch_normalization():
        s = '''my = nn.Sequential(
    nn.Linear(dataloader.dataset.dataset.X.shape[1], 250),
    nn.BatchNorm1d(250),
    nn.ReLU(),
    nn.Linear(250, 500),
    nn.BatchNorm1d(500),
    nn.ReLU(),
    nn.Linear(500, 250),
    nn.BatchNorm1d(250),
    nn.ReLU(),
    nn.Linear(250, 50),
    nn.BatchNorm1d(50),
    nn.ReLU(),
    nn.Linear(50, 1)
).to(device)
        '''
        return pc.copy(s)    

    def pretrained_model_import():
        s = '''import torchvision.models as models
model = models.vgg16(weights='IMAGENET1K_V1')
print(model, '\n')

layers_count = sum(1 for module in model.modules() if (isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear)))
print(f'Кол-во слоев: {layers_count}\n')

params_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f'Количество настраиваемых параметров: {params_count}')
        '''
        return pc.copy(s)   

    def pretrained_model_freeze_all():
        s = '''for param in model.parameters():
    param.requires_grad = False
        '''
        return pc.copy(s)   

    def pretrained_model_freeze_all_conv():
        s = '''# Заморозить все сверточные слои, кроме последнего
for i, layer in enumerate(model.features):
    if isinstance(layer, torch.nn.Conv2d):
        if i < (len(model.features) - 1):  # Все слои, кроме последнего Conv
            for param in layer.parameters():
                param.requires_grad = False
        '''
        return pc.copy(s)   

    def cnn_full_solution():
        s = '''import pandas as pd
import numpy as np

import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, TensorDataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
from tqdm import tqdm

import matplotlib.pyplot as plt

data_dir = 'chars'

# Предобработка изображений
transform = transforms.Compose([
    transforms.Resize([128, 128]),
    transforms.ToTensor()
])

# Загрузка данных
full_dataset = ImageFolder(data_dir, transform=transform)

train_size = int(0.7 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

device = torch.device('cpu')

model = nn.Sequential(
    nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Flatten(),
    nn.Linear(16384, 128),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(64, 2)
).to(device)

def accuracy(data_loader, model, device):
    y_pred = []
    y_true = []

    model.eval()
    with torch.no_grad():
    for X_batch, y_batch in data_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
    return accuracy_score(y_true, y_pred)

batch_size = 32
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

num_epochs = 40
print_every = 1

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(params=model.parameters(), lr = 0.001)
train_losses = []
test_accuracy = []
train_accuracy = []
model.train()
for epoch in tqdm(range(num_epochs)):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        predict = model(X_batch)
        loss = criterion(predict, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    train_losses.append(loss_for_epoch)
    train_accuracy_for_epoch = accuracy(train_loader, model, device)
    test_accuracy_for_epoch = accuracy(test_loader, model, device)
    train_accuracy.append(train_accuracy_for_epoch)
    test_accuracy.append(test_accuracy_for_epoch)
    if epoch % 1 == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch} | Train accuracy: {train_accuracy_for_epoch} | Test accuracy: {test_accuracy_for_epoch}")
        '''
        return pc.copy(s)


    def pretrained_model_import():
        s = '''import torchvision.models as models
model = models.vgg16(weights='IMAGENET1K_V1')
print(model, '\n')

layers_count = sum(1 for module in model.modules() if (isinstance(module, nn.Conv2d) or isinstance(module, nn.Linear)))
print(f'Кол-во слоев: {layers_count}\n')

params_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f'Количество настраиваемых параметров: {params_count}')
        '''
        return pc.copy(s)   

    def adam_model_train():
        s = '''batch_size = 32
epochs = 100
print_every = 20

criterion = nn.MSELoss()
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

adamw_model = nn.Sequential(
    nn.Linear(train_dataset.tensors[0].shape[1], 64),
    nn.ReLU(),
    nn.Linear(64, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 32),
    nn.ReLU(),
    nn.Linear(32, 1)
)

adamw_optimizer = optim.Adam(params=adamw_model.parameters(), lr = 0.001)
adamw_losses = []
for epoch in range(epochs):
    epoch_loss = 0
    model.train()
    for batch_X, batch_y in train_loader:
        adamw_optimizer.zero_grad()
        outputs = adamw_model(batch_X)
        loss = criterion(outputs, batch_y.reshape(-1, 1))
        loss.backward()
        adamw_optimizer.step()
        epoch_loss += loss.item()
    epoch_loss /= len(train_loader)
    adamw_losses.append(epoch_loss)

    if (epoch + 1) % print_every == 0:
        y_true, y_pred = collect(adamw_model, train_loader)
        y_true_test, y_pred_test = collect(adamw_model, test_loader)
        
        train_r2 = r2_score(y_true, y_pred)
        test_r2 = r2_score(y_true_test, y_pred_test)
        
        train_mae = mean_absolute_error(y_true, y_pred)
        test_mae = mean_absolute_error(y_true_test, y_pred_test)
        print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.8f}, Train R2: {train_r2}, Test R2: {test_r2}, Train MAE: {train_mae}, Test MAE: {test_mae}')
        '''
        return pc.copy(s)   

    def class_weights():
        s = '''from sklearn.utils.class_weight import compute_class_weight

classes = np.array([0, 1])  

# Compute class weights
class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=y)

for i, weight in enumerate(class_weights):
    print(f"Class {classes[i]}: {weight}")
        '''
        return pc.copy(s)  

    def full_cnn():
        s = '''model = nn.Sequential(
    # Первый сверточный блок
    nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    
    # Второй сверточный блок
    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    
    # Полносвязная часть
    nn.Flatten(start_dim=1),
    nn.Linear(115200, 256),  # Размер выхода после сверточных слоев
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 2),  # 10 классов
    nn.Softmax(dim=1)
)

batch_size = 32
epochs = 50
print_every = 1
losses = []
criterion = nn.CrossEntropyLoss()
# criterion = nn.CrossEntropyLoss(weight = torch.tensor(class_weights))

optimizer = optim.Adam(model.parameters(), lr=0.001)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

for epoch in range(epochs):
    epoch_loss = []
    model.train()
    for batch_X, batch_y in train_loader:
        
        optimizer.zero_grad()

        y_pred = model(batch_X)

        loss = criterion(y_pred, batch_y)
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss: {np.mean(epoch_loss):.4f}, ...')

        '''
        return pc.copy(s)  

    def full_regression():
        s = '''model = nn.Sequential(
    nn.Linear(X_train.shape[1], 1024),
    nn.ReLU(),

    nn.Linear(1024, 512),
    nn.ReLU(),

    nn.Linear(512, 64),
    nn.ReLU(),

    nn.Linear(64, 1)
)

batch_size = 64
epochs = 20
print_every = 1
losses = []
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

for epoch in range(epochs):
    epoch_loss = []
    model.train()
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        y_pred = model(batch_X)
        loss = criterion(batch_y, y_pred)
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss: {np.mean(epoch_loss):.4f}, ...')

        '''
        return pc.copy(s)  
    
    def full_classification():
        s = '''model = nn.Sequential(
    nn.Linear(X_train.shape[1], 1024),
    nn.ReLU(),

    nn.Linear(1024, 512),
    nn.ReLU(),

    nn.Linear(512, 256),
    nn.ReLU(),

    nn.Linear(256, 128),
    nn.ReLU(),

    nn.Linear(128, 32),
    nn.ReLU(),

    nn.Linear(32, 2),
    # nn.Softmax(dim=1)
)


batch_size = 32
epochs = 30
print_every = 1
losses = []
criterion = nn.CrossEntropyLoss()
# criterion = nn.CrossEntropyLoss(weight = torch.tensor(class_weights))
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

for epoch in range(epochs):
    epoch_loss = []
    model.train()
    for batch_X, batch_y in train_loader:
        
        optimizer.zero_grad()

        y_pred = model(batch_X)

        loss = criterion(y_pred, batch_y)
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss: {np.mean(epoch_loss):.4f}, ...')

        '''
        return pc.copy(s)  

    def optim_r_imports():
        s = '''
import pandas as pd
import numpy as np
import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
        '''
        return pc.copy(s)  

    def optim_r_1_gold():
        s = '''# первая ячейка первое задание gold 
data = pd.read_csv('gold.csv')

X = data.drop('Gold_T+22', axis=1) 
y = data['Gold_T+22']

numerical_cols = X.columns.tolist()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test.values, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
        '''
        return pc.copy(s)  

    def optim_r_1_bike():
        s = '''# первая ячейка первой задачи bike

data = pd.read_csv('bike_cnt.csv')

# Дата в числовой формат
data['dteday'] = pd.to_datetime(data['dteday'])
data['dteday'] = pd.to_numeric(data['dteday'])

data = data.drop(['instant'], axis=1)

X = data.drop('cnt', axis=1)
y = data['cnt']

categorical_cols = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
numerical_cols = ['dteday', 'temp', 'atemp', 'hum', 'windspeed']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)
# X_processed = X_processed.toarray()

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train.values, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test.values, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
        '''
        return pc.copy(s)  

    def optim_r_2_bikegold():
        s = '''# вторая ячейка первое задание bike gold 
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
        '''
        return pc.copy(s)  

    def optim_r_3_bikegold():
        s = '''# третья ячейка первое задание bike gold
def train_model(optimizer, model, criterion, train_loader, epochs=100, print_every=10):
    train_losses = []
    for epoch in range(epochs):
        epoch_loss = 0
        model.train()
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            output = model(batch_X)
            loss = criterion(output.flatten(), batch_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(train_loader)
        train_losses.append(avg_loss)
        
        if (epoch + 1) % print_every == 0:
            print(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}')
    
    return train_losses

# Функция для оценки модели на тестовом наборе по 3 метрикам
def evaluate_model(model, X_test, y_test):
    model.eval()
    with torch.no_grad():
        y_pred = model(X_test).flatten()
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, mae, r2

        '''
        return pc.copy(s)  

    def optim_r_4_bikegold():
        s = '''# четвертая ячейка первое задание bike gold

# Сравнение оптимизаторов
model = Model()
optimizers = {
    'SGD': optim.SGD(model.parameters(), lr=0.01),
    'Adam': optim.Adam(model.parameters(), lr=0.001),
    'AdamW': optim.AdamW(model.parameters(), lr=0.001)
}
for opt_name, optimizer in optimizers.items():
    print(f"Training with {opt_name}")
    model = Model()
    criterion = nn.MSELoss()
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    train_losses = train_model(optimizer, model, criterion, train_loader, epochs=100, print_every=10)
    
    # Оценка модели
    mse, mae, r2 = evaluate_model(model, X_test, y_test)
    
    # Построение графика потерь
    plt.plot(train_losses, label=opt_name)
    
    print(f'{opt_name} Test Results: MSE={mse:.4f}, MAE={mae:.4f}, R2={r2:.4f}')

plt.title('Loss Curves')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Оптимизаторы будут иметь различное влияние на обучение модели и итоговое качество. 
# В частности, Adam и AdamW часто показывают лучшие результаты по сравнению с SGD, так как они адаптируют скорость обучения на каждом шаге.

# SGD: Может показывать более высокую степень колебаний и медленное сходимость.
# Adam: Обычно является наиболее эффективным оптимизатором для задач с меньшими колебаниями и более быстрой сходимостью.
# AdamW: Похож на Adam, но с улучшенной обработкой веса регуляризации.
        '''
        return pc.copy(s)  

    def optim_c_1_bank():
        s = '''# первая ячейка задачи bank

data = pd.read_csv('bank.csv')

# # Дата в числовой формат
# data['dteday'] = pd.to_datetime(data['dteday'])
# data['dteday'] = pd.to_numeric(data['dteday'])

X = data.drop(['deposit'], axis=1)
y = data.deposit.values
y[y == 'no'] = 0
y[y == 'yes'] = 1
y = y.astype(int)

categorical_cols = ['job', 'marital',	'education',	'default', 'housing', 'loan',	'contact', 'month', 'poutcome']
numerical_cols = ['age', 'balance', 'day', 'duration',	'campaign',	'pdays',	'previous']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)
# X_processed = X_processed.toarray()

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
        '''
        return pc.copy(s)  

    def optim_c_2_bank():
        s = '''# вторая ячейка задание bank
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 2)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
model = Model()
        '''
        return pc.copy(s)  

    def optim_c_3_bank():
        s = '''# третья ячейка первое задание bank
def train_model(optimizer, model, criterion, train_loader, epochs=100, print_every=10):
    train_losses = []
    for epoch in range(epochs):
        epoch_loss = 0
        model.train()
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            output = model(batch_X)
            loss = criterion(output, batch_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(train_loader)
        train_losses.append(avg_loss)
        
        if (epoch + 1) % print_every == 0:
            print(f'Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}')
    
    return train_losses

#считаем метрику f1 для классификации
import torch.nn.functional as F
def evaluate_model(model, X_test, y_test):
    model.eval()
    with torch.no_grad():
        y_pred_logits = model(X_test)
        y_pred_probs = F.softmax(y_pred_logits, dim=1)
        y_pred_classes = torch.argmax(y_pred_probs, dim=1)

    y_pred_classes = y_pred_classes.cpu().numpy()
    y_test = y_test.cpu().numpy()

    f1 = f1_score(y_test, y_pred_classes, average='weighted')
    return f1
        '''
        return pc.copy(s)  

    def optim_c_4_bank():
        s = '''# четвертая ячейка первое задание bank

# Сравнение оптимизаторов
optimizers = {
    'SGD': optim.SGD(model.parameters(), lr=0.01),
    'Adam': optim.Adam(model.parameters(), lr=0.001),
    'AdamW': optim.AdamW(model.parameters(), lr=0.001)
}
for opt_name, optimizer in optimizers.items():
    print(f"Training with {opt_name}")
    model = Model()
    criterion = nn.CrossEntropyLoss()
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    train_losses = train_model(optimizer, model, criterion, train_loader, epochs=100, print_every=10)
    
    # Оценка модели
    f1 = evaluate_model(model, X_test, y_test)
    
    # Построение графика потерь
    plt.plot(train_losses, label=opt_name)
    print(f1)
    # print(f'{opt_name} Test Results: MSE={mse:.4f}, MAE={mae:.4f}, R2={r2:.4f}')

plt.title('Loss Curves')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Оптимизаторы будут иметь различное влияние на обучение модели и итоговое качество. 
# В частности, Adam и AdamW часто показывают лучшие результаты по сравнению с SGD, так как они адаптируют скорость обучения на каждом шаге.

# SGD: Может показывать более высокую степень колебаний и медленное сходимость.
# Adam: Обычно является наиболее эффективным оптимизатором для задач с меньшими колебаниями и более быстрой сходимостью.
# AdamW: Похож на Adam, но с улучшенной обработкой веса регуляризации.
        '''
        return pc.copy(s)  

    def model_r_imports():
        s = '''import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt
        '''
        return pc.copy(s)  

    def model_r_1_bikegold():
        s = '''# первая ячейка 2 задания bike, gold
data = pd.read_csv("bike_cnt.csv") #если bike_cnt, то y=cnt


X = data.drop("cnt", axis=1)
y = data["cnt"] #если bike_cnt, то y=cnt

numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = X.select_dtypes(include=["object"]).columns

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline([("imputer", SimpleImputer(strategy="mean")), ("scaler", StandardScaler())]), numerical_cols),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), 
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical_cols),
    ]
)

X_preprocessed = preprocessor.fit_transform(X)
y = y.values

X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.3, random_state=42)

X_train_dense = X_train.toarray()
X_test_dense = X_test.toarray()
y_train_dense = X_train.toarray()  
y_test_dense = X_test.toarray()
X_train_tensor = torch.tensor(X_train_dense, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_dense, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train_dense, dtype=torch.float32).unsqueeze(1)
y_test_tensor = torch.tensor(y_test_dense, dtype=torch.float32).unsqueeze(1)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)
        '''
        return pc.copy(s)  

    def model_r_2_bikegold():
        s = '''# вторая ячейка 2 задания bike, gold
class SimpleNN(nn.Module):
    def __init__(self, input_dim):
        super(SimpleNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1)  # Выходной слой для регрессии
        )
    
    def forward(self, x):
        return self.fc(x)

class DeepNN(nn.Module):
    def __init__(self, input_dim):
        super(DeepNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),  # Dropout для регуляризации
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1)
        )
    
    def forward(self, x):
        return self.fc(x)
        '''
        return pc.copy(s)  

    def model_r_3_bikegold():
        s = '''# третья ячейка 2 задания gold, bike
def train_model(model, criterion, optimizer, train_loader, test_loader, print_every=10, epochs=100):
    train_losses = []
    test_losses = []
    for epoch in range(epochs):
            model.train()
            epoch_loss = 0
            for batch_X, batch_y in train_loader:
                optimizer.zero_grad()
                outputs = model(batch_X)
                loss = criterion(outputs, batch_y)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            train_losses.append(epoch_loss / len(train_loader))
            
            model.eval()
            test_loss = 0
            with torch.no_grad():
                for batch_X, batch_y in test_loader:
                    outputs = model(batch_X)
                    loss = criterion(outputs, batch_y)
                    test_loss += loss.item()
            test_losses.append(test_loss / len(test_loader))
            if (epoch+1) % print_every == 0:
                print(f"Epoch {epoch+1}/{epochs}, Train Loss: {train_losses[-1]:.4f}, Test Loss: {test_losses[-1]:.4f}")
        
    return train_losses, test_losses


input_dim = X_train.shape[1]

models = {
    "SimpleNN": SimpleNN(input_dim),
    "DeepNN": DeepNN(input_dim),
}

criterion = nn.MSELoss()
results = {}

for name, model in models.items():
    print(f"Training {name}")
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    train_losses, test_losses = train_model(model, criterion, optimizer, train_loader, test_loader, epochs=100)
    results[name] = (train_losses, test_losses)
        '''
        return pc.copy(s)  

    def model_r_4_bikegoldbank():
        s = '''# четвёртая ячейка 2 задания gold, bike, bank
def plot_losses_separately(results):
    # График всех train losses
    plt.figure(figsize=(10, 6))
    for name, (train_losses, _) in results.items():
        plt.plot(train_losses, label=f"{name} Train Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training Loss for All Models")
    plt.legend()
    plt.grid(True)
    plt.show()

    # График всех test losses
    plt.figure(figsize=(10, 6))
    for name, (_, test_losses) in results.items():
        plt.plot(test_losses, label=f"{name} Test Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Test Loss for All Models")
    plt.legend()
    plt.grid(True)
    plt.show()

# Построение графиков
plot_losses_separately(results)
        '''
        return pc.copy(s)  

    def model_c_1_bank():
        s = '''# первая ячейка 2 задания bank
data = pd.read_csv("bank.csv") 


X = data.drop(["deposit"], axis=1)
y = data.deposit.values
y[y == 'no'] = 0
y[y == 'yes'] = 1
y = y.astype(int)

numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = X.select_dtypes(include=["object"]).columns

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline([("imputer", SimpleImputer(strategy="mean")), ("scaler", StandardScaler())]), numerical_cols),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), 
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical_cols),
    ]
)

X_preprocessed = preprocessor.fit_transform(X)
y = y

X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.3, random_state=42)

# X_train_dense = X_train.toarray()
# X_test_dense = X_test.toarray()
# y_train_dense = X_train.toarray()  
# y_test_dense = X_test.toarray()
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long).unsqueeze(1)
y_test_tensor = torch.tensor(y_test, dtype=torch.long).unsqueeze(1)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)
        '''
        return pc.copy(s)  

    def model_c_2_bank():
        s = '''# вторая ячейка 2 задания bank
class SimpleNN(nn.Module):
    def __init__(self, input_dim):
        super(SimpleNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 2)  # Выходной слой для регрессии
        )
    
    def forward(self, x):
        return self.fc(x)

class DeepNN(nn.Module):
    def __init__(self, input_dim):
        super(DeepNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),  # Dropout для регуляризации
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 2)
        )
    
    def forward(self, x):
        return self.fc(x)
        '''
        return pc.copy(s)  

    def model_c_3_bank():
        s = '''# третья ячейка 2 задачи bank
def train_model(model, criterion, optimizer, train_loader, test_loader, num_epochs=100, print_every=10):
    train_accuracies = []
    test_accuracies = []

    for epoch in range(num_epochs):
        model.train()
        correct_train = 0
        total_train = 0

        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()

            if len(batch_y.shape) > 1:
                batch_y = batch_y.squeeze()

            outputs = model(batch_X)  # Размер [batch_size, num_classes]
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            _, predicted = torch.max(outputs, 1)
            correct_train += (predicted == batch_y).sum().item()
            total_train += batch_y.size(0)

        # Точность на обучающем наборе
        train_accuracy = correct_train / total_train
        train_accuracies.append(train_accuracy)

        model.eval()
        correct_test = 0
        total_test = 0
        with torch.no_grad():
            for batch_X, batch_y in test_loader:
                if len(batch_y.shape) > 1:
                    batch_y = batch_y.squeeze()

                outputs = model(batch_X)
                _, predicted = torch.max(outputs, 1)
                correct_test += (predicted == batch_y).sum().item()
                total_test += batch_y.size(0)

        # Точность на тестовом наборе
        test_accuracy = correct_test / total_test
        test_accuracies.append(test_accuracy)

        if (epoch + 1) % print_every == 0:
            print(f"Epoch {epoch + 1}/{num_epochs}, Train Acc: {train_accuracy:.4f}, Test Acc: {test_accuracy:.4f}")

    return train_accuracies, test_accuracies


# Инициализация моделей, критерия и оптимизатора
input_dim = X_train.shape[1]

models = {
    "SimpleNN": SimpleNN(input_dim),
    "DeepNN": DeepNN(input_dim),
}

criterion = nn.CrossEntropyLoss()  # Для классификации
results = {}

for name, model in models.items():
    print(f"Training {name}")
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    train_accuracies, test_accuracies = train_model(
        model,
        criterion,
        optimizer,
        train_loader,
        test_loader,
        num_epochs=100,
        print_every=10
    )
    results[name] = (train_accuracies, test_accuracies)
        '''
        return pc.copy(s)  

    def n_eng_handwritten_preprocessing():
        s = '''import os
import zipfile
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# Путь к архиву
zip_path = "eng_handwritten.zip"
extract_dir = "eng_handwritten"  # Директория для извлечения данных

# Распаковка архива
if not os.path.exists(extract_dir):  # Проверяем, распакован ли архив
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)  # Извлечение содержимого в папку
        print(f"Архив распакован в папку: {extract_dir}")

# data_dir = os.path.join(extract_dir, "eng_handwritten")
data_dir = extract_dir

# Предобработка изображений
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Преобразование в градации серого
    transforms.Resize((128, 128)),                 # Изменение размера изображений
    transforms.ToTensor(),                       # Преобразование в тензор
    transforms.Normalize((0.5,), (0.5,))         # Нормализация данных
])

# Загрузка полного датасета
full_dataset = ImageFolder(data_dir, transform=transform)

# Разделение на тренировочную и тестовую выборки
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

# Создание загрузчиков данных
batch_size = 32

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Проверка корректности данных
class_names = full_dataset.classes  # Названия классов (A-Z)
print(f"Классы: {class_names}")
print(f"Размер тренировочного набора: {len(train_dataset)}")
print(f"Размер тестового набора: {len(test_dataset)}")
        '''
        return pc.copy(s)  

    def n_eng_handwritten_diff_deep():
        s = '''import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from sklearn.metrics import f1_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# 1. Определение класса CNN с переменным количеством блоков
class VariableCNN(nn.Module):
    def __init__(self, num_blocks, num_classes):
        super(VariableCNN, self).__init__()
        self.layers = nn.ModuleList()
        in_channels = 1

        # Создание свёрточных блоков
        for _ in range(num_blocks):
            self.layers.append(nn.Conv2d(in_channels=in_channels, out_channels=16, kernel_size=3, stride=1, padding=1))
            self.layers.append(nn.ReLU())
            self.layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
            in_channels = 16  # Устанавливаем out_channels для следующего блока

        # Полносвязные слои
        self.fc1 = nn.Linear(16 * (28 // (2 ** num_blocks)) ** 2, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        x = x.view(x.size(0), -1)  # Выпрямление
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x


# 2. Функция обучения и оценки модели
def train_and_evaluate(num_blocks, train_loader, val_loader, num_classes, device):
    model = VariableCNN(num_blocks, num_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 50  # Уменьшенное количество эпох для ускорения экспериментов
    for epoch in range(num_epochs):
        model.train()
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

    # Оценка модели на валидационном множестве
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for batch_X, batch_y in val_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            outputs = model(batch_X)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(batch_y.cpu().numpy())

    # Вычисление метрики micro F1
    micro_f1 = f1_score(all_labels, all_preds, average='micro')
    return micro_f1, model


# 3. Подготовка данных (разделение на обучающую и валидационную выборки)
batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(test_dataset, batch_size=batch_size)

# Устройство
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Проведение экспериментов
blocks_range = range(1, 5)  # Число свёрточных блоков от 1 до 4
f1_scores = []
models = {}

for num_blocks in blocks_range:
    print(f"Обучение модели с {num_blocks} свёрточным(и) блоком(ами)...")
    micro_f1, model = train_and_evaluate(num_blocks, train_loader, val_loader, num_classes, device)
    f1_scores.append(micro_f1)
    models[num_blocks] = model
    print(f"Micro F1 для {num_blocks} блоков: {micro_f1:.4f}")

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(blocks_range, f1_scores, marker='o', linestyle='-', color='b')
plt.title("Зависимость micro F1 от числа свёрточных блоков", fontsize=14)
plt.xlabel("Число свёрточных блоков", fontsize=12)
plt.ylabel("Micro F1", fontsize=12)
plt.grid(True)
plt.show()

# Выбор лучшей модели
best_num_blocks = blocks_range[np.argmax(f1_scores)]
best_model = models[best_num_blocks]
print(f"Лучшая архитектура имеет {best_num_blocks} свёрточных блока(ов) с Micro F1 = {max(f1_scores):.4f}")

# 4. Оценка производительности на тестовом множестве
best_model.eval()
all_preds = []
all_labels = []
with torch.no_grad():
    for batch_X, batch_y in val_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        outputs = best_model(batch_X)
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(batch_y.cpu().numpy())

# Оценка F1 и вывод отчета
test_micro_f1 = f1_score(all_labels, all_preds, average='micro')
print(f"Micro F1 на тестовом множестве: {test_micro_f1:.4f}")

# Анализ ошибок
class_report = classification_report(all_labels, all_preds, target_names=full_dataset.classes)
print("Отчёт о классификации:")
print(class_report)
        '''
        return pc.copy(s)  

    def n_chars_preprocessing():
        s = '''import os
import zipfile
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# Путь к архиву
zip_path = "chars.zip"
extract_dir = "chars"  # Директория для извлечения данных

# Распаковка архива
if not os.path.exists(extract_dir):  # Проверяем, распакован ли архив
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)  # Извлечение содержимого в папку
        print(f"Архив распакован в папку: {extract_dir}")

data_dir = os.path.join(extract_dir, "chars")
# data_dir = extract_dir

# Предобработка изображений
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Преобразование в градации серого
    transforms.Resize((128, 128)),                 # Изменение размера изображений
    transforms.ToTensor(),                       # Преобразование в тензор
    transforms.Normalize((0.5,), (0.5,))         # Нормализация данных
])

# Загрузка полного датасета
full_dataset = ImageFolder(data_dir, transform=transform)

# Разделение на тренировочную и тестовую выборки
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

# Создание загрузчиков данных
batch_size = 32

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Проверка корректности данных
class_names = full_dataset.classes  # Названия классов (A-Z)
print(f"Классы: {class_names}")
print(f"Размер тренировочного набора: {len(train_dataset)}")
print(f"Размер тестового набора: {len(test_dataset)}")
        '''
        return pc.copy(s)  

    def n_clothes_multi_preprocessing():
        s = '''import os
import zipfile
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# Путь к архиву
zip_path = "clothes_multi.zip"
extract_dir = "clothes_multi"  # Директория для извлечения данных

# Распаковка архива
if not os.path.exists(extract_dir):  # Проверяем, распакован ли архив
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)  # Извлечение содержимого в папку
        print(f"Архив распакован в папку: {extract_dir}")

data_dir = os.path.join(extract_dir, "clothes_multi")
# data_dir = extract_dir

# Предобработка изображений
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Преобразование в градации серого
    transforms.Resize((128, 128)),                 # Изменение размера изображений
    transforms.ToTensor(),                       # Преобразование в тензор
    transforms.Normalize((0.5,), (0.5,))         # Нормализация данных
])

# Загрузка полного датасета
full_dataset = ImageFolder(data_dir, transform=transform)

# Разделение на тренировочную и тестовую выборки
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

# Создание загрузчиков данных
batch_size = 32

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Проверка корректности данных
class_names = full_dataset.classes  # Названия классов (A-Z)
print(f"Классы: {class_names}")
print(f"Размер тренировочного набора: {len(train_dataset)}")
print(f"Размер тестового набора: {len(test_dataset)}")
        '''
        return pc.copy(s)  

    def n_sign_language_preprocessing():
        s = '''import os
import zipfile
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# Путь к архиву
zip_path = "sign_language.zip"
extract_dir = "sign_language"  # Директория для извлечения данных

# Распаковка архива
if not os.path.exists(extract_dir):  # Проверяем, распакован ли архив
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)  # Извлечение содержимого в папку
        print(f"Архив распакован в папку: {extract_dir}")

data_dir = os.path.join(extract_dir, "sign_language")
# data_dir = extract_dir

# Предобработка изображений
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # Преобразование в градации серого
    transforms.Resize((128, 128)),                 # Изменение размера изображений
    transforms.ToTensor(),                       # Преобразование в тензор
    transforms.Normalize((0.5,), (0.5,))         # Нормализация данных
])

# Загрузка полного датасета
full_dataset = ImageFolder(data_dir, transform=transform)

# Разделение на тренировочную и тестовую выборки
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

# Создание загрузчиков данных
batch_size = 32

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Проверка корректности данных
class_names = full_dataset.classes  # Названия классов (A-Z)
print(f"Классы: {class_names}")
print(f"Размер тренировочного набора: {len(train_dataset)}")
print(f"Размер тестового набора: {len(test_dataset)}")
        '''
        return pc.copy(s)  

    def n_cnn():
        s = '''import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        # Свёрточные слои
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1) 
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1) 

        self.fc1 = nn.Linear(128 * 32 * 32, 256)
        self.fc2 = nn.Linear(256, num_classes)

        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))

        x = x.view(x.size(0), -1)

        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
        '''
        return pc.copy(s)  

    def n_training():
        s = '''batch_size = 64
num_epochs = 10
print_every = 10
num_classes = len(full_dataset.classes)

# Инициализация модели
model = CNN(num_classes)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Функция потерь и оптимизатор
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Загрузчики данных
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

# Цикл обучения
for epoch in range(num_epochs):
    model.train()  # Устанавливаем режим обучения
    epoch_loss = 0
    correct = 0
    total = 0

    for batch_X, batch_y in train_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)

        # Обнуление градиентов
        optimizer.zero_grad()

        # Прямой проход
        outputs = model(batch_X)

        # Вычисление функции потерь
        loss = criterion(outputs, batch_y)

        # Обратный проход и обновление весов
        loss.backward()
        optimizer.step()

        # Обновление метрик
        epoch_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += batch_y.size(0)
        correct += (predicted == batch_y).sum().item()

    # Печать статистики каждые `print_every` эпох
    if (epoch + 1) % print_every == 0:
        train_accuracy = 100 * correct / total
        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss:.4f}, Accuracy: {train_accuracy:.2f}%")

# Оценка на тестовом наборе
model.eval()  # Устанавливаем режим оценки
test_loss = 0
correct = 0
total = 0

with torch.no_grad():
    for batch_X, batch_y in test_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)

        # Прямой проход
        outputs = model(batch_X)

        # Вычисление потерь
        loss = criterion(outputs, batch_y)
        test_loss += loss.item()

        # Вычисление точности
        _, predicted = torch.max(outputs, 1)
        total += batch_y.size(0)
        correct += (predicted == batch_y).sum().item()

test_accuracy = 100 * correct / total
print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.2f}%")
        '''
        return pc.copy(s)  

    def n_demo():
        s = '''import random
import matplotlib.pyplot as plt

# Функция для отображения изображений с предсказанными и реальными метками
def show_predictions(model, loader, dataset_classes, device, num_images=10):
    model.eval()
    images_shown = 0
    fig, axes = plt.subplots(1, num_images, figsize=(20, 5))

    with torch.no_grad():
        for batch_X, batch_y in loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            outputs = model(batch_X)
            _, predicted = torch.max(outputs, 1)

            for i in range(batch_X.size(0)):
                if images_shown >= num_images:
                    break
                
                # Подготовка изображения и меток
                image = batch_X[i].cpu().squeeze(0).numpy()
                true_label = dataset_classes[batch_y[i].item()]
                pred_label = dataset_classes[predicted[i].item()]

                # Отображение изображения
                ax = axes[images_shown]
                ax.imshow(image, cmap='gray')
                ax.axis('off')
                ax.set_title(f'True: {true_label}\nPred: {pred_label}', fontsize=10)
                
                images_shown += 1
            
            if images_shown >= num_images:
                break

    plt.tight_layout()
    plt.show()

# Вызов функции для лучшей модели
show_predictions(model, test_loader, full_dataset.classes, device, num_images=10)
        '''
        return pc.copy(s)  

    def n_confusion_matrix():
        s = '''import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def analyze_problematic_classes(model, loader, dataset_classes, device):
    model.eval()
    all_preds = []
    all_labels = []

    # Собираем предсказания и истинные метки
    with torch.no_grad():
        for batch_X, batch_y in loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            outputs = model(batch_X)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(batch_y.cpu().numpy())

    # Построение матрицы ошибок
    cm = confusion_matrix(all_labels, all_preds)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]  # Нормализуем

    # Визуализация
    plt.figure(figsize=(15, 15))
    sns.heatmap(cm_normalized, annot=True, fmt=".2f", cmap="Blues", xticklabels=dataset_classes, yticklabels=dataset_classes)
    plt.xlabel("Предсказанный класс")
    plt.ylabel("Истинный класс")
    plt.title("Матрица ошибок (Confusion Matrix)")
    plt.show()
    report = classification_report(all_labels, all_preds, target_names=dataset_classes, zero_division=0)
    # print(report)

# Вызов функции для тестовой выборки
analyze_problematic_classes(model, test_loader, full_dataset.classes, device)
        '''
        return pc.copy(s)
    
    def check_balance_imgs():
        s = '''d = dict()
inv_map = {v: k for k, v in full_dataset.class_to_idx.items()}
for key in full_dataset.class_to_idx:
    d[key] = 0
for image in full_dataset.imgs:
    d[inv_map[image[1]]] += 1
        '''

    def print_one_img():
        s = '''random_idx = random.randint(0, len(full_dataset) - 1)
image, label = full_dataset[random_idx]
image = image.permute(1, 2, 0)
plt.imshow(image)
plt.title(f"Class: {label}")
plt.axis('off')
plt.show()
        '''
        return pc.copy(s)
    
    def color_and_cloth():
        s = '''colors = sorted(set(folder.split('_')[0] for folder in os.listdir(data_dir)))
clothes = sorted(set(folder.split('_')[1] for folder in os.listdir(data_dir)))
color_to_idx = {color: i for i, color in enumerate(colors)}
clothes_to_idx = {cloth: i for i, cloth in enumerate(clothes)}
        '''

    def multihead_model():
        s = '''class MultiHeadCNN(nn.Module):
    def __init__(self, num_colors, num_clothes):
        super(MultiHeadCNN, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Flatten()
        )
        self.fc_shared = nn.Linear(64 * 16 * 16, 128)
        self.fc_color = nn.Linear(128, num_colors)
        self.fc_clothes = nn.Linear(128, num_clothes)

    def forward(self, x):
        x = self.conv(x)
        x = self.fc_shared(x)
        color_out = self.fc_color(x)
        clothes_out = self.fc_clothes(x)
        return color_out, clothes_out
        '''
        return pc.copy(s)
    
    def multi_head_train():
        s='''for epoch in range(epochs):
    model.train()
    total_loss = 0
    for images, labels in train_loader:
        images = images.to(device)

        # Преобразуем индексы в имена классов
        class_names = [full_dataset.classes[label] for label in labels.tolist()]
        
        # Извлекаем цвет и тип одежды, а затем преобразуем в индексы
        color_labels = torch.tensor([color_to_idx[name.split('_')[0]] for name in class_names], dtype=torch.long, device=device)
        clothes_labels = torch.tensor([clothes_to_idx[name.split('_')[1]] for name in class_names], dtype=torch.long, device=device)

        optimizer.zero_grad()
        color_pred, clothes_pred = model(images)

        loss_color = criterion(color_pred, color_labels)
        loss_clothes = criterion(clothes_pred, clothes_labels)
        loss = loss_color + loss_clothes
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader):.4f}")

print("Обучение завершено!")
        '''
        return pc.copy(s)
    def print_multi_predict():
        s = '''model.eval()  # Переключаем модель в режим оценки

with torch.no_grad():
    images, labels = next(iter(test_loader))  # Берём один батч изображений
    images = images[:4].to(device)  # Оставляем только 4 изображения

    # Получаем истинные метки
    class_names = [full_dataset.classes[label] for label in labels[:4].tolist()]
    true_colors = [name.split('_')[0] for name in class_names]
    true_clothes = [name.split('_')[1] for name in class_names]

    # Делаем предсказание
    color_pred, clothes_pred = model(images)
    pred_colors_idx = torch.argmax(color_pred, dim=1).cpu().tolist()
    pred_clothes_idx = torch.argmax(clothes_pred, dim=1).cpu().tolist()

    # Преобразуем индексы в названия классов
    pred_colors = [colors[i] for i in pred_colors_idx]
    pred_clothes = [clothes[i] for i in pred_clothes_idx]

    # Отображаем изображения с предсказаниями
    fig, axes = plt.subplots(2, 2, figsize=(6, 6))  # 2 строки × 2 столбца
    axes = axes.flatten()

    for i in range(4):
        img = images[i].cpu().permute(1, 2, 0) * 0.5 + 0.5  # Денормализация
        axes[i].imshow(img)
        axes[i].axis("off")
        axes[i].set_title(f"True: {true_colors[i]} {true_clothes[i]}\nPred: {pred_colors[i]} {pred_clothes[i]}", fontsize=10)

    plt.tight_layout()
    plt.show()
    '''
        return pc.copy(s)
    def pca_decomposition():
        s = '''from sklearn.decomposition import PCA

feature_extractor = nn.Sequential(*list(model.children())[:-1]).to(device)
feature_extractor.eval()
features = []
labels = []
with torch.no_grad():
    for batch_X, batch_y in DataLoader(full_dataset, batch_size=batch_size, shuffle=False):
        batch_X = batch_X.to(device)
        output = feature_extractor(batch_X)
        features.append(output.cpu().numpy())
        labels.append(batch_y.numpy())
features = np.concatenate(features, axis=0)
labels = np.concatenate(labels, axis=0)
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(features)
plt.figure(figsize=(10, 8))
scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=labels, cmap='tab10', alpha=0.7)
plt.legend(handles=scatter.legend_elements()[0], labels=full_dataset.classes, bbox_to_anchor=(1.05, 1), loc='upper right')
plt.xlabel('PCA Компонента 1')
plt.ylabel('PCA Компонента 2')
plt.title('PCA')
plt.tight_layout()
plt.show()
        '''
        return pc.copy(s)
    
    def bank_drop():
        s = '''data = pd.read_csv('bank.csv')#data, предобработка(data.info())

X = data.drop(['deposit'], axis=1)
y = data['deposit'].map({'no':0,'yes':1}) #y

categorical_cols = ['job', 'marital','education','default', 'housing', 'loan','contact', 'month', 'poutcome']
numerical_cols = ['age', 'balance', 'day', 'duration','campaign',	'pdays','previous']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_processed, y.values, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)


model = nn.Sequential(
    nn.Linear(X_train.shape[1], 512),
    nn.ReLU(),

    nn.Linear(512, 1024),
    nn.ReLU(),

    nn.Linear(1024, 256),
    nn.ReLU(),

    nn.Linear(256, 128),
    nn.ReLU(),

    nn.Linear(128, 32),
    nn.ReLU(),

    nn.Linear(32, 2),)

from sklearn.utils.class_weight import compute_class_weight
import numpy as np

classes = np.array([0, 1])  

# Compute class weights
class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=y)

for i, weight in enumerate(class_weights):
    print(f"Class {classes[i]}: {weight}")


batch_size = 32
epochs = 30
print_every = 1
losses = []

criterion = nn.CrossEntropyLoss(weight = torch.tensor(class_weights, dtype=torch.float32))
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

from tqdm import tqdm
for epoch in tqdm(range(epochs)):
    epoch_loss = []
    model.train()
    for batch_X, batch_y in train_loader:
        
        optimizer.zero_grad()

        y_pred = model(batch_X)

        loss = criterion(y_pred, batch_y.long())
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Train_Loss: {np.mean(epoch_loss):.4f}')

plt.plot(losses)
plt.title('Train Loss')

#Выводим confusion_matrix и classification_report на тестовой выборке
y_pred = []
y_true = []
device = torch.device('cpu')

model.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
y_pred = torch.tensor(y_pred)
y_true = torch.tensor(y_true)
sns.heatmap(confusion_matrix(y_true, y_pred), annot = True, fmt = f'.2f')
print(classification_report(y_true, y_pred))

# Добавляем в модель Dropout слои

model2 = nn.Sequential(
    nn.Linear(X_train.shape[1], 512),
    nn.ReLU(),
    nn.Dropout(0.3),
    
    nn.Linear(512, 1024),
    nn.ReLU(),
    nn.Dropout(0.3),

    nn.Linear(1024, 256),
    nn.ReLU(),

    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.3),

    nn.Linear(128, 32),
    nn.ReLU(),

    nn.Linear(32, 2),)


batch_size = 32
epochs = 30
print_every = 1
losses2 = []

criterion = nn.CrossEntropyLoss(weight = torch.tensor(class_weights, dtype=torch.float32))
optimizer = optim.Adam(model2.parameters(), lr=0.001)


for epoch in tqdm(range(epochs)):
    epoch_loss = []
    model2.train()
    for batch_X, batch_y in train_loader:
        
        optimizer.zero_grad()

        y_pred = model2(batch_X)

        loss = criterion(y_pred, batch_y.long())
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses2.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Train_Loss: {np.mean(epoch_loss):.4f}')

plt.plot(losses, label='Модель без Dropout')
plt.plot(losses2, label='Модель с Dropout')
plt.title('Train_Loss модели с Dropout и без Dropout')
plt.legend()

#По графику значений функции потерь видно, что из-за Dropout слоев модель при тех же параметрах обучаестя медленнее

#При дальнешейм обучении скорее всего мы увидим, что модель с Dropout дойдет до значений без них и при этом вероятнее будет лучше описывать данные, так как Dropout борется с переобучением

y_pred = []
y_true = []
device = torch.device('cpu')

model2.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model2(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
y_pred = torch.tensor(y_pred)
y_true = torch.tensor(y_true)
sns.heatmap(confusion_matrix(y_true, y_pred), annot = True, fmt = f'.2f')
print(classification_report(y_true, y_pred))
    '''
        return pc.copy(s)
    
    def bank_optimi():
        s = '''import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных
data = pd.read_csv('C:/Users/Professional/Desktop/bank.csv')
X = data.drop(['deposit'], axis=1)
y = data['deposit'].map({'no':0, 'yes':1})

# Предобработка данных
categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
numerical_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X_processed, y.values, test_size=0.2, random_state=42)

# Конвертация в тензоры
X_train = torch.tensor(X_processed.toarray() if hasattr(X_processed, 'toarray') else X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test.toarray() if hasattr(X_test, 'toarray') else X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

# Dataset и DataLoader
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

# Расчет весов классов
count_0 = np.sum(y == 0)
count_1 = np.sum(y == 1)
pos_weight = torch.tensor([count_0 / count_1], dtype=torch.float32)

# Гиперпараметры
batch_size = 64
epochs = 50
lr = 0.001

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

# Архитектура модели
class BankClassifier(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
        )
        
    def forward(self, x):
        return self.net(x)

# Инициализация моделей и оптимизаторов
input_size = X_train.shape[1]
models = {
    'Adam': BankClassifier(input_size),
    'SGD': BankClassifier(input_size),
    'RMSprop': BankClassifier(input_size),
    'AdamW': BankClassifier(input_size)
}

optimizers = {
    'Adam': optim.Adam(models['Adam'].parameters(), lr=lr),
    'SGD': optim.SGD(models['SGD'].parameters(), lr=lr, momentum=0.9),
    'RMSprop': optim.RMSprop(models['RMSprop'].parameters(), lr=lr),
    'AdamW': optim.AdamW(models['AdamW'].parameters(), lr=lr)
}

criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

# Обучение моделей
loss_history = {key: [] for key in models}

for name in models:
    model = models[name]
    optimizer = optimizers[name]
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            labels = labels.unsqueeze(1)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        epoch_loss = running_loss / len(train_loader)
        loss_history[name].append(epoch_loss)
        if (epoch + 1) % 10 == 0:
            print(f'{name} | Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}')

# Визуализация кривых обучения
plt.figure(figsize=(12, 6))
for name, losses in loss_history.items():
    plt.plot(losses, label=name)
plt.title('Сравнение оптимизаторов')
plt.xlabel('Эпохи')
plt.ylabel('Потери')
plt.legend()
plt.show()

# Функция для оценки модели
def evaluate_model(model):
    model.eval()
    y_true, y_pred = [], []
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            predicted = (torch.sigmoid(outputs) > 0.5).squeeze().int()
            y_true.extend(labels.int().tolist())
            y_pred.extend(predicted.tolist())
    
    print('Confusion Matrix:')
    print(confusion_matrix(y_true, y_pred))
    print('\nClassification Report:')
    print(classification_report(y_true, y_pred))

# Оценка всех моделей
for name, model in models.items():
    print(f'\n{name} Evaluation:')
    evaluate_model(model)
#Сравнение оптимизаторов по Loss:
#Adam и AdamW: Показывают стабильное снижение потерь, достигая минимальных значений (Adam: 0.1927, AdamW: 0.2278). Это связано с адаптивным learning rate, который позволяет избегать локальных минимумов.

#RMSprop: Демонстрирует самую низкую конечную потерь (0.1823), что может указывать на эффективность адаптивного момента для данной задачи.

#SGD: Имеет самые высокие потери (0.4636), что объясняется фиксированным learning rate и отсутствием адаптации к градиентам.
    '''
        return pc.copy(s)
    
    def bank_dis():
        s = '''import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных
data = pd.read_csv('C:/Users/Professional/Desktop/bank.csv')
X = data.drop(['deposit'], axis=1)
y = data['deposit'].map({'no':0, 'yes':1})

# Предобработка данных
categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
numerical_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(sparse=False), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X_processed, y.values, test_size=0.2, random_state=42)

# Конвертация в тензоры
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

# Dataset и DataLoader
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

# Расчет весов классов
count_0 = (y_train == 0).sum().item()
count_1 = (y_train == 1).sum().item()
pos_weight = torch.tensor([count_0 / count_1], dtype=torch.float32)

# Гиперпараметры
batch_size = 64
epochs = 50
lr = 0.001

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

# Архитектура модели
class BankClassifier(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
        
    def forward(self, x):
        return self.net(x)

# Инициализация модели
input_size = X_train.shape[1]
model = BankClassifier(input_size)
optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

# Обучение
train_losses = []
model.train()
for epoch in range(epochs):
    running_loss = 0.0
    for inputs, labels in train_loader:
        labels = labels.unsqueeze(1)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    epoch_loss = running_loss / len(train_loader)
    train_losses.append(epoch_loss)
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}')

# График потерь
plt.plot(train_losses)
plt.title('Training Loss Curve')
plt.xlabel('Epochs')
plt.ylabel('BCE Loss')
plt.show()

# Оценка модели
model.eval()
y_true, y_pred = [], []
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        predicted = (torch.sigmoid(outputs) > 0.5).int().squeeze()
        y_true.extend(labels.int().tolist())
        y_pred.extend(predicted.tolist())

print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\nClassification Report:")
print(classification_report(y_true, y_pred))

# Сравнение с моделью без учета дисбаланса
model_unbalanced = BankClassifier(input_size)
optimizer_unbalanced = optim.Adam(model_unbalanced.parameters(), lr=lr)
criterion_unbalanced = nn.BCEWithLogitsLoss()

# Обучение без весов
train_losses_unbalanced = []
model_unbalanced.train()
for epoch in range(epochs):
    running_loss = 0.0
    for inputs, labels in train_loader:
        labels = labels.unsqueeze(1)
        optimizer_unbalanced.zero_grad()
        outputs = model_unbalanced(inputs)
        loss = criterion_unbalanced(outputs, labels)
        loss.backward()
        optimizer_unbalanced.step()
        running_loss += loss.item()
    
    epoch_loss = running_loss / len(train_loader)
    train_losses_unbalanced.append(epoch_loss)
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}')

# Оценка без весов
model_unbalanced.eval()
y_pred_unbalanced = []
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model_unbalanced(inputs)
        predicted = (torch.sigmoid(outputs) > 0.5).int().squeeze()
        y_pred_unbalanced.extend(predicted.tolist())

print("\nWithout Class Weighting:")
print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred_unbalanced))
print("\nClassification Report:")
print(classification_report(y_true, y_pred_unbalanced))
    '''
        return pc.copy(s)
    
    def gold_optimz():
        s = '''data = pd.read_csv('datasets/regression/gold.csv')
data.head()
X = data.drop(['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22'], axis = 1)
y = data[['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']]
for col in data:
    print(data[col].dtype)
for col in data:
    print(data[col].isna().sum()) #Все признаки числовые, пропущенных значений нет Нормализую X

scaler = StandardScaler()
X_processed = scaler.fit_transform(X)
X_processed.shape

X_train, X_test, y_train, y_test = train_test_split(X_processed, y.values, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
len(train_dataset),len(test_dataset)

batch_size = 64
epochs = 500
print_every = 10

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
#Сравниваю несколько оптимизаторов
#Adam
adam_model = nn.Sequential(
    nn.Linear(train_dataset.tensors[0].shape[1], 64),
    nn.ReLU(),
    nn.Linear(64, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 32),
    nn.ReLU(),
    nn.Linear(32, 4)
)

adam_optimizer = optim.Adam(adam_model.parameters(), lr = 0.00001)
criterion = nn.MSELoss()
adam_losses = []

adam_model.train()
for epoch in range(epochs):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        predict = adam_model(X_batch)
        loss = criterion(predict, y_batch)
        loss.backward()
        adam_optimizer.step()
        adam_optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    adam_losses.append(loss_for_epoch)

    if epoch % print_every == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch:.6f}")      

#Rms
rmsprop_model = nn.Sequential(
    nn.Linear(train_dataset.tensors[0].shape[1], 64),
    nn.ReLU(),
    nn.Linear(64, 256),
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 32),
    nn.ReLU(),
    nn.Linear(32, 4)
)

rmsprop_optimizer = optim.RMSprop(rmsprop_model.parameters(), lr = 0.00001)
criterion = nn.MSELoss()
rmsprop_losses = []

rmsprop_model.train()
for epoch in range(epochs):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        predict = rmsprop_model(X_batch)
        loss = criterion(predict, y_batch)
        loss.backward()
        rmsprop_optimizer.step()
        rmsprop_optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    rmsprop_losses.append(loss_for_epoch)

    if epoch % print_every == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch:.6f}")         
#Adamw, sgd
plt.figure(figsize = (12, 8))
plt.plot(adam_losses, c = 'r', label = 'Adam')
plt.plot(rmsprop_losses, c = 'g', label = 'RMSProp')
plt.plot(adamw_losses, c = 'b', label = 'AdamW')
plt.plot(sgd_losses, c = 'black', label = 'SGD')
plt.legend()
plt.title('Ошибки в процессе обучения разными оптимизаторами за 500 эпох')
plt.show()

#Все оптимизаторы, кроме SGD, показали хороший результат в процессе обучения модели (Adam, AdamW и RMSProp показали практический одинаковый результат и практически одинаковую финальную ошибку за 500 эпох), только SGD оказался хуже, т.к. у него медленее сходимость и ему потребуется больше эпох и лучше подобранный learning rate для обучения модели до хороших показателей. Видно, что ошибка у SGD уменьшается медленее, и еще она перестала падать, что может говорить о том, что мы уперлись в локальный минимум и нужно корректировать learning rate
#Проверим и графически отобразим результаты на тестовом множестве для каждого оптимизатора
def test_loss(model):
    with torch.no_grad():
        y_pred = model(X_test)
        y_true = y_test
        loss = criterion(y_pred, y_true)
    return loss

adam_test_loss = test_loss(adam_model).item()
adam_test_loss
adamw_test_loss = test_loss(adamw_model).item()
adamw_test_loss
sgd_test_loss = test_loss(sgd_model).item()
sgd_test_loss
rmsprop_test_loss = test_loss(rmsprop_model).item()
rmsprop_test_loss
test_losses = [adam_test_loss, rmsprop_test_loss, adamw_test_loss, sgd_test_loss]
test_losses
optimizers = ['Adam', 'RMSProp', 'AdamW', 'SGD']
import seaborn as sns
plt.title('Ошибка на тестовом множестве для каждого оптимизатора')
sns.barplot(x = [1,2,3,4], y = test_losses, hue=optimizers);
#Видим, что лучшую ошибку на тестовом множестве показал оптимизатор Adam
    '''
        return pc.copy(s)
    
    def lang_pca():
        s = '''data_dir = 'images/sign_language/sign_language'

transform = transforms.Compose([
    transforms.Resize([128, 128]),
    transforms.ToTensor(),
    transforms.Normalize([0.5,],[0.5,])
])


full_dataset = ImageFolder(data_dir, transform=transform)

train_size = int(0.7 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

device = torch.device('cpu')
full_dataset.classes

model = nn.Sequential(
    nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),

    nn.Flatten(),
    nn.Linear(25088 , 128),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Dropout(),
    nn.Linear(64, len(full_dataset.classes))
).to(device)

classes = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  

class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=full_dataset.targets)

for i, weight in enumerate(class_weights):
    print(f"Class {classes[i]}: {weight}")

batch_size = 32
epochs = 30
print_every = 1
losses = []
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

for epoch in tqdm(range(epochs)):
    epoch_loss = []
    model.train()
    for batch_X, batch_y in train_loader:
        
        optimizer.zero_grad()

        y_pred = model(batch_X)

        loss = criterion(y_pred, batch_y)
        epoch_loss.append(loss.item())
        loss.backward()
        optimizer.step()
        

    losses.append(np.mean(epoch_loss))
    if (epoch+1) % print_every == 0:
        print(f'Epoch {epoch+1}/{epochs}, Train_Loss: {np.mean(epoch_loss):.4f}')

        
plt.plot(losses)
plt.title('Train Loss')
#Выводим confusion_matrix и classification_report на тестовой выборке

y_pred = []
y_true = []
device = torch.device('cpu')

model.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        outputs = model(X_batch)
        predicted = torch.argmax(outputs, 1)
        y_pred.extend(predicted.cpu().numpy())
        y_true.extend(y_batch.cpu().numpy())
y_pred = torch.tensor(y_pred)
y_true = torch.tensor(y_true)
sns.heatmap(confusion_matrix(y_true, y_pred), annot = True, fmt = f'.2f')
print(classification_report(y_true, y_pred))
        
from sklearn.decomposition import PCA

feature_extractor = nn.Sequential(*list(model.children())[:-1]).to(device)
feature_extractor.eval()
features = []
labels = []
with torch.no_grad():
    for batch_X, batch_y in DataLoader(full_dataset, batch_size=batch_size, shuffle=False):
        batch_X = batch_X.to(device)
        output = feature_extractor(batch_X)
        features.append(output.cpu().numpy())
        labels.append(batch_y.numpy())
features = np.concatenate(features, axis=0)
labels = np.concatenate(labels, axis=0)
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(features)
plt.figure(figsize=(10, 8))
scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=labels, cmap='tab10', alpha=0.7)
plt.legend(handles=scatter.legend_elements()[0], labels=full_dataset.classes, bbox_to_anchor=(1.05, 1), loc='upper right')
plt.xlabel('PCA Компонента 1')
plt.ylabel('PCA Компонента 2')
plt.title('PCA')
plt.tight_layout()
plt.show()
    '''
        return pc.copy(s)
    
    def chars_cnn():
        s = '''data_dir = "datasets/images/chars/"

# Предобработка изображений
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,), (0.5,))
])

# Загрузка данных
full_dataset = ImageFolder(data_dir, transform=transform)

train_size = int(0.7 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

cnn_model = nn.Sequential(
    nn.Conv2d(in_channels=3, out_channels=10, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(in_channels=10, out_channels=20, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(in_channels=20, out_channels=40, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(10240, 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, len(train_dataset.dataset.classes))
)
epochs = 50
print_every = 1

cnn_optimizer = optim.Adam(cnn_model.parameters(), lr = 0.001)
criterion = nn.CrossEntropyLoss()
cnn_losses = []

cnn_model.train()
for epoch in range(epochs):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        predict = cnn_model(X_batch)
        loss = criterion(predict, y_batch)
        loss.backward()
        cnn_optimizer.step()
        cnn_optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    cnn_losses.append(loss_for_epoch)

    if epoch % print_every == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch:.6f}")        


from sklearn.metrics import f1_score, accuracy_score
y_trues = []
y_preds = []
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        y_pred = cnn_model(X_batch)
        y_true = y_batch
        y_preds.extend(np.array(y_pred))
        y_trues.extend(np.array(y_true))
y_trues = np.array(y_trues)
y_preds = np.argmax(np.array(y_preds), 1)
len(y_preds),len(y_trues) 

print(f'Значение F1 на тестовом множестве: {f1_score(y_trues, y_preds):.4f}')

print(f'Значение accuracy на тестовом множестве: {accuracy_score(y_trues, y_preds):.4f}')

#Повторяю решение задачи, применив аугментацию к обучающему множеству
train_transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,), (0.5,))
])

test_transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,), (0.5,))
])

full_dataset = ImageFolder(data_dir)

train_size = int(0.7 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

train_dataset.dataset.transform = train_transform
test_dataset.dataset.transform = test_transform

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

epochs = 50
print_every = 1

cnn_optimizer = optim.Adam(cnn_model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
cnn_losses = []

cnn_model.train()
for epoch in range(epochs):
    loss_for_epoch = 0
    for X_batch, y_batch in train_loader:
        predict = cnn_model(X_batch)
        loss = criterion(predict, y_batch)
        loss.backward()
        cnn_optimizer.step()
        cnn_optimizer.zero_grad()
        loss_for_epoch += loss.item()
    loss_for_epoch /= len(train_loader)
    cnn_losses.append(loss_for_epoch)

    if epoch % print_every == 0:
        print(f"Epoch: {epoch} | Train loss for epoch: {loss_for_epoch:.6f}")

#Получим F1 на тестовом множестве для модели, обученной на расширенном датасете
y_trues = []
y_preds = []
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        y_pred = cnn_model(X_batch)
        y_true = y_batch
        y_preds.extend(np.array(y_pred))
        y_trues.extend(np.array(y_true))
y_trues = np.array(y_trues)
y_preds = np.argmax(np.array(y_preds), 1)

print(f'Значение F1 на тестовом множестве: {f1_score(y_trues, y_preds):.4f}')

print(f'Значение accuracy на тестовом множестве: {accuracy_score(y_trues, y_preds):.4f}')
    '''
        return pc.copy(s)
    
    def bike_r2_bathc():
        s = '''data = pd.read_csv(r"C:\Users\225061\Downloads\for_exam\datasets\regression\bike_cnt.csv").drop(columns = 'dteday',axis =1)
data.head()

X = data.drop(columns = "cnt", axis =1).to_numpy().astype('float')
y = data['cnt'].to_numpy().astype('float')

categorical_cols = []
numerical_cols = data.columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols)
    ])

data_processed = pd.DataFrame(preprocessor.fit_transform(data))
X_processed = data_processed.drop(columns=13, axis =1).to_numpy()
y_processed = data_processed[13].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X_processed, y_processed, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

model_no_bn = nn.Sequential(
    nn.Linear(X_train.shape[1], 1024),
    nn.ReLU(),
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Linear(512, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)
epochs = 10
models = {'с BatchNorm': model, 'без BatchNorm': model_no_bn}
results = {}

for name, model in models.items():
    model_losses = []
    test_r2 = []
    
    model_optimizer = optim.Adam(model.parameters(), lr=0.0001)
    
    for epoch in range(epochs):
        epoch_loss = []
        model.train()
        for batch_X, batch_y in train_loader:
            model_optimizer.zero_grad()
            y_pred = model(batch_X).squeeze()
            loss = criterion(batch_y, y_pred)
            epoch_loss.append(loss.item())
            loss.backward()
            model_optimizer.step()
        
        model_losses.append(np.mean(epoch_loss))

        if (epoch + 1) % print_every == 0:
            model.eval()
            with torch.no_grad():
                y_test_pred = model(X_test.clone().detach().requires_grad_(False).float()).squeeze()
                test_loss = criterion(y_test.clone().detach().requires_grad_(False).float(), y_test_pred).item()
                test_r2.append(r2_score(y_test.numpy(), y_test_pred.numpy().flatten()))
    
    results[name] = {'losses': model_losses, 'r2': test_r2}
    print(results)
    #Видно, что с нормализацией модель обучается быстрее
        '''
        return pc.copy(s)
    


      