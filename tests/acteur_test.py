
#  TEST DE L'EXPEDITEUR
def test_expediteur_crud(client):

    donnees = {
        "nom": "Alami", "prenom": "Sara", "telephone": "0600112233",
        "email": "sara@mail.com", "adresse": "Rabat Agdal"
    }
    reponse = client.post("/expediteurs", json=donnees)
    assert reponse.status_code == 200
    id_exp = reponse.json()["id"]

    reponse_up = client.patch(f"/expediteurs/{id_exp}", json={"telephone": "0700000000"})
    assert reponse_up.status_code == 200
    assert reponse_up.json()["telephone"] == "0700000000"

    reponse_del = client.delete(f"/expediteurs/{id_exp}")
    assert reponse_del.status_code == 200



def test_livreur_crud(client):
    # CRÉATION
    donnees_livreur = {
        "nom": "Bakari", "prenom": "Driss", "telephone": "0611223344",
        "vehicule": "Moto Honda", "zone_assignee": "Casablanca-Anfa"
    }
    reponse = client.post("/livreurs", json=donnees_livreur)
    assert reponse.status_code == 200
    id_liv = reponse.json()["id"]

    # VÉRIFICATION
    assert reponse.json()["vehicule"] == "Moto Honda"

    # SUPPRESSION
    reponse_del = client.delete(f"/livreurs/{id_liv}")
    assert reponse_del.status_code == 200



def test_expediteur_introuvable(client):
    reponse = client.delete("/expediteurs/999")
    
    assert reponse.status_code == 404
    assert "n'a pas été trouvé" in reponse.json()["detail"]