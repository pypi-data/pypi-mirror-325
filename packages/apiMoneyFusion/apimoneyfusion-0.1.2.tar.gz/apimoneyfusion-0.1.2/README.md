# API MONEY FUSION PAYEMENT PYTHON

Elle permet d'intéragir avec l'API de paiement de MoneyFusion. Elle facilite la création et la récupération des paiements via des requêtes HTTP.

## Installation

vous pourrez l'installer avec :

```sh
pip install apiMoneyFusion
```

## Utilisation

### Importation

```python
from apiMoneyFusion import PaymentClient
```

### Initialisation du client

```python
client = PaymentClient(api_key_url="https://api.moneyfusion.net")
```

### Créer un paiement

```python
payment = client.create_payment(
    total_price="10000",
    articles=[{"name": "Article 1", "price": "5000", "quantity": 1}],
    numero_send="0101010101",
    nom_client="assemienDev",
    user_id=1,
    order_id=123,
    return_url="https://votre-domaine.com/callback"
)

print(payment)
```

Réponse attendue :

```json
{
    "statut": true,
    "token": "f5EJ33JYmxqosi8BvaEt",
    "message": "paiement en cours",
    "url": "https://payin.moneyfusion.net/payment/f5EJ33JYmxqosi8BvaEt/10000/John Doe"
}
```

### Récupérer un paiement

```python
payment_info = client.get_payment("8L5teSc5TaIkP3ds9Dlx")
print(payment_info)
```

Réponse attendue :

```json
{
    "statut": true,
    "data": {
        "_id": "6748d365967cb4766fdd1616",
        "tokenPay": "8L5teSc5TaIkP3ds9Dlx",
        "numeroSend": "None",
        "nomclient": "assemienDev",
        "personal_Info": [{"userId": 1, "orderId": 123}],
        "numeroTransaction": "",
        "Montant": 475,
        "frais": 25,
        "statut": "paid",
        "moyen": "card",
        "return_url": "https://votre-domaine.com/callback",
        "createdAt": "2024-11-28T20:32:37.037Z"
    },
    "message": "details paiement"
}
```

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à proposer des améliorations ou signaler des bugs en ouvrant une issue sur GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

