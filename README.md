<h1 align="center">📊 Insurance Cost Predictor</h1>
<h3 align="center">End-to-End Machine Learning Regression Pipeline with Deployment</h3>

<p align="center">
  <a href="https://huggingface.co/spaces/Indrajit147/insurance-cost-predictor">
    <img src="https://img.shields.io/badge/Live-Demo-yellow?logo=huggingface" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.4-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>
This project predicts individual medical insurance charges using demographic and health-related features.
It demonstrates a complete <b>end-to-end machine learning workflow</b>, including:
</p>

<ul>
  <li>Data preprocessing</li>
  <li>Feature engineering</li>
  <li>Model selection</li>
  <li>Cross-validation</li>
  <li>Hyperparameter tuning</li>
  <li>Pipeline construction</li>
  <li>Model serialization</li>
  <li>Web deployment using Gradio</li>
  <li>Cloud hosting via Hugging Face Spaces</li>
</ul>

<p>
The final model explains nearly <b>90% of variance (R² ≈ 0.90)</b> in insurance charges.
</p>

<hr>

<h2>📂 Dataset</h2>

<p><b>Source:</b> Kaggle – Medical Cost Personal Dataset</p>
<p>
<b>Link:</b> 
<a href="https://www.kaggle.com/datasets/mirichoi0218/insurance" target="_blank">
https://www.kaggle.com/datasets/mirichoi0218/insurance
</a>
</p>

<h3>Features</h3>
<ul>
  <li>age</li>
  <li>sex</li>
  <li>bmi</li>
  <li>children</li>
  <li>smoker</li>
  <li>region</li>
  <li>charges (target)</li>
</ul>

<hr>

<h2>🧹 Data Preprocessing</h2>

<ul>
  <li>Standardized column names</li>
  <li>Removed duplicate entries</li>
  <li>Cleaned categorical text values</li>
  <li>Handled missing values using imputation</li>
  <li>Outlier treatment via IQR clipping</li>
  <li>Feature engineering:
    <ul>
      <li>BMI category grouping</li>
      <li>Age squared term</li>
      <li>BMI × Smoker interaction feature</li>
    </ul>
  </li>
  <li>Target transformation using log scaling (log1p)</li>
</ul>

<p>
All preprocessing steps were integrated into a <b>scikit-learn Pipeline</b> to prevent data leakage.
</p>

<hr>

<h2>🤖 Model Selection</h2>

<p><b>Primary Model:</b> HistGradientBoostingRegressor</p>

<p>
Chosen because:
</p>

<ul>
  <li>Handles nonlinear relationships effectively</li>
  <li>Strong performance on tabular datasets</li>
  <li>Robust to feature interactions</li>
  <li>Efficient and scalable</li>
</ul>

<hr>

<h2>📈 Model Evaluation</h2>

<h3>Cross-Validation (5-Fold)</h3>
<ul>
  <li><b>CV R²:</b> 0.8266 ± 0.0264</li>
  <li><b>CV RMSE:</b> 4825.86 ± 149.82</li>
</ul>

<h3>Test Set Performance</h3>
<ul>
  <li><b>R²:</b> 0.8989</li>
  <li><b>RMSE:</b> 4309.19</li>
  <li><b>MAE:</b> 2048.26</li>
</ul>

<p>
The model generalizes well with no signs of overfitting.
</p>

<hr>

<h2>⚙️ Hyperparameter Tuning</h2>

<p>
RandomizedSearchCV was used to tune:
</p>

<ul>
  <li>max_depth</li>
  <li>learning_rate</li>
  <li>max_iter</li>
  <li>min_samples_leaf</li>
  <li>l2_regularization</li>
</ul>

<p>
The best estimator was selected based on cross-validated RMSE.
</p>

<hr>

<h2>🌐 Live Deployment</h2>

<p>
The trained model was serialized using <b>joblib</b> and deployed using:
</p>

<ul>
  <li><b>Gradio</b> (web interface)</li>
  <li><b>Hugging Face Spaces</b> (cloud hosting)</li>
</ul>

<p>
<b>Live Demo:</b><br>
👉 <a href="https://huggingface.co/spaces/Indrajit147/insurance-cost-predictor" target="_blank">
https://huggingface.co/spaces/Indrajit147/insurance-cost-predictor
</a>
</p>

<hr>

<h2>🛠️ How to Run Locally</h2>

<pre>
git clone https://github.com/Indrajit147/insurance-cost-predictor.git
cd insurance-cost-predictor
pip install -r requirements.txt
python app.py
</pre>

<p>Then open:</p>

<pre>
http://localhost:7860
</pre>

<hr>

<h2>📁 Repository Structure</h2>

<pre>
insurance-cost-predictor/
│
├── Insurance_Cost_Predictor.ipynb
├── app.py
├── insurance_best_pipeline.joblib
├── insurance.csv
├── requirements.txt
├── LICENSE
└── README.md
</pre>

<hr>

<h2>🧠 Key Learnings</h2>

<ul>
  <li>Building leakage-free ML pipelines</li>
  <li>Feature interaction engineering</li>
  <li>Proper cross-validation strategy</li>
  <li>Model persistence challenges across Python versions</li>
  <li>Production deployment using Hugging Face Spaces</li>
  <li>Environment consistency management</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Indrajit</b><br>
Machine Learning & AI Enthusiast<br>
Electronics & Communication Engineering<br>
ECE, KUET
</p>
