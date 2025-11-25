# Project Flow Review & Analysis Variations

## Current Flow Overview

### 1. **Data Pipeline**
```
Raw Data → Clean (remove NaN) → Preprocess (binarize) → Calculate Parameters → Compute Probabilities → Output Results
```

### 2. **Current Analysis**
- **Preprocessing**: 3 binarization methods (25th percentile, average, 10th percentile)
- **Model**: Naive Bayes with 4 factors (H, S, A, P) predicting E
- **Queries**:
  - P(E|H,S,A,P) with all factors positive/negative
  - P(E|factor) for individual factors
  - Best/worst predictor identification

---

## Suggested Analysis Variations

### 1. **Additional Binarization Thresholds**
**Current**: 25th percentile (0.75), average, 10th percentile (0.9)

**Add**:
- **Median (50th percentile)**: More balanced split
- **Custom percentiles**: 5th, 15th, 30th, 40th, 60th, 70th, 80th, 85th, 95th
- **Standard deviation based**: mean ± 0.5σ, mean ± 1σ
- **Equal frequency bins**: Split into equal-sized groups

**Implementation**: Add more `ProcessingType` enum values

---

### 2. **Factor Interaction Analysis**
**Current**: Only looks at individual factors or all factors together

**Add**:
- **Pairwise combinations**: P(E|H=1, S=1), P(E|A=1, P=1), etc.
- **Three-factor combinations**: P(E|H=1, S=1, A=1), etc.
- **Factor importance ranking**: Which pairs/triplets are most predictive?
- **Interaction strength**: Compare P(E|A,B) vs P(E|A) × P(E|B) to detect interactions

**Implementation**: New function `calculate_pairwise()` and `calculate_triplets()`

---

### 3. **Sensitivity Analysis**
**Purpose**: Understand how robust predictions are to changes in evidence

**Variations**:
- **Single factor flip**: P(E|H=1,S=1,A=1,P=0) vs P(E|H=1,S=1,A=1,P=1)
- **Factor importance**: Calculate how much probability changes when each factor flips
- **Threshold sensitivity**: Compare results across different binarization thresholds
- **Missing data simulation**: What if one factor is unknown? Use marginal probabilities

**Implementation**: 
```python
def sensitivity_analysis(parameters, base_evidence):
    # Flip each factor one at a time and measure probability change
    pass
```

---

### 4. **Model Validation & Comparison**
**Current**: No validation

**Add**:
- **Train/Test Split**: Split data 80/20, train on train set, evaluate on test set
- **Cross-validation**: K-fold cross-validation to assess model stability
- **Accuracy metrics**: 
  - Classification accuracy (predict E=1 if P(E=1|evidence) > 0.5)
  - Precision, Recall, F1-score
  - Confusion matrix
- **Compare thresholds**: Which binarization method gives best predictions?
- **Baseline comparison**: Compare against simple baseline (always predict majority class)

**Implementation**: New `validation.py` module

---

### 5. **Extended Probability Queries**
**Current**: Only queries all-1 or all-0 combinations

**Add**:
- **Mixed evidence scenarios**: 
  - P(E|H=1, S=0, A=1, P=0) - some factors positive, some negative
  - All 16 possible combinations (2^4)
- **Conditional on exam outcome**: P(H=1|E=1), P(S=1|E=1), etc. (reverse direction)
- **Joint probabilities**: P(E=1, H=1, S=1) - probability of all occurring together
- **Marginal probabilities**: P(H=1), P(S=1), etc. - overall factor distributions

**Implementation**: Extend `probability_of_performance()` to handle all combinations

---

### 6. **Statistical Significance Testing**
**Purpose**: Determine if observed differences are statistically significant

**Tests**:
- **Chi-square test**: Are factors independent of exam outcome?
- **Fisher's exact test**: For small sample sizes
- **Confidence intervals**: For probability estimates
- **Effect size**: How strong is the relationship? (Cramér's V, odds ratios)

**Implementation**: New `statistics.py` module using scipy.stats

---

### 7. **Factor Correlation & Dependencies**
**Current**: Assumes Naive Bayes (factors independent given E)

**Add**:
- **Correlation matrix**: Check if factors are actually independent
- **Conditional independence tests**: Are H, S, A, P independent given E?
- **Factor dependencies**: Which factors tend to co-occur?
- **Bayesian network structure learning**: Learn optimal structure instead of assuming Naive Bayes

**Implementation**: 
```python
def check_independence(data):
    # Calculate correlations between factors
    # Test conditional independence
    pass
```

---

### 8. **Comparative Analysis Across Thresholds**
**Current**: Runs all thresholds but doesn't compare them

**Add**:
- **Threshold comparison table**: Side-by-side comparison of results
- **Consistency check**: Which factors are consistently best across thresholds?
- **Threshold recommendation**: Which threshold gives most meaningful results?
- **Visualization**: Plot how probabilities change with different thresholds

**Implementation**: Aggregate results from all processing types

---

### 9. **Subgroup Analysis**
**Purpose**: Understand if relationships differ for different student groups

**Variations**:
- **By exam performance**: Analyze separately for students who passed vs failed
- **By factor combinations**: Students with high H but low S vs others
- **Extreme cases**: Top 10% vs bottom 10% students
- **Factor-specific groups**: High attendance students vs low attendance

**Implementation**: Filter data by conditions before analysis

---

### 10. **Predictive Scenarios**
**Purpose**: Real-world "what-if" scenarios**

**Scenarios**:
- **Intervention scenarios**: 
  - "If we improve attendance by 20%, what's P(E=1)?"
  - "If we increase study hours, what's the expected improvement?"
- **Risk assessment**: 
  - "What's P(E=0) for a student with H=0, S=0, A=1, P=1?"
  - Identify at-risk students
- **Optimal factor combinations**: What combination maximizes P(E=1)?

**Implementation**: Scenario-based query functions

---

### 11. **Visualization & Reporting**
**Current**: Text-based output only

**Add**:
- **Probability heatmaps**: Visualize P(E|H,S,A,P) for all combinations
- **Factor importance bar charts**: Visualize individual factor probabilities
- **Comparison charts**: Compare results across thresholds
- **Network diagrams**: Visualize Bayesian network structure
- **Interactive dashboard**: Allow users to input evidence and see predictions

**Implementation**: Use matplotlib/seaborn or create HTML reports

---

### 12. **Advanced Modeling**
**Current**: Simple Naive Bayes

**Add**:
- **Laplace smoothing**: Handle zero probabilities
- **Weighted factors**: Some factors may be more important
- **Non-binary factors**: Keep continuous values, use Gaussian Naive Bayes
- **Hierarchical models**: Different models for different student groups
- **Ensemble methods**: Combine multiple threshold models

**Implementation**: Extend model architecture

---

### 13. **Data Quality Analysis**
**Purpose**: Understand data characteristics before modeling

**Add**:
- **Distribution analysis**: Histograms, box plots for each factor
- **Outlier detection**: Identify unusual students
- **Missing data patterns**: If any missing data exists, analyze patterns
- **Data balance**: Check if E=1 vs E=0 is balanced
- **Factor distributions**: How are H, S, A, P distributed?

**Implementation**: New `data_exploration.py` module

---

### 14. **Model Interpretability**
**Purpose**: Explain why model makes certain predictions

**Add**:
- **Feature contribution**: Which factors contribute most to each prediction?
- **Counterfactual analysis**: "What would need to change for student to pass?"
- **Decision rules**: Simple if-then rules based on model
- **Probability decomposition**: Show how P(E|evidence) is calculated step-by-step

**Implementation**: Explanation functions

---

### 15. **Export & Integration**
**Current**: Text files only

**Add**:
- **CSV export**: Structured results for further analysis
- **JSON export**: Machine-readable format
- **Summary statistics**: Aggregate statistics across all analyses
- **Comparison reports**: Automated comparison across all variations

**Implementation**: Enhanced output functions

---

## Recommended Priority Order

### High Priority (Core Extensions)
1. **Extended Probability Queries** (#5) - More comprehensive analysis
2. **Factor Interaction Analysis** (#2) - Understand relationships
3. **Sensitivity Analysis** (#3) - Robustness testing
4. **Model Validation** (#4) - Ensure model quality

### Medium Priority (Enhanced Understanding)
5. **Statistical Significance Testing** (#6)
6. **Comparative Analysis Across Thresholds** (#8)
7. **Subgroup Analysis** (#9)
8. **Visualization** (#11)

### Lower Priority (Advanced Features)
9. **Advanced Modeling** (#12)
10. **Data Quality Analysis** (#13)
11. **Model Interpretability** (#14)

---

## Implementation Suggestions

### New Files to Create:
- `analysis_variations.py` - Additional analysis functions
- `validation.py` - Model validation functions
- `statistics.py` - Statistical tests
- `visualization.py` - Plotting functions
- `scenarios.py` - Scenario-based queries
- `comparison.py` - Cross-threshold comparisons

### Extend Existing Files:
- `preprocess.py` - Add more ProcessingType options
- `calculations.py` - Add interaction and extended query functions
- `main.py` - Add options to run different analysis types

---

## Example: Quick Win Implementation

**Add Factor Pairs Analysis** (Easy to implement, high value):

```python
def calculate_factor_pairs(parameters):
    """Calculate P(E=1 | factor1=1, factor2=1) for all pairs"""
    pairs = [
        ("h", "s"), ("h", "a"), ("h", "p"),
        ("s", "a"), ("s", "p"),
        ("a", "p")
    ]
    results = {}
    for f1, f2 in pairs:
        # Use probability_of_performance with other factors set to 0
        # or calculate directly from parameters
        prob = probability_of_performance(parameters, 1, 
                                        h=1 if f1=="h" or f2=="h" else 0,
                                        s=1 if f1=="s" or f2=="s" else 0,
                                        a=1 if f1=="a" or f2=="a" else 0,
                                        p=1 if f1=="p" or f2=="p" else 0)
        results[f"{f1}_{f2}"] = prob
    return results
```

This would reveal which factor pairs are most predictive together!

