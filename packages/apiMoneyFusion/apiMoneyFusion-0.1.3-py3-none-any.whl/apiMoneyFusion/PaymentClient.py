import requests
from typing import Dict


class PaymentClient:
    def __init__(self, api_key_url: str):
        """
        Initialise le client de paiement

        Args:
            api_key_url (str): Clé API URL pour generer dans fusion pay
        """
        self.api_key_url = api_key_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def create_payment(self,
                       total_price: str,
                       articles: list,
                       numero_send: str,
                       nom_client: str,
                       user_id: int,
                       order_id: int,
                       return_url: str) -> Dict:
        """
        Crée un nouveau paiement avec les détails de la commande

        Args:
            total_price (str): Prix total de la commande
            articles (list): Liste des articles commandés
            numero_send (str): Numéro d'envoi
            nom_client (str): Nom du client
            user_id (int): ID de l'utilisateur
            order_id (int): ID de la commande
            return_url (str): URL de retour après le paiement(utiliser une url https avec un nom de domaine)

        Returns:
            Dict: Contient les informations suivantes:
                - statut (bool): État de la création du paiement
                - token (str): Token unique du paiement
                - message (str): Message décrivant l'état du paiement
                - url (str): URL de redirection vers la page de paiement

            Example:
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
                {
                    'statut': True,
                    'token': 'f5EJ33JYmxqosi8BvaEt',
                    'message': 'paiement en cours',
                    'url': 'https://payin.moneyfusion.net/payment/f5EJ33JYmxqosi8BvaEt/10000/JOHN Doe'
                }
        """

        payload = {
            "totalPrice": total_price,
            "article": articles,
            "numeroSend": numero_send,
            "nomclient": nom_client,
            "personal_Info": [{
                "userId": user_id,
                "orderId": order_id
            }],
            "return_url": return_url
        }

        response = self.session.post(
            f'{self.api_key_url}',
            json=payload
        )

        response.raise_for_status()
        return response.json()


    def get_payment(self, payment_id: str) -> Dict:
        """
        Récupère les informations détaillées d'un paiement.

        Args:
            payment_id (str): Identifiant unique du paiement (token)

        Returns:
            Dict: Contient les informations suivantes:
                - statut (bool): État de la requête
                - data (Dict): Informations détaillées du paiement
                    - _id (str): Identifiant unique en base de données
                    - tokenPay (str): Token du paiement
                    - numeroSend (str): Numéro d'envoi
                    - nomclient (str): Nom du client
                    - personal_Info (List[Dict]): Informations personnelles
                        - userId (int): ID de l'utilisateur
                        - orderId (int): ID de la commande
                    - numeroTransaction (str): Numéro de la transaction
                    - Montant (int): Montant du paiement
                    - frais (int): Frais appliqués
                    - statut (str): État du paiement ('pending', 'failure', 'no paid', 'paid')
                    - moyen (str): Moyen de paiement utilisé
                    - return_url (str): URL de retour
                    - createdAt (str): Date de création (format ISO)
                - message (str): Message descriptif

        Example:
            payment_info = client.get_payment("8L5teSc5TaIkP3ds9Dlx")
            print(payment_info)
            {
                'statut': True,
                'data': {
                    '_id': '6748d365967cb4766fdd1616',
                    'tokenPay': '8L5teSc5TaIkP3ds9Dlx',
                    'numeroSend': 'None',
                    'nomclient': 'assemienDev',
                    'personal_Info': [{'userId': 1, 'orderId': 123}],
                    'numeroTransaction': '',
                    'Montant': 475,
                    'frais': 25,
                    'statut': 'paid',
                    'moyen': 'card',
                    'return_url': 'https://votre-domaine.com/callback',
                    'createdAt': '2024-11-28T20:32:37.037Z'
                },
                'message': 'details paiement'
            }
        """

        response = self.session.get(
            f'https://www.pay.moneyfusion.net/paiementNotif/{payment_id}'
        )

        response.raise_for_status()
        return response.json()