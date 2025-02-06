# My EDA Helper - Boost Your Exploratory Data Analysis Process! 🚀

[![PyPI Version](https://img.shields.io/pypi/v/my_eda_helper?color=blue)](https://pypi.org/project/my_eda_helper/)

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](https://github.com/shemanto27/eda-helper-py/pulls)

**EDA Helper** is a Python package designed to streamline your Exploratory Data Analysis (EDA) process. It provides a collection of helper functions to quickly analyze, visualize, and summarize datasets. Whether you're working with numeric, categorical, or datetime data, this package has you covered!

---

## Credits 🙏

This package is inspired by the brilliant work of [@MisbahullahSheriff](https://github.com/MisbahullahSheriff). The original EDA helper functions were created by him, and I have extended and organized them for easier use. Additional functions and improvements have been added by me ([@shemanto27](https://github.com/shemanto27)).

---

## Installation 📦

You can install the package via `pip`:

```bash
pip install my_eda_helper
```

For Google Colab users, install it directly in your notebook:
```bash
!pip install my_eda_helper
```

## Usage 🛠️

### 1. Import the Package
```python
import my_eda_helper as eda
```

### 2. High-Level Analysis

#### Missing Data

**Find Missing Values:**
```python
missing_data = eda.missing_info(df)
print(missing_data)
```

**Plot Missing Data:**
```python
eda.plot_missing_info(df)
```

#### Correlation Analysis

**Numeric Features (Pearson/Spearman):**
```python
eda.correlation_heatmap(df)
```

**Categorical Features (Cramer's V):**
```python
eda.cramersV_heatmap(df)
```

#### Pair Plots
```python
eda.pair_plots(df)
```

### 3. Detailed Analysis

#### Numeric Features

**Summary:**
```python
eda.num_summary(df, "Age")
```

**Univariate Plots:**
```python
eda.num_univar_plots(df, "Fare")
```

**Bivariate Plots:**
```python
eda.num_bivar_plots(df, "Age", "Fare")
```

#### Categorical Features

**Summary:**
```python
eda.cat_summary(df, "Sex")
```

**Univariate Plots:**
```python
eda.cat_univar_plots(df, "Embarked")
```

**Bivariate Plots:**
```python
eda.num_cat_bivar_plots(df, "Fare", "Sex")
```

### Hypothesis Testing

**Numeric vs Numeric:**
```python
eda.num_num_hyp_testing(df, "Age", "Fare")
```

**Numeric vs Categorical:**
```python
eda.num_cat_hyp_testing(df, "Fare", "Sex")
```

**Categorical vs Categorical:**
```python
eda.hyp_cat_cat(df, "Sex", "Survived")
```

---

## Contributing 🤝
Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to:

1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:  
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

Please ensure your code follows the project's style and includes appropriate tests.

---

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Support 💬
If you have any questions, suggestions, or issues, please open an issue on the GitHub repository.

**Happy EDA! 🎉**
