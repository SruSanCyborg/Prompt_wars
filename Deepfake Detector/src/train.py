import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import kagglehub
import argparse
from tqdm import tqdm
import matplotlib.pyplot as plt
print(torch.cuda.is_available())
# Set up argument parsing
parser = argparse.ArgumentParser(description='Deepfake Detection Model Training')
parser.add_argument('--epochs', type=int, default=10, help='Number of training epochs')
parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
parser.add_argument('--model_name', type=str, default='resnet18', choices=['resnet18', 'efficientnet'], help='Model architecture')
args = parser.parse_args()

# Dataset class
class DeepfakeDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.samples = []
        
        # Assuming structure: root_dir/real/ and root_dir/fake/
        for label, folder in enumerate(['real', 'fake']):
            folder_path = os.path.join(root_dir, folder)
            if os.path.exists(folder_path):  # Check if folder exists
                for img_name in os.listdir(folder_path):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        self.samples.append((os.path.join(folder_path, img_name), label))
        
        print(f"Loaded {len(self.samples)} images from {self.root_dir}")
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        try:
            image = Image.open(img_path).convert('RGB')
            if self.transform:
                image = self.transform(image)
            return image, label
        except Exception as e:
            print(f"Error loading image {img_path}: {str(e)}")
            return None, None

# Download dataset from Kaggle
def download_dataset():
    try:
        print("Downloading dataset from Kaggle...")
        dataset_path = kagglehub.dataset_download("manjilkarki/deepfake-and-real-images")
        print(f"Dataset downloaded to: {dataset_path}")
        return dataset_path
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        return None

# Initialize model
def initialize_model(model_name='resnet18'):
    if model_name == 'resnet18':
        model = models.resnet18(pretrained=True)
        num_features = model.fc.in_features
        model.fc = nn.Sequential(
            nn.Linear(num_features, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 2)  # [real, fake]
        )
    elif model_name == 'efficientnet':
        model = models.efficientnet_b0(pretrained=True)
        num_features = model.classifier[1].in_features
        model.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(num_features, 2)
        )
    return model

# Training function
def train_model(model, dataloaders, criterion, optimizer, num_epochs=10):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    
    train_loss_history = []
    val_loss_history = []
    train_acc_history = []
    val_acc_history = []
    
    for epoch in range(num_epochs):
        print(f'Epoch {epoch+1}/{num_epochs}')
        print('-' * 10)
        
        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode
                
            running_loss = 0.0
            running_corrects = 0
            
            # Iterate over data
            for inputs, labels in tqdm(dataloaders[phase]):
                inputs = inputs.to(device)
                labels = labels.to(device)
                
                # Zero the parameter gradients
                optimizer.zero_grad()
                
                # Forward pass
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)
                    
                    # Backward pass + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()
                
                # Statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
                
            epoch_loss = running_loss / len(dataloaders[phase].dataset)
            epoch_acc = running_corrects.double() / len(dataloaders[phase].dataset)
            
            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')
            
            # Record history
            if phase == 'train':
                train_loss_history.append(epoch_loss)
                train_acc_history.append(epoch_acc.item() if hasattr(epoch_acc, "item") else float(epoch_acc))
            else:
                val_loss_history.append(epoch_loss)
                val_acc_history.append(epoch_acc.item() if hasattr(epoch_acc, "item") else float(epoch_acc))
    
    # Plot training history
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(train_loss_history, label='Train Loss')
    plt.plot(val_loss_history, label='Val Loss')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(train_acc_history, label='Train Acc')
    plt.plot(val_acc_history, label='Val Acc')
    plt.legend()
    
    plt.savefig('training_history.png')
    plt.close()
    
    return model

def main():
    # Download dataset
    dataset_path = download_dataset()
    if dataset_path is None:
        print("Using local dataset instead")
        dataset_path = "src/data"  # Fallback to local data directory
    
    print("Dataset path:", dataset_path)
    print("Contents:", os.listdir(dataset_path))
    
    dataset_path = os.path.join(dataset_path, 'Dataset')
    print("New dataset path:", dataset_path)
    print("New contents:", os.listdir(dataset_path))

    # Data augmentation and normalization
    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ]),
    }
    
    # Create datasets
    image_datasets = {
        'train': DeepfakeDataset(os.path.join(dataset_path, 'train'), data_transforms['train']),
        'val': DeepfakeDataset(os.path.join(dataset_path, 'val'), data_transforms['val'])
    }
    
    # Filter out None values (failed image loads)
    for phase in ['train', 'val']:
        image_datasets[phase].samples = [s for s in image_datasets[phase].samples if s[1] is not None]
    
    # Create dataloaders
    dataloaders = {
        'train': DataLoader(image_datasets['train'], batch_size=args.batch_size, shuffle=True, num_workers=4),
        'val': DataLoader(image_datasets['val'], batch_size=args.batch_size, shuffle=False, num_workers=4)
    }
    
    print(f"Train dataset size: {len(image_datasets['train'])}")
    print(f"Validation dataset size: {len(image_datasets['val'])}")
    
    # Initialize model
    model = initialize_model(args.model_name)
    print(f"Using {args.model_name} architecture")
    
    # Set up training
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    
    # Train the model
    model = train_model(
        model, 
        dataloaders, 
        criterion, 
        optimizer, 
        num_epochs=args.epochs
    )
    
    # Save the model
    os.makedirs('saved_models', exist_ok=True)
    model_path = f"saved_models/deepfake_{args.model_name}.pth"
    torch.save(model.state_dict(), model_path)
    print(f"Model saved to {model_path}")

    print(f"Train samples: {len(image_datasets['train'])}")
    print(f"Val samples: {len(image_datasets['val'])}")
    if len(image_datasets['train']) == 0 or len(image_datasets['val']) == 0:
        print("ERROR: No images found in train or val dataset. Check your dataset structure!")
        return

if __name__ == '__main__':
    main()
