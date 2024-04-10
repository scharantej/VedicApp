## Flask Application Design for Vedic Mathematics Website ##

### HTML Files ###
- **index.html** (Homepage):
    - Introduction to Vedic mathematics, its benefits, and history.
    - Links to sections on different Vedic sutras and techniques.
- **sutras.html** (Vedic Sutras):
    - List of Vedic sutras with brief descriptions and examples.
    - Links to pages on specific sutras for in-depth explanations.
- **techniques.html** (Vedic Techniques):
    - List of Vedic techniques with explanations and examples.
    - Links to pages on specific techniques for detailed guidance.
- **examples.html** (Examples and Problems):
    - Real-world examples of Vedic mathematics applications.
    - Practice problems and solutions for self-assessment.

### Routes ###
- **@app.route('/')** (Homepage):
    - Renders the index.html page, displaying the introduction to Vedic mathematics.
- **@app.route('/sutras')** (Vedic Sutras):
    - Renders the suras.html page, listing the Vedic sutras and providing links to detailed pages.
- **@app.route('/sutras/<sutra_name>')** (Specific Sutra):
    - Renders a page providing in-depth explanation and examples of a specific Vedic sutra.
- **@app.route('/techniques')** (Vedic Techniques):
    - Renders the techniques.html page, listing the Vedic techniques and providing links to detailed pages.
- **@app.route('/techniques/<technique_name>')** (Specific Technique):
    - Renders a page providing detailed explanation and examples of a specific Vedic technique.
- **@app.route('/examples')** (Examples and Problems):
    - Renders the examples.html page, showcasing real-world applications of Vedic mathematics and providing practice problems.