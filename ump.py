from graphviz import Digraph

# Create a new directed graph
uml = Digraph("EcommerceSearchEngine", format="jpeg")
uml.attr(rankdir="TB", size="12,12")

# User Interaction Layer
uml.node("User", "User Interaction Layer\n(Search Query, Suggestions)", shape="ellipse")

# Query Understanding Layer
uml.node("QueryUnderstanding", "Query Understanding Layer\n(Query Parsing, Spelling Correction,\nNLU, Synonym Expansion)", shape="rectangle")

# Data Retrieval Layer
uml.node("DataRetrieval", "Data Retrieval Layer\n(Elasticsearch, Kafka Pipeline,\nProduct DB)", shape="rectangle")

# Ranking Layer
uml.node("Ranking", "Ranking Layer\n(Feature Engineering, XGBoost,\nBERT Re-ranker)", shape="rectangle")

# Personalization Layer
uml.node("Personalization", "Personalization Layer\n(Collaborative Filtering,\nContent-based Filtering,\nReinforcement Learning)", shape="rectangle")

# Business Logic Layer
uml.node("BusinessLogic", "Business Logic Layer\n(Sponsored Products,\nStock Status Adjustment)", shape="rectangle")

# Analytics and Feedback Loop
uml.node("Analytics", "Analytics and Feedback Loop\n(Logs, Metrics, Model Retraining)", shape="rectangle")

# Infrastructure Layer
uml.node("Infrastructure", "Infrastructure Layer\n(Load Balancers, Redis Cache,\nDocker, Kubernetes)", shape="rectangle")

# Connections
uml.edges([
    ("User", "QueryUnderstanding"),
    ("QueryUnderstanding", "DataRetrieval"),
    ("DataRetrieval", "Ranking"),
    ("Ranking", "BusinessLogic"),
    ("Ranking", "Personalization"),
    ("BusinessLogic", "Personalization"),
    ("Personalization", "Ranking"),
    ("Ranking", "Analytics"),
    ("Analytics", "DataRetrieval"),
    ("Analytics", "Ranking"),
    ("Ranking", "User"),  # Feedback of final results to the user
    ("Infrastructure", "QueryUnderstanding"),
    ("Infrastructure", "DataRetrieval"),
    ("Infrastructure", "Ranking"),
])

# Render UML Diagram
uml_filepath = "ecommerce_search_engine_uml.jpeg"
uml.render(uml_filepath, format="jpeg", cleanup=True)
# uml_filepath + ".png"

