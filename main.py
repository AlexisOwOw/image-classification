from feature_extractor import FeatureExtractor
import numpy as np
from gaussian_naive_bayes import GaussianNaiveBayes
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import _criterion
#from decision_tree_classifier import DecitionTreeClassifier, DecitionTreeNode


def main():
    extractor = FeatureExtractor()
    train_features_pca, train_labels, test_features_pca, test_labels = extractor.process()

    train_features_pca = np.array(train_features_pca)
    test_features_pca = np.array(test_features_pca)
    train_labels = train_labels.detach().cpu().numpy()
    test_labels = test_labels.detach().cpu().numpy()

    print("\nStarting the training process (Custom GNB)...")
    gnb = GaussianNaiveBayes()
    gnb.train_model(train_features_pca, train_labels)
    test_predictions = gnb.predict(test_features_pca)
    test_predictions = np.array(test_predictions)
    accuracy = np.mean(test_predictions == test_labels)
    print("Custom Naive Bayes Accuracy:", accuracy)

    print("\nStarting the training process (Scikit GNB)...")
    sklearn_gnb = GaussianNB()
    sklearn_gnb.fit(train_features_pca, train_labels)
    sklearn_test_predictions = sklearn_gnb.predict(test_features_pca)
    sklearn_accuracy = accuracy_score(test_labels, sklearn_test_predictions)
    print("Scikit-learn Naive Bayes Accuracy:", sklearn_accuracy)

    print("\nStarting the training process (Custom DTC)...")

    print("\nStarting the training process (Scikit DTC)...")
    sklearn_dtc = DecisionTreeClassifier()
    sklearn_dtc.fit(train_features_pca, train_labels)
    sklearn_dtc_test_predictions = sklearn_dtc.predict(test_features_pca)
    sklearn_dtc_accuracy = accuracy_score(test_labels, sklearn_dtc_test_predictions)
    print("Scikit-learn Decision Tree Accuracy: ", sklearn_dtc_accuracy)


if __name__ == "__main__":
    main()
