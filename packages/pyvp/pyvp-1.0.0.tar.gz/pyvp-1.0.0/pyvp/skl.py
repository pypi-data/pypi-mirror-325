questions = {1: {'code': """# 2 регрессия gold
import pandas as pd
import numpy as np
import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
##
data = pd.read_csv('gold.csv')
data.dropna()
data[['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']]
##
X = data.drop(['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22'], axis=1)
y = data[['Gold_T-7', 'Gold_T-14', 'Gold_T-22', 'Gold_T+22']]
X = np.array(X)
y = np.array(y)
scaler = StandardScaler()
X_processed = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
##
class Model(nn.Module):
    def __init__(self, input_size):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(input_size, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64,64)
        self.fc4 = nn.Linear(64, 4)
        
        self.drop = nn.Dropout(0.4)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.drop(x)

        x = self.relu(self.fc2(x))
        x = self.drop(x)

        x = self.relu(self.fc3(x))
        x = self.drop(x)

        x = self.fc4(x)

        return x
##
batch_size = 64
epochs = 100
print_every = 10

criterion = nn.MSELoss()

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

def train(model, optimizer):
    print('-' * 100)
    model.train()
    total_loss = []
    for epoch in range(epochs):
        epoch_loss = 0
        
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            y_pred = model(batch_X)
            loss = criterion(y_pred, batch_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            
        epoch_loss /= len(train_loader)
        total_loss.append(epoch_loss)
        
        if (epoch+1) % print_every == 0:
            print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss[-1]}')
    return model, total_loss
##
model = Model(X.shape[1])
adam_model, train_adam = train(model, optim.Adam(model.parameters(), lr=0.001))
##
model = Model(X.shape[1])
nadam_model, train_nadam = train(model, optim.NAdam(model.parameters(), lr=0.001))
##
model = Model(X.shape[1])
rms_model, train_rms = train(model, optim.RMSprop(model.parameters(), lr=0.001))
##
plt.plot(train_adam, label='Adam')
plt.plot(train_nadam, label='Nadam')
plt.plot(train_rms, label='RMSprop')
plt.ylim(0, 0.0006)
plt.legend()
plt.grid()
##
def result(model):
    with torch.no_grad():
        y_pred = model(X_test).numpy()
        mae = mean_absolute_error(y_pred, y_test.numpy())
        return mae

adam_mae = result(adam_model)
nadam_mae = result(nadam_model)
rms_mae = result(rms_model)
print('MAE')
print(f'Adam: {adam_mae}')
print(f'NAdam: {nadam_mae}')
print(f'RMSprop: {rms_mae}')"""},
             2: {'code': """import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Загрузка и подготовка данных
data = pd.read_csv('Movie_regression.xls')  # Если действительно CSV
data = data.dropna()  # Удаляем все строки с пропусками

# Выбираем категориальные и числовые признаки
categorical_columns = data.select_dtypes(include=['object']).columns
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.drop('Marketing expense', errors='ignore')

# Разделение на X и y
X = data.drop(columns=['Marketing expense'])
y = data['Marketing expense']

# Трансформация признаков (StandardScaler для числовых, OneHotEncoder для категорий)
column_transformer = ColumnTransformer([
    ('num', StandardScaler(), numerical_columns),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])
X = column_transformer.fit_transform(X)

# Нормализация целевой переменной
y = y.values.reshape(-1, 1)
scaler_y = StandardScaler()
y_scaled = scaler_y.fit_transform(y)

# Train / Test split
X_train, X_test, y_train_scaled, y_test_scaled = train_test_split(
    X, y_scaled, test_size=0.2, random_state=42
)

# Превращаем в тензоры для PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train_scaled, dtype=torch.float32)
X_test_tensor  = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor  = torch.tensor(y_test_scaled, dtype=torch.float32)

# Определяем модели

class OneFC(nn.Module):
    def __init__(self, input_size):
        super(OneFC, self).__init__()
        self.fc = nn.Linear(input_size, 1)
    def forward(self, x):
        return self.fc(x)

class TwoFC(nn.Module):
    def __init__(self, input_size):
        super(TwoFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

class ThreeFC(nn.Module):
    def __init__(self, input_size):
        super(ThreeFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class FourFC(nn.Module):
    def __init__(self, input_size):
        super(FourFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        return self.fc4(x)

# Создаём DataLoader

batch_size = 64
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
lr = 0.01
epochs = 100

# Функция обучения, используя DataLoader

def train_model(model, optimizer, criterion, train_loader, X_test, y_test, scaler_y, epochs=100, print_every=10):
    model.train()

    train_losses = []
    test_losses = []

    for epoch in range(epochs):
        epoch_loss = 0.0

        # --- Шаг обучения ---
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            y_pred = model(batch_X)
            loss = criterion(y_pred, batch_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()

        # Средний лосс за эпоху (по batch'ам)
        epoch_loss /= len(train_loader)
        train_losses.append(epoch_loss)

        # --- Шаг валидации ---
        model.eval()
        with torch.no_grad():
            y_pred_test = model(X_test)
            y_pred_test_np = y_pred_test.numpy()
            y_test_np = y_test.numpy()
            # Переводим в исходный масштаб
            y_pred_unscaled = scaler_y.inverse_transform(y_pred_test_np)
            y_test_unscaled = scaler_y.inverse_transform(y_test_np)
            test_loss_mse = mean_squared_error(y_test_unscaled, y_pred_unscaled)
            test_losses.append(test_loss_mse)

        if (epoch + 1) % print_every == 0:
            print(f"Epoch {epoch + 1}/{epochs}, "
                  f"Train Loss={epoch_loss:.4f}, "
                  f"Test MSE={test_loss_mse:.4f}")

        model.train()  # Возвращаемся в режим train на следующую эпоху

    return train_losses, test_losses

# Функция окончательной оценки на тесте

def evaluate_model(model, X_test, y_test_scaled, scaler_y):
    model.eval()
    with torch.no_grad():
        y_pred_scaled = model(X_test).numpy()
    y_test_unscaled = scaler_y.inverse_transform(y_test_scaled.numpy())
    y_pred_unscaled = scaler_y.inverse_transform(y_pred_scaled)

    mse = mean_squared_error(y_test_unscaled, y_pred_unscaled)
    mae = mean_absolute_error(y_test_unscaled, y_pred_unscaled)
    r2 = r2_score(y_test_unscaled, y_pred_unscaled)
    return mse, mae, r2

# Обучаем и собираем результаты

input_size = X_train.shape[1]
criterion = nn.MSELoss()

# Модель 1: OneFC
one_fc = OneFC(input_size)
optimizer_one = optim.Adam(one_fc.parameters(), lr=lr)
print("Training OneFC...")
one_train_losses, one_test_losses = train_model(
    one_fc, optimizer_one, criterion,
    train_loader,
    X_test_tensor, y_test_tensor,
    scaler_y=scaler_y,
    epochs=epochs,
    print_every=10
)
one_mse, one_mae, one_r2 = evaluate_model(one_fc, X_test_tensor, y_test_tensor, scaler_y)
print(f"OneFC -> MSE={one_mse:.4f}, MAE={one_mae:.4f}, R2={one_r2:.4f}\n")

# Модель 2: TwoFC
two_fc = TwoFC(input_size)
optimizer_two = optim.Adam(two_fc.parameters(), lr=lr)
print("Training TwoFC...")
two_train_losses, two_test_losses = train_model(
    two_fc, optimizer_two, criterion,
    train_loader,
    X_test_tensor, y_test_tensor,
    scaler_y=scaler_y,
    epochs=epochs,
    print_every=10
)
two_mse, two_mae, two_r2 = evaluate_model(two_fc, X_test_tensor, y_test_tensor, scaler_y)
print(f"TwoFC -> MSE={two_mse:.4f}, MAE={two_mae:.4f}, R2={two_r2:.4f}\n")

# Модель 3: ThreeFC
three_fc = ThreeFC(input_size)
optimizer_three = optim.Adam(three_fc.parameters(), lr=lr)
print("Training ThreeFC...")
three_train_losses, three_test_losses = train_model(
    three_fc, optimizer_three, criterion,
    train_loader,
    X_test_tensor, y_test_tensor,
    scaler_y=scaler_y,
    epochs=epochs,
    print_every=10
)
three_mse, three_mae, three_r2 = evaluate_model(three_fc, X_test_tensor, y_test_tensor, scaler_y)
print(f"ThreeFC -> MSE={three_mse:.4f}, MAE={three_mae:.4f}, R2={three_r2:.4f}\n")

# Модель 4: FourFC
four_fc = FourFC(input_size)
optimizer_four = optim.Adam(four_fc.parameters(), lr=lr)
print("Training FourFC...")
four_train_losses, four_test_losses = train_model(
    four_fc, optimizer_four, criterion,
    train_loader,
    X_test_tensor, y_test_tensor,
    scaler_y=scaler_y,
    epochs=epochs,
    print_every=10
)
four_mse, four_mae, four_r2 = evaluate_model(four_fc, X_test_tensor, y_test_tensor, scaler_y)
print(f"FourFC -> MSE={four_mse:.4f}, MAE={four_mae:.4f}, R2={four_r2:.4f}\n")

# Сравнительная таблица

results_dict = {
    'Model': ['OneFC', 'TwoFC', 'ThreeFC', 'FourFC'],
    'MSE':   [one_mse, two_mse, three_mse, four_mse],
    'MAE':   [one_mae, two_mae, three_mae, four_mae],
    'R2':    [one_r2, two_r2, three_r2, four_r2]
}
results_df = pd.DataFrame(results_dict)
print("\nСравнительная таблица результатов:")
display(results_df)

# Графики

# Train Loss для каждой модели
plt.figure(figsize=(12, 5))
plt.plot(one_train_losses, label='OneFC - Train Loss')
plt.plot(two_train_losses, label='TwoFC - Train Loss')
plt.plot(three_train_losses, label='ThreeFC - Train Loss')
plt.plot(four_train_losses, label='FourFC - Train Loss')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('Training Loss Comparison')
plt.legend()
plt.show()

# Test MSE по эпохам
plt.figure(figsize=(12, 5))
plt.plot(one_test_losses, label='OneFC - Test MSE')
plt.plot(two_test_losses, label='TwoFC - Test MSE')
plt.plot(three_test_losses, label='ThreeFC - Test MSE')
plt.plot(four_test_losses, label='FourFC - Test MSE')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('Test MSE Comparison')
plt.legend()
plt.show()"""},
             3: {'code': """import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# 1. Загрузка данных
data = pd.read_csv('international-airline-passengers.csv')
data['time'] = pd.to_datetime(data['time'])
data['time'] = data['time'].map(pd.Timestamp.toordinal)

# 2. Создаём два независимых скейлера: для time и для пассажиров
time_scaler = MinMaxScaler()
pass_scaler = MinMaxScaler()

# 3. Масштабирование признака time и целевого столбца passengers по отдельности
data['time'] = time_scaler.fit_transform(data[['time']])
data['passengers'] = pass_scaler.fit_transform(data[['passengers']])

# 4. Разделение на X и y
X = data['time'].values.reshape(-1, 1).astype(np.float32)
y = data['passengers'].values.astype(np.float32)

# 5. Разделяем на тренировочную и тестовую выборки (shuffle=False для временного ряда)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# 6. Преобразование numpy в тензоры
X_train_tensor = torch.tensor(X_train)
y_train_tensor = torch.tensor(y_train).unsqueeze(1)  # (N,) -> (N,1)
X_test_tensor = torch.tensor(X_test)
y_test_tensor = torch.tensor(y_test).unsqueeze(1)

# 7. Определение модели
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(1, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 8. Функция обучения
def train_model(optimizer_name, model, criterion, optimizer, X_train, y_train, X_test, y_test, epochs=100):
    train_losses = []
    val_losses = []

    for epoch in range(epochs):
        # Обучение
        model.train()
        optimizer.zero_grad()

        y_pred = model(X_train)
        loss = criterion(y_pred, y_train)

        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())

        # Валидация
        model.eval()
        with torch.no_grad():
            y_val_pred = model(X_test)
            val_loss = criterion(y_val_pred, y_test)
            val_losses.append(val_loss.item())

        if (epoch + 1) % 10 == 0:
            print(f"{optimizer_name} - Epoch {epoch+1}/{epochs}, "f"Train Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}")

    return train_losses, val_losses

# 9. Подготавливаем разные оптимизаторы
optimizers = {
    "SGD":  lambda params: optim.SGD(params, lr=0.01),
    "Adam": lambda params: optim.Adam(params, lr=0.01),
    "AdamW":lambda params: optim.AdamW(params, lr=0.01)
}

# Словари для сохранения истории обучения и метрик
history_results = {}
metrics_results = {}

# 10. Запуск цикла обучения для каждого оптимизатора
for name, optimizer_func in optimizers.items():
    print(f"\n\nTraining with {name} optimizer...")

    # Инициализация новой модели
    model = NeuralNetwork()
    criterion = nn.MSELoss()
    optimizer = optimizer_func(model.parameters())

    # Обучение
    train_losses, val_losses = train_model(
        name, model, criterion, optimizer,
        X_train_tensor, y_train_tensor,
        X_test_tensor, y_test_tensor,
        epochs=100
    )
    history_results[name] = (train_losses, val_losses)

    # Прогноз на тестовой выборке (в масштабированном виде)
    model.eval()
    with torch.no_grad():
        y_pred_scaled = model(X_test_tensor).numpy()  # shape: (n_samples, 1)

    # 11. Инвертирование масштаба для y
    y_pred_original = pass_scaler.inverse_transform(y_pred_scaled)  # (n_samples, 1)
    y_test_original = pass_scaler.inverse_transform(y_test.reshape(-1, 1))  # (n_samples, 1)

    # Расчёт метрик на исходном масштабе
    mse = mean_squared_error(y_test_original, y_pred_original)
    mae = mean_absolute_error(y_test_original, y_pred_original)
    r2 = r2_score(y_test_original, y_pred_original)
    metrics_results[name] = {"MSE": mse, "MAE": mae, "R2": r2}

    print(f"{name} results: MSE={mse:.4f}, MAE={mae:.4f}, R2={r2:.4f}")

# 13. Визуализация кривых обучения (train & val)
plt.figure(figsize=(12, 5))
for name, (train_losses, val_losses) in history_results.items():
    plt.plot(train_losses, label=f'{name} - Training Loss')
    plt.plot(val_losses, label=f'{name} - Validation Loss')

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss by Optimizer')
plt.legend()
plt.show()

# 14. Отображение итоговых метрик
metrics_df = pd.DataFrame(metrics_results).T
print(metrics_df)"""},
             4: {'code': """# 2 классификация bank - confusion matrix & classification report
# несбалансированные классы (модифицировать функцию потерь) - сравнить
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt
import seaborn as sns
##
data = pd.read_csv('bank.csv')
data = data.dropna()
target_column = 'deposit'
X = data.drop(columns=[target_column])
y = data[target_column]
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

categorical_columns = X.select_dtypes(include=['object']).columns
numerical_columns = X.select_dtypes(exclude=['object']).columns
column_transformer = ColumnTransformer([
    ('num', 'passthrough', numerical_columns),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])
X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

unique_classes = np.unique(y_train)
class_weights_array = compute_class_weight('balanced', classes=unique_classes, y=y_train)
class_weights_tensor = torch.tensor(class_weights_array, dtype=torch.float32)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

batch_size = 64
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

##
class ThreeFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ThreeFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
##
def train_model(model, optimizer, criterion, train_loader, epochs=20, print_every=1):
    model.train()
    history = {'train_loss': []}
    for epoch in range(epochs):
        running_loss = 0.0
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        history['train_loss'].append(running_loss / len(train_loader))
        if (epoch + 1) % print_every == 0:
            print(f"Epoch [{epoch+1}/{epochs}] Train Loss: {running_loss / len(train_loader):.4f}")
    return history
##
input_size = X_train_tensor.shape[1]
num_classes = len(unique_classes)
criterion = nn.CrossEntropyLoss()
lr = 0.01
print("\nОбучаем модель с оптимизатором Adam...")
model_instance = ThreeFC(input_size, num_classes)
optimizer = optim.Adam(model_instance.parameters(), lr=lr)
history = train_model(model_instance, optimizer, criterion, train_loader, epochs=10)
plt.figure(figsize=(10, 5))
plt.plot(history['train_loss'], label="Train Loss")
plt.title("График потерь по эпохам")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()
##
model_instance.eval()
with torch.no_grad():
    test_outputs = model_instance(X_test_tensor)
    _, predicted_test = torch.max(test_outputs, 1)
    print("Classification Report:\n", classification_report(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy()))
    cm = confusion_matrix(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy())
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=unique_classes, yticklabels=unique_classes)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()
##
criterion = nn.CrossEntropyLoss(weight=class_weights_tensor)
print("\nОбучаем модель с учетом весов классов...")
model_instance = ThreeFC(input_size, num_classes)
optimizer = optim.Adam(model_instance.parameters(), lr=lr)
history = train_model(model_instance, optimizer, criterion, train_loader, epochs=10)
##
model_instance.eval()
with torch.no_grad():
    test_outputs = model_instance(X_test_tensor)
    _, predicted_test = torch.max(test_outputs, 1)
    print("Classification Report (с весами классов):\n", classification_report(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy()))
    cm = confusion_matrix(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy())
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=unique_classes, yticklabels=unique_classes)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix (с весами классов)")
    plt.show()"""},
             5: {'code': """# 2 классификация bank - confusion matrix & classification report
# Dropout сравнение
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt
import seaborn as sns
##
data = pd.read_csv('bank.csv')
data = data.dropna()
target_column = 'deposit'
X = data.drop(columns=[target_column])
y = data[target_column]
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

categorical_columns = X.select_dtypes(include=['object']).columns
numerical_columns = X.select_dtypes(exclude=['object']).columns
column_transformer = ColumnTransformer([
    ('num', 'passthrough', numerical_columns),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])
X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

unique_classes = np.unique(y_train)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

batch_size = 64
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
##
class ThreeFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ThreeFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class ThreeFC_Dropout(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ThreeFC_Dropout, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.dropout1 = nn.Dropout(0.3)
        self.fc2 = nn.Linear(64, 32)
        self.dropout2 = nn.Dropout(0.3)
        self.fc3 = nn.Linear(32, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout1(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout2(x)
        return self.fc3(x)

def train_model(model, optimizer, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=20, print_every=1):
    model.train()
    history = {'train_loss': []}
    for epoch in range(epochs):
        running_loss = 0.0
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        history['train_loss'].append(running_loss / len(train_loader))
        if (epoch + 1) % print_every == 0:
            print(f"Epoch [{epoch+1}/{epochs}] Train Loss: {running_loss / len(train_loader):.4f}")
    return history
##
input_size = X_train_tensor.shape[1]
num_classes = len(unique_classes)
criterion = nn.CrossEntropyLoss()
lr = 0.01

print("\nОбучаем модель без Dropout...")
model_no_dropout = ThreeFC(input_size, num_classes)
optimizer_no_dropout = optim.Adam(model_no_dropout.parameters(), lr=lr)
history_no_dropout = train_model(model_no_dropout, optimizer_no_dropout, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=10)
##
print("\nОбучаем модель с Dropout...")
model_with_dropout = ThreeFC_Dropout(input_size, num_classes)
optimizer_with_dropout = optim.Adam(model_with_dropout.parameters(), lr=lr)
history_with_dropout = train_model(model_with_dropout, optimizer_with_dropout, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=10)
##
plt.figure(figsize=(10, 5))
plt.plot(history_no_dropout['train_loss'], label="Train Loss - No Dropout")
plt.plot(history_with_dropout['train_loss'], label="Train Loss - Dropout")
plt.title("График потерь по эпохам")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()
##
for model, name in zip([model_no_dropout, model_with_dropout], ["Без Dropout", "С Dropout"]):
    model.eval()
    with torch.no_grad():
        test_outputs = model(X_test_tensor)
        _, predicted_test = torch.max(test_outputs, 1)
        print(f"Classification Report ({name}):\n", classification_report(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy()))
        cm = confusion_matrix(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy())
        plt.figure(figsize=(6, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=unique_classes, yticklabels=unique_classes)
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title(f"Confusion Matrix ({name})")
        plt.show()"""},
             6: {'code': """# 2 классификация bank - разные оптимизаторы
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Для предобработки
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt

# Загрузка и предобработка данных
data = pd.read_csv('bank.csv')
data = data.dropna()
target_column = 'deposit'
X = data.drop(columns=[target_column])
y = data[target_column]
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

categorical_columns = X.select_dtypes(include=['object']).columns
numerical_columns = X.select_dtypes(exclude=['object']).columns
column_transformer = ColumnTransformer([
    ('num', 'passthrough', numerical_columns),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])
X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

unique_classes = np.unique(y_train)
class_weights_array = compute_class_weight('balanced', classes=unique_classes, y=y_train)
class_weights_tensor = torch.tensor(class_weights_array, dtype=torch.float32)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

batch_size = 64
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Определение модели
class ThreeFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ThreeFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Функция обучения

def train_model(model, optimizer, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=20, print_every=1):
    model.train()
    history = {'train_loss': [], 'train_accuracy': [], 'test_accuracy': [], 'test_f1': []}
    for epoch in range(epochs):
        running_loss = 0.0
        correct_train, total_train = 0, 0
        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct_train += (predicted == batch_y).sum().item()
            total_train += batch_y.size(0)
        train_acc = correct_train / total_train
        model.eval()
        with torch.no_grad():
            test_outputs = model(X_test_tensor)
            _, predicted_test = torch.max(test_outputs, 1)
            test_acc = accuracy_score(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy())
            test_f1 = f1_score(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy(), average='weighted')
        model.train()
        history['train_loss'].append(running_loss / len(train_loader))
        history['train_accuracy'].append(train_acc)
        history['test_accuracy'].append(test_acc)
        history['test_f1'].append(test_f1)
        if (epoch + 1) % print_every == 0:
            print(f"Epoch [{epoch+1}/{epochs}] Train Acc: {train_acc:.4f}, Test Acc: {test_acc:.4f}, Test F1: {test_f1:.4f}")
    return history

input_size = X_train_tensor.shape[1]
num_classes = len(unique_classes)
criterion = nn.CrossEntropyLoss(weight=class_weights_tensor)
lr = 0.01

optimizers = {
    'Adam': optim.Adam,
    'Nadam': optim.NAdam,
    'RMSprop': optim.RMSprop
}

history_dict = {}
final_results = []

for opt_name, opt_class in optimizers.items():
    print(f"\nОбучаем модель с оптимизатором {opt_name}...")
    model_instance = ThreeFC(input_size, num_classes)
    optimizer = opt_class(model_instance.parameters(), lr=lr)
    history = train_model(model_instance, optimizer, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=10)
    history_dict[opt_name] = history
    final_results.append({'Optimizer': opt_name, 'Test Accuracy': history['test_accuracy'][-1], 'Test F1': history['test_f1'][-1]})

results_df = pd.DataFrame(final_results)
print("\nСравнительная таблица (финальные метрики на тесте):")
print(results_df)

plt.figure(figsize=(10, 5))
for opt_name, hist in history_dict.items():
    plt.plot(hist['test_accuracy'], label=f"{opt_name} - Test Acc")
plt.title("Сравнение Test Accuracy по эпохам")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()"""},
             7: {'code': """# 2 классификация bank - разные модели
# классификация
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.utils.class_weight import compute_class_weight
import matplotlib.pyplot as plt
##
data = pd.read_csv('bank.csv')
data = data.dropna()
target_column = 'deposit'

X = data.drop(columns=[target_column])
y = data[target_column]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

categorical_columns = X.select_dtypes(include=['object']).columns
numerical_columns = X.select_dtypes(exclude=['object']).columns

column_transformer = ColumnTransformer([
    ('num', 'passthrough', numerical_columns),  # без изменений
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])
X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y_encoded,
    test_size=0.2, random_state=42, stratify=y_encoded
)
##
unique_classes = np.unique(y_train)
class_weights_array = compute_class_weight(
    class_weight='balanced',
    classes=unique_classes,
    y=y_train
)
print("Веса классов (по порядку классов в unique_classes):")
for cls, w in zip(unique_classes, class_weights_array):
    print(f"Class {cls} -> weight {w:.4f}")

class_weights_tensor = torch.tensor(class_weights_array, dtype=torch.float32)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)

X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

batch_size = 64
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
##
class OneFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(OneFC, self).__init__()
        self.fc = nn.Linear(input_size, num_classes)
    def forward(self, x):
        return self.fc(x)

class TwoFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(TwoFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

class ThreeFC(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ThreeFC, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, num_classes)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
##
def train_model(model, optimizer, criterion, train_loader, X_test_tensor, y_test_tensor, epochs=20, print_every=1):
    model.train()
    history = {
        'train_loss': [],
        'train_accuracy': [],
        'train_f1': [],
        'test_accuracy': [],
        'test_f1': []}
    for epoch in range(epochs):
        running_loss = 0.0
        correct_train = 0
        total_train = 0
        all_preds_train = []
        all_labels_train = []

        for batch_X, batch_y in train_loader:
            optimizer.zero_grad()

            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            _, predicted = torch.max(outputs, 1)
            correct_train += (predicted == batch_y).sum().item()
            total_train += batch_y.size(0)
            all_preds_train.extend(predicted.cpu().numpy())
            all_labels_train.extend(batch_y.cpu().numpy())

        epoch_loss = running_loss / len(train_loader)
        train_acc = correct_train / total_train
        train_f1 = f1_score(all_labels_train, all_preds_train, average='weighted')

        model.eval()
        with torch.no_grad():
            test_outputs = model(X_test_tensor)
            _, predicted_test = torch.max(test_outputs, 1)
            test_acc = accuracy_score(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy())
            test_f1 = f1_score(y_test_tensor.cpu().numpy(), predicted_test.cpu().numpy(), average='weighted')
        model.train()

        history['train_loss'].append(epoch_loss)
        history['train_accuracy'].append(train_acc)
        history['train_f1'].append(train_f1)
        history['test_accuracy'].append(test_acc)
        history['test_f1'].append(test_f1)

        if (epoch + 1) % print_every == 0:
            print(f"Epoch [{epoch+1}/{epochs}] "
                  f"Train Loss: {epoch_loss:.4f}, "
                  f"Train Acc: {train_acc:.4f}, "
                  f"Test Acc: {test_acc:.4f}, "
                  f"Test F1: {test_f1:.4f}")

    return history

##
input_size = X_train_tensor.shape[1]
num_classes = len(unique_classes)

criterion = nn.CrossEntropyLoss(weight=class_weights_tensor)
lr = 0.01
models = {
    'OneFC': OneFC(input_size, num_classes),
    'TwoFC': TwoFC(input_size, num_classes),
    'ThreeFC': ThreeFC(input_size, num_classes),
}
history_dict = {}
final_results = []
for model_name, model_instance in models.items():
    print(f"\nОбучаем модель {model_name}...")
    optimizer = optim.Adam(model_instance.parameters(), lr=lr)
    history = train_model(model_instance, optimizer, criterion, train_loader,
                          X_test_tensor, y_test_tensor,
                          epochs=10, print_every=1)

    history_dict[model_name] = history
    test_acc = history['test_accuracy'][-1]
    test_f1 = history['test_f1'][-1]
    final_results.append({
        'Model': model_name,
        'Test Accuracy': test_acc,
        'Test F1': test_f1
    })
##
results_df = pd.DataFrame(final_results)
print("\nСравнительная таблица (финальные метрики на тесте):")
print(results_df)
##
plt.figure(figsize=(10, 5))
for model_name, hist in history_dict.items():
    plt.plot(hist['train_accuracy'], label=f"{model_name} - Train Acc")
plt.title("Сравнение Train Accuracy по эпохам")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
##
plt.figure(figsize=(10, 5))
for model_name, hist in history_dict.items():
    plt.plot(hist['test_accuracy'], label=f"{model_name} - Test Acc")
plt.title("Сравнение Test Accuracy по эпохам")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()"""},
             8: {'code': """# 3 chars - аугментация (случайные преобразования)
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split, ConcatDataset
from sklearn.metrics import f1_score
import numpy as np
import matplotlib.pyplot as plt
##
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 10
LR = 0.001
DATA_PATH = "chars"

def calculate_mean_std(loader):
    mean = torch.zeros(3)
    std = torch.zeros(3)
    total_samples = 0
    for images, _ in loader:
        batch_samples = images.size(0)
        images = images.view(batch_samples, 3, -1)
        mean += images.mean(dim=[0, 2]) * batch_samples
        std += images.std(dim=[0, 2]) * batch_samples
        total_samples += batch_samples

    mean /= total_samples
    std /= total_samples
    return mean, std

calc_transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor()
])
calc_dataset = datasets.ImageFolder(DATA_PATH, transform=calc_transform)
calc_loader = DataLoader(calc_dataset, batch_size=BATCH_SIZE, shuffle=False)

mean, std = calculate_mean_std(calc_loader)
base_transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean.tolist(), std=std.tolist())
])
##
aug_transform = transforms.Compose([
    transforms.RandomRotation(20),
    transforms.RandomHorizontalFlip(),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.ColorJitter(brightness=0.3, contrast=0.3),
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean.tolist(), std=std.tolist())
])
##
dataset = datasets.ImageFolder(DATA_PATH, transform=base_transform)
num_classes = len(dataset.classes)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

augmented_dataset = datasets.ImageFolder(DATA_PATH, transform=aug_transform)
train_extended = ConcatDataset([train_dataset, augmented_dataset])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
train_loader_extended = DataLoader(train_extended, batch_size=BATCH_SIZE, shuffle=True)
##
class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * (IMG_SIZE // 4) * (IMG_SIZE // 4), 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        x = self.pool(torch.relu(self.bn1(self.conv1(x))))
        x = self.pool(torch.relu(self.bn2(self.conv2(x))))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.bn_fc(self.fc1(x)))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
##
def train_model(model, train_loader, test_loader, criterion, optimizer, epochs):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")

    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.numpy())
            all_labels.extend(labels.numpy())

    f1 = f1_score(all_labels, all_preds, average='micro')
    return f1
##
model_base = CNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model_base.parameters(), lr=LR)

print("Обучение модели на обычном датасете...")
f1_base = train_model(model_base, train_loader, test_loader, criterion, optimizer, EPOCHS)
print(f"F1-score (без аугментации): {f1_base:.4f}")
##
model_augmented = CNN(num_classes)
optimizer_aug = optim.Adam(model_augmented.parameters(), lr=LR)

print("Обучение модели на расширенном датасете...")
f1_augmented = train_model(model_augmented, train_loader_extended, test_loader, criterion, optimizer_aug, EPOCHS)
print(f"F1-score (c аугментацией): {f1_augmented:.4f}")
plt.bar(["Без аугментации", "С аугментацией"], [f1_base, f1_augmented], color=['blue', 'green'])
plt.ylabel("F1-score")
plt.title("Сравнение F1-score на тестовом датасете")
plt.show()"""},
             9: {'code': """import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import f1_score
import numpy as np
##
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 10
LR = 0.001
dataset_path = "eng_handwritten"

def central_crop(image, size=IMG_SIZE, crop_ratio=0.2):
    width, height = image.size
    crop_width = int(width * crop_ratio / 2)
    crop_height = int(height * crop_ratio / 2)
    left = crop_width
    top = crop_height
    right = width - crop_width
    bottom = height - crop_height
    return image.crop((left, top, right, bottom)).resize((size, size))
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Lambda(lambda img: central_crop(img, IMG_SIZE, crop_ratio=0.2)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])
##
dataset = datasets.ImageFolder(root=dataset_path, transform=transform)
train_size = int(0.7 * len(dataset))
val_size = int(0.15 * len(dataset))
test_size = len(dataset) - train_size - val_size
train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
##
class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * (IMG_SIZE // 8) * (IMG_SIZE // 8), 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        x = self.pool(torch.relu(self.bn1(self.conv1(x))))
        x = self.pool(torch.relu(self.bn2(self.conv2(x))))
        x = self.pool(torch.relu(self.bn3(self.conv3(x))))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.bn_fc(self.fc1(x)))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
##
num_classes = len(dataset.classes)
model = CNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

def train(model, train_loader, val_loader, criterion, optimizer, epochs, patience=3):
    best_f1 = 0
    patience_counter = 0
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        model.eval()
        all_preds, all_labels = [], []
        with torch.no_grad():
            for images, labels in val_loader:
                outputs = model(images)
                preds = torch.argmax(outputs, dim=1)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())
        
        f1 = f1_score(all_labels, all_preds, average='micro')
        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}, train micro F1: {f1:.4f}")
        
        if f1 > best_f1:
            best_f1 = f1
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print("Early stopping triggered")
                break
train(model, train_loader, val_loader, criterion, optimizer, EPOCHS)
##
def evaluate(model, loader):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for images, labels in loader:
            outputs = model(images)
            preds = torch.argmax(outputs, dim=1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    f1 = f1_score(all_labels, all_preds, average='micro')
    print(f"Test Micro F1: {f1:.4f}")
evaluate(model, test_loader)"""},
             10: {'code': """# 3 sign_language - сравнение по количеству сверток
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
from sklearn.metrics import f1_score
##
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Используемое устройство:", device)
batch_size = 32
learning_rate = 0.001
num_epochs = 10
image_size = 128
data_dir = "train"

transform_calc = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor()
])

calc_dataset = datasets.ImageFolder(data_dir, transform=transform_calc)
calc_loader = DataLoader(calc_dataset, batch_size=batch_size, shuffle=False)

def calculate_mean_std(loader):
    with torch.no_grad():
        total_sum = torch.zeros(3)
        total_squared_sum = torch.zeros(3)
        total_pixels = 0
        for inputs, _ in loader:
            inputs = inputs.view(inputs.size(0), inputs.size(1), -1)
            total_sum += inputs.sum(dim=[0, 2])
            total_squared_sum += (inputs ** 2).sum(dim=[0, 2])
            total_pixels += inputs.size(0) * inputs.size(2)
        mean = total_sum / total_pixels
        std = torch.sqrt(total_squared_sum / total_pixels - mean ** 2)
    return mean, std

mean, std = calculate_mean_std(calc_loader)
print(f"Mean: {mean}, Std: {std}")

transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean.tolist(), std=std.tolist())
])

##
full_dataset = datasets.ImageFolder(data_dir, transform=transform)
num_classes = len(full_dataset.classes)
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = random_split(full_dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
print("Классы:", full_dataset.classes)
print(f"Размер train: {len(train_dataset)}, размер test: {len(test_dataset)}")

##
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2) 
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * (image_size // 4) * (image_size // 4), 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x))) 
        x = self.pool(self.relu(self.conv2(x))) 
        x = x.view(x.size(0), -1) 
        x = self.relu(self.fc1(x)) 
        x = self.fc2(x)
        return x

class DeeperCNN(nn.Module):
    def __init__(self, num_classes, image_size):
        super(DeeperCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1) 
        self.bn1 = nn.BatchNorm2d(16)  
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1) 
        self.bn2 = nn.BatchNorm2d(32)  
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1) 
        self.bn3 = nn.BatchNorm2d(64) 
        self.pool = nn.MaxPool2d(2, 2)  
        self.fc1 = nn.Linear(64 * (image_size // 8) * (image_size // 8), 128) 
        self.bn_fc1 = nn.BatchNorm1d(128)  
        self.dropout = nn.Dropout(0.5)  
        self.fc2 = nn.Linear(128, num_classes) 
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.bn1(self.conv1(x)))) 
        x = self.pool(self.relu(self.bn2(self.conv2(x))))  
        x = self.pool(self.relu(self.bn3(self.conv3(x))))  
        x = x.view(x.size(0), -1)
        x = self.relu(self.bn_fc1(self.fc1(x)))  
        x = self.dropout(x)  
        x = self.fc2(x)  
        return x
##
def train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs):
    model.to(device)
    train_losses = []
    test_losses = []
    test_f1_scores = []

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        epoch_train_loss = running_loss / len(train_loader)
        train_losses.append(epoch_train_loss)

        model.eval()
        running_test_loss = 0.0
        all_labels = []
        all_preds = []
        with torch.no_grad():
            for inputs, labels in test_loader:
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                running_test_loss += loss.item()
                _, preds = torch.max(outputs, 1)
                all_labels.extend(labels.cpu().numpy())
                all_preds.extend(preds.cpu().numpy())

        epoch_test_loss = running_test_loss / len(test_loader)
        test_losses.append(epoch_test_loss)

        f1 = f1_score(all_labels, all_preds, average='micro')
        test_f1_scores.append(f1)

        print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {epoch_train_loss:.4f}, "
              f"Test Loss: {epoch_test_loss:.4f}, Micro-F1: {f1:.4f}")

    return train_losses, test_losses, test_f1_scores
##
criterion = nn.CrossEntropyLoss()
print("\nОбучение SimpleCNN...")
model1 = SimpleCNN(num_classes)
optimizer1 = optim.Adam(model1.parameters(), lr=learning_rate)
train_losses1, test_losses1, test_f1_scores1 = train_model(
    model1, train_loader, test_loader, criterion, optimizer1, num_epochs
)
print("\nОбучение DeeperCNN...")
model2 = DeeperCNN(num_classes)
optimizer2 = optim.Adam(model2.parameters(), lr=learning_rate)
train_losses2, test_losses2, test_f1_scores2 = train_model(
    model2, train_loader, test_loader, criterion, optimizer2, num_epochs
)
##
plt.figure(figsize=(8, 5))
plt.plot(test_f1_scores1, label='SimpleCNN (2 conv blocks)')
plt.plot(test_f1_scores2, label='DeeperCNN (3 conv blocks)')
plt.xlabel('Epoch')
plt.ylabel('Micro-F1 on Test')
plt.title('Сравнение F1 двух архитектур')
plt.legend()
plt.show()"""},
             11: {'code': """# 3 sign_language - confusion matrix & classification report
#   найди наиболее похожие на основе векторного представления
import random
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
##
data_dir = "sign_language"
batch_size = 32
learning_rate = 1e-3
num_epochs = 5
image_size = 64


calc_transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor()
])

calc_dataset = datasets.ImageFolder(root=data_dir, transform=calc_transform)
calc_loader = DataLoader(calc_dataset, batch_size=batch_size, shuffle=False)
mean = torch.zeros(3)
std = torch.zeros(3)
total = 0
for images, _ in calc_loader:
    b, c, h, w = images.shape
    images = images.view(b, c, -1)
    mean += images.mean(dim=2).sum(dim=0)
    std += images.std(dim=2).sum(dim=0)
    total += b
mean /= total
std /= total

transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean.tolist(), std.tolist())
])

full_dataset = datasets.ImageFolder(root=data_dir, transform=transform)
train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = random_split(full_dataset, [train_size, test_size])
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
class_names = full_dataset.classes
num_classes = len(class_names)
##
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        self.dropout = nn.Dropout(p=0.3)
        self.fc1 = nn.Linear(32*(image_size//4)*(image_size//4), 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        x = self.fc1(x)
        x = self.bn_fc(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
    def get_embedding(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        x = self.fc1(x)
        x = self.bn_fc(x)
        x = self.relu(x)
        return x
##
model = SimpleCNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


def train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs):
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        model.eval()
        test_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in test_loader:
                outputs = model(images)
                loss = criterion(outputs, labels)
                test_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)
        print(f"Epoch [{epoch+1}/{num_epochs}], "
              f"Train Loss: {running_loss/len(train_loader):.4f}, "
              f"Test Loss: {test_loss/len(test_loader):.4f}, "
              f"Test Acc: {correct/total:.4f}")


train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs)
##
y_true = []
y_pred = []
model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        y_true.extend(labels.numpy())
        y_pred.extend(predicted.numpy())
cm = confusion_matrix(y_true, y_pred)
cr = classification_report(y_true, y_pred, target_names=class_names)

print(cm)
print(cr)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=class_names, yticklabels=class_names, fmt='g')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
##
misclassified_images = []
misclassified_labels = []
misclassified_preds = []

model.eval()
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        mismatch = (predicted != labels)
        if mismatch.any():
            for i in range(len(images)):
                if mismatch[i]:
                    misclassified_images.append(images[i])
                    misclassified_labels.append(labels[i].item())
                    misclassified_preds.append(predicted[i].item())

if len(misclassified_images) > 0:
    mistake_idx = 0
    mistaken_image = misclassified_images[mistake_idx]
    true_label = misclassified_labels[mistake_idx]
    pred_label = misclassified_preds[mistake_idx]
    print(f"True: {class_names[true_label]}, Pred: {class_names[pred_label]}")
else:
    mistaken_image = None

if mistaken_image is not None:
    mistaken_image_batch = mistaken_image.unsqueeze(0)
    mistaken_embedding = model.get_embedding(mistaken_image_batch).detach().numpy()
    all_embeddings = []
    all_images = []
    for idx in range(len(full_dataset)):
        img, label = full_dataset[idx]
        emb = model.get_embedding(img.unsqueeze(0)).detach().numpy()[0]
        all_embeddings.append(emb)
        all_images.append((img, label))
    all_embeddings = np.array(all_embeddings)
    distances = np.linalg.norm(all_embeddings - mistaken_embedding, axis=1) # Евклидово расстояние
    K = 5 # K ближайших соседей (наименьшее расстояние)
    nearest_indices = np.argsort(distances)[:K]
    fig, axs = plt.subplots(1, K+1, figsize=(15,3))
    img_show = mistaken_image.permute(1,2,0).numpy()
    img_show = img_show * np.array(std) + np.array(mean)
    img_show = np.clip(img_show,0,1)
    axs[0].imshow(img_show)
    axs[0].set_title(f"True: {class_names[true_label]}, Pred: {class_names[pred_label]}")
    axs[0].axis('off')
    for i, idx_near in enumerate(nearest_indices):
        nearest_img, nearest_label = all_images[idx_near]
        nearest_img_show = nearest_img.permute(1,2,0).numpy()
        nearest_img_show = nearest_img_show * np.array(std) + np.array(mean)
        nearest_img_show = np.clip(nearest_img_show,0,1)
        axs[i+1].imshow(nearest_img_show)
        axs[i+1].set_title(f"Dist: {distances[idx_near]:.2f}, Cls: {class_names[nearest_label]}")
        axs[i+1].axis('off')
    plt.tight_layout()
    plt.show()"""},
             12: {'code': """# 3 sign_language PCA
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split, Dataset
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
from sklearn.decomposition import PCA
##
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Используемое устройство:", device)

batch_size = 32
learning_rate = 0.001
num_epochs = 10
image_size = 128
data_dir = "sign_language"

transform_calc = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor()
])
##
calc_dataset = datasets.ImageFolder(data_dir, transform=transform_calc)
calc_loader = DataLoader(calc_dataset, batch_size=batch_size, shuffle=False)

def calculate_mean_std(loader):
    with torch.no_grad():
        total_sum = torch.zeros(3)
        total_squared_sum = torch.zeros(3)
        total_pixels = 0
        for inputs, _ in loader:
            # inputs shape: [B, 3, H, W]
            # Сольём H*W в один размер
            inputs = inputs.view(inputs.size(0), inputs.size(1), -1)
            total_sum += inputs.sum(dim=[0, 2])
            total_squared_sum += (inputs ** 2).sum(dim=[0, 2])
            total_pixels += inputs.size(0) * inputs.size(2)
        mean = total_sum / total_pixels
        std = torch.sqrt(total_squared_sum / total_pixels - mean ** 2)
    return mean, std

mean, std = calculate_mean_std(calc_loader)
print(f"Mean: {mean}, Std: {std}")

transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean.tolist(), std=std.tolist())
])
##
full_dataset = datasets.ImageFolder(data_dir, transform=transform)
num_classes = len(full_dataset.classes)

train_size = int(0.8 * len(full_dataset))
test_size = len(full_dataset) - train_size
train_dataset, test_dataset = random_split(full_dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

print(f"Размер train: {len(train_dataset)}, размер test: {len(test_dataset)}")
##
def dataset_to_arrays(dataset):
    xs = []
    ys = []
    for img, label in dataset:
        x_flat = img.view(-1).numpy() # превращаем в вектор
        xs.append(x_flat)
        ys.append(label)
    X = np.vstack(xs)
    Y = np.array(ys)
    return X, Y

X_train_raw, y_train = dataset_to_arrays(train_dataset)
X_test_raw, y_test = dataset_to_arrays(test_dataset)

print("X_train_raw:", X_train_raw.shape)  # (N_train, 3*H*W)
print("X_test_raw:", X_test_raw.shape)    # (N_test, 3*H*W)


##
n_components = 128  # любое подходящее число компонент
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train_raw) # fit на train
X_test_pca = pca.transform(X_test_raw) # transform test

print("X_train_pca:", X_train_pca.shape) # (N_train, n_components)
print("X_test_pca:", X_test_pca.shape)

class PCADataset(Dataset):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x = self.X[idx]
        y = self.Y[idx]
        return torch.from_numpy(x).float(), torch.tensor(y, dtype=torch.long) # возвращаем Tensor float32 для входа в PyTorch

train_dataset_pca = PCADataset(X_train_pca, y_train)
test_dataset_pca = PCADataset(X_test_pca, y_test)

train_loader_pca = DataLoader(train_dataset_pca, batch_size=batch_size, shuffle=True)
test_loader_pca = DataLoader(test_dataset_pca, batch_size=batch_size, shuffle=False)

##
class CNN(nn.Module):
    def __init__(self, num_classes, image_size=128):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * (image_size // 4) * (image_size // 4), 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x))) 
        x = self.pool(self.relu(self.conv2(x)))  
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))     
        x = self.fc2(x) 
        return x

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    
##
def train_model(model, train_loader, test_loader, criterion, optimizer, device, num_epochs=10):
    model.to(device)
    train_losses = []
    test_losses = []
    test_f1_scores = []

    for epoch in range(num_epochs):
        # -- train --
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        epoch_train_loss = running_loss / len(train_loader)
        train_losses.append(epoch_train_loss)

        # -- eval --
        model.eval()
        running_test_loss = 0.0
        all_labels = []
        all_preds = []
        with torch.no_grad():
            for inputs, labels in test_loader:
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                running_test_loss += loss.item()

                _, preds = torch.max(outputs, 1)
                all_labels.extend(labels.cpu().numpy())
                all_preds.extend(preds.cpu().numpy())

        epoch_test_loss = running_test_loss / len(test_loader)
        test_losses.append(epoch_test_loss)

        f1 = f1_score(all_labels, all_preds, average='micro')
        test_f1_scores.append(f1)

        print(f"Epoch {epoch+1}/{num_epochs}, "
              f"Train Loss: {epoch_train_loss:.4f}, "
              f"Test Loss: {epoch_test_loss:.4f}, "
              f"Micro-F1: {f1:.4f}")

    return train_losses, test_losses, test_f1_scores
##
criterion = nn.CrossEntropyLoss()
print("\nОбучение CNN")
model_cnn = CNN(num_classes=num_classes, image_size=image_size)
optimizer_cnn = optim.Adam(model_cnn.parameters(), lr=learning_rate)
train_losses_cnn, test_losses_cnn, test_f1_scores_cnn = train_model(
    model_cnn, train_loader, test_loader, criterion, optimizer_cnn, device, num_epochs=num_epochs
)
##
print("\nОбучение MLP на PCA-признаках")
model_pca = MLP(input_size=n_components, hidden_size=128, num_classes=num_classes)
optimizer_pca = optim.Adam(model_pca.parameters(), lr=learning_rate)

train_losses_pca, test_losses_pca, test_f1_scores_pca = train_model(
    model_pca, train_loader_pca, test_loader_pca, criterion, optimizer_pca, device, num_epochs=num_epochs
)
##
# Пример: возьмём первые 5 изображений из тестовой выборки
n_images_to_show = 5
indices = range(n_images_to_show)
X_test_pca_subset = X_test_pca[indices]
X_test_reconstructed = pca.inverse_transform(X_test_pca_subset)

def reshape_for_plot(x_flat, channels=3, height=128, width=128):
    x_img = x_flat.reshape(channels, height, width)
    x_img = np.transpose(x_img, (1, 2, 0))
    return x_img

H, W = 128, 128

fig, axes = plt.subplots(2, n_images_to_show, figsize=(3*n_images_to_show, 6))
for i, idx in enumerate(indices):
    original_flat = X_test_raw[idx]
    original_img = reshape_for_plot(original_flat, channels=3, height=H, width=W)
    original_img = original_img - original_img.min()
    original_img = original_img / original_img.max()
    reconstructed_flat = X_test_reconstructed[i]
    reconstructed_img = reshape_for_plot(reconstructed_flat, channels=3, height=H, width=W)
    reconstructed_img = reconstructed_img - reconstructed_img.min()
    reconstructed_img = reconstructed_img / reconstructed_img.max()

    axes[0, i].imshow(original_img)
    axes[0, i].set_title(f"Original #{idx}")
    axes[0, i].axis('off')
    axes[1, i].imshow(reconstructed_img)
    axes[1, i].set_title(f"Reconstructed #{idx}")
    axes[1, i].axis('off')
plt.tight_layout()
plt.show()
##
epochs_range = range(1, num_epochs+1)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(epochs_range, test_losses_cnn, label='CNN Test Loss')
plt.plot(epochs_range, test_losses_pca, label='PCA+MLP Test Loss')
plt.title("Test Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.subplot(1,2,2)
plt.plot(epochs_range, test_f1_scores_cnn, label='CNN F1')
plt.plot(epochs_range, test_f1_scores_pca, label='PCA+MLP F1')
plt.title("Micro-F1 Score")
plt.xlabel("Epoch")
plt.ylabel("F1")
plt.legend()

plt.tight_layout()
plt.show()"""},
             13: {'code': """# 3 clothes_multi 
import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import f1_score
import numpy as np
##
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 10
LR = 0.001
dataset_path = "clothes_multi"

def split_labels(folder_name):
    color, item = folder_name.split("_")
    return color, item

color_labels = set()
item_labels = set()
for folder in os.listdir(dataset_path):
    color, item = split_labels(folder)
    color_labels.add(color)
    item_labels.add(item)

color_labels = sorted(list(color_labels))
item_labels = sorted(list(item_labels))

color_to_idx = {color: i for i, color in enumerate(color_labels)}
item_to_idx = {item: i for i, item in enumerate(item_labels)}
##
def calculate_mean_std(loader):
    with torch.no_grad():
        total_sum = torch.zeros(3)
        total_squared_sum = torch.zeros(3)
        total_pixels = 0
        for inputs, _ in loader:
            inputs = inputs.view(inputs.size(0), inputs.size(1), -1)
            total_sum += inputs.sum(dim=[0, 2])
            total_squared_sum += (inputs ** 2).sum(dim=[0, 2])
            total_pixels += inputs.size(0) * inputs.size(2)
        mean = total_sum / total_pixels
        std = torch.sqrt(total_squared_sum / total_pixels - mean ** 2)
    return mean, std

transform_basic = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor()
])

dataset_temp = datasets.ImageFolder(root=dataset_path, transform=transform_basic)
temp_loader = DataLoader(dataset_temp, batch_size=BATCH_SIZE, shuffle=False)
mean, std = calculate_mean_std(temp_loader)

transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])

class MultiLabelDataset(datasets.ImageFolder):
    def __getitem__(self, index):
        img, _ = super().__getitem__(index)
        folder_name = self.classes[self.targets[index]]
        color, item = split_labels(folder_name)
        color_label = torch.zeros(len(color_labels))
        item_label = torch.zeros(len(item_labels))
        color_label[color_to_idx[color]] = 1
        item_label[item_to_idx[item]] = 1
        return img, torch.cat((color_label, item_label))

dataset = MultiLabelDataset(root=dataset_path, transform=transform)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
##
class MultiLabelCNN(nn.Module):
    def __init__(self, num_colors, num_items):
        super(MultiLabelCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * (IMG_SIZE // 4) * (IMG_SIZE // 4), 128)
        self.bn_fc = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, num_colors + num_items)
        self.dropout = nn.Dropout(0.3)
    
    def forward(self, x):
        x = self.pool(torch.relu(self.bn1(self.conv1(x))))
        x = self.pool(torch.relu(self.bn2(self.conv2(x))))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.bn_fc(self.fc1(x)))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc2(x))
        return x
##
model = MultiLabelCNN(len(color_labels), len(item_labels))
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

def train(model, train_loader, criterion, optimizer, epochs):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")

train(model, train_loader, criterion, optimizer, EPOCHS)
##
def evaluate(model, loader):
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for images, labels in loader:
            outputs = model(images)
            preds = (outputs > 0.5).float()
            all_preds.append(preds.cpu().numpy())
            all_labels.append(labels.cpu().numpy())
    all_preds = np.vstack(all_preds)
    all_labels = np.vstack(all_labels)
    f1 = f1_score(all_labels, all_preds, average='macro')
    print(f"F1 Score: {f1:.4f}")

evaluate(model, train_loader)
evaluate(model, test_loader)"""},}

themes = '''
Регрессия
1. gold
2. с разной архитектурой
3. с разными оптимизаторами

Классификация 
4. bank несбалансированные классы (модифицировать функцию потерь) - сравнить
5. bank dropout сравнение
6. bank разные оптимизаторы
7. bank разные модели

CNN
8. chars случайные преобразования аугментация
9. handwritten_eng f1 micro и ранняя остановка
10. sign_language зависимость метрики от количества сверток
11. sign_language похожие изображения
12. sign_language сравнение с PCA
13. clothes_multi одновременно тип одежды и цвет
'''
m_to_dict = {0: 'theory', 1: 'code'}

import pyperclip as pc


def info():
    '''
    Добавляет в буфер обмена список тем, по которым потом обращаться при помощи функции get(n, m), где n - номер темы, m = 0 => теория, m = 1 => практика
    '''
    pc.copy(themes)


def info_cl():
    '''
    Создает класс, в документации которого список тем, по которым потом обращаться при помощи функции get(n, m), где n - номер темы, m = 0 => теория, m = 1 => практика
    '''

    class sol():
        __doc__ = themes

    return sol()


def get(n, m: int):
    '''
    Добавляет в буфер обмена ответ по теме (n - номер темы; m = 0 => теория, m = 1 => практика)
    '''
    if 0 < n < 37:
        if -1 < m < 2:
            pc.copy(questions[n][m_to_dict[m]])
        else:
            pc.copy('Неправильный выбор типа задания')
    else:
        pc.copy('Неправильный выбор номера темы')


def get_cl(n, m):
    '''
    Создает объект класса, в документации (shift + tab) которого лежит ответ по теме (n - номер темы; m = 0 => теория, m = 1 => практика)
    '''

    class sol:
        def __init__(self, n, m):
            self.n = n
            self.m = m
            self.doc = questions[self.n][m_to_dict[self.m]]

        @property
        def __doc__(self):
            return self.doc

    return sol(n, m)