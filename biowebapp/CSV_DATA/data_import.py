import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect('../../BioinformaticsData.sqlite3')
c = conn.cursor()

# Load data from pfam_descriptions.csv
with open('pfam_descriptions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        c.execute("SELECT * FROM pfam_descriptions WHERE domain_id=?",
                  (i['domain_id'],))
        result = c.fetchone()
        if result is None:  # if the domain_id is not already in the table
            c.execute("INSERT INTO pfam_descriptions (domain_id, domain_description) VALUES (?, ?);",
                      (i['domain_id'], i['domain_description']))

# Load data from assignment_data_set.csv
with open('assignment_data_set.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        c.execute("SELECT * FROM organisms WHERE taxa_id=?", (i['taxa_id'],))
        result = c.fetchone()
        if result is None:  # if the taxa_id is not already in the table
            c.execute("INSERT INTO organisms (taxa_id, genus, species) VALUES (?, ?, ?);",
                      (i['taxa_id'], i['genus'], i['species']))

        c.execute("SELECT * FROM proteins WHERE protein_id=?",
                  (i['protein_id'],))
        result = c.fetchone()
        if result is None:  # if the protein_id is not already in the table
            c.execute("INSERT INTO proteins (protein_id, taxa_id, clade, description, start, stop, length) VALUES (?, ?, ?, ?, ?, ?, ?);",
                      (i['protein_id'], i['taxa_id'], i['clade'], i['description'], i['start'], i['stop'], i['length']))

        c.execute("SELECT * FROM domains WHERE protein_id=? AND domain_id=?",
                  (i['protein_id'], i['domain_id']))
        result = c.fetchone()
        if result is None:  # if the domain_id is not already in the table
            c.execute("INSERT INTO domains (protein_id, domain_id) VALUES (?, ?);",
                      (i['protein_id'], i['domain_id']))

# Load data from assignment_data_sequence.csv
with open('assignment_data_sequences.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        c.execute("SELECT * FROM sequences WHERE protein_id=?",
                  (i['protein_id'],))
        result = c.fetchone()
        if result is None:  # if the protein_id is not already in the table
            c.execute("INSERT INTO sequences (protein_id, sequence) VALUES (?, ?);",
                      (i['protein_id'], i['sequence']))

# Commit changes and close connection
conn.commit()
conn.close()
