from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "Siparişim gelmedi",
    "Ödeme yaptım ama gözükmüyor",
    "Hesabıma giriş yapamıyorum"
]

labels = ["delivery", "payment", "account"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

test = ["Siparişim çok geç kaldı"]
X_test = vectorizer.transform(test)

print(model.predict(X_test))
