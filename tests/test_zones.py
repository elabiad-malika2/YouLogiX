def test_zone_complet(client):
    nouvelle_zone={
        "nom":"Test",
        "code_postal":"90000"
    }
    response_create=client.post("/zones",json=nouvelle_zone)

    assert response_create.status_code == 200

    zone_id=response_create.json()["id"]

    # Modification

    response_update=client.patch(f"/zones/{zone_id}",json={"nom":"AAAA"})

    assert response_update.status_code == 200

    assert response_update.json()["nom"]=="AAAA"

    # Suppresion

    response_delete=client.delete(f"/zones/{zone_id}")

    assert response_delete.status_code == 200