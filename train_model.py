import pickle
from sklearn.linear_model import LinearRegression
# 1. ట్రైనింగ్ డేటా: X = [Square Feet, Number of Rooms], y = ఇంటి ధర (రూపాయల్లో)

X = [(1000, 2),
     (1200, 3),
     (1500, 3),
     (1800, 4),
     (2200, 4)
     ]
y = [4000000, 4800000, 6200000, 7500000, 9500000]


# 2. మెషిన్ లెర్నింగ్ మోడల్‌ని ట్రైన్ చేస్తున్నాం

model = LinearRegression()
model.fit(X, y)

# 3. ట్రైన్ అయిన మోడల్‌ని 'house_model.pkl' అనే ఫైల్ లాగా సేవ్ చేస్తున్నాం

with open ("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("SUCCESS: house_model.pkl file created successfully!")