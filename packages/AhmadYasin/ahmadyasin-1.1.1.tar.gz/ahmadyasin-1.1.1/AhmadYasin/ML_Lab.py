# ML_Lab
def get_ml_code():
    ml_code = """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from xgboost import XGBClassifier
    from catboost import CatBoostClassifier
    from sklearn.decomposition import PCA, TruncatedSVD
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    # 1. Load Dataset
    def load_dataset(file_path):
        #Load dataset from a file path.
        data = pd.read_csv(file_path)
        print(f"Dataset Shape: {data.shape}")
        return data

    # 2. Perform EDA
    def perform_eda(data):
        #Perform Exploratory Data Analysis on the dataset.
        print("\n--- Dataset Info ---")
        print(data.info())
        print("\n--- Dataset Description ---")
        print(data.describe())
        print("\n--- Missing Values ---")
        print(data.isnull().sum())

        # Visualizations
        print("\n--- Visualizing Dataset ---")
        plt.figure(figsize=(12, 6))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x=data.columns[-1])
        plt.title("Target Variable Distribution")
        plt.show()

        for col in data.select_dtypes(include=["float64", "int64"]).columns[:-1]:
            plt.figure(figsize=(6, 4))
            sns.histplot(data[col], kde=True, bins=30)
            plt.title(f"Distribution of {col}")
            plt.show()

        for col in data.select_dtypes(include=["object"]).columns:
            plt.figure(figsize=(6, 4))
            sns.countplot(data=data, x=col)
            plt.title(f"Count of {col}")
            plt.show()

    # 3. Preprocessing and PCA/SVD
    def preprocess_and_reduce(data, target_col):
        #Preprocess the dataset and apply PCA and SVD.
        X = data.drop(columns=[target_col])
        y = data[target_col]
        
        # One-hot encode categorical variables if any
        X = pd.get_dummies(X, drop_first=True)
        
        # PCA
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)
        print("\nPCA Explained Variance Ratio:", pca.explained_variance_ratio_)
        
        plt.figure(figsize=(8, 6))
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis")
        plt.title("PCA: First Two Components")
        plt.colorbar(label="Target")
        plt.show()

        # SVD
        svd = TruncatedSVD(n_components=2)
        X_svd = svd.fit_transform(X)
        print("\nSVD Explained Variance Ratio:", svd.explained_variance_ratio_)
        
        plt.figure(figsize=(8, 6))
        plt.scatter(X_svd[:, 0], X_svd[:, 1], c=y, cmap="plasma")
        plt.title("SVD: First Two Components")
        plt.colorbar(label="Target")
        plt.show()

        return X, y

    # 4. Train Models
    def train_models(X, y):
        #Train multiple models and evaluate them.
        models = {
            "Random Forest": RandomForestClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss"),
            "CatBoost": CatBoostClassifier(verbose=0)
        }
        
        results = {}
        for name, model in models.items():
            print(f"\n--- Training {name} ---")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            results[name] = acc
            
            print(f"{name} Accuracy: {acc:.4f}")
            print("Classification Report:\n", classification_report(y_test, y_pred))
            
            # Confusion Matrix
            cm = confusion_matrix(y_test, y_pred)
            plt.figure(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
            plt.title(f"Confusion Matrix - {name}")
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            plt.show()
            
        return results

    # 5. Display Results
    def display_results(results):
        #Display and visualize results.
        print("\n--- Model Performance ---")
        for model, accuracy in results.items():
            print(f"{model}: {accuracy:.4f}")
        
        # Bar Plot for Model Performance
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(results.keys()), y=list(results.values()), palette="viridis")
        plt.title("Model Performance")
        plt.xlabel("Models")
        plt.ylabel("Accuracy")
        plt.ylim(0, 1)
        plt.show()

    # Main Execution
    if __name__ == "__main__":
        # Path to your dataset
        file_path = "path_to_your_dataset.csv"  # Replace with your dataset file path
        
        # Load Dataset
        data = load_dataset(file_path)
        
        # Perform EDA
        perform_eda(data)
        
        # Preprocess and Apply PCA/SVD
        target_col = data.columns[-1]  # Assuming the last column is the target
        X, y = preprocess_and_reduce(data, target_col)
        
        # Train Models
        results = train_models(X, y)
        
        # Display Results
        display_results(results)
    """
    return ml_code

def get_ann_Scratch_code():
    
    ann_code = """
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn import datasets
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import OneHotEncoder, StandardScaler

        # Activation function and its derivative
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        def sigmoid_derivative(x):
            return x * (1 - x)

        # Train ANN with only input and output layer
        def train_ann_no_hidden(X, y, input_size, output_size, epochs=10000, learning_rate=0.1):
            np.random.seed(42)
            W = np.random.randn(input_size, output_size)
            b = np.zeros((1, output_size))
            
            error_list = []
            
            for epoch in range(epochs):
                # Forward propagation
                Z = np.dot(X, W) + b
                A = sigmoid(Z)
                
                # Compute error
                error = y - A
                error_list.append(np.mean(np.abs(error)))
                
                # Backpropagation
                dA = error * sigmoid_derivative(A)
                dW = np.dot(X.T, dA)
                db = np.sum(dA, axis=0, keepdims=True)
                
                # Update weights and biases
                W += learning_rate * dW
                b += learning_rate * db
                
                if epoch % 1000 == 0:
                    print(f'Epoch {epoch}, Error: {error_list[-1]}')
            
            return W, b, error_list

        # Train ANN with input, hidden, and output layer
        def train_ann_with_hidden(X, y, input_size, hidden_size, output_size, epochs=10000, learning_rate=0.1):
            np.random.seed(42)
            W1 = np.random.randn(input_size, hidden_size)
            b1 = np.zeros((1, hidden_size))
            W2 = np.random.randn(hidden_size, output_size)
            b2 = np.zeros((1, output_size))
            
            error_list = []
            
            for epoch in range(epochs):
                # Forward propagation
                Z1 = np.dot(X, W1) + b1
                A1 = sigmoid(Z1)
                Z2 = np.dot(A1, W2) + b2
                A2 = sigmoid(Z2)
                
                # Compute error
                error = y - A2
                error_list.append(np.mean(np.abs(error)))
                
                # Backpropagation
                dA2 = error * sigmoid_derivative(A2)
                dW2 = np.dot(A1.T, dA2)
                db2 = np.sum(dA2, axis=0, keepdims=True)
                
                dA1 = np.dot(dA2, W2.T) * sigmoid_derivative(A1)
                dW1 = np.dot(X.T, dA1)
                db1 = np.sum(dA1, axis=0, keepdims=True)
                
                # Update weights and biases
                W1 += learning_rate * dW1
                b1 += learning_rate * db1
                W2 += learning_rate * dW2
                b2 += learning_rate * db2
                
                if epoch % 1000 == 0:
                    print(f'Epoch {epoch}, Error: {error_list[-1]}')
            
            return W1, b1, W2, b2, error_list

        # Load and preprocess the Iris dataset
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target.reshape(-1, 1)

        # One-hot encode the target values
        encoder = OneHotEncoder(sparse=False)
        y = encoder.fit_transform(y)

        # Normalize the features
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Split dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train and test both models
        input_size = X_train.shape[1]
        output_size = y_train.shape[1]

        # Train simple ANN without hidden layer
        W, b, error_list_no_hidden = train_ann_no_hidden(X_train, y_train, input_size, output_size)

        # Train ANN with hidden layer
        hidden_size = 5
        W1, b1, W2, b2, error_list_with_hidden = train_ann_with_hidden(X_train, y_train, input_size, hidden_size, output_size)

        # Plot error reduction for both models
        plt.plot(error_list_no_hidden, label='No Hidden Layer')
        plt.plot(error_list_with_hidden, label='With Hidden Layer')
        plt.xlabel('Epochs')
        plt.ylabel('Mean Absolute Error')
        plt.title('Training Error Reduction')
        plt.legend()
        plt.show()

        # Evaluate both models
        # Model without hidden layer
        Z = np.dot(X_test, W) + b
        A = sigmoid(Z)
        y_pred_no_hidden = np.argmax(A, axis=1)
        y_true = np.argmax(y_test, axis=1)
        accuracy_no_hidden = np.mean(y_pred_no_hidden == y_true) * 100
        print(f'Accuracy without hidden layer: {accuracy_no_hidden:.2f}%')

        # Model with hidden layer
        Z1 = np.dot(X_test, W1) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = sigmoid(Z2)
        y_pred_with_hidden = np.argmax(A2, axis=1)
        accuracy_with_hidden = np.mean(y_pred_with_hidden == y_true) * 100
        print(f'Accuracy with hidden layer: {accuracy_with_hidden:.2f}%')

    """
    return ann_code

def DBScan_AGlomrative():
    code = """
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.spatial.distance import euclidean

    # Generate sample dataset
    np.random.seed(42)
    X = np.vstack((np.random.randn(50, 2) * 0.3 + [1, 1],
                np.random.randn(50, 2) * 0.3 + [3, 3],
                np.random.randn(50, 2) * 0.3 + [6, 1]))

    ### DBSCAN Implementation from Scratch ###
    def dbscan(X, eps, min_samples):
        labels = np.full(X.shape[0], -1)  # -1 means unclassified
        cluster_id = 0
        
        def region_query(point_idx):
            #Find neighbors within eps radius
            return [i for i in range(len(X)) if euclidean(X[point_idx], X[i]) <= eps]
        
        def expand_cluster(point_idx, neighbors):
            #Expand the cluster recursively
            labels[point_idx] = cluster_id
            i = 0
            while i < len(neighbors):
                neighbor = neighbors[i]
                if labels[neighbor] == -1:  # If unclassified
                    labels[neighbor] = cluster_id
                    new_neighbors = region_query(neighbor)
                    if len(new_neighbors) >= min_samples:
                        neighbors.extend(new_neighbors)  # Expand neighbors
                i += 1
        
        for i in range(len(X)):
            if labels[i] == -1:  # If unclassified
                neighbors = region_query(i)
                if len(neighbors) >= min_samples:
                    expand_cluster(i, neighbors)
                    cluster_id += 1
        
        return labels

        dbscan_labels = dbscan(X, eps=0.5, min_samples=5)

        # Plot DBSCAN Results
        plt.scatter(X[:, 0], X[:, 1], c=dbscan_labels, cmap='viridis', edgecolors='k')
        plt.title("DBSCAN Clustering")
        plt.show()

        ### Hierarchical Agglomerative Clustering from Scratch ###
        def hierarchical_clustering(X, num_clusters):
            clusters = {i: [i] for i in range(len(X))}  # Initialize each point as a cluster
            
            def find_closest_clusters():
                #Find the two closest clusters based on Euclidean distance
                min_dist = float('inf')
                closest_pair = None
                for i in clusters:
                    for j in clusters:
                        if i != j:
                            dist = np.mean([euclidean(X[p1], X[p2]) for p1 in clusters[i] for p2 in clusters[j]])
                            if dist < min_dist:
                                min_dist = dist
                                closest_pair = (i, j)
                return closest_pair
            
            while len(clusters) > num_clusters:
                c1, c2 = find_closest_clusters()
                clusters[c1].extend(clusters[c2])
                del clusters[c2]  # Merge clusters
            
            labels = np.zeros(len(X))
            for cluster_id, points in enumerate(clusters.values()):
                for p in points:
                    labels[p] = cluster_id
            return labels

        hierarchical_labels = hierarchical_clustering(X, num_clusters=3)

        # Plot Hierarchical Clustering Results
        plt.scatter(X[:, 0], X[:, 1], c=hierarchical_labels, cmap='viridis', edgecolors='k')
        plt.title("Hierarchical Clustering")
        plt.show()
    """
    return code
    