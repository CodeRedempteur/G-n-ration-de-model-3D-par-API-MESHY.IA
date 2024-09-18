# Génération de modèles 3D via l'API Meshy.AI

Bienvenue dans ce projet utilisant l'API de Meshy.AI pour générer des modèles 3D à partir de requêtes textuelles. Ce projet vous guide à travers les différentes étapes pour utiliser efficacement l'API et générer vos propres modèles 3D.

N'hésiter pas à aller voir la vidéo sur youtube pour voir chaque étapes détaillés : [Lien youtube](https://www.youtube.com/watch?v=QNS74m1X0Zo&list=PLwxzgoKfBuLGemfvDMs5gaMvlRMwTXmYc&index=9&ab_channel=CodeRedempteur)

## 🎥 Introduction à Meshy.AI

Découvrez comment utiliser l'API Meshy.AI pour générer des modèles 3D de manière simple et rapide. Pour en savoir plus sur son fonctionnement, consultez la documentation officielle de [Meshy.AI](https://www.meshy.ai/api).

## 🚀 Comment utiliser ce projet ?

1. **Clonez le dépôt** : `git clone https://github.com/votre-utilisateur/mesh-ai-3d-project.git`
2. **Ouvrez le fichier Python** : Téléchargez le fichier Python dans votre éditeur préféré (Visual Studio Code, PyCharm, etc.).
3. **Ajoutez votre clé API** : Remplacez la 3ème ligne du fichier par votre propre token d'API :

    ```python
    api_key = "votre_token"
    ```
    > Vous pouvez obtenir votre clé d'API en suivant [ce lien](https://www.meshy.ai/api).

4. **Lancez le script** : Exécutez le script depuis votre terminal ou IDE préféré.

5. **Entrez votre requête** : Dans le terminal, entrez une requête de modèle, par exemple `"Black Bear"`. 

6. **Téléchargement du modèle** : Une fois le modèle généré, il sera automatiquement téléchargé dans votre répertoire par défaut (généralement Téléchargements) ou vous verrez l'URL de téléchargement dans le terminal sous ce format :

    ```json
    {'model_urls': {'glb': 'https://assets.meshy.ai/...'}}
    ```
    Vous pouvez alors cliquer sur le lien pour télécharger le fichier `.glb` du modèle.

## 📜 Licence et conditions d'utilisation

Ce projet est sous licence [MIT](LICENSE). Vous êtes libre de l'utiliser, de le modifier et de le distribuer, à condition de respecter les termes de la licence.

> **Note** : Ce projet est actuellement **maintenu** et les contributions sont les bienvenues sur le discord officiel : [Discord](https://discord.gg/JR3ENr5Db5)

## ☕️ Supportez le projet

Si ce projet vous a été utile, vous pouvez me soutenir via les plateformes suivantes :

- [Patreon](https://www.patreon.com/coderedempteur/membership)
- [Buy Me a Coffee](https://buymeacoffee.com/coderredemy)

Merci pour votre soutien et bon développement 3D avec Meshy.AI ! 🖼️
