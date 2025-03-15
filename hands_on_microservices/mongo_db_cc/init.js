// Connexion à la base MongoDB
db = db.getSiblingDB("cc");

// Création de la collection des dépôts GitHub
db.createCollection("cc_items");

// Création d’un index sur le champ "name" pour accélérer les recherches
db.cc_items.createIndex({ id: 1 }, {unique: true});

db.cc_items.insert({ id: 1, value: "Message 1"});

print("✅ Bases de données et index MongoDB initialisés !");