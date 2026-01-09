def test_create_colis(client):
    
    
    nouvelle_colis = {
        "description": "test",
        "poids": 11,
        "ville_destination": "Marrakech",
        "id_expediteur": 2,
        "id_destinataire": 3,
        "id_zone": 3,
        "id_gestionnaire": 1
    }
    
    response_create = client.post("/colis/create",json=nouvelle_colis)
    assert response_create.status_code == 200
    
    colis_id = response_create.json()["id"]
    
    
    # assign colis :
    
    assign_params = {
        "colis_id":colis_id,
        "livreur_id":2
    }
    
    response_assign = client.patch("/colis/assign",params=assign_params)
    assert response_assign.status_code == 200
    
    
    # update status : 
    
    update_params = {
        "colis_id": colis_id,
        "new_statut": "livré"
    }
    
    response_update_statut = client.patch("/colis/statut/update",params=update_params)
    assert response_update_statut.status_code == 200
    
    
    searh_params = {"zone_name":"Centre Ville"}
    
    response_search = client.post("/colis/search/zone",params=searh_params)
    assert response_search.status_code == 200
    
    

    
    
    
    

    
    