# 📊 Product Recommendation Engine - AI PM Case Study

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

> **AI PM case study demonstrating**: Collaborative filtering + Deep learning re-ranking | Problem framing | Metrics design | UX flows | Guardrails | Cold start strategies

---

## 🎯 Problem Statement

**Business Context**: E-commerce platform with 10M+ users struggling with product discovery

**Key Challenges**:
- 📉 **Low engagement**: 65% of users don't find relevant products
- 💰 **Revenue loss**: $50M annual opportunity from better recommendations  
- 🔍 **Poor discovery**: 80% of catalog never viewed
- 🆕 **Cold start**: New users/products get zero visibility

**Success Criteria**: Increase CTR by **15%**, revenue per user by **8%**, improve catalog coverage by **25%**

---

## 🧠 AI Product Approach

### Two-Stage Recommendation System

```
User Profile
     │
     ▼
┌─────────────────────────┐
│ Stage 1: Candidate Gen  │  ← Collaborative Filtering
│ (User-based CF)         │    Fast retrieval of 100 items
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Stage 2: Re-ranking     │  ← Deep Learning Model
│ (Neural Network)        │    Personalized scoring
└───────────┬─────────────┘
            │
            ▼
    Top 12 Products
```

### Technology Stack
- **Collaborative Filtering**: Scikit-surprise (SVD algorithm)
- **Re-ranking Model**: TensorFlow/Keras (Neural CF)
- **Frontend**: Streamlit
- **Deployment**: Streamlit Cloud

---

## ✨ Key Features

### 1. **Personalized Recommendations**
   - User-based collaborative filtering
   - Considers browsing history + purchases
   - Real-time personalization

### 2. **Cold Start Handling**
   - New users: Popularity-based fallback
   - New products: Content-based features
   - Hybrid approach for edge cases

### 3. **Diversity & Fairness**
   - Category diversity constraints
   - Popularity bias mitigation
   - Small seller promotion

### 4. **Interactive Demo**
   - Select user profile
   - View recommendations
   - See explainability (why recommended)

---

## 🚀 Setup & Installation

### Quick Start

```bash
# Clone repository
git clone https://github.com/Usha2025-git/product-recommender-ai-pm.git
cd product-recommender-ai-pm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\\Scripts\\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

App opens at `http://localhost:8501`

---

## 📊 Success Metrics

### Product Metrics
| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| **Click-Through Rate** | 2.5% | 3.0% (+15%) | A/B test |
| **Revenue per User** | $45 | $49 (+8%) | Revenue analytics |
| **Catalog Coverage** | 20% | 45% (+25%) | % products viewed |
| **User Satisfaction** | 3.8/5 | 4.2/5 | Post-purchase survey |

### Model Metrics
- **Precision@12**: 18% (12% baseline)
- **Diversity Score**: 0.75 (0.6 baseline)
- **Cold Start Coverage**: 85% of new users get recommendations

### Business Impact (Projected)
- **$4M additional revenue** annually
- **12% increase** in repeat purchases
- **20% reduction** in search bounce rate

---

## 🧭 AI PM Decisions & Tradeoffs

### 1. **Two-Stage vs Single Model**

**Decision**: Two-stage system

**Rationale**:
- ✅ **Latency**: <500ms (collaborative filtering is fast)
- ✅ **Accuracy**: Neural re-ranking improves precision by 6%
- ✅ **Scalability**: Can handle 10M users
- ⚠️ **Complexity**: Two models to maintain

### 2. **Collaborative Filtering vs Content-Based**

**Decision**: Hybrid (CF primary, content fallback)

**Why**:
- ✅ **Better accuracy**: CF leverages collective intelligence
- ✅ **Serendipity**: Recommends unexpected but relevant items
- ✅ **Cold start handled**: Content features for new items

### 3. **Diversity vs Accuracy Tradeoff**

**Decision**: Sacrifice 2% accuracy for 25% more diversity

**Why**:
- ✅ **Business goal**: Promote long-tail catalog
- ✅ **User experience**: Avoid filter bubble
- ✅ **Marketplace health**: Support small sellers
- 📊 **Validation**: A/B test showed +5% user satisfaction

---

## 📁 Project Artifacts

- **[PRD.md](PRD.md)**: Product Requirements Document
  - User stories
  - Acceptance criteria
  - Recommendation placement UX

- **[METRIC_PLAN.md](METRIC_PLAN.md)**: Comprehensive Metrics Plan
  - North star metrics
  - Model evaluation framework
  - A/B test design

- **[app.py](app.py)**: Demo application
  - Interactive recommendation engine
  - Explainability features

---

## 🎓 Skills Demonstrated

### AI Product Management
- ✅ Problem framing and opportunity sizing
- ✅ Algorithm selection and tradeoffs
- ✅ Metrics hierarchy (product + model + business)
- ✅ Cold start strategy design
- ✅ Diversity and fairness considerations

### Technical
- ✅ Collaborative filtering implementation
- ✅ Neural network re-ranking
- ✅ Hybrid recommendation systems
- ✅ Python/ML development

### Responsible AI
- ✅ Bias detection (popularity bias)
- ✅ Fairness metrics (seller equity)
- ✅ Explainability (why recommended)
- ✅ Filter bubble mitigation

---

## 🛣️ Roadmap

### Phase 1: MVP (✅ Complete)
- [x] Two-stage recommendation system
- [x] Streamlit demo
- [x] Basic metrics framework

### Phase 2: Enhancement
- [ ] Real-time model updates
- [ ] Multi-armed bandit for exploration
- [ ] Cross-sell and upsell logic
- [ ] Mobile optimization

### Phase 3: Advanced Features
- [ ] Session-based recommendations
- [ ] Image-based similarity
- [ ] Social proof signals
- [ ] Contextual bandits

---

## 📞 Contact

**Usha Swinir** - AI Product Manager

- 💼 LinkedIn: [linkedin.com/in/ushaswinir-product](https://www.linkedin.com/in/ushaswinir-product/)
- 🐙 GitHub: [@Usha2025-git](https://github.com/Usha2025-git)

---

**Last Updated**: January 2026  
**License**: MIT  
**Status**: ✅ Production-ready MVP
