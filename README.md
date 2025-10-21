## Sentiment Analysis on HappyDB Dataset

### Dataset Source
This project uses the **HappyDB dataset** from [Megagon Labs](https://github.com/megagonlabs/HappyDB/tree/master), a corpus of 100,000+ crowd-sourced happy moments collected from Amazon Mechanical Turk workers.

**Dataset Citation:**
```
Akari Asai, Sara Evensen, Behzad Golshan, Alon Halevy, Vivian Li, Andrei Lopatenko, 
Daniela Stepanov, Yoshihiko Suhara, Wang-Chiew Tan, Yinzhan Xu, 
"HappyDB: A Corpus of 100,000 Crowdsourced Happy Moments", LREC '18, May 2018.
```

### Project Overview
+ **Project Title:** Sentiment Analysis on HappyDB: Gender-based Emotional Expression Across Age Groups
+ **Researcher:** Zichen Zhao
+ **Dataset:** [HappyDB GitHub Repository](https://github.com/megagonlabs/HappyDB/tree/master)

### Research Objectives
1. **Data Preprocessing:** Remove stopwords and normalize age groups
2. **Demographic Filtering:** Focus on US participants and analyze by gender
3. **Data Integration:** Merge demographic and happy moments datasets
4. **Sentiment Analysis:** Calculate sentiment word frequency percentages by gender
5. **Word Frequency Analysis:** Extract and analyze sentiment word patterns
6. **Visualization:** Generate comparative charts showing word usage by age and gender
7. **Insights Generation:** Identify patterns in emotional expression across demographics

### Dataset Statistics
- **Total Happy Moments:** 100,922
- **Distinct Users:** 10,843  
- **US Participants:** 79,063
- **Male Participants:** 44,259
- **Female Participants:** 34,100
- **Average Words per Happy Moment:** 19.66

### Key Findings
This sentiment analysis reveals significant patterns in emotional expression across age and gender demographics in the United States. The analysis leverages the comprehensive HappyDB dataset to identify nuanced linguistic patterns in how different demographic groups express happiness and sentiment.
1. Age-Related Patterns in Word Usage: The analysis identifies age 40 as a pivotal point marking significant shifts in word usage frequencies between younger and older cohorts. This age milestone delineates differing linguistic expressions of sentiment, suggesting a potential influence of life stage on sentiment expression.
2. Gender Disparities in Sentiment Words Pre-40: Prior to the age of 40, there is a pronounced disparity in the sentiment words predominantly used by males and females. Males are more likely to use words such as "amazed," "anger," "appreciative," "attracted," "blind," "chances," "comedian," "cutting," and "definite." Conversely, females frequently use words like "comforter," "cried," "desperate," "determination," and "kiss." This disparity highlights a gendered difference in expressing sentiments, with males and females gravitating towards different lexical choices to articulate their feelings and experiences.
3. Post-40 Surge in Male Word Usage: Among males, there is a notable increase in the usage of specific words after the age of 40, including "delay," "delectable," "delight," "died," "disappointed," "efficient," "energetic," "errors," and "frustration." This surge reflects a shift in sentiment expression that may be associated with mid-life experiences and perspectives.
4. Post-40 Surge in Female Word Usage: Similarly, females exhibit a distinct increase in the use of certain words post-40, such as "disorder," "dream," "ease," "giggling," "grace," "hugged," "limited," and "lonely." This change suggests a nuanced evolution in how females articulate sentiments as they transition into later life stages, possibly reflecting differing emotional landscapes and life experiences.
These findings underscore the complexity of sentiment expression as influenced by gender and age, pointing to the importance of considering these factors in linguistic and psychological research. Further analysis is required to delve deeper into the underlying causes and implications of these patterns, which may inform interventions and supports tailored to different demographic groups.

### Methodology
- **Sentiment Analysis:** VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer
- **Text Preprocessing:** Stopword removal, lowercase conversion, tokenization
- **Age Normalization:** Grouped participants into age ranges for analysis
- **Gender Analysis:** Separate processing for male and female participants
- **Visualization:** Comparative bar charts showing word frequency by age and gender

### Project Structure
```
Sentiment-Analysis-on-HappyDB/
├── data/                    # Dataset files (ignored by git)
│   ├── cleaned_hm.csv      # Happy moments data
│   └── demographic.csv     # Demographic information
├── doc/                     # Documentation
│   └── main.ipynb          # Main analysis notebook
├── figs/                    # Generated visualizations
│   └── word_frequency_compare/  # Comparison charts
├── output/                  # Processed data outputs
│   ├── male_data.csv       # Male participant data
│   └── female_data.csv     # Female participant data
├── lib/                     # Custom functions
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Sentiment-Analysis-on-HappyDB
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download HappyDB dataset:**
   ```bash
   git clone https://github.com/megagonlabs/HappyDB.git
   # Copy data files to ./data/ directory
   ```

4. **Run the analysis:**
   ```bash
   jupyter notebook doc/main.ipynb
   ```

### Strengths
- **Gender-Specific Insights:** Reveals how gender influences sentiment expression and communication styles
- **Life Stage Analysis:** Identifies age 40 as a pivotal point for emotional expression changes
- **Cultural Context:** Provides US-specific insights into emotional expression patterns
- **Comprehensive Dataset:** Leverages large-scale crowd-sourced data (100K+ happy moments)

### Limitations
- **Context Sensitivity:** Word-based analysis may miss contextual nuances in sentiment expression
- **Cultural Scope:** US-focused analysis limits global generalizability
- **Qualitative Aspects:** May miss emotional intensity and complexity not captured by word frequency
- **Temporal Factors:** Cross-sectional data may not capture longitudinal emotional development

### Citation
If you use this analysis or the HappyDB dataset in your research, please cite:

**HappyDB Dataset:**
```
Akari Asai, Sara Evensen, Behzad Golshan, Alon Halevy, Vivian Li, Andrei Lopatenko, 
Daniela Stepanov, Yoshihiko Suhara, Wang-Chiew Tan, Yinzhan Xu, 
"HappyDB: A Corpus of 100,000 Crowdsourced Happy Moments", LREC '18, May 2018.
```

### Contact
For questions about this analysis, please contact: zz3119@columbia.edu

For questions about the HappyDB dataset, please contact: happydb@recruit.ai

### License
This project follows the same license terms as the original HappyDB dataset. Please refer to the [HappyDB repository](https://github.com/megagonlabs/HappyDB/tree/master) for licensing information.
